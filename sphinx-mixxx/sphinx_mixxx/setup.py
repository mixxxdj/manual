from .domains import MixxxDomain

from sphinx.domains.std import StandardDomain


def setup(app):
    app.add_domain(MixxxDomain)

    StandardDomain.initial_data["labels"]["controlindex"] =\
        ("mixxx-control", "", "Control Index")

    StandardDomain.initial_data["anonlabels"]["controlindex"] =\
        ("mixxx-control", "")

    return {"version": "0.1"}
