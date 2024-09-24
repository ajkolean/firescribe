from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Config(BaseSettings):
    """Class to store and access configuration variables."""

    OPENAI_API_KEY: str
    ASSISTANT_ID: str
    VECTOR_STORE_ID: str
    MAX_CHUNK_SIZE_TOKENS: int
    CHUNK_OVERLAP_TOKENS: int
    BASE_PATH: str
    FILE_HASHES_PATH: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )

    def print_config(self) -> None:
        """Utility function to print current config variables."""
        print(f"OpenAI API Key: {self.OPENAI_API_KEY}")
        print(f"Assistant ID: {self.ASSISTANT_ID}")
        print(f"Vector Store ID: {self.VECTOR_STORE_ID}")
        print(f"Max Chunk Size: {self.MAX_CHUNK_SIZE_TOKENS}")
        print(f"Chunk Overlap: {self.CHUNK_OVERLAP_TOKENS}")
        print(f"Base Path: {self.BASE_PATH}")
        print(f"File Hashes Path: {self.FILE_HASHES_PATH}")
