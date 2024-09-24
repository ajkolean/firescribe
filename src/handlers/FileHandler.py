import json
import os
from typing import Any

from src.utils.settings import settings


class FileHandler:
    """Utility class for handling file operations."""

    @staticmethod
    def read_json(file_path: str) -> dict[str, Any]:
        """Reads a JSON file and returns its content."""
        full_path = FileHandler.get_full_path(file_path)
        with open(full_path, "r", encoding="utf-8") as json_file:
            return json.load(json_file)

    @staticmethod
    def write_json(file_path: str, data: dict[str, Any]) -> None:
        """Writes a dictionary to a JSON file with indentation."""
        full_path = FileHandler.get_full_path(file_path)
        with open(full_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def read_text(file_path: str) -> str:
        """Reads a text file and returns its content as a string."""
        full_path = FileHandler.get_full_path(file_path)
        with open(full_path, "r", encoding="utf-8") as text_file:
            return text_file.read()

    @staticmethod
    def write_text(file_path: str, content: str) -> None:
        """Writes a string to a text file."""
        full_path = FileHandler.get_full_path(file_path)
        with open(full_path, "w", encoding="utf-8") as text_file:
            text_file.write(content)

    @staticmethod
    def file_exists(file_path: str) -> bool:
        """Checks if a file exists at the given path."""
        full_path = FileHandler.get_full_path(file_path)
        return os.path.isfile(full_path)

    @staticmethod
    def create_directory(directory_path: str) -> None:
        """Creates a directory if it doesn't exist, handling any exceptions."""
        full_path = FileHandler.get_full_path(directory_path)
        try:
            os.makedirs(full_path, exist_ok=True)
        except OSError as e:
            print(f"Error creating directory {full_path}: {e}")

    @staticmethod
    def get_full_path(relative_path: str) -> str:
        """Constructs the full path using the base path from Config."""
        return os.path.abspath(os.path.join(settings.base_path, relative_path))


# Example usage
if __name__ == "__main__":
    FileHandler.create_directory("data")

    json_data = {"name": "FireScribe", "version": "0.1.0"}
    FileHandler.write_json("data/info.json", json_data)

    if FileHandler.file_exists("data/info.json"):
        loaded_json = FileHandler.read_json("data/info.json")
        print(f"Loaded JSON: {loaded_json}")

    FileHandler.write_text("data/info.txt", "This is FireScribe's data.")

    if FileHandler.file_exists("data/info.txt"):
        loaded_text = FileHandler.read_text("data/info.txt")
        print(f"Loaded Text: {loaded_text}")
