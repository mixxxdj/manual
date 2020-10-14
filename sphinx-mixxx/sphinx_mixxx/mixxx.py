import re
from docutils.parsers.rst import directives
from sphinx.domains import Domain, Index
from sphinx.domains.std import StandardDomain
from sphinx.locale import __
from sphinx.roles import XRefRole
from sphinx.directives import ObjectDescription
from sphinx.util import logging
from sphinx.util.nodes import make_refnode
from sphinx import addnodes

logger = logging.getLogger(__name__)


def generate_targets(target):
    return {
        target,
        re.sub(r"(?<=\[Channel)\d+(?=\])", "N", target),
        re.sub(r"(?<=\[Auxiliary)\d+(?=\])", "N", target),
        re.sub(r"(?<=\[Microphone)\d+(?=\])", "N", target),
        re.sub(r"(?<=\[PreviewDeck)\d+(?=\])", "N", target),
        re.sub(r"(?<=\[Sampler)\d+(?=\])", "N", target),
        re.sub(r"(?<=\[EffectRack1_EffectUnit)\d+(?=\])", "N", target),
        re.sub(r"(?<=\[EffectRack1_EffectUnitN_Effect)\d+(?=\])", "M", target),
    }


class MixxxControlGroupNode(ObjectDescription):
    """A custom node that describes a Mixxx Control Group."""

    required_arguments = 1

    def handle_signature(self, sig, signode):
        signode += addnodes.desc_name(text="[{}]".format(sig))
        signode += addnodes.desc_type(text="Group")
        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        anchor = "controlgroup-" + sig
        signode["ids"].append(anchor)

    def run(self):
        groupname = self.arguments[0].strip()
        self.env.ref_context["mixxx:controlgroup"] = groupname
        return super().run()


class MixxxControlNode(ObjectDescription):
    """A custom node that describes a Mixxx Control."""

    required_arguments = 1

    option_spec = {
        "noindex": directives.flag,
        "noindexentry": directives.flag,
        "range": directives.unchanged_required,
        "feedback": directives.unchanged_required,
        "group": directives.unchanged_required,
    }

    def handle_signature(self, sig, signode):
        matchobj = re.match(r"(?P<group>\[.*\]),(?P<control>.*)", sig)
        group, control = matchobj.groups()

        signode["group"] = group
        signode["control"] = control
        signode["fullname"] = sig

        signode += addnodes.desc_annotation(group, group)
        signode += addnodes.desc_name(control, control)

        return sig, group

    def add_target_and_index(self, name_cls, sig, signode):
        anchor = "control-" + signode["group"] + "-" + signode["control"]
        signode["ids"].append(anchor)
        if "noindex" not in self.options:
            signame = type(self).__name__
            name = "{}.{}.{}".format(MixxxDomain.name, signame, sig)
            objs = self.env.domaindata[MixxxDomain.name]["objects"]
            objs.add((name, sig, signode["group"], self.env.docname, anchor, 0))


class MixxxControlIndex(Index):
    name = "control"
    localname = "Control Index"
    shortname = "Control"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate(self, docnames=None):
        """
        Return entries for the index given by *name*.  If *docnames* is given,
        restrict to entries referring to these docnames.  The return value is a
        tuple of ``(content, collapse)``, where * collapse* is a boolean that
        determines if sub-entries should start collapsed (for output formats
        that support collapsing sub-entries).

        *content* is a sequence of ``(letter, entries)`` tuples, where *letter*
        is the "heading" for the given *entries*, usually the starting letter.
        *entries* is a sequence of single entries, where a single entry is a
        sequence ``[name, subtype, docname, anchor, extra, qualifier, descr]``.

        The items in this sequence have the following meaning:
        - `name` -- the name of the index entry to be displayed
        - `subtype` -- sub-entry related type:
          0 -- normal entry
          1 -- entry with sub-entries
          2 -- sub-entry
        - `docname` -- docname where the entry is located
        - `anchor` -- anchor for the entry within `docname`
        - `extra` -- extra info for the entry
        - `qualifier` -- qualifier for the description
        - `descr` -- description for the entry
        Qualifier and description are not rendered e.g. in LaTeX output.
        """

        content = {}
        items = ((name, dispname, typ, docname, anchor)
                 for name, dispname, typ, docname, anchor, prio
                 in self.domain.get_objects())
        items = sorted(items, key=lambda item: item[0])
        for name, dispname, typ, docname, anchor in items:
            lis = content.setdefault(typ, set())
            lis.add((dispname, 0, docname, anchor, docname, "", typ))
        re = [(k, v) for k, v in sorted(content.items())]

        return (re, True)


class MixxxDomain(Domain):
    name = "mixxx"
    label = "Mixxx"

    roles = {
        "cogroupref": XRefRole(),
        "coref": XRefRole(),
    }

    directives = {
        "controlgroup": MixxxControlGroupNode,
        "control": MixxxControlNode,
    }

    indices = {
        MixxxControlIndex,
    }

    initial_data = {
        "objects": set(),
    }

    def get_full_qualified_name(self, node):
        """Return full qualified name for a given node"""
        nodename = type(node).__name__
        return "{}.{}.{}".format(self.name, nodename, node.arguments[0])

    def get_objects(self):
        yield from self.data["objects"]

    def resolve_xref(self, env, fromdocname, builder, typ,
                     target, node, contnode):

        targets = generate_targets(target)
        corefs = sorted(self.get_objects(), key=lambda x: x[5])
        matches = None
        if typ == "coref":
            matches = [
                (docname, anchor)
                for name, sig, group, docname, anchor, prio in corefs
                if sig in targets
            ]
        elif typ == "cogroupref":
            groups = [
                group for name, sig, group, docname, anchor, prio in corefs
                if group in targets
            ]
            if groups:
                matches = [("mixxx-control", "cap-{}".format(groups[0]))]
        else:
            logger.warning(__('Unsupported cross-references %r'),
                           target, type='ref', subtype='mixxx', location=node)
            return None

        if not matches:
            logger.warning(__('no target found for cross-reference %r'),
                           target, type='ref', subtype='mixxx', location=node)
            return None

        if len(matches) > 1:
            logger.warning(
                __('more than one target found for cross-reference %r: %s'),
                target, ', '.join(match[0] for match in matches),
                type='ref', subtype='python', location=node)

        todocname, targ = matches[0]
        return make_refnode(
            builder, fromdocname, todocname, targ, contnode, targ)


def setup(app):
    app.add_domain(MixxxDomain)

    StandardDomain.initial_data["labels"]["controlindex"] =\
        ("mixxx-control", "", "Control Index")

    StandardDomain.initial_data["anonlabels"]["controlindex"] =\
        ("mixxx-control", "")

    return {"version": "0.1"}
