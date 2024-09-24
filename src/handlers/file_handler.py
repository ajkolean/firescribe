import json
import logging
import os
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class FileHandler:
    """Utility class for handling file operations."""

    @staticmethod
    def read_json(file_path: str) -> dict[str, Any]:
        """Reads a JSON file and returns its content."""
        full_path = FileHandler.get_full_path(file_path)
        logger.info(f"Reading JSON file from {full_path}")
        try:
            with open(full_path, "r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            logger.error(f"File not found: {full_path}")
            raise
        except Exception as e:
            logger.exception(f"Error reading JSON file {full_path}: {e}")
            raise

    @staticmethod
    def write_json(file_path: str, data: dict[str, Any]) -> None:
        """Writes a dictionary to a JSON file with indentation."""
        full_path = FileHandler.get_full_path(file_path)
        logger.info(f"Writing JSON file to {full_path}")
        try:
            with open(full_path, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4)
        except Exception as e:
            logger.exception(f"Error writing JSON file {full_path}: {e}")
            raise

    @staticmethod
    def read_text(file_path: str) -> str:
        """Reads a text file and returns its content as a string."""
        full_path = FileHandler.get_full_path(file_path)
        logger.info(f"Reading text file from {full_path}")
        try:
            with open(full_path, "r", encoding="utf-8") as text_file:
                return text_file.read()
        except FileNotFoundError:
            logger.error(f"File not found: {full_path}")
            raise
        except Exception as e:
            logger.exception(f"Error reading text file {full_path}: {e}")
            raise

    @staticmethod
    def write_text(file_path: str, content: str) -> None:
        """Writes a string to a text file."""
        full_path = FileHandler.get_full_path(file_path)
        logger.info(f"Writing text file to {full_path}")
        try:
            with open(full_path, "w", encoding="utf-8") as text_file:
                text_file.write(content)
        except Exception as e:
            logger.exception(f"Error writing text file {full_path}: {e}")
            raise

    @staticmethod
    def file_exists(file_path: str) -> bool:
        """Checks if a file exists at the given path."""
        full_path = FileHandler.get_full_path(file_path)
        exists = os.path.isfile(full_path)
        logger.info(f"Checking if file exists at {full_path}: {exists}")
        return exists

    @staticmethod
    def create_directory(directory_path: str) -> None:
        """Creates a directory if it doesn't exist, handling any exceptions."""
        full_path = FileHandler.get_full_path(directory_path)
        logger.info(f"Creating directory at {full_path}")
        try:
            os.makedirs(full_path, exist_ok=True)
        except OSError as e:
            logger.error(f"Error creating directory {full_path}: {e}")
            raise

    @staticmethod
    def get_full_path(relative_path: str) -> str:
        """Constructs the full path using the base path from Config."""
        # Assuming there's a BASE_PATH defined somewhere
        base_path = Path.cwd()
        full_path = os.path.abspath(os.path.join(base_path, relative_path))
        logger.debug(f"Full path for {relative_path}: {full_path}")
        return full_path
