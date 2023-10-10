import importlib.metadata
import os

from typer import Typer

_DISTRIBUTION_METADATA = importlib.metadata.metadata("tvsd")

# author = _DISTRIBUTION_METADATA["Author"]
# project = _DISTRIBUTION_METADATA["Name"]
__version__ = _DISTRIBUTION_METADATA["Version"]
__app_name__ = "tvsd"


app = Typer(name=__name__, rich_markup_mode="rich")
state = {
    "verbose": False,
    "series_dir": "TV Series",
    "specials_dir": "Specials",
    "base_path": "/Volumes/Viewable",
    "temp_base_path": "/Volumes/Viewable/temp",
}
current_dir = os.getcwd()

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(7)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
    ID_ERROR: "to-do id error",
}
