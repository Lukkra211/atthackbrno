#!/usr/bin/python3
import click

from control import Controller


@click.command()
@click.option('--system', type=click.Path(exists=True))
@click.option('--ai', type=click.Path(writable=True))
@click.option('--mode', type=click.Choice(['run', 'train']))
@click.option('--dark', type=click.Choice(['y', 'n']))

def main(system, ai, mode, dark):
    """
    TrafficAI command line tool
    """
    controller = Controller()
    controller.load_system(system, ai)

    if mode == 'run':
        controller.present(dark)
    elif mode == 'train':
        controller.develop()

if __name__ == '__main__':
    main()
