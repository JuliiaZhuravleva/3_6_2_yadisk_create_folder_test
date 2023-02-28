import pytest
import configparser
from ya_disk import YandexDisk


def get_yadisk_token():
    config = configparser.ConfigParser()
    config.read("../settings.ini")
    return config['tokens']['yadisk_token']


@pytest.mark.parametrize(
    'folder_name', [('test'), ('test2')]
)
def test_create_folder_status(folder_name):
    yadisk = YandexDisk(get_yadisk_token())
    current_folders = yadisk.get_folders_list()
    if folder_name in current_folders:
        assert False, f'Папка {folder_name} уже существует'
    else:
        result_code = yadisk.create_folder(folder_name)
        assert result_code == 201
        yadisk.delete_folder(folder_name)


@pytest.mark.parametrize(
    'folder_name', [('test'), ('test2')]
)
def test_create_folder_name(folder_name):
    yadisk = YandexDisk(get_yadisk_token())
    current_folders = yadisk.get_folders_list()
    if folder_name in current_folders:
        assert False, f'Папка {folder_name} уже существует'
    else:
        yadisk.create_folder(folder_name)
        current_folders = yadisk.get_folders_list()
        assert folder_name in current_folders
        yadisk.delete_folder(folder_name)


@pytest.mark.parametrize(
    'folder_name', [('test'), ('test2')]
)
def test_create_folder_authorization(folder_name):
    yadisk = YandexDisk('111')
    result_code = yadisk.create_folder(folder_name)
    assert result_code == 401
