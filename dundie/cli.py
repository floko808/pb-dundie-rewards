import json
import warnings

import pkg_resources
import rich_click as click
from rich.console import Console
from rich.table import Table
from sqlalchemy.exc import SAWarning
from sqlmodel.sql.expression import Select, SelectOfScalar

from dundie import core

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

warnings.filterwarnings("ignore", category=SAWarning)

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True


@click.group()
@click.version_option(pkg_resources.get_distribution("dundie").version)
def main():
    """Dunder Mifflin Rewards System
    This cli application controls DM rewards
    """


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Loads the file to the database

    - Validates data
    - Parses the file
    - Loads to database

    `dundie load <path to the file>`

    ie: path/to_the_file/file.csv
    """
    table = Table(title="Dunder Mifflin Associates")
    headers = ["email", "name", "dept", "role", "currency", "created"]
    for header in headers:
        table.add_column(header, style="green")

    result = core.load(filepath)
    for person in result:
        table.add_row(*[str(value) for value in person.values()], style="red")
    console = Console()
    console.print(table)


@main.command()
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.option("--output", default=None)
def show(output, **query):
    """Shows data stored in the database"""
    result = core.read(**query)
    if output:
        with open(output, "w") as output_file:
            output_file.write(json.dumps(result))
    if not result:
        print(f"nothing to show: {result}")

    table = Table(title="Dunder Mifflin Report")
    for key in result[0]:
        table.add_column(key.title(), style="magenta")

    for person in result:
        person["value"] = f"{person['value']:.2f}"
        person["balance"] = f"{person['balance']:.2f}"
        table.add_row(*[str(value) for value in person.values()])
    console = Console()
    console.print(table)


@main.command()
@click.argument("value", type=int, required=True)
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.pass_context
def add(ctx, value, **query):
    """Add points to the user or department"""
    core.add(value, **query)
    ctx.invoke(show, **query)


@main.command()
@click.argument("value", type=int, required=True)
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.pass_context
def remove(ctx, value, **query):
    """Add points to the user or department"""
    core.remove(-value, **query)
    ctx.invoke(show, **query)
