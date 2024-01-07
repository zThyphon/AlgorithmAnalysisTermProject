def dijkstraAlgorithm(adjacencyMatrix, neighborHoodMatrix, sourceNode, destinationNode):
    #Get how many vertices exists
    numberOfVertices = len(adjacencyMatrix)

    #Assign as infinity for non-relaxed edges
    distanceToEdges = [float("inf") for x in range(numberOfVertices)]
    #Assign false for non-visited nodes
    visited = [False for x in range(numberOfVertices)]

    distanceToEdges[sourceNode] = 0

    #Assign an array for recording visitedNodes
    visitedNodes = []

    while True:
        """
        Assigning shortest distance as infinity
        because it isn't relaxed
        """
        shortestDistance = float("inf")
        shortestIndex = -1

        #Checks non visited edges
        for i in range(numberOfVertices):
            if distanceToEdges[i] < shortestDistance and not visited[i]:
                shortestDistance = distanceToEdges[i]
                shortestIndex = i

        if shortestIndex == -1:
            return distanceToEdges, visitedNodes

        #Relaxation
        for i in range(numberOfVertices):
            if adjacencyMatrix[shortestIndex][i] == 1 and distanceToEdges[i] > distanceToEdges[shortestIndex] + neighborHoodMatrix[shortestIndex][i]:
                distanceToEdges[i] = distanceToEdges[shortestIndex] + neighborHoodMatrix[shortestIndex][i]

        visited[shortestIndex] = True
        visitedNodes.append(shortestIndex)

        if visited[destinationNode]:
            break

    """
    Calculating total distance between
    source node and destination node
    """
    totalDistance = 0
    for distance in distanceToEdges:
        if (distance != float("inf")):
            totalDistance = totalDistance+distance

    return totalDistance, visitedNodes



def bellmanFordAlgorithm(adjacencyMatrix, neighborhoodMatrix, delayMatrix, sourceNode, destinationNode):
    #Get how many vertices exists
    numberOfVertices = len(adjacencyMatrix)
    #Assign as infinity for non-relaxed edges
    distances = [float("inf")] * numberOfVertices
    distances[sourceNode] = 0
    # Assign visited list of edges
    listOfEdges = [None] * numberOfVertices 

    # Relax edges (V-1) times
    for x in range(numberOfVertices - 1):
        for i in range(numberOfVertices):
            for j in range(numberOfVertices):
                if adjacencyMatrix[i][j] == 1 and distances[j] > distances[i] + neighborhoodMatrix[i][j]:
                    distances[j] = distances[i] + adjacencyMatrix[i][j]
                    listOfEdges[j] = i 

    """
    Check for negative cycles
    because it will cause infinity loop in algorithm
    """                
    for i in range(numberOfVertices):
        for j in range(numberOfVertices):
            if adjacencyMatrix[i][j] == 1 and distances[j] > distances[i] + neighborhoodMatrix[i][j]:
                return [], True  # Negative cycle detected

    #Construction of the visited nodes
    visitedNodes = []
    currentNode = destinationNode
    while currentNode is not None:
        visitedNodes.append(currentNode)
        currentNode = listOfEdges[currentNode]
    visitedNodes.reverse()

    #Construction of the path
    visitedPaths = []
    for i in range(0,len(visitedNodes)-1):
        visitedPath = []
        for j in range(i,i+2):
            visitedPath.append(visitedNodes[j])
        visitedPaths.append(visitedPath)

    #Calculation of total distance and total delay
    totalDistance = 0
    totalDelay = 0
    for path in visitedPaths:
        startNode = path[0]
        endNode = path[1]
        totalDistance += neighborhoodMatrix[startNode][endNode]
        totalDelay += delayMatrix[startNode][endNode]
    return totalDistance, totalDelay, visitedNodes

def floydWarshallAlgorithm(adjacencyMatrix, neighborhoodMatrix, delayMatrix, startNode, endNode):
    #Get how many vertices exists
    numberOfVertices = len(adjacencyMatrix)

    """
    Assigning distance matrix 
    with values from neighborhoodMatrix
    """
    distanceMatrix = [
        [float("inf") for x in range(numberOfVertices)] 
        for x in range(numberOfVertices)]
    
    #Assigning distance matrix 
    for i in range(numberOfVertices):
        for j in range(numberOfVertices):
            if i == j:
                distanceMatrix[i][j] = 0
            elif adjacencyMatrix[i][j] == 1:
                distanceMatrix[i][j] = neighborhoodMatrix[i][j]

    """
    Applying Floyd-Warshall algorithm
    """
    for k in range(numberOfVertices):
        for i in range(numberOfVertices):
            for j in range(numberOfVertices):
                if distanceMatrix[i][k] + distanceMatrix[k][j] < distanceMatrix[i][j]:
                    distanceMatrix[i][j] = distanceMatrix[i][k] + distanceMatrix[k][j]

    #Check if there is a path from startNode to endNode
    if distanceMatrix[startNode][endNode] == float("inf"):
        return None  # No path exists

    """
    Getting visited Nodes between source node 
    and destination node 
    """
    visitedNodes = [startNode]
    current = startNode
    while current != endNode:
        for nextNode in range(numberOfVertices):
            if (
                current != nextNode
                and distanceMatrix[current][nextNode] + distanceMatrix[nextNode][endNode] == distanceMatrix[current][endNode]
            ):
                visitedNodes.append(nextNode)
                current = nextNode
                break
    
    #Getting path
    visitedPaths = []
    for i in range(0, len(visitedNodes) - 1):
        visitedPath = [visitedNodes[i], visitedNodes[i + 1]]
        visitedPaths.append(visitedPath)

    #Calculating total distance and total delay
    totalDistance = 0
    totalDelay = 0
    for path in visitedPaths:
        startNode = path[0]
        endNode = path[1]
        totalDistance += neighborhoodMatrix[startNode][endNode]
        totalDelay += delayMatrix[startNode][endNode]
        
    return totalDistance, totalDelay, visitedNodes

