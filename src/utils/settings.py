from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class OpenAIConfig(BaseModel):
    """API-related configuration."""

    api_key: str
    assistant_id: str
    vector_store_id: str
    max_chunk_size_tokens: int
    chunk_overlap_tokens: int


class Settings(BaseSettings):
    """Main application settings that composes other config models."""

    base_path: str = Field(default=...)
    openai: OpenAIConfig = Field(default=...)

    model_config = SettingsConfigDict(
        env_nested_delimiter="__",  # Allows for nested variables
    )


settings = Settings()
