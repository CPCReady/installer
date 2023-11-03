
import click
from CPCReady import __version__
from CPCReady import func_run as emulador
from CPCReady import func_palette as pal
from CPCReady import func_sprite as sprites
from CPCReady import func_screen as screens
from CPCReady import func_project as projects
from CPCReady import func_build as compile
from CPCReady import func_info as information
from CPCReady import func_update as update
from CPCReady import common as cm
import logging
import requests

requests.packages.urllib3.disable_warnings()
logging.getLogger("requests").setLevel(logging.WARNING)

@click.version_option(version=__version__)

@click.group()
def main():
    """ CLI SDK for programming in Amstrad Locomotive Basic and Compiled Basic with Ugbasic. """

@main.command()
@click.option('--file', '-f',   required=False, help="File with emulator configurations")
@click.option('--setting', '-s',required=True,  help="Emulator Settings Name")

def run(file, setting):
    """ Execute DSK/CDT in emulator. """
    try:
        if not file:
            file = cm.CFG_EMULATORS
        emulador.launch(file,setting)
    except Exception as e:
        raise Exception(f"Error {str(e)}")

@main.command()
@click.option("-i", "--image", "image", type=click.STRING, help="Input file name",required=True)
@click.option("-m", "--mode", "mode",   type=click.Choice(["0","1","2"]), help="Image Mode (0, 1, 2)",required=True)

def palette(image, mode):
    """ Extract the color palette from the image. """
    pal.getData(image, mode)


@main.command()
@click.option("-i", "--image", type=click.STRING, help="Input file name",required=True)
@click.option("-m", "--mode",  type=click.Choice(["0","1","2"]), help="Image Mode (0, 1, 2)",required=True)
@click.option("-o", "--out",   type=click.STRING, help="Out path file name",required=True)
@click.option("-h", "--height",type=click.INT, help="Height sprite size",required=True)
@click.option("-w", "--width", type=click.INT, help="Width sprite size",required=True)

def sprite(image, mode, out, height, width):
    """ Extract the color palette from the image. """
    sprites.create(image, mode, out, height, width)

@main.command()
@click.option("-i", "--image", type=click.STRING, help="Input file name.",required=True)
@click.option("-m", "--mode",  type=click.Choice(["0","1","2"]), help="Image Mode (0, 1, 2)",required=True)
@click.option("-o", "--out",   type=click.STRING, help="Out path file name.",required=True)
@click.option("-d", "--dsk",   is_flag=True, help="Generate DSK with only the scr image.",required=False)


def screen(image, mode, out, dsk):
    """ Convert an image to Amstrad scr format. """
    screens.create(image, mode, out, dsk)

@main.command()

def project():
    """ Create the project structure for CPCReady. """
    projects.create()

@main.command()
@click.option("-s", "--scope",  default="all", type=click.Choice(["dsk","cdt","all"]), help="Scope of creating disk and tape images.",required=False)

def build(scope):
    """ Create project disk and cdt image. """
    try:
        compile.create(scope)
    except Exception as e:
        raise Exception(f"Error {str(e)}")

@main.command()

def info():
    """ Show infor CPCReady. """
    try:
        information.show(True)
    except Exception as e:
        raise Exception(f"Error {str(e)}")


@main.command()
def upgrade():
    """ Upgrade CPCReady. """
    try:
        update.version(False)
    except Exception as e:
        raise Exception(f"Error {str(e)}")


if __name__ == '__main__':
    main()