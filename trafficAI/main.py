#!/usr/bin/python3
import click

from control import Controller


@click.command()
@click.option('--system', type=click.Path(exists=True))
@click.option('--ai', type=click.Path(writable=True))
@click.option('--mode', type=click.Choice(['run', 'train']))
@click.option('--time', default=0, help='How long the ai will learn')
def main(system, ai, mode, time):
    """
    TrafficAI command line tool
    """
    controller = Controller()
    controller.load_system(system, ai)

    if mode == 'run':
        controller.present()
    elif mode == 'train':
        if time != 0:
            controller.develop_by_time(time)
        else:
            controller.develop()


if __name__ == '__main__':
    main()
