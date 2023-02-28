from ya_disk import YandexDisk

import configparser
from pprint import pprint


def get_yadisk_token():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    return config['tokens']['yadisk_token']


if __name__ == '__main__':
    yadisk = YandexDisk(get_yadisk_token())
    folders = yadisk.get_folders_list()
    pprint(folders)



