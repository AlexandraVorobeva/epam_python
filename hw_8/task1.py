from keyword import iskeyword


class KeyValueStorage:
    """KeyValueStorage is wrapper class for this key value storage.
    Takes path to file with key=value
    Has its keys and values accessible as collection items and as attributes.
    """

    def __init__(self, filename: str):
        self.dict = {}
        with open(filename, "r") as fl:
            key_value = fl.read()
        key_value = [list(item.split("=")) for item in key_value.split()]
        for item in key_value:
            key, value = item
            value = value.rstrip()
            if iskeyword(key) or not key.isidentifier():
                raise ValueError("Incorrect key!")
            if value.isdigit():
                value = int(value)
            if key not in self.dict:
                self.dict[key] = value

    def __getitem__(self, item: str):
        return self.dict[item]

    def __getattr__(self, key: str):
        return self.dict[key]
