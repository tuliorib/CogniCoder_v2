from typing import Any, Dict, List
from .interfaces import DocumentStore, StorageBackend, DocumentNotFoundError

class DocumentStoreImpl(DocumentStore):
    def __init__(self, storage_backend: StorageBackend):
        self.storage = storage_backend

    def create(self, collection: str, document_id: str, data: Dict[str, Any]) -> None:
        self.storage.save(collection, document_id, data)

    def read(self, collection: str, document_id: str) -> Dict[str, Any]:
        return self.storage.load(collection, document_id)

    def update(self, collection: str, document_id: str, data: Dict[str, Any]) -> None:
        self.storage.save(collection, document_id, data)

    def delete(self, collection: str, document_id: str) -> None:
        self.storage.remove(collection, document_id)

    def list_documents(self, collection: str) -> List[str]:
        return self.storage.list_all(collection)
