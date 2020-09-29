import random

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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        # maps IDs to user objects (lookup tabel for User Objects given IDs)
        self.users = {}
        # Adjacency list
        # Maps user_ids to a list of other users (who are their friends)   
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        ### add vertex to adjacency list 
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
    
        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i + 1}")

        # Create friendships
        # Generate all possible friendships
        # Avoid duplicate friendships
        # Runtime O(n^2) (linear)
        possible_friendships = []
        for user_id in self.users: #runtime O(n)
            for friend_id in range(user_id + 1, len(self.users.keys()) + 1): #runtime O(n-1), O(n-2), etc...= O(n/2) --> O(n)
                # user_id == user_id_2 cannot happen
                # if friendship between user_id and user_id_2 already exists
                #   don't add friendship between user_id_2 and user_id
                possible_friendships.append( (user_id, friend_id) ) #runtime O(1)

        # Randomly selected x friendships
        # the formula for x is num_users * avg_friendships // 2 
        # Shuffle the array and pick x elements from the front of it
        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        ###BFT
        # Create a Queue
        queue = Queue()

        # Create a set of visited (presviously seen) Vertices

        visited = {}  # Note that this is a dictionary, not a set
        # Add first user_id to Queue as a path
        queue.enqueue([user_id])

        # While the Queue is not empty:
        while queue.size() > 0:
            # Dequeue a current path
            current_path = queue.dequeue()
            # Get current vertex from end of path
            current_vertex = current_path[-1]
            if current_vertex not in visited:
            # add vertex to visited_set
                # Also add the path that brough us to this vertex
                # i.e. add a key and value to the visited Dictionary
                    # the key is the current vertex, and the value is the path
                visited[current_vertex] = current_path
                
                # queue up all neighbors as paths
                for neighbor in self.friendships[current_vertex]:
                    # make a new copy of the current path
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph (10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
