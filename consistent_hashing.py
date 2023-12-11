class Node:
    def __init__(self, id, hash_value):
        self.hash = hash_value
        self.id = value
        self.storage = {}


class Hashing:
    def __init__(self):
        self.nodes = []

    def get_nearest_clockwise_node(self, hash_value):
        for node in self.nodes:
            if node.hash > hash_value:
                return node
        return self.nodes[0] if len(self.nodes) > 0 else None

    def add_node(self, node_id):
        hash_value = hash(node_id)
        next_node = self.get_nearest_clockwise_node(hash_value)
        node = Node(node_id, hash_value)
        if next_node:
            for key, value in next_node.storage.items():
                if key < hash_value:
                    node.storage[key] = value
                    del next_node.storage[key]
        self.nodes.append(node)
        self.nodes.sort(key=lambda x: x.hash)

    def get_node(self, node_id):
        for node in nodes:
            if node.id == node_id:
                return node
        return None

    def remove_node(self, node_id):
        node = get_node(node_id)
        hash_value = hash(node_id)
        next_node = self.get_nearest_clockwise_node(hash_value)
        if next_node:
            for key, value in node.storage.items():
                next_node.storage[key] = value
        self.nodes.remove(node)
        self.nodes.sort(key=lambda x: x.hash)

    def get(self, key):
        hash_value = hash(key)
        node = self.get_nearest_clockwise_node(hash_value)
        if node:
            return node.storage.get(key)
        return None

    def set(self, key, value):
        hash_value = hash(key)
        node = self.get_nearest_clockwise_node(hash_value)
        if node:
            node.storage[key] = value

    def delete(self, key):
        hash_value = hash(key)
        node = self.get_nearest_clockwise_node(hash_value)
        if node:
            del node.storage[key]
