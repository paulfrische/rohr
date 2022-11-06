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
    return rohr.Pipeline()

def test_basic_pipeline_functionality(pipeline):
    pipeline.add(CapitalizeNode()).add(SpaceNode())
    test_string = 'test'
    result = pipeline.run(test_string)
    assert result == '  Test  '
