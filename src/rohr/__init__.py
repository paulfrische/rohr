"""
rohr, build data processing pipelines fast and easy
"""

from abc import ABC, abstractmethod

class Node(ABC):
    """
    Abstract Node class, to create nodes inherit from this class
    """
    @abstractmethod
    def run(self, data) -> None:
        """
        Method to process given data
        """
