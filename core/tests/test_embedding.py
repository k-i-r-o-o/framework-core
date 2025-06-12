import pytest
from core.types.embedding import Embedding

def test_embedding_attributes():
    vector = [0.1, 0.2, 0.3, 0.4]
    model = "test-model"

    embedding = Embedding(vector=vector, model_name=model)

    # Assert attributes directly
    assert embedding.vector == vector
    assert embedding.model_name == model

    # Assert via methods
    assert embedding.get_vector() == vector
    assert embedding.get_model_name() == model
