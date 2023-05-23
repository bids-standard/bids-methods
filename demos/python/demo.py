import chevron
from os import path
from os.path import join

from bids import BIDSLayout

from rich import print


def root_dir():
    return path.abspath(join(path.dirname(__file__), "..", ".."))


def highlight_missing_tags(foo):
    foo = f"[blue]{foo}[/blue]"
    foo = foo.replace("{{", "[/blue][red]{{")
    foo = foo.replace("}}", "}}[/red][blue]")
    return foo


def print_to_screen(template_name, metadata):
    templates_dir = join(root_dir(), "templates")

    partials_path = join(root_dir(), "partials")

    with open(join(templates_dir, template_name), "r") as template:
        args = {
            "template": template,
            "data": metadata,
            "partials_path": partials_path,
            "keep": True,
        }

        foo = chevron.render(**args)

        print(highlight_missing_tags(foo))


def main():
    data_dir = join(root_dir(), "demos", "data")

    data_path = join(data_dir, "ds000117")

    layout = BIDSLayout(data_path)

    print("\n[bold]ANAT[/bold]")
    files = layout.get(suffix="T1w", extension=".nii.gz")
    metadata = files[0].get_metadata()
    print_to_screen("anat.mustache", metadata)

    print("\n[bold]BOLD[/bold]")
    files = layout.get(suffix="bold", extension=".nii.gz", run=1)
    metadata = files[0].get_metadata()
    print_to_screen("func.mustache", metadata)

    print("\n[bold]DWI[/bold]")
    files = layout.get(suffix="dwi", extension=".nii.gz")
    metadata = files[0].get_metadata()
    print_to_screen("dwi.mustache", metadata)

    print("\n[bold]MEG[/bold]")
    files = layout.get(suffix="meg", run=1)
    metadata = files[0].get_metadata()
    print_to_screen("meeg.mustache", metadata)


if __name__ == "__main__":
    main()
