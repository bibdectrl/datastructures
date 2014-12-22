class Vertex:
    def __init__(self, key):
        self.key = key
        self.connections = {}

    def addNeighbour(self, vert, weight = 0):
        self.connections[vert] = weight

    def __str__(self):
        return str(self.key) + " connected to " + str([vert.key for vert in self.connections])

    def getConnections(self):
        return self.connections.keys()

    def getID(self):
        return self.key
    
    def getWeight(self, neighbour):
        return self.connections[neighbour]
            

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newvertex = Vertex(key)
        self.vertices[key] = newvertex
        return newvertex

    def addEdge(self, fromVert, toVert, weight = 0):
        if fromVert not in self.vertices:
            nv = self.addVertex(fromVert)
        if toVert not in self.vertices:
            nv = self.addVertex(toVert)
        self.vertices[fromVert].addNeighbour(self.vertices[toVert], weight)              

    def getVertex(self, vertkey):
        if vertkey in self.vertices:
            return self.vertices[vertkey]
        else:
            return None

    def __contains__(self, vert):
        return vert in self.vertices


    def getVertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.value())

        

       
