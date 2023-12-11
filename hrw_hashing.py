class Node:
    def __init__(self, id):
        self.id = id
        self.storage = {}


class HRWHashing:
    def __init__(self):
        self.nodes = []

    def calculate_weight(self, node_id, key):
        return int(hashlib.sha256(f"{key}:{node_id}".encode()).hexdigest(), 16)

    def get_node_from_key(self, key):
        """Return the node to which the given key hashes to."""
        assert len(self.nodes) > 0
        max_weight = -1
        max_node = None
        for node in self.nodes:
            weight = calculate_weight(node, key)
            if weight > max_weight:
                max_weight = weight
                max_node = node
        return max_node

    def get_node_from_key_exlude_me(self, key, current_node):
        """Return the node to which the given key hashes to."""
        assert len(self.nodes) > 0
        max_weight = -1
        max_node = None
        for node in self.nodes:
            if node.id == current_node.id:
                continue
            weight = calculate_weight(node, key)
            if weight > max_weight:
                max_weight = weight
                max_node = node
        return max_node

    def add_node(self, node_id):
        nn_node = Node(node_id)
        for node in self.nodes:
            for key, value in node.storage.items():
                if self.calculate_weight(nn_node, key) > self.calculate_weight(
                    node.id, key
                ):
                    # if weight is now more for the new node, then move the key to the new node
                    nn_node.storage[key] = value
                    del node.storage[key]

        self.nodes.append(nn_node)

    def get_node(self, node_id):
        for node in nodes:
            if node.id == node_id:
                return node
        return None

    def remove_node(self, node_id):
        node = get_node(node_id)
        for key, value in node.storage.items():
            next_best_weight_node = get_node_from_key_exlude_me(key, node)
            next_best_weight_node[key] = value
        self.nodes.remove(node)

    def get(self, key):
        node = self.get_node_from_key(key)
        if node:
            return node.storage.get(key)
        return None

    def set(self, key, value):
        node = self.get_node_from_key(key)
        if node:
            node.storage[key] = value

    def delete(self, key):
        node = self.get_node_from_key(key)
        if node:
            del node.storage[key]
