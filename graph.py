
class Node:
   def __init__(self, value):
      self.value = value
      self.adjacentNodes = []


def buildGraph(vertexNames, edges):
   vertices = dict([(vertexNames[i], Node(vertexNames[i])) for i in range(len(vertexNames))])

   for name in vertices:
      vertices[name].value = name

   for (v,w) in edges:
      vertices[v].adjacentNodes.append(vertices[w])

   return vertices[vertexNames[0]]

