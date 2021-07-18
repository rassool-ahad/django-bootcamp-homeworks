import os


def printFilesName_Generator(fileaddr: str):
    "os.walk is just a generator why we define generator again??????"
    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            yield os.path.join(root, name)


def printFilesNameFormat_Generator(fileaddr: str, format: str):
    for root, dirs, files in os.walk("." + format, topdown=True):
        for name in files:
            yield os.path.join(root, name)
