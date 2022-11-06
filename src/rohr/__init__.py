"""
rohr, build data processing pipelines fast and easy.
"""

from abc import ABC, abstractmethod

class Node(ABC):
    """
    Abstract Node class, to create nodes inherit from this class.
    """
    @abstractmethod
    def run(self, data):
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
        self.nodes: list[Node|callable] = list(args)

    def add(self, node: [Node,callable]) -> 'Pipeline':
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
            if isinstance(node, Node):
                result = node.run(result)
            else:
                result = node(result)

        return result

