import pytest

import rohr

class CapitalizeNode(rohr.Node):
    def run(self, data: str) -> str:
        return data.capitalize()

class SpaceNode(rohr.Node):
    def run(self, data: str) -> str:
        return f'  {data}  '

@pytest.fixture
def pipeline():
    return rohr.Pipeline(CapitalizeNode(), SpaceNode())

def test_basic_pipeline_functionality(pipeline):
    test_string = 'test'
    result = pipeline.run(test_string)
    assert result == '  Test  '

def test_pipeline_function_nodes(pipeline):
    def xx_node(data: str) -> str:
        return f'xX{data}Xx'

    pipeline.add(xx_node)
    test_string = 'test'
    result = pipeline.run(test_string)
    assert result == 'xX  Test  Xx'
