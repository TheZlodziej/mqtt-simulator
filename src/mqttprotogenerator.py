from pkgutil import iter_modules
import protofiles
import importlib
from google.protobuf.message import Message
from random import getrandbits, randint, random, choice, randbytes
from string import ascii_lowercase
import pandas as pd
from os import stat


class MqttProtoGenerator():
    logger = None

    def __init__(self, message_name: str, message_file_path=''):
        self.message_constructors = MqttProtoGenerator.get_message_constructors()
        self.message_constructor = self.message_constructors[message_name]
        self.constructed_messages = None
        self.message_name = message_name
        if message_file_path != '':
            try:
                self.file_time_stamp = stat(message_file_path).st_mtime
            except FileNotFoundError:
                MqttProtoGenerator.logger.error(
                    f"ERROR: File {message_file_path} not found. Defaulting to sending random messages")
                self.message_file_path = ''
                return

            self.message_file_path = message_file_path
            self.constructed_messages = self.read_message_csv(
                message_name, message_file_path)
            self.curr_message = 0

    def get_message_constructors():
        message_constructors = {}
        for submodule in iter_modules(protofiles.__path__):
            submodule_name = submodule.name
            submodule_fullname = f"protofiles.{submodule_name}"
            imported_module = importlib.import_module(submodule_fullname)
            for v in vars(imported_module).values():
                if not (isinstance(v, type) and issubclass(v, Message)):
                    continue
                message_constructors[v.__name__] = v
        return message_constructors

    def get_random_message(self):
        message = self.message_constructor()
        for field_descriptor in self.message_constructor.DESCRIPTOR.fields:

            message_type = field_descriptor.message_type
            if field_descriptor.message_type is not None:
                gen = MqttProtoGenerator(message_type.name)
                m = gen.get_random_message()
                attr = getattr(message, field_descriptor.name)
                attr.CopyFrom(m)
                continue
            field_type = field_descriptor.type
            # boolean
            if field_type == 8:
                setattr(message, field_descriptor.name, getrandbits(1))
            # string
            elif field_type == 9:
                setattr(message, field_descriptor.name, ''.join(
                    choice(ascii_lowercase) for i in range(10)))
            # float or double
            elif field_type == 2 or field_type == 1:
                setattr(message, field_descriptor.name, random())
            # bytes
            elif field_type == 12:
                setattr(message, field_descriptor.name, randbytes(10))
            # int
            else:
                setattr(message, field_descriptor.name,
                        randint(0, 1000))
        return message

    def get_next_message(self):
        ret = None
        if self.constructed_messages is not None:
            time_stamp = stat(self.message_file_path).st_mtime
            if time_stamp != self.file_time_stamp:
                MqttProtoGenerator.logger.info(
                    f"INFO: file {self.message_file_path} changed. Reconstructing messages")
                self.constructed_messages = self.read_message_csv(
                    self.message_name, message_file=self.message_file_path)
                self.file_time_stamp = time_stamp
                self.curr_message = 0

            ret = self.constructed_messages[self.curr_message]
            self.curr_message = (self.curr_message +
                                 1) % len(self.constructed_messages)
        else:
            ret = self.get_random_message()
        return ret

    def read_message_csv(self, message_name: str, message_file: str) -> list:
        df = None
        try:
            df = pd.read_csv(message_file)
        except FileNotFoundError:
            MqttProtoGenerator.logger.error(
                f"ERROR: File {message_file} not found. Defaulting to sending random messages")
            return

        messages = []
        for i in range(df.shape[0]):
            fields = dict()
            for field in df.columns:
                fields[field] = df[field][i]
            messages.append(self.construct_message(message_name, fields))
        return messages

    def construct_message(self, message_name: str, fields: dict) -> Message:
        message_constructor = self.message_constructors[message_name]
        new_message = message_constructor()
        for field_descriptor in message_constructor.DESCRIPTOR.fields:

            message_type = field_descriptor.message_type
            if field_descriptor.message_type is not None:
                passed_on_fields = dict()
                for field in fields.keys():
                    if message_type.name not in field:
                        continue
                    sub_fields = field.split('.')
                    try:
                        new_field_name = sub_fields[sub_fields.index(
                            message_type.name)+1:]
                    except ValueError:
                        if ' ' in field:
                            MqttProtoGenerator.logger.error(
                                f"ERROR: Field {field} contains spaces!!! You should not do that!")
                        else:
                            MqttProtoGenerator.logger.error(
                                f"ERROR: Field with key \'{field}\' not found in message \'{message_name}\'.")
                            return new_message
                    passed_on_fields['.'.join(
                        new_field_name)] = fields[field]
                m = self.construct_message(message_type.name, passed_on_fields)
                attr = getattr(new_message, field_descriptor.name)
                attr.CopyFrom(m)
                continue
            field_type = field_descriptor.type
            if field_descriptor.name not in fields.keys():
                MqttProtoGenerator.logger.info(
                    f"INFO: data for field \'{field_descriptor.name}\' not found when constructing message \'{message_name}\'.")
                continue
            # bolean
            if field_type == 8:
                setattr(new_message, field_descriptor.name,
                        bool(fields[field_descriptor.name]))
            # string
            elif field_type == 9:
                setattr(new_message, field_descriptor.name,
                        fields[field_descriptor.name])
            # float or double
            elif field_type == 2 or field_type == 1:
                setattr(new_message, field_descriptor.name,
                        float(fields[field_descriptor.name]))
            # bytes
            elif field_type == 12:
                setattr(new_message, field_descriptor.name,
                        fields[field_descriptor.name])

            # int
            else:
                setattr(new_message, field_descriptor.name,
                        int(fields[field_descriptor.name]))
        return new_message
