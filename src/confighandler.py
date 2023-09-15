import json


class ConfigHandler:
    def __init__(self, path: str):
        self.__json_path = path
        self.__init_config_file()

    def __init_config_file(self):
        try:
            with open(self.__json_path, "r") as json_file:
                self.__data = json.load(json_file)
        except FileNotFoundError:
            self.__data = dict()

    def __save_to_file(self):
        with open(self.__json_path, "w") as json_file:
            json.dump(self.__data, json_file, indent=4)

    # puts/overrides value in config
    # saves current __data value to
    # example
    # config.put("a.b", 1) should result in { a: { b: 1 } } object
    def put(self, where: str, value: str | int | float | dict) -> None:
        keys = where.split(".")  # -> ["a", "b"]
        data = self.__data
        for key in keys[:-1]:
            if key not in data:
                data[key] = dict()
            data = data[key]
        data[keys[-1]] = value
        self.__save_to_file()

    # returns value from config
    # example
    # config.get("a.b") with data = { a: { b: 1 } } should return 1
    def get(self, what) -> str | int | float | dict | None:
        keys = what.split(".")
        data = self.__data
        for key in keys:
            if key not in data:
                return None
            data = data[key]
        return data

    # removes value from config
    # example
    # config.remove("a.b", 1) should result with { a: {} } when starting with { a: { b: 1 } } object
    def remove(self, what) -> None:
        keys = what.split(".")
        data = self.__data
        for key in keys[:-1]:
            if key not in data:
                return None
            data = data[key]
        del data[keys[-1]]
        self.__save_to_file()
