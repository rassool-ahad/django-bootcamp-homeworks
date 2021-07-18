class BackupOpen:
    backuptext = ""

    def __init__(self, fileaddr, option):
        self.fileaddr = fileaddr
        self.option = option
        try:
            __f = open(fileaddr, "r")
            self.backuptext = __f.read()
            print(self.backuptext)
            __f.close()
        except FileNotFoundError:
            raise Exception("there is no file with that name to backup")

    def __enter__(self):
        self.__file = open(self.fileaddr, self.option)
        return self

    def read(self):
        return self.__file.read()

    def write(self, s: str):
        self.__file.write(s)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print("oops")
            self.__file.close()
            with open(self.fileaddr, "w") as __:
                print("asd")
                print(self.backuptext)
                __.write(self.backuptext)
        return True


with BackupOpen("rasool.txt", "w") as file:
    file.write("rasool")
    raise Exception

with open("rasool.txt") as f:
    print(f.read())
    # print(s)
