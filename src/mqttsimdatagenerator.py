from random import randint, choice, uniform
from string import ascii_letters
from re import findall, search
from uuid import uuid1 as uuid
from functools import partial
from datetime import datetime


class MqttSimDataGenerator:
    def __init__(self, data_format: str):
        self.__make_formatted_string(data_format)

    def next_message(self):
        message = self.__format_str
        for id, value_fun in self.__replace_dict.items():
            message = message.replace(f"{{{id}}}", str(value_fun()), 1)
        return message

    def reinitalize(self, data_format):
        if hasattr(self, "__file_data"):
            delattr(self, "__file_data")
        self.__make_formatted_string(data_format)

    def __make_formatted_string(self, data_format):
        function_pattern = r'(<%([a-zA-Z]+) *((?:(?:[^ ]+)=(?:(?:[^ ]+)|(?:[\[][^\]]*[\]])|(?:[\'"][^\'"]*[\'"])) *)+)? *%>)'
        matches = findall(function_pattern, data_format)

        self.__replace_dict = dict()
        self.__format_str = data_format

        function_mapper = {
            "randi": self.__init_randi,
            "randf": self.__init_randf,
            "randu": self.__init_randu,
            "rands": self.__init_rands,
            "file": self.__init_file,
            "time": self.__init_time,
        }

        # replacement functions found
        for match in matches:
            id = str(uuid())
            to_replace = match[0]
            function = match[1]
            args = match[2]
            if function not in function_mapper.keys():
                continue
            function_mapper.get(function)(id, args)
            self.__format_str = self.__format_str.replace(
                to_replace, f"{{{id}}}", 1)

    def __extract_min_max_or_default(self, args: str, dflt: (int | float, int | float), conv_fun: object) -> (int | float, int | float):
        min_match = search(r"min=(-?\d*.\d+)", args)
        max_match = search(r"min=(-?\d*.\d+)", args)

        min_val = conv_fun(min_match.group(
            1)) if min_match is not None else dflt[0]
        max_val = conv_fun(max_match.group(
            1)) if max_match is not None else dflt[1]

        return (min_val, max_val)

    def __extract_collection_length_or_none(self, args: str) -> (list | None, int | None):
        collection_match = search(r'collection=\[([^\]])*\]', args)
        length_match = search(r"length=(\d+)", args)
        if collection_match is not None:
            collection_value = collection_match.group(0)
            collection_strings = findall(
                r'["\']([^"\']*)["\']', collection_value) if collection_value else []
            return (collection_strings, None)

        length_val = int(length_match.group(
            1)) if length_match is not None else None
        return (None, length_val)

    def __extract_src_and_separator_or_default(self, args: str, dflt: (str | None, str)) -> (str | None, str):
        src_match = search(r'src=["\'](.*?)["\']', args)
        separator_match = search(r'separator=["\'](.*?)["\']', args)

        src_value = src_match.group(1) if src_match is not None else dflt[0]
        separator_value = separator_match.group(
            1) if separator_match is not None else dflt[1]
        return (src_value, separator_value)

    def __init_file(self, id: str, args: str) -> None:
        if not hasattr(self, "__file_data"):
            self.__file_data = dict()

        splitted_file_content = ["no file source"]
        src_val, separator_val = self.__extract_src_and_separator_or_default(
            args, (None, "\n"))

        if src_val is not None:
            try:
                with open(src_val, "r") as file:
                    splitted_file_content = file.read().split(separator_val)
            except FileNotFoundError:
                splitted_file_content = ["file not found"]

        self.__file_data[id] = {"content": splitted_file_content, "index": 0}
        self.__replace_dict[id] = partial(self.__next_file_value, id)

    def __init_randi(self, id: str, args: str) -> None:
        min_val, max_val = self.__extract_min_max_or_default(
            args, (-(2**31), 2**31 - 1), int)
        self.__replace_dict[id] = partial(self.__next_randi, min_val, max_val)

    def __init_randu(self, id: str, args: str) -> None:
        min_val, max_val = self.__extract_min_max_or_default(
            args, (0, 2**32), int)
        self.__replace_dict[id] = partial(self.__next_randu, min_val, max_val)

    def __init_randf(self, id: str, args: str) -> None:
        min_val, max_val = self.__extract_min_max_or_default(
            args, (0, 1), float)
        self.__replace_dict[id] = partial(self.__next_randf, min_val, max_val)

    def __init_rands(self, id: str, args: str) -> None:
        collection_val, length_val = self.__extract_collection_length_or_none(
            args)
        self.__replace_dict[id] = partial(
            self.__next_rands, collection_val, length_val)

    def __init_time(self, id: str, args: str) -> None:
        self.__replace_dict[id] = self.__next_time

    # handle randf
    # returns random float from given range (default = [0; 1]
    #
    # example
    # <%randf%> -> returns float from [0; 1]
    # <%randf min=-1%> -> returns float from [-1; 1]
    # <%randf min=-1 max=10%> -> returns float from [-1; 10]
    def __next_randf(self, min: float, max: float) -> float:
        return uniform(min, max)

    # handle randi
    # returns random int from given range (default = [-max uint32; max uint32])
    #
    # example
    # <%randi%> -> returns int from [-2^31; 2^31 - 1]
    # <%randi max=10> -> returns int from [-2^31; 10]
    # <%randi min=-1 max=1%> -> returns -1 | 0 | 1
    def __next_randi(self, min: int, max: int) -> int:
        return randint(min, max)

    # handle randu
    # returns random unsigned int from given range (default=[0; max uint32])
    # if min < 0, the function will assign min to 0.
    #
    # example
    # <%randu%> -> returns int from [0; 2^32]
    # <%randu min=-10%> -> returns int from [0; 2^32]
    # <%randu min=10 max=20> -> returns int from [10; 20]
    def __next_randu(self, min: int, max: int) -> int:
        if min < 0:
            min = 0
        return self.__next_randi(min, max)

    # handle file
    # returns next value from file as string
    # if it reaches end of file, it will start over

    def __next_file_value(self, id) -> str:
        file_data = self.__file_data.get(id)
        idx = file_data["index"]
        data = file_data["content"]
        file_data["index"] = (idx + 1) % len(data)
        return f'"{data[idx]}"'

    # handle rands
    # returns random element from collection (length is ignored) or
    # random string with given length (default=10)
    #
    # example
    # <%rands collection=["asd", "bdc", "123"]%> -> returns "asd" | "bdc" | "123"
    # <%rands length=5%> -> returns random string with length = 5
    # <%rands%> -> returns random string with length = default = 10
    # if both length and collection are defined, the function will return random string from collection
    # if collection is empty it will print random string with given/default length
    def __next_rands(self, collection: list | None, length: int | None) -> str:
        if collection is not None and collection:
            return f'"{choice(collection)}"'
        return f'"{"".join(choice(ascii_letters) for _ in range(length if length is not None else 10))}"'

    # handle time
    # returns current time
    #
    # example
    # <%time%> -> returns current time as string

    def __next_time(self) -> str:
        return f'"{str(datetime.now().time())}"'
