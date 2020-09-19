

# Step 1 - describe the problem in graph terms
# Step 2 - build the graph
# Step 3 - traverse the graph (bfs/dfs or bft/dft)

### STEP 1 
# Each node represents a person
# Each edge represents a parent -> child connection

### STEP 2 Build the graph

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


###get_ancestors (aka: get_neighbors)

def get_ancestor(ancestors, child):
    children = []
    for heir in ancestors:
        if heir[1] == child:
            children.append(heir[0])
    return children

### STEP 3 Traverse the graph (bft)
def earliest_ancestor(ancestors, starting_node):
    #create empty queue
    queue = Queue()
    #add starting vertex to queue
    queue.enqueue([starting_node])
    #track visited vertices
    visited = set()
    #initialize path length
    path_length = 1
    #sets relative as -1 if no parent
    earliest_known_ancestor = -1

    #while queue is greater than 0
    while queue.size() > 0:
        # dequeue first path
        path = queue.dequeue()
        # grab the last vertex from the path
        current_node = path[-1]

        # if that vertex has not been visited
        if current_node not in visited:
            # mark as visited
            visited.add(current_node)

        # checks for need to update
        if len(path) >= path_length and current_node <earliest_known_ancestor or len(path) > path_length:
            #updates path length
            path_length = len(path)
            #updates earliest known ancestor
            earliest_known_ancestor = current_node

        # then add a path to its parent to the back of the queue
        for parent in get_ancestor(ancestors, current_node):
            #copy path
            path_copy = list(path)
            #append parent
            path_copy.append(parent)
            queue.enqueue(path_copy)

    return earliest_known_ancestor