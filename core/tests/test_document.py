from core.types.document import Document
from core.interfaces.data.document import IDocument

def test_document_interface_compliance():
    doc = Document(id="1", text="hello", metadata={"source": "unit_test"})
    assert isinstance(doc, IDocument)
    assert doc.get_id() == "1"
    assert doc.get_content() == "hello"
    assert doc.get_metadata()["source"] == "unit_test"
