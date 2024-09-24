from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class OpenAIConfig(BaseModel):
    """API-related configuration."""

    api_key: str = Field(default="src")
    assistant_id: str = Field(default="src")
    vector_store_id: str = Field(default="src")
    max_chunk_size_tokens: int = Field(default=0)
    chunk_overlap_tokens: int = Field(default=0)


class Settings(BaseSettings):
    """Main application settings that composes other config models."""

    base_path: str = Field(default="src")
    openai: OpenAIConfig = Field(default=OpenAIConfig())
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
