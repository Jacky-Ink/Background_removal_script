# Background_removal_script - скрипт для удалени фона на изображениях

1. Склонировать репозитарий:
    git clone https://github.com/Jacky-Ink/Background_removal_script.git

2. Установить виртуальное окружение:
    python -m venv venv

3. Активировать виртуальное окружение:
    source venv/Scripts/activate

4. Выполнить команду:
    pip install rembg

5. Прописать пути к папкам input_imgs и output_imgs в файле main.py

6. Установить модели для работы программы
    Все модели загружаются и сохраняются в домашней папке пользователя в каталоге `.u2net`.

    Доступные модели:

    -   u2net ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx), [source](https://github.com/xuebinqin/U-2-Net)): Предварительно обученная модель для общих случаев использования.
    -   u2netp ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2netp.onnx), [source](https://github.com/xuebinqin/U-2-Net)): Облегченная версия модели u2net.
    -   u2net_human_seg ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net_human_seg.onnx), [source](https://github.com/xuebinqin/U-2-Net)):Предварительно обученная модель для сегментации человека.
    -   u2net_cloth_seg ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net_cloth_seg.onnx), [source](https://github.com/levindabhi/cloth-segmentation)): Предварительно обученная модель для парсинга тканей из портрета человека. Здесь одежда разбита на 3 категории: Верхняя часть тела, нижняя часть тела и полное тело.
    -   silueta ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/silueta.onnx), [source](https://github.com/xuebinqin/U-2-Net/issues/295)): То же, что и u2net, но размер уменьшен до 43 Мб.

## License

Copyright (c) 2022-present [Inna Klyakhina(Jacky-Ink)](https://github.com/Jacky-Ink)

Licensed under [MIT License](./LICENSE)