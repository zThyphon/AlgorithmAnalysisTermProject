import getMatrices as matrices
import algorithms

#Define fileNames dictionary
fileNames = {
    "adjacencyMatrixFileName": "USNET_AjdMatrix.txt",
    "USNETFileName": "USNET.txt"
}


#Define request object
request = {
    "sourceNode":6,
    "destinationNode":21,
    "bandwithDemand": 5
}


def Solution(fileNames,request):
    #Get filenames
    adjacencyMatrixFileName = fileNames["adjacencyMatrixFileName"]
    usnetFileName = fileNames["USNETFileName"]

    """
    Getting sourceNode, destinationNode and bandwithDemand
    from request object 
    """
    sourceNode = request["sourceNode"]
    destinationNode = request["destinationNode"]
    bandwithDemand = request["bandwithDemand"]

    #Getting matrices
    adjacencyMatrix = matrices.getAdjacencyMatrix(adjacencyMatrixFileName)
    neighborHoodMatrix = matrices.getNeighborhoodMatrix(usnetFileName)
    bandwithMatrix = matrices.getBandwithMatrix(usnetFileName)
    delayMatrix = matrices.getDelayMatrix(usnetFileName)
    updatedAdjacencyMatrix = matrices.updateAdjacencyMatrix(adjacencyMatrix,bandwithMatrix,bandwithDemand)

    #Applying algorithms and printing the solutions
    print(f"Shortest Distance Between Node {sourceNode} and Node {destinationNode} with Bandwith Demand {bandwithDemand}")
    print("Dijkstra Algorithm")
    shortestDistance,visitedNodes = algorithms.dijkstraAlgorithm(updatedAdjacencyMatrix, neighborHoodMatrix, sourceNode, destinationNode)
    print("Total Distance")
    print(shortestDistance)
    print("Visited Nodes")
    print(visitedNodes)
    print("/////////////////////////////////////////////////")

    print("Bellman Ford Algorithm")
    shortestDistance, totalDelay, visitedNodes = algorithms.bellmanFordAlgorithm(updatedAdjacencyMatrix,neighborHoodMatrix,delayMatrix,sourceNode,destinationNode)
    shortestDistance = shortestDistance * bandwithDemand
    print("Total Distance")
    print(shortestDistance)
    print("Total Delay")
    print(totalDelay)
    print("Visited Nodes")
    print(visitedNodes)
    print("/////////////////////////////////////////////////")
    print("Flody Warshall Algorithm")
    shortestDistance, totalDelay, visitedNodes = algorithms.floydWarshallAlgorithm(updatedAdjacencyMatrix,neighborHoodMatrix,delayMatrix,sourceNode,destinationNode)
    shortestDistance = shortestDistance * bandwithDemand
    print("Total Distance")
    print(shortestDistance)
    print("Total Delay")
    print(totalDelay)
    print("Visited Nodes")
    print(visitedNodes)


if __name__ == "__main__":
    Solution(fileNames,request)