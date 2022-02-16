# ====== BREADTH FIRST SEARCH ======

# uses a queue to store the nodes it has to visit
# once a node is visited, all the next nodes are added to a queue and visited in that order
# to conserve breadth first

# ========== ALGORITHM ===========

def bfs(graph, node, visited):
    # takes in the graph to be searched, the start node and a visited array
    queue = [node] # we initialise the queue to just have the start node in it which we 
    # will soon look at
    while len(queue) > 0: # whilst the queue is not empty i.e. there are still items left to search
        node = queue.pop(0) # remove item from the end of the queue and make it node
        visited.append(node) # we are now visiting this node...
        for neighbour in graph[node]: # for all its connections
            if neighbour not in queue: # if its connection is not already queued
                if neighbour not in visited: # AND if we haven't already visited it
                    queue.append(neighbour) # add it to the queue to be searched
    return visited # return the list of all the items in the graph

# ======== TEST ==========

graph = {"A" : ["C","D"],
    	"B" : ["D", "E"],
		"C" : ["A", "D", "F", "I"],
		"D" : ["A", "B", "C", "E"],
		"E" : ["B", "D"],
		"F" : ["C", "G", "H"],
		"G" : ["F"],
		"H" : ["F"],
		"I" : ["C"]}

print(bfs(graph, "A", [])) # works :)