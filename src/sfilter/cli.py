import click

from src.sfilter.main import run_all


@click.command()
@click.argument("path")
def main(path):
    run_all(path)
