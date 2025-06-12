from abc import ABC, abstractmethod
from typing import List


class IEmbedding(ABC):
    """
    Interface for embedding representation.
    """

    @abstractmethod
    def get_vector(self) -> List[float]:
        """
        Returns the embedding vector.

        :return: List of floats representing the embedding vector.
        """
        pass

    @abstractmethod
    def get_model_name(self) -> str:
        """
        Returns the name of the model that produced the embedding.

        :return: Model name as a string.
        """
        pass
