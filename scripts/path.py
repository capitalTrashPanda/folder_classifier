import os
import configparser


def get_log_path():
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    config_file = os.path.join(parent_dir, "configs", "config.ini")

    config = configparser.ConfigParser()
    config.read(config_file, encoding="utf-8")

    log_path = config.get("paths", "log_path")
    return log_path
