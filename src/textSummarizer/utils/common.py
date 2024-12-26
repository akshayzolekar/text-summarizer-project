import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, Optional


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads the yaml file and returns

    Parameters
    ----------
    path_to_yaml: str
        path like input

    Raises
    ------
    ValueError
        If yaml is empty
    e
        empty file

    Returns
    -------
    ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    create a list of directories

    Parameters
    ----------
    path_to_directories: list
        list of path of directories
    verbose: bool
        verbose
    Returns
    -------
    None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB

    Parameters
    ----------
    path: Path
        path of the file

    Returns
    -------
    size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"