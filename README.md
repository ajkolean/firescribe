# Firescribe

pip3 install openai tiktoken watchdog jsonschema PyYAML requests python-dotenv loguru black pylint

# Packages

pip3 install tiktoken

Here's a revised and detailed file tree based on your latest input, with comments explaining each part:

/firescribe/ # Root directory of the Firewalker Project
│
├── /src/ # Core logic and utilities
│ ├── /handlers/ # File handling and management
│ │ ├── FileHandler.py # Handles file read/write and general file operations
│ │ └── SyncHandler.py # Automates syncing local files and vector store
│ │
│ ├── /validation/ # JSON schema validation
│ │ ├── JsonValidator.py # Validates JSON documents against schemas
│ │ └── SchemaLoader.py # Loads and applies JSON Schemas to documents
│ │
│ ├── /openai_service/ # OpenAI interaction wrapper and assistants
│ │ ├── OpenAIService.py # Wrapper for OpenAI's API (Assistants, Vector Store)
│ │ └── AssistantManager.py # Manages the interaction with multiple assistants
│ │
│ ├── /assistants/ # Directory for assistant-specific functionality
│ │ ├── Extractor.py # Assistant A: Handles extracting data from documents
│ │ ├── Transformer.py # Assistant B: Transforms extracted data to fit the new schema
│ │ ├── Refiner.py # Assistant C: Refines transformed data and ensures high-level consistency
│ │ └── Validator.py # Assistant D: Final validation, consistency checks, and writing to vector store
│ │
│ ├── /utils/ # Helper functions and utilities
│ │ ├── Logger.py # Centralized logging for the entire project
│ │ └── Config.py # Configuration handling (environment variables, paths, etc.)
│ │
│ ├── main.py # Main entry point for running the migration process
│ └── config.json # Global configurations (paths, OpenAI API keys, schema paths, etc.)
│
├── /schemas/ # JSON Schemas for entity types (used by Validator.py and SchemaLoader.py)
│ ├── core_schema.json # The core schema for all entities
│ ├── character_schema.json # Schema specific to character entities
│ ├── location_schema.json # Schema specific to location entities
│ └── event_schema.json # Schema specific to events
│
├── /data/ # Document storage (syncs with the vector store)
│ ├── /migrated_documents/ # Documents that have been successfully migrated using the new schema
│ ├── /assistant_output/ # Directory for storing data produced by each assistant (before validation)
│ │ ├── Extractor/ # Output from Assistant A (extracted data)
│ │ ├── Transformer/ # Output from Assistant B (transformed data, fitting the schema)
│ │ └── Refiner/ # Output from Assistant C (refined and pre-validated data)
│ │
│ └── /vector_sync/ # Directory where Assistant D writes to sync with vector store
│ └── embeddings.db # Local persistent vector store for documents (embeddings)
│
├── /logs/ # Logs for validation, processing, and assistant activity
│ ├── validation.log # Logs related to JSON validation and schema conformity
│ ├── processing.log # Logs for document processing and migrations
│ ├── assistant_activity.log # Logs specific to the actions of Assistants A, B, C, and D
│
├── .gitignore # To avoid tracking temporary, cache, or environment files
└── README.md # Instructions and documentation for developers

```

### Key Updates:
1. **No source documents**: Since you mentioned source documents are stored elsewhere and used directly from the vector store, I've removed that section.
2. **/assistants/**: Added a directory specifically for assistant scripts (Extractor, Transformer, Refiner, Validator). Each has a clear role in the migration process, and I've added an **assistant_output** directory for storing intermediate results.
3. **/vector_sync/**: Moved to hold the final, validated documents that Assistant D ensures are consistent and ready for the vector store.
4. **/logs/**: Now logs are at the top level and include assistant-specific logs, validation logs, and overall process logs.

### Summary of the File Tree Flow:
- **Extractor (Assistant A)** processes documents from the vector store, outputs initial data in `/assistant_output/Extractor/`.
- **Transformer (Assistant B)** reformats the extracted data to match the new schema.
- **Refiner (Assistant C)** refines the transformed data, improving consistency before validation.
- **Validator (Assistant D)** runs a final consistency check and ensures everything is ready for the vector store, saving in `/vector_sync/`.

This structure ensures each assistant has its dedicated role and space, making it easy to trace the migration process from extraction to validation.
```
