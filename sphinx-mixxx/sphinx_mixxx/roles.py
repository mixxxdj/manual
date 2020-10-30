from typing import List, Tuple

from docutils import nodes
from sphinx.roles import SphinxRole


class HWLabel(SphinxRole):
    """Label on external hardware (such as controllers)."""

    def run(self) -> Tuple[List[nodes.Node], List[nodes.system_message]]:
        node = nodes.inline(rawtext=self.rawtext, classes=[self.name])
        node += nodes.Text(self.text)
        return [node], []


specific_docroles = {
    "hwlabel": HWLabel(),
}
