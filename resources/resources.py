from pathlib import Path


def path(picture):
    return str(Path(__file__).parent.joinpath(picture))
