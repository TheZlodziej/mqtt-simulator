from mqttsim import MqttSim, MqttSimConfig
from argparse import ArgumentParser, Namespace
from logging import getLogger, Formatter, FileHandler, DEBUG, StreamHandler
from PySide6.QtWidgets import QApplication
from gui.ui import MqttSimMainWindow
from sys import stdout, exit
from time import sleep


def main(args: Namespace):
    # config setup
    config = MqttSimConfig("config.json")
    # end config setup

    # standalone functions (cmd line config edit)
    if args.add_topic:
        topic, format, interval = args.add_topic
        topic_config = {
            "topic": topic,
            "format": format,
            "interval": interval,
            "manual": False
        }
        config.put_topic(topic, topic_config)
        return

    if args.set_broker:
        host, port = args.set_broker
        config.put_broker(host, int(port))
        return
    # cmd line config edit

    # logger setup
    logger = getLogger("MqttSimLogger")
    logger.setLevel(DEBUG)
    file_handler = FileHandler("logs.txt")
    file_handler.setFormatter(Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(file_handler)
    if args.verbose:
        logger.addHandler(StreamHandler(stdout))
    # end logger setup

    # sim setup
    sim = MqttSim(config, logger)
    sim.start()
    if args.no_gui:
        if not sim.connect_to_broker():
            logger.critical("Could not connect to broker.")
            return
        while True:
            try:
                sleep(0.1)  # dummy task
            except KeyboardInterrupt:
                break
    else:
        try:
            app = QApplication()
            window = MqttSimMainWindow(sim)
            window.show()
            app.exec()
        except KeyboardInterrupt:
            app.quit()
        except Exception as e:
            logger.error(e)
    sim.stop()
    # end sim setup


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(prog="mqtt simulator", description="simulate flow of data over mqtt")
    parser.add_argument(
        "-nogui",
        "--no-gui",
        action="store_true",
        help="Specify whether the app should launch without graphical user interface",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Print logs in console")

    parser.add_argument(
        "-at",
        "--add-topic",
        metavar=("topic_name", "data_format", "interval"),
        type=str,
        nargs=3,
        help="Add topic to config",
    )
    parser.add_argument(
        "-sb",
        "--set-broker",
        metavar=("host", "port"),
        type=str,
        nargs=2,
        help="Set broker hostname (& port)",
    )
    return parser


if __name__ == "__main__":
    main(create_parser().parse_args())
    exit(0)
