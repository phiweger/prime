'''
prime command line.
'''


import click
# https://kushaldas.in/posts/building-command-line-tools-in-python-with-click.html


from prime.batch import batch
from prime.gather import gather
from prime.tm import tm


@click.group()
def cli():
    pass


cli.add_command(batch)
cli.add_command(gather)
cli.add_command(tm)
