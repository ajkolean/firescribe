# Firescribe

/FirewalkerProject/
│
├── /src/                     # Core logic and utilities
│   ├── /handlers/             # File handling and management
│   │   ├── FileHandler.py     # Handles file read/write, syncs with Watchdog
│   │   └── SyncHandler.py     # Automates syncing local and vector store
│   │
│   ├── /validation/           # JSON schema validation
│   │   ├── JsonValidator.py   # Validates JSON against schemas
│   │   └── SchemaLoader.py    # Loads and applies JSON Schemas
│   │
│   ├── /openai/               # OpenAI interaction wrapper
│   │   ├── OpenAIClient.py    # Wrapper for OpenAI's API (Assistants, Vector Store)
│   │   └── AssistantManager.py# Manages multiple assistants (Extractor, Refiner, etc.)
│   │
│   ├── /utils/                # Helper functions and utilities
│   │   ├── Logger.py          # Centralized logging
│   │   └── Config.py          # Configuration and environment variables
│   │
│   ├── main.py                # Main entry point for running the conversion
│   └── config.json            # Global configurations (paths, OpenAI API keys, etc.)
│
├── /schemas/                  # JSON Schemas for each entity type
│   ├── core_schema.json       # The core schema for all entities
│   ├── character_schema.json  # Character-specific schema
│   ├── location_schema.json   # Location-specific schema
│   └── ...                    # Additional schemas for events, arcs, etc.
│
├── /data/                     # Document storage (local sync with vector store)
│   ├── /old_docs/             # The original unconverted documents
│   ├── /converted_docs/       # Converted documents using the new schema
│   └── /logs/                 # Logs for validation and processing
│
├── /vector_store/             # Embeddings and vector store sync
│   └── embeddings.db          # Persistent local vector store for documents
│
├── .gitignore                 # To avoid tracking temporary, cache, or environment files
└── README.md                  # Instructions and documentation for developers
