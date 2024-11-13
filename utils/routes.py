def structure_routes(routes):
    tree = {}
    for route in routes:
        parts = route["route"].strip("/").split("/")
        current_level = tree
        for i, part in enumerate(parts):
            if part not in current_level:
                current_level[part] = {"route": None, "child": {}}
            if i == len(parts) - 1:
                current_level[part].update(route)
            current_level = current_level[part]["child"]
    return tree


def yield_all_children(dictionary):
    # Yield the current dictionary to the caller
    yield dictionary
    # Iterate through all key-value pairs in the dictionary
    for key, value in dictionary.items():
        # If the value is a dictionary, we check if we need to go deeper
        if isinstance(value, dict):
            yield from yield_all_children(value)
        # If the key is 'child' and its value is a non-empty dictionary, we traverse this child
        elif key == "child" and value:
            yield from yield_all_children(value)
