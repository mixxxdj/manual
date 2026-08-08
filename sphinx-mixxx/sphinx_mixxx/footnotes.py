from docutils import nodes
from sphinx.transforms import SphinxTransform


class PerSectionFootnotes(SphinxTransform):
    default_priority = 999

    def apply(self, **kwargs):
        if not self.app.config.per_section_footnotes:
            return

        doctree = self.document

        if not doctree.footnotes:
            return

        intervals = []
        self._collect_sections(doctree, None, intervals)

        if not intervals:
            return

        intervals.sort(key=lambda x: x[0])

        footnotes_by_section = {}
        footnotes_to_move = set()

        for footnote in doctree.footnotes:
            fn_line = footnote.line
            if fn_line is None:
                self._detach_from_parent(footnote)
                doctree.append(footnote)
                continue

            target = self._find_containing_section(intervals, fn_line)
            if target is None:
                self._detach_from_parent(footnote)
                doctree.append(footnote)
                continue

            footnotes_by_section.setdefault(target, []).append(footnote)
            footnotes_to_move.add(footnote)

        if not footnotes_by_section:
            return

        for section, footnotes_list in footnotes_by_section.items():
            for footnote in footnotes_list:
                self._insert_before_first_subsection(section, footnote)

        doctree.footnotes[:] = [
            fn for fn in doctree.footnotes if fn not in footnotes_to_move
        ]

    @staticmethod
    def _collect_sections(node, parent_next_start, intervals):
        own_children = [
            c for c in node.children if isinstance(c, nodes.section)
        ]
        for i, child in enumerate(own_children):
            next_start = (
                own_children[i + 1].line
                if i + 1 < len(own_children)
                else parent_next_start
            )
            start = child.line
            if start is not None:
                intervals.append((start, next_start, child))
            PerSectionFootnotes._collect_sections(child, next_start, intervals)

    @staticmethod
    def _find_containing_section(intervals, fn_line):
        all_starts = [start for start, _, _ in intervals]
        if all_starts and fn_line > max(all_starts):
            bounded = any(
                next_start is not None and start <= fn_line < next_start
                for start, next_start, _ in intervals
            )
            if not bounded:
                return None

        candidate = None
        for start, next_start, section in intervals:
            if start > fn_line:
                break
            if next_start is not None and fn_line >= next_start:
                continue
            if candidate is None or start > candidate[0]:
                candidate = (start, section)
        return candidate[1] if candidate else None

    @staticmethod
    def _detach_from_parent(node):
        if node.parent is not None and node in node.parent.children:
            node.parent.children.remove(node)

    @staticmethod
    def _insert_before_first_subsection(section, node):
        if node.parent is not None and node in node.parent.children:
            node.parent.children.remove(node)
        for i, child in enumerate(section.children):
            if isinstance(child, nodes.section):
                section.insert(i, node)
                return
        section.append(node)
