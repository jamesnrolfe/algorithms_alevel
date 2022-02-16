# ===== DEPTH FIRST SEARCH =======

# looks deep into the list, and simply prints out all the results. 
# can probably be modified to find a target value and return true etc, if it is found

# ========= ALGORITHM ===========

def dfs(graph, node, visited):
    # takes in a graph to be searched, the currentNode we are looking at and a list for visited items, initilised as an empty array
    if node not in visited: # if we haven't visisted it already
        print(node) # print it
        visited.append(node) # add it to visited
        for neighbour in graph[node]: # then search all its child nodes
            dfs(graph, neighbour, visited) # using the same technique
    
# ========== TEST ===========

graph = {"A" : ["C","D"],
    	"B" : ["D", "E"],
		"C" : ["A", "D", "F", "I"],
		"D" : ["A", "B", "C", "E"],
		"E" : ["B", "D"],
		"F" : ["C", "G", "H"],
		"G" : ["F"],
		"H" : ["F"],
		"I" : ["C"]}

print(dfs(graph, "A", [])) # works :)