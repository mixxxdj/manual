from .domains import MixxxDomain
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

    return {"version": "0.1"}
