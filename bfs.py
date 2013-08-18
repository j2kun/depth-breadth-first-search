from graph import Node, buildGraph
from collections import deque

def breadthFirst(startingNode, soughtValue):
   visitedNodes = set()
   queue = deque([startingNode])

   while len(queue) > 0:
      node = queue.pop()
      if node in visitedNodes:
         continue

      visitedNodes.add(node)
      if node.value == soughtValue:
         return True

      for n in node.adjacentNodes:
         if n not in visitedNodes:
            queue.appendleft(n)
   return False

if __name__ == "__main__":
   vertices = ["A", "B", "C", "D", "E", "F"]
   edges = [("A","B"), ("B","C"), ("C","E"), ("E","D"), ("E","F"), ("D","B")]

   G = buildGraph(vertices, edges)

   print breadthFirst(G, "F")
   print breadthFirst(G, "G")
