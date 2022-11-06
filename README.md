# rohr

Build easy data processing pipelines in python.

Example:
```python
import rohr

class CapitalizeNode(rohr.Node):
    def run(self, data: str) -> str:
        return data.capitalize()

class SpaceNode(rohr.Node):
    def run(self, data: str) -> str:
        return f'  {data}  '

pipeline = rohr.Pipeline()
pipeline.add(CapitalizeNode()).add(SpaceNode())

name = 'paul'

result = pipeline.run(name)
# result is `  Paul  `
print(result)
```
