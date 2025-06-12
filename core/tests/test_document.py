# tests/test_document.py

import pytest
from core.types.document import Document

def test_document_fields_and_methods():
    doc_id = "doc-123"
    content = "This is a test document."
    metadata = {"source": "unit_test", "page": 1}

    # Instantiate Document
    doc = Document(id=doc_id, text=content, metadata=metadata)

    # Assertions for fields
    assert doc.id == doc_id
    assert doc.text == content
    assert doc.metadata == metadata

    # Assertions for methods
    assert doc.get_id() == doc_id
    assert doc.get_content() == content
    assert doc.get_metadata() == metadata
