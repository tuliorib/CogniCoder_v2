# src/core/document_store/factory.py

from typing import Dict, Any
from .document_store_impl import DocumentStoreImpl
from .backends.local_storage import LocalStorageBackend
from .interfaces import DocumentStore
from ..utils.config_handler import load_config

class DocumentStoreFactory:
    @staticmethod
    def create_document_store(config_path: str) -> DocumentStore:
        config = load_config(config_path)
        if config is None:
            raise ValueError("Failed to load configuration")

        storage_type = config.get('storage_type')
        if storage_type == 'local':
            backend = LocalStorageBackend(config.get('data_directory', './data'))
        elif storage_type == 'mongodb':
            # TODO: Implement MongoDB backend
            raise NotImplementedError("MongoDB storage not yet implemented")
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")

        return DocumentStoreImpl(backend)
