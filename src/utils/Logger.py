# # src/utils/Logger.py

# from dotenv import load_dotenv
# from logfire import logfire
# from pydantic import Field
# from pydantic_settings import BaseSettings, SettingsConfigDict

# load_dotenv()


# class LoggerConfig(BaseSettings):
#     """Configuration class for Logfire and general logging settings."""

#     logfire_token: str = Field(alias="LOGFIRE_TOKEN")
#     log_level: str = Field(default="info", alias="LOG_LEVEL")
#     logfire_service_name: str = Field(
#         default="FireScribe", alias="LOGFIRE_SERVICE_NAME"
#     )
#     logfire_service_version: str = Field(
#         default="0.1.0", alias="LOGFIRE_SERVICE_VERSION"
#     )

#     model_config = SettingsConfigDict(
#         env_file=".env", env_file_encoding="utf-8"
#     )


# class Logger:
#     """Centralized logging utility using Pydantic for configuration and Logfire."""

#     _instance = None
#     config: LoggerConfig = LoggerConfig()

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(Logger, cls).__new__(cls)
#             cls._instance._initialize_logger()
#         return cls._instance

#     def _initialize_logger(self) -> None:
#         """Initializes the Logfire logger with the appropriate configurations."""
#         logfire.configure(
#             token=self.config.logfire_token,
#             service_name=self.config.logfire_service_name,
#             service_version=self.config.logfire_service_version,
#             console={"min_log_level": self.config.log_level},
#         )

#         # Example log to ensure the logger is initialized correctly
#         logfire.info(
#             "Logger initialized",
#             service=self.config.logfire_service_name,
#             version=self.config.logfire_service_version,
#         )

#     def get_logger(self):
#         """Return the configured Logfire logger."""
#         return logfire

#     def log_event(self, level: str, message: str, **attributes):
#         """General-purpose logging function."""
#         logfire.log(level, message, attributes)
#         logfire.log(level, message, attributes)
