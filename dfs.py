from graph import Node, buildGraph

class FoundNodeException(Exception):
   pass

def recursiveDepthFirst(node, soughtValue):
   try:
      recursiveDepthFirstWorker(node, soughtValue, set())
      return False
   except FoundNodeException:
      return True

def recursiveDepthFirstWorker(node, soughtValue, visitedNodes):
   if node.value == soughtValue:
      raise FoundNodeException()

   visitedNodes.add(node)

   for adjNode in node.adjacentNodes:
      if adjNode not in visitedNodes:
         recursiveDepthFirstWorker(adjNode, soughtValue, visitedNodes)


def depthFirst(startingNode, soughtValue):
   ''' Using a stack. '''
   visitedNodes = set()
   stack = [startingNode]

   while len(stack) > 0:
      node = stack.pop()
      if node in visitedNodes:
         continue

      visitedNodes.add(node)
      if node.value == soughtValue:
         return True

      for n in node.adjacentNodes:
         if n not in visitedNodes:
            stack.append(n)
   return False

if __name__ == "__main__":
   vertices = ["A", "B", "C", "D", "E", "F"]
   edges = [("A","B"), ("B","C"), ("C","E"), ("E","D"), ("E","F"), ("D","B")]

   G = buildGraph(vertices, edges)
   print recursiveDepthFirst(G, "F")
   print recursiveDepthFirst(G, "G")

   print depthFirst(G, "F")
   print depthFirst(G, "G")
