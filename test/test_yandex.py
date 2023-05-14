from yadisk import Yandex

'''не удалось вставить токен из файла конфиг = пишет ошибку Keyerror,
 но в main все работает'''

token = 'y0_AgAAAAA3-sRwAADLWwAAAADaqLx8sT3owWYJSV2w44RBt2AmZpOHwFE'
yandex = Yandex(token=token)

class Test_yandex:
    def test_create_folder(self):
        result = yandex.create_folder(folder_path='test_folder')
        expected = 201
        assert result == expected

    def test_delete_folder(self):
        result = yandex.delete_folder(folder_path='test_folder')
        expected = 202
        assert result == expected

    def test_wrong_data(self):
        result = yandex.create_folder(folder_path=None)
        expected = 400
        assert result == expected