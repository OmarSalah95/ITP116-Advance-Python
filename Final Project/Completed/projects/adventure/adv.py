from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval
# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map directly into into a dictionary thanks to lazy loading with literal evaluation
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

world.loadGraph(roomGraph)

# UNCOMMENT TO VIEW MAP
world.printRooms()

player = Player("Name", world.startingRoom)

# Fill this out
traversalPath = []

player_map={0:{}}
for direction in world.startingRoom.getExits():
    player_map[0][direction] = '?'

def unexplored_rooms_down_path(origin, starting_direction, ghost_explorer = None, visited = None):
        """
        Tally total number of rooms down a given path that have not yet been explored.
        Recursively creates copy of the player (a "ghost") that checks each potential connected path and increments the room_total with each unexplored room it finds
        """
        # Make sure we don't backtrack, but also make sure we return 0 from the recursive call
        # Instead of the current total
        # If that room is not in the players map AND has not been visited by this DFT...
            # Mark it as visited and increment the unexplored rooms count                
            # Then send a new ghost explorer down each of the potential connected rooms
                # But only if that direction exists and if the room that way has not been visited
        room_total = 0
        if ghost_explorer is None:
            ghost_explorer = Player("BOO", player.currentRoom)
        if visited is None:
            visited = set()
        ghost_explorer.travel(starting_direction)
        r = ghost_explorer.currentRoom.id
        if r is origin:
            return 0
        if r not in player_map and r not in visited:
            visited.add(r)
            room_total += 1
            for d in ['n', 'e', 's', 'w']:
                if ghost_explorer.currentRoom.getRoomInDirection(d) is not None and ghost_explorer.currentRoom.getRoomInDirection(d) not in visited:
                    ghost_copy = Player("Copy", ghost_explorer.currentRoom)
                    room_total += unexplored_rooms_down_path(r, d, ghost_copy, visited)
        return room_total


def explore_shortest():
    """
    Checks the potential paths from the current room, returns the direction that contains
    the fewest (but non-zero) number of unexplored rooms down that path.
    In the larger graph where many room paths are interconnected, a shorter number typically
    denotes a dead end branch which is more efficient to traverse the first time you see it
    """
    results = set()
    current = player.currentRoom
    direction = current.getExits()

    for d in direction:
        next_room = current.getRoomInDirection(d)
        unexplored = unexplored_rooms_down_path(current.id, d)
        if unexplored > 0:
            results.add((d, unexplored))
    if len(results) > 0:
        return min(results, key = lambda t: t[1])[0]
    else:
        return None

def bfs_for_unexplored():
    """
    Performs BFS to find shortest path to room with unexplored exit from current location
    Returns the first path to meet this criteria
    """
    # Create an empty queue and enqueue a PATH to the current room
    q = Queue()
    q.enqueue([player.currentRoom.id])
    # Create a Set to store visited rooms
    v = set()

    while q.size() > 0:
        p = q.dequeue()
        last_room = p[-1]
        if last_room not in v:
            # Check if it has unexplored rooms
            if '?' in list(player_map[last_room].values()):
                # >>> IF YES, RETURN PATH (excluding starting room) so player can go travel shortest path to room with unexplored exit
                return p[1:]
            # Else mark it as visited
            v.add(last_room)
            # Then add a PATH to its neighbors to the back of the queue
            for direction in player_map[last_room]:
                path_copy = p.copy()
                path_copy.append(player_map[last_room][direction])
                q.enqueue(path_copy)

def origin(direction):
    """
    Small util function returning the opposite of a direction
    used in quickly determining the origin direction when a player arrives in a new room
    """
    opposite = {"n": "s", "e": "w", "s": "n", "w": "e"}
    return opposite[direction]

def dft_for_dead_end():
        # Grab direction that leads to unexplored exit
        # next_dir = explore_random()
        # if only one unexplored direction, always go there
        # otherwise, search down the multiple possibilities and go down the one that has the fewest unexplored rooms (typically a dead end branch)
        # Change current room's exit in that direction to the next room
        # Add travel direction to traversal path
        # Travel there
        # mark previous room as explored direction
    while '?' in list(player_map[player.currentRoom.id].values()):
        current_id = player.currentRoom.id
        unexplored_rooms =[]
        for key, val in list(player_map[player.currentRoom.id].items()):
            if val == '?':
                unexplored_rooms.append(key)
        if len(unexplored_rooms) == 1:
            next_dir = unexplored_rooms[0]
        else:
            next_dir = explore_shortest()
            if next_dir == None:
                break
        player_map[player.currentRoom.id][next_dir] = player.currentRoom.getRoomInDirection(next_dir).id
        traversalPath.append(next_dir)
        player.travel(next_dir)
        if player.currentRoom.id not in player_map:
            player_map[player.currentRoom.id] = {}
        if len(player_map[player.currentRoom.id]) <1:
            for direction in player.currentRoom.getExits():
                player_map[player.currentRoom.id][direction] = '?'
        player_map[player.currentRoom.id][origin(next_dir)] = current_id

def travel_to_nearest_unexplored():
    """
    Once a room with no unexplored exits is reached, run a BFS to find 
    the shortest path to a room with an unexplored exit for each room in 
    that path, then move that direction and log the movement in the traversal path
    """

    bfs_path = bfs_for_unexplored()
    while bfs_path is not None and len(bfs_path) > 0:
        next_room = bfs_path.pop(0)
        next_direction = next((k for k, v in player_map[player.currentRoom.id].items() if v == next_room), None)
        traversalPath.append(next_direction)
        player.travel(next_direction)


def populate_traversal_path():
    """
    While the player's map is shorter than the number of rooms, continue looping
    through DFT until a dead end OR already fully-explored room is found,
    then perform BFS to find shortest path to room with unexplored path and go there
    """
    while len(player_map) < len(roomGraph):      
        dft_for_dead_end()
        travel_to_nearest_unexplored()

# # The actual maze traversal function
populate_traversal_path()

# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)

for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")


player.currentRoom.printRoomDescription(player)
running = True
while running:
    cmds = input("Select a direction to travel: ").lower().split(" ")
    if cmds[0].strip() == "quit":
        running = False
    
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] != "quit":
        print("I did not understand that command.")
