from graph import Node, buildGraph
from collections import deque

def search(startingNode, soughtValue, pile):
   visitedNodes = set()
   nodePile = pile()
   nodePile.add(startingNode)

   while len(nodePile) > 0:
      node = nodePile.remove()
      if node in visitedNodes:
         continue

      visitedNodes.add(node)
      if node.value == soughtValue:
         return True

      for n in node.adjacentNodes:
         if n not in visitedNodes:
            nodePile.add(n)
   return False

class MyStack(deque):
   def add(self, item):
      self.append(item)

   def remove(self):
      return self.pop()

class MyQueue(deque):
   def add(self, item):
      self.appendleft(item)

   def remove(self):
      return self.pop()

if __name__ == "__main__":
   depthFirst = lambda node, val: search(node, val, MyStack)
   breadthFirst = lambda node, val: search(node, val, MyQueue)

   vertices = ["A", "B", "C", "D", "E", "F"]
   edges = [("A","B"), ("B","C"), ("C","E"), ("E","D"), ("E","F"), ("D","B")]

   G = buildGraph(vertices, edges)

   print depthFirst(G, "F")
   print depthFirst(G, "G")
