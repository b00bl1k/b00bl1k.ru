Title: Тестирование загрузки изображений с помощью pytest-django
Date: 2021-04-20

Для начала напишем фикстуру, которая создаёт изображение для загрузки:

```py
@pytest.fixture(scope="session")
def image_file(tmpdir_factory):
    img = PilImage.new("RGB", (640, 480))
    fn = tmpdir_factory.mktemp("data").join("img.jpg")
    img.save(str(fn))
    return fn
```

Я использую `PIL` для создания подходящего изображения.

Далее приведён код, который тестирует загрузку изображения методом POST:

```py
def test_upload_image(client, image_file, settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir
    with open(image_file, "rb") as fp:
        response = client.post(url, {"image": fp})
    assert response.status_code == 200
```

Перед загрузкой файла изменяется значение `MEDIA_ROOT` на временный каталог. 
Здесь использована стандартная pytest фикстура `tmpdir` и фикстура `settings` из 
модуля [pytest-django](https://github.com/pytest-dev/pytest-django).
