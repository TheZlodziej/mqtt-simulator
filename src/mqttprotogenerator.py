from protofiles import location_pb2
from pkgutil import iter_modules
import protofiles
import importlib
from google.protobuf.message import Message
import random
import string


class MqttProtoGenerator():

    def __init__(self, message_name: string):
        self.message_constructors = MqttProtoGenerator.get_message_constructors()
        self.message_constructor = self.message_constructors[message_name]

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
                setattr(message, field_descriptor.name, random.getrandbits(1))
            # string
            elif field_type == 9:
                setattr(message, field_descriptor.name, ''.join(
                    random.choice(string.ascii_lowercase) for i in range(10)))
            # float or double
            elif field_type == 2 or field_type == 1:
                setattr(message, field_descriptor.name, random.random())
            # bytes
            elif field_type == 12:
                setattr(message, field_descriptor.name, random.randbytes(10))
            # int
            else:
                setattr(message, field_descriptor.name,
                        random.randint(0, 1000))
        return message


# gen = MqttProtoGenerator(location_pb2.GPSData)
# for _, constructor in gen.message_constructors.items():
    # g = MqttProtoGenerator(constructor)
    # mess = g.get_random_message()
    # print(mess)
