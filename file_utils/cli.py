# -*- coding: utf-8 -*-

"""Console script for file_utils."""

import click


@click.command()
def main(args=None):
    """Console script for file_utils."""
    click.echo("Replace this message by putting your code into "
               "file_utils.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
