import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.argument('name')
def hello(count, name):
    """Simple program that greets a NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!") # Use click.echo for consistent output

if __name__ == '__main__':
    hello()
