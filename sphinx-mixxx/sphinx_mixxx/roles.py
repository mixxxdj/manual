from sphinx.roles import GUILabel


class HWLabel(GUILabel):
    """Label on external hardware (such as controllers)."""


specific_docroles = {
    'hwlabel': HWLabel(),
}
