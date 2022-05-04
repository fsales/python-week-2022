import typer
from beerlog.core import add_beer_to_database

main = typer.Typer(help="Beerr Management Application")


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database."""
    if add_beer_to_database(name, style, flavor, image, cost):
        print("🍺 beer added to database")
   # else:
   #    print("\N{no_entry}")
@main.command("list")
def list_beers(style: str):
    """Lists beers in database"""
    print(style)
