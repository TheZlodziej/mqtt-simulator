from abstractdatagenerator import DataGenerator
from jsondatagenerator import JsonDataGenerator
from protogenerator import ProtoDataGenerator

def get_data_generator(config) -> DataGenerator:
    if "data_format" in config:
        return JsonDataGenerator(config)
    elif "message" in config:
        return ProtoDataGenerator(config)


