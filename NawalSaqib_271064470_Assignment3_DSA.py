class BSTWaypointNode:
    def __init__(self, waypoint_id, priority):
        self.id = waypoint_id
        self.priority = priority
        self.left = None
        self.right = None

class BSTWaypointManager:
    def __init__(self):
        self.root = None

    def insert_node(self, waypoint_id, priority):
        self.root = self.insert(self.root, waypoint_id, priority)

    def insert(self, node, waypoint_id, priority):
        if node is None:
            return BSTWaypointNode(waypoint_id, priority)
        if waypoint_id < node.id:
            node.left = self.insert(node.left, waypoint_id, priority)
        elif waypoint_id > node.id:
            node.right = self.insert(node.right, waypoint_id, priority)
        else:
            node.priority = priority
        return node

    def delete(self, waypoint_id):
        self.root = self.delete_node(self.root, waypoint_id)

    def delete_node(self, node, waypoint_id):
        if node is None:
            return None
        if waypoint_id < node.id:
            node.left = self.delete_node(node.left, waypoint_id)
        elif waypoint_id > node.id:
            node.right = self.delete_node(node.right, waypoint_id)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            min_larger_node = self.min_node(node.right)
            node.id, node.priority = min_larger_node.id, min_larger_node.priority
            node.right = self.delete_node(node.right, min_larger_node.id)
        return node

    def search(self, waypoint_id):
        node = self.find(self.root, waypoint_id)
        return node is not None

    def find(self, node, waypoint_id):
        if node is None:
            return None
        if waypoint_id == node.id:
            return node
        elif waypoint_id < node.id:
            return self.find(node.left, waypoint_id)
        else:
            return self.find(node.right, waypoint_id)
    
    def in_order_traversal(self, node, result = None):
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append((node.id, node.priority))
            self.in_order_traversal(node.right, result)
        return result

    def min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def get_min_priority_in_range(self, node, low, high):
        if node is None:
            return (None, float("inf")) 
        
        if node.id < low:
            return self.get_min_priority_in_range(node.right, low, high)

        if node.id > high:
            return self.get_min_priority_in_range(node.left, low, high)

        left_waypoint = self.get_min_priority_in_range(node.left, low, high)
        right_waypoint = self.get_min_priority_in_range(node.right, low, high)

        current = (node.id, node.priority) 

        min_waypoint = current
        if left_waypoint[1] < min_waypoint[1]:
            min_waypoint = left_waypoint
        if right_waypoint[1] < min_waypoint[1]:
            min_waypoint = right_waypoint

        return min_waypoint

    def get_min_priority(self, low, high):
        waypoint_id, priority = self.get_min_priority_in_range(self.root, low, high)
        if waypoint_id is None:
            print("No waypoints found in the given range.")
        else:
            print("Min priority waypoint in range:", waypoint_id, priority)
        return (waypoint_id, priority)

class AVLWaypointNode:
    def __init__(self, waypoint_id, priority):
        self.id = waypoint_id
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1
        self.min_priority = priority

class AVLWaypointManager:
    def __init__(self):
        self.root = None

    def insert_node(self, waypoint_id, priority):
        self.root = self.insert(self.root, waypoint_id, priority)

    def insert(self, node, waypoint_id, priority):
        if node is None:
            return AVLWaypointNode(waypoint_id, priority)
        if waypoint_id < node.id:
            node.left = self.insert(node.left, waypoint_id, priority)
        elif waypoint_id > node.id:
            node.right = self.insert(node.right, waypoint_id, priority)
        else:
            node.priority = priority
            self.update_height_and_min_priority(node) 
            return node

        self.update_height_and_min_priority(node)
        return self.balancing(node)

    def delete_node(self, waypoint_id):
        self.root = self.delete(self.root, waypoint_id)

    def delete(self, node, waypoint_id):
        if node is None:
            return None
        if waypoint_id < node.id:
            node.left = self.delete(node.left, waypoint_id)
        elif waypoint_id > node.id:
            node.right = self.delete(node.right, waypoint_id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_larger_node = self.min_node(node.right)
                node.id, node.priority = min_larger_node.id, min_larger_node.priority
                node.right = self.delete(node.right, min_larger_node.id)

        self.update_height_and_min_priority(node)
        return self.balancing(node)

    def search(self, waypoint_id):
        node = self.find(self.root, waypoint_id)
        return node is not None

    def find(self, node, waypoint_id):
        if node is None:
            return None
        if waypoint_id == node.id:
            return node
        elif waypoint_id < node.id:
            return self.find(node.left, waypoint_id)
        else:
            return self.find(node.right, waypoint_id)

    def min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def height(self, node):
        if node:
            return node.height
        else:
            return 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def balancing(self, node):
        balance = self.balance_factor(node)

        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def rotate_left(self, pivot):
        new_root = pivot.right
        moved_subtree = new_root.left
        new_root.left = pivot
        pivot.right = moved_subtree
        self.update_height_and_min_priority(pivot)
        self.update_height_and_min_priority(new_root)
        return new_root

    def rotate_right(self, pivot):
        new_root = pivot.left
        moved_subtree = new_root.right
        new_root.right = pivot
        pivot.left = moved_subtree
        self.update_height_and_min_priority(pivot)
        self.update_height_and_min_priority(new_root)
        return new_root
    
    def update_height_and_min_priority(self, node):
        if not node:
            return
        if node.left:
            left_min = node.left.min_priority
        else:
            left_min = float("inf")

        if node.right:
            right_min = node.right.min_priority
        else:
            right_min = float("inf")
        
        if node.left:
            left_height = node.left.height
        else:
            left_height = 0

        if node.right:
            right_height = node.right.height
        else:
            right_height = 0

        node.height = 1 + max(left_height, right_height)
        node.min_priority = min(node.priority, left_min, right_min)
    
    def get_min_priority_in_range(self, node, low, high):
        if node is None:
            return (None, float("inf")) 
        
        if node.id < low:
            return self.get_min_priority_in_range(node.right, low, high)

        if node.id > high:
            return self.get_min_priority_in_range(node.left, low, high)

        left_waypoint = self.get_min_priority_in_range(node.left, low, high)
        right_waypoint = self.get_min_priority_in_range(node.right, low, high)

        current = (node.id, node.priority) 

        min_waypoint = current
        if left_waypoint[1] < min_waypoint[1]:
            min_waypoint = left_waypoint
        if right_waypoint[1] < min_waypoint[1]:
            min_waypoint = right_waypoint

        return min_waypoint

    def get_min_priority(self, low, high):
        waypoint_id, priority = self.get_min_priority_in_range(self.root, low, high)
        if waypoint_id is None:
            print("No waypoints found in the given range.")
        else:
            print("Min priority waypoint in range:", waypoint_id, priority)
        return (waypoint_id, priority)

    def get_all_waypoints_inorder(self):
        result = []
        def inorder(node):
            if node:
                inorder(node.left)
                result.append((node.id, node.priority))
                inorder(node.right)
        inorder(self.root)
        return result

import random

def load_waypoints(filename):
    waypoints = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                waypoint_id = int(parts[0])
                priority = int(parts[1])
                waypoints.append((waypoint_id, priority))
    return waypoints

def parse_line(line):
    parts = line.strip().split()
    return int(parts[0]), int(parts[1])

def simulate_avl_operations(avl_tree, filename):
    # 1. Read waypoints from file
    waypoints = []
    with open(filename, "r") as f:
        for line in f:
            waypoint_id, priority = parse_line(line)
            waypoints.append((waypoint_id, priority))

    print("Inserting initial waypoints...")
    # 2. Insert initial waypoints into AVL tree
    for waypoint_id, priority in waypoints:
        avl_tree.insert_node(waypoint_id, priority)

    inserted_ids = set(wp[0] for wp in waypoints)

    # 3. Perform 500 random insertions
    print("Performing 500 random insertions...")
    for _ in range(500):
        new_id = random.randint(1, 100000)
        new_priority = random.randint(1, 1000)
        avl_tree.insert_node(new_id, new_priority)
        inserted_ids.add(new_id)

    # 4. Perform 300 random deletions
    print("Performing 300 random deletions...")
    delete_candidates = random.sample(sorted(inserted_ids), min(300, len(inserted_ids)))
    for id in delete_candidates:
        avl_tree.delete_node(id)
        inserted_ids.discard(id)

    #5. 400 range min priority queries
    print("Performing 400 range minimum priority queries...")
    for _ in range(400):
        low = random.randint(1, 50000)
        high = random.randint(low, 100000)
        avl_tree.get_min_priority(low, high)


    #6. 300 direct waypoint lookups
    print("Performing 300 direct waypoint lookups...")
    lookup_ids = random.sample(sorted(inserted_ids), min(300, len(inserted_ids)))
    found_count = 0
    for id in lookup_ids:
        if avl_tree.search(id):
            found_count += 1
    print("Looked up " + str(len(lookup_ids)) + " ids, found " + str(found_count) + " active waypoints.")

    # 7. Write updated waypoints back to the file
    print("Writing updated waypoints back to file...")
    updated_waypoints = avl_tree.get_all_waypoints_inorder()
    with open(filename, 'w') as f:
        for waypoint_id, priority in updated_waypoints:
            f.write(str(waypoint_id) + " " + str(priority) + "\n")

    print("Simulation complete.")

def main():
    avl_tree = AVLWaypointManager()
    filename = "C:/Users/HP/Documents/waypoints.txt"
    simulate_avl_operations(avl_tree, filename)
main()


class LazyAVLNode:
    def __init__(self, id, priority):
        self.id = id
        self.priority = priority
        self.height = 1
        self.left = None
        self.right = None
        self.deleted = False
        self.min_priority = priority

class LazyAVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node:
            return node.height
        else:
            return 0
        
    def update_height_and_min_priority(self, node):
        if not node:
            return
        if node.left:
            left_min = node.left.min_priority
        else:
            left_min = float("inf")

        if node.right:
            right_min = node.right.min_priority
        else:
            right_min = float("inf")

        if not node.deleted:
            current_priority = node.priority
        else:
            current_priority = float("inf")
        
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        node.min_priority = min(current_priority, left_min, right_min)

    def rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        self.update_height_and_min_priority(root)
        self.update_height_and_min_priority(new_root)
        return new_root

    def rotate_right(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        self.update_height_and_min_priority(root)
        self.update_height_and_min_priority(new_root)
        return new_root

    def get_balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, node, id, priority):
        if not node:
            return LazyAVLNode(id, priority)

        if id < node.id:
            node.left = self.insert(node.left, id, priority)
        elif id > node.id:
            node.right = self.insert(node.right, id, priority)
        else:
            if node.deleted:
                node.deleted = False
                node.priority = priority
            else:
                node.priority = priority
            self.update_height_and_min_priority(node)
            return node

        self.update_height_and_min_priority(node)

        balance = self.get_balance(node)

        if balance > 1 and id < node.left.id:
            return self.rotate_right(node)
        
        if balance < -1 and id > node.right.id:
            return self.rotate_left(node)
        
        if balance > 1 and id > node.left.id:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        if balance < -1 and id < node.right.id:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert_node(self, id, priority):
        self.root = self.insert(self.root, id, priority)

    def lazy_delete(self, node, id):
        if not node:
            return node

        if id < node.id:
            node.left = self.lazy_delete(node.left, id)
        elif id > node.id:
            node.right = self.lazy_delete(node.right, id)
        else:
            node.deleted = True

        self.update_height_and_min_priority(node)
        return node

    def delete(self, id):
        self.root = self.lazy_delete(self.root, id)

    def _reactivate(self, node, id):
        if not node:
            return node

        if id < node.id:
            node.left = self._reactivate(node.left, id)
        elif id > node.id:
            node.right = self._reactivate(node.right, id)
        else:
            node.deleted = False

        self.update_height_and_min_priority(node)
        return node

    def reactivate(self, id):
        self.root = self._reactivate(self.root, id)
    
    def search_node(self, waypoint_id):
        return self.search(self.root, waypoint_id)

    def search(self, node, waypoint_id):
        if node is None:
            return None
        if waypoint_id < node.id:
            return self.search(node.left, waypoint_id)
        elif waypoint_id > node.id:
            return self.search(node.right, waypoint_id)
        else:
            if not node.deleted:
                return node
            else:
                return None

    def get_min_priority_in_range(self, node, low, high):
        if node is None:
            return (None, float("inf"))

        if not getattr(node, "deleted", False):
            current_priority = node.priority
        else:
            current_priority = float("inf")

        if node.id < low:
            return self.get_min_priority_in_range(node.right, low, high)

        if node.id > high:
            return self.get_min_priority_in_range(node.left, low, high)

        left_result = self.get_min_priority_in_range(node.left, low, high)
        right_result = self.get_min_priority_in_range(node.right, low, high)
        current_result = (node.id, current_priority)

        min_result = current_result
        if left_result[1] < min_result[1]:
            min_result = left_result
        if right_result[1] < min_result[1]:
            min_result = right_result

        return min_result

    def get_min_priority(self, low, high):
        return self.get_min_priority_in_range(self.root, low, high)
    

def simulate_lazy_deletion(tree):
    print("\n" + "Starting Lazy Deletion Simulation: ")

    # 1. Insert 20 waypoints
    print("Inserting 20 waypoints")
    waypoints = [(i, random.randint(1, 100)) for i in range(1, 21)]
    for waypoint_id, priority in waypoints:
        tree.insert_node(waypoint_id, priority)
    print("Inserted:", waypoints)

    # 2. Lazily delete 5 random waypoints
    deleted_ids = random.sample([wp[0] for wp in waypoints], 5)
    print("\n" + "Lazily deleting waypoints with IDs:", deleted_ids)
    for waypoint_id in deleted_ids:
        tree.delete(waypoint_id)

    # 3. Searching all 20 waypoints and check active status
    print("\nSearch results (active only):")
    for waypoint_id, _ in waypoints:
        result = tree.search_node(waypoint_id)
        if result is not None:
            status = "Found"
        else:
            status = "Deleted"
        print("Waypoint ID " + str(waypoint_id) + ": " + status)


    # 4. Perform a range min-priority query on full range
    print("\n" + "Performing min-priority query in range 1 to 20 (ignores deleted):")
    result = tree.get_min_priority_in_range(tree.root, 1, 20)
    if result[0] is not None:
        print("Min active waypoint in range: ID=" + str(result[0]) + ", Priority=" + str(result[1]))
    else:
        print("No active waypoints found in range.")

    # 5. Reactivate one of the lazily deleted waypoints
    if deleted_ids:
        re_id = deleted_ids[0]
        new_priority = random.randint(1, 100)
        print("\nReinserting (reactivating) waypoint ID " + str(re_id) + " with new priority " + str(new_priority))
        tree.insert_node(re_id, new_priority)

        # Search again
        result = tree.search_node(re_id)
        if result is not None:
            status = "Found"
        else:
            status = "Deleted"
        print("Waypoint ID " + str(re_id) + " after reinsertion: " + status)

    print("----- Simulation Complete -----")

def main():
    lazy_avl_tree = LazyAVLTree()
    simulate_lazy_deletion(lazy_avl_tree)
main()