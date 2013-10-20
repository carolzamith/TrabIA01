__author__ = 'Carol'


class Node:

    parent = None
    children = None
    name = ""

    def __init__(self,name):
        self.children = []
        self.name = name


    def set_parent(self, node):
        self.parent = node
        self.parent.children.append(self)

    def get_child(self, name):
        pass


    def bfs(self, search):
        # maintain a queue of paths
        queue = []
        # push the first path into the queue
        queue.append(self)
        while queue:
            # get the first path from the queue
            node = queue.pop(0)
            # path found
            if node.name == search:
                return node
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for adjacent in node.children:
                queue.append(adjacent)

        return None


    def backtrace(self, node):
        path = []
        while node.parent and node != self:
            path.append(node)
            node = node.parent

        path.append(self)
        path.reverse()
        return path


    def __repr__(self):
        return self.name