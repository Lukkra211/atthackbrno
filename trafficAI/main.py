import click

from control import Controller


@click.argument('--system', type=click.Path(exists=True))
def main(system):
    controller = Controller()
    controller.load_system(system)


if __name__ == '__main__':
    main()
