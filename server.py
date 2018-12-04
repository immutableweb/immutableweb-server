#!/usr/bin/env python3

import click

from immutablewebserver import runserver


@click.command()
@click.option('--host', default="0.0.0.0", help='which host IP to bind to.')
@click.option('--port', default=8080, help='which port to bind to.')
@click.option('--debug', default=True, help='turn on debug mode')
def run(host, port, debug):
    runserver(host, port, debug)


if __name__ == "__main__":
    run()
