import requests


class YandexDisk:
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_resources(self, path='/'):
        params = {'path': path}
        response = requests.get(self.url, headers=self.get_headers(), params=params).json()
        return response['_embedded']['items']

    def get_folders_list(self):
        resources = self.get_resources()
        folders = [item['name'] for item in resources if item['type'] == 'dir']
        return folders

    def create_folder(self, path):
        params = {'path': path}
        response = requests.put(self.url, headers=self.get_headers(), params=params)
        return response.status_code

    def delete_folder(self, path):
        params = {'path': path}
        response = requests.delete(self.url, headers=self.get_headers(), params=params)
        return response.status_code
