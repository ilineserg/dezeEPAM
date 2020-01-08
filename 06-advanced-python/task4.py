"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:
> print(folder1)
V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1
А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True
"""


class PrintableFolder:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __contains__(self, item):
        if any(map(lambda x: item is x, self.content)):
            return True
        for folder in filter(lambda a: isinstance(a, PrintableFolder), self.content):
            is_exist = item in folder
            if is_exist:
                return True

    def __str__(self):
        item_prefix = "\r|-> "
        content_str = ""
        for item in self.content:
            item_str = str(item)
            if isinstance(item, PrintableFolder):
                item_str = item_str.replace("\r", "\r\r")
            content_str += item_prefix + item_str
        return f"V {self.name}\n{content_str}".replace("\r\r", "\r|   ")


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}\n"


if __name__ == "__main__":
    file1 = PrintableFile("file1")
    file2 = PrintableFile("file2")
    file3 = PrintableFile("file3")
    file4 = PrintableFile("file4")
    folder4 = PrintableFolder(name="folder4", content=[file4])
    folder3 = PrintableFolder(name="folder3", content=[folder4, file3])
    folder2 = PrintableFolder(name="folder2", content=[folder3, file2])
    folder1 = PrintableFolder(name="folder1", content=[folder2, file1])

    print(folder1)

    print(folder3 in folder2)
