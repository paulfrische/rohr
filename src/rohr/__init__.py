"""
rohr, build data processing pipelines fast and easy.
"""

from abc import ABC, abstractmethod

class Node(ABC):
    """
    Abstract Node class, to create nodes inherit from this class.
    """
    @abstractmethod
    def run(self, data) -> None:
        """
        Method to process given data.
        """

class Pipeline:
    """
    Pipeline class to process data with given nodes.
    """

    def __init__(self, *args: tuple[Node]) -> None:
        """
        Construct pipeline with given nodes.
        """
        self.nodes: list[Node] = list(args)

    def add(self, node: Node) -> 'Pipeline':
        """
        Add node to pipeline.
        """
        self.nodes.append(node)
        return self

    def run(self, data):
        """
        Processes given data and returns results. When data is mutable it will mutate it.
        """
        result = data
        for node in self.nodes:
            result = node.run(data)

        return result

