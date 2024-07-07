import os
import configparser

config = configparser.ConfigParser()
config_path = r"C:\Users\tandc\OneDrive\桌面\folder_classifier\configs\config.ini"
config.read(config_path)


def get_file_dir():
    return os.path.dirname(__file__)


def get_config_value(section, key):
    return config.get(section, key)


def get_project_dir(project_name):
    path = get_file_dir()
    while True:
        parent = os.path.dirname(path)
        parent_base = os.path.basename(parent)
        if parent_base == project_name:
            return parent
        path = parent


def get_folder_path(folder_name):
    project_name = get_config_value("Project", "name")
    folder_name = get_config_value("Paths", folder_name)
    folder_path = os.path.join(get_project_dir(project_name), folder_name)
    return folder_path
