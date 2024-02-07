"""Script to view what the templates would look like after rendering."""

from pathlib import Path

import chevron
from rich import print

from bids import BIDSLayout

# Tog1gling KEEP to True will render the empty variables in RED
# Only work with the version of chevron from github and not pypi
KEEP = True

# bids examples dataset to work with
# see in  "demos/data/bids-examples"
dataset = "ds000117"


def root_dir() -> Path:
    return Path(__file__).parents[2]


def highlight_missing_tags(text: str) -> str:
    text = f"[blue]{text}[/blue]"
    text = text.replace("{{", "[/blue][red]{{")
    text = text.replace("}}", "}}[/red][blue]")
    return text


def print_to_screen(layout, template_name, suffix) -> None:
    files = layout.get(suffix=suffix)

    if len(files) < 1:
        return

    metadata = files[0].get_metadata()
    metadata["suffix"] = suffix

    render_template(template_name, metadata)


def render_template(template_name, metadata) -> None:
    templates_dir = root_dir() / "templates"

    partials_path = root_dir() / "partials"

    with open(templates_dir / template_name, "r") as template:
        args = {
            "template": template,
            "data": metadata,
            "partials_path": partials_path,
            "keep": KEEP,
        }

        text = chevron.render(**args)

        print(highlight_missing_tags(text))


def main():
    data_dir = root_dir() / "demos" / "data" / "bids-examples"

    data_path = data_dir / "ds000117"

    layout = BIDSLayout(data_path)

    # %%
    print(f"\n[bold]# MRI[/bold]")

    files = layout.get(suffix="T1w")
    if len(files) > 1:
        metadata = files[0].get_metadata()
        render_template("institution.mustache", metadata)
        render_template("mri_scanner_info.mustache", metadata)

    suffix_template = {
        "T1w": "anat",
        "bold": "func",
        "dwi": "dwi",
        "perf": "perf",
    }

    for suffix, template in suffix_template.items():
        print(f"\n[bold]## {suffix.upper()}[/bold]")
        print_to_screen(layout, f"{template}.mustache", suffix)

    # %%
    print(f"\n[bold]# PET[/bold]")

    print(f"\n[bold]## {'pet'.upper()}[/bold]")
    print_to_screen(layout, "pet.mustache", suffix)

    # %%
    print(f"\n[bold]# MEEG[/bold]")

    suffix_template = {
        "eeg": "meeg",
        "meg": "meeg",
    }

    for suffix, template in suffix_template.items():
        print(f"\n[bold]## {suffix.upper()}[/bold]")
        print_to_screen(layout, f"{template}.mustache", suffix)


if __name__ == "__main__":
    main()
