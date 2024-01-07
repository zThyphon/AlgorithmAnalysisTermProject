try:
    #Get adjacency matrix function
    def getAdjacencyMatrix(adjacencyMatrixFileName):
        #Open file
        with open(adjacencyMatrixFileName, "r") as file:
            #Get lines from file
            lines = file.readlines()
            #Create the matrix
            adjacencyMatrix = []
            #Get lines
            for i in range(0, 24):
                #Get adjacency matrix values in the line
                #Split the line with using ":"
                lines[i] = lines[i].split(":")
                """
                Create the row matrix for the 
                adding to the matrix
                """
                row = []
                #Add rows
                for j in range(0,24):
                    row.append(int(lines[i][j]))
                adjacencyMatrix.append(row)

            #Return adjacency matrix
            return adjacencyMatrix
    
    #Get neighborhood matrix function
    def getNeighborhoodMatrix(usnetFileName):
        #Open file
        with open(usnetFileName, "r") as file:
            #Get lines from file
            lines = file.readlines()
            #Create matrix
            neighborHoodMatrix = []
            #Get lines
            for i in range(0, 24):
                #Get adjacency matrix values in the line
                #Split the line with using ":"
                lines[i] = lines[i].split(":")
                """
                Create the row matrix for the 
                adding to the matrix
                """
                row = []
                #Add rows
                for j in range(0,24):
                    row.append(int(lines[i][j]))
                neighborHoodMatrix.append(row)

        #Return neighborhood matrix
        return neighborHoodMatrix
    
    #Get bandwith matrix function
    def getBandwithMatrix(usnetFileName):
        #Open file
        with open(usnetFileName, "r") as file:
            #Get lines from file
            lines = file.readlines()
            #Create matrix
            bandwithMatrix = []
            #Get lines
            for i in range(25, 49):
                #Get adjacency matrix values in the line
                #Split the line with using ":"
                lines[i] = lines[i].split(":")
                """
                Create the row matrix for the 
                adding to the matrix
                """
                row = []
                #Add rows
                for j in range(0,24):
                    row.append(int(lines[i][j]))
                bandwithMatrix.append(row)
        
        #Return bandwith matrix
        return bandwithMatrix
    
    #Get delay matrix function
    def getDelayMatrix(usnetFileName):
        #Open file
        with open(usnetFileName, "r") as file:
            #Get lines from line
            lines = file.readlines()
            #Create matrix
            delayMatrix = []
            """
            Create the row matrix for the 
            adding to the matrix
            """
            for i in range(50, 74):
                lines[i] = lines[i].split(":")
                row = []
                for j in range(0,24):
                    row.append(int(lines[i][j]))
                delayMatrix.append(row)

        #Return delay matrix
        return delayMatrix

    """
    Update adjacency matrix function
    Updates adjacency matrix value as 0 
    if it is not meeting the bandwith demand
    """
    def updateAdjacencyMatrix(adjacencyMatrix,bandwithMatrix,bandwithDemand):
        for i in range(0,24):
            for j in range(0,24):
                if(bandwithMatrix[i][j] < bandwithDemand):
                    adjacencyMatrix[i][j] = 0
        
        return adjacencyMatrix
    
except FileNotFoundError:
    print("File not exist.")

except Exception as error:
    print(f"An error occurred: {error}")

