import json
import os
from pathlib import Path
from typing import Any, Dict, List
from ..interfaces import StorageBackend, DocumentNotFoundError

class LocalStorageBackend(StorageBackend):
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)

    def _ensure_collection_path(self, collection: str) -> Path:
        path = self.base_path / collection
        path.mkdir(parents=True, exist_ok=True)
        return path

    def save(self, collection: str, document_id: str, data: Dict[str, Any]) -> None:
        path = self._ensure_collection_path(collection) / f"{document_id}.json"
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)

    def load(self, collection: str, document_id: str) -> Dict[str, Any]:
        path = self._ensure_collection_path(collection) / f"{document_id}.json"
        if not path.exists():
            raise DocumentNotFoundError(f"Document {document_id} not found in {collection}")
        with open(path, 'r') as f:
            return json.load(f)

    def remove(self, collection: str, document_id: str) -> None:
        path = self._ensure_collection_path(collection) / f"{document_id}.json"
        if not path.exists():
            raise DocumentNotFoundError(f"Document {document_id} not found in {collection}")
        path.unlink()

    def list_all(self, collection: str) -> List[str]:
        path = self._ensure_collection_path(collection)
        return [f.stem for f in path.glob('*.json')]
