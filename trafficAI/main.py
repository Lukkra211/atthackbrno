#!/usr/bin/python3
import click

from control import Controller


@click.command()
@click.option('--system', type=click.Path(exists=True))
@click.option('--mode', type=click.Choice(['run', 'train']))
def main(system, mode):
    """
    TrafficAI command line tool
    """
    controller = Controller()
    controller.load_system(system)

    if mode == 'run':
        controller.present()
    elif mode == 'train':
        controller.develop()


if __name__ == '__main__':
    main()
