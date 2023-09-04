from mqttsim import MqttSim, MqttSimConfig
from argparse import ArgumentParser


def main(args):
    config = MqttSimConfig('config.json')

    if args.add_topic:
        topic, format = args.add_topic
        config.put_topic(topic, format)

    if args.set_broker:
        url = args.set_broker
        config.put_broker(url)

    # app = MqttSim(config)


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(prog='mqtt simulator',
                            description='simulate flow of data over mqtt')
    parser.add_argument("-at", "--add-topic", metavar=("topic_name",
                        "data_format"), type=str, nargs=2, help="Add topic to config")
    parser.add_argument("-sb", "--set-broker", metavar=("url"),
                        type=str, help="Set broker url")
    return parser


if __name__ == '__main__':
    main(create_parser().parse_args())
