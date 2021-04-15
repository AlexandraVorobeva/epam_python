from keyword import iskeyword


class KeyValueStorage:
    """KeyValueStorage is wrapper class for this key value storage.
    Takes path to file with key=value
    Has its keys and values accessible as collection items and as attributes.
    """

    def __init__(self, filename: str):
        self.file_content = {}
        with open(filename, "r") as fl:
            file = fl.readlines()
            for line in file:
                key, value = line.strip().split("=")
                value = int(value) if value.isnumeric() else value
                if key.isidentifier() and not iskeyword(key):
                    self.file_content[key] = value
                else:
                    raise ValueError("Invalid key!")

    def __getitem__(self, item: str):
        return self.file_content[item]

    def __getattr__(self, key: str):
        return self.file_content[key]
