# tests/core/document_store/test_document_store.py

import os
import sys
import unittest

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, project_root)

from src.core.document_store.factory import DocumentStoreFactory
from src.core.document_store.interfaces import DocumentNotFoundError

class TestDocumentStore(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Get the path to the config file
        cls.config_path = os.path.join(project_root, 'config', 'document_store.config')
        
        # Ensure the config file exists
        if not os.path.exists(cls.config_path):
            raise FileNotFoundError(f"Config file not found: {cls.config_path}")

        # Create a DocumentStore instance
        cls.doc_store = DocumentStoreFactory.create_document_store(cls.config_path)

    def setUp(self):
        # Create a prompt template before each test
        self.doc_store.create('prompt_templates', 'code_generation', {
            'name': 'Code Generation',
            'template': 'Generate a {language} function that {task}.'
        })

    # def tearDown(self):
    #     # Clean up after each test
    #     try:
    #         self.doc_store.delete('prompt_templates', 'code_generation')
    #     except DocumentNotFoundError:
    #         pass  # If it's already deleted, that's fine

    def test_create_and_read_document(self):
        # Read the prompt template
        template = self.doc_store.read('prompt_templates', 'code_generation')
        self.assertIsNotNone(template)
        self.assertEqual(template['name'], 'Code Generation')
        self.assertEqual(template['template'], 'Generate a {language} function that {task}.')

    def test_list_documents(self):
        # List all prompt templates
        templates = self.doc_store.list_documents('prompt_templates')
        self.assertIn('code_generation', templates)

    def test_update_document(self):
        # Update the prompt template
        self.doc_store.update('prompt_templates', 'code_generation', {
            'name': 'Updated Code Generation',
            'template': 'Create a {language} function to {task}.'
        })

        # Read the updated template
        updated_template = self.doc_store.read('prompt_templates', 'code_generation')
        self.assertEqual(updated_template['name'], 'Updated Code Generation')
        self.assertEqual(updated_template['template'], 'Create a {language} function to {task}.')

    # def test_delete_document(self):
    #     # Delete the prompt template
    #     self.doc_store.delete('prompt_templates', 'code_generation')

    #     # Try to read the deleted template
    #     with self.assertRaises(DocumentNotFoundError):
    #         self.doc_store.read('prompt_templates', 'code_generation')

if __name__ == "__main__":
    unittest.main()
