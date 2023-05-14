import requests
import configparser


def get_token():
    c = configparser.ConfigParser()
    c.read('config.ini')
    token = c['user_info']['ya_token']
    return token


class Yandex:
    def __init__(self, token, url='https://cloud-api.yandex.net/v1/disk/resources'):
        self.token = token
        self.url = url

    def get_headers(self):
        return {
            'Content_Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, folder_path):
        headers = self.get_headers()
        params = {'path': folder_path}
        response = requests.put(self.url, headers=headers, params=params)
        return response.status_code

    def delete_folder(self, folder_path):
        headers = self.get_headers()
        params = {
            'path': folder_path,
            'permanently': 'true',
            'force_async': 'true'
        }
        response = requests.delete(self.url, headers=headers, params=params)
        return response.status_code

if __name__=='__main__':
    token = get_token()
    yandex = Yandex(token=token)
    print(yandex.create_folder('test_folder'))
    print(yandex.delete_folder('test_folder'))