from .domains import MixxxDomain
from .footnotes import PerSectionFootnotes
from .roles import specific_docroles

from docutils.parsers.rst import roles

from sphinx.domains.std import StandardDomain


def setup(app):
    app.add_domain(MixxxDomain)

    for rolename, func in specific_docroles.items():
        roles.register_local_role(rolename, func)

    StandardDomain.initial_data["labels"]["controlindex"] = (
        "mixxx-control",
        "",
        "Control Index",
    )

    StandardDomain.initial_data["anonlabels"]["controlindex"] = (
        "mixxx-control",
        "",
    )

    app.add_config_value("per_section_footnotes", False, "env")
    app.add_post_transform(PerSectionFootnotes)

    return {
        "version": "0.1",
        "parallel_read_safe": False,
        "parallel_write_safe": False,
    }
