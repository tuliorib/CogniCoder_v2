from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class DocumentNotFoundError(Exception):
    pass

class DocumentStore(ABC):
    @abstractmethod
    def create(self, collection: str, document_id: str, data: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def read(self, collection: str, document_id: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def update(self, collection: str, document_id: str, data: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def delete(self, collection: str, document_id: str) -> None:
        pass

    @abstractmethod
    def list_documents(self, collection: str) -> List[str]:
        pass

class StorageBackend(ABC):
    @abstractmethod
    def save(self, collection: str, document_id: str, data: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def load(self, collection: str, document_id: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def remove(self, collection: str, document_id: str) -> None:
        pass

    @abstractmethod
    def list_all(self, collection: str) -> List[str]:
        pass
