import csv
import os
import platform
import json


class DataWriter:

    def __init__(self):
        self.path_separator = "\\" if platform.system() == "Windows" else "/"
        self.path = self.path_separator.join(os.path.dirname(__file__).split(self.path_separator)[:-2])

    def __check_duplicate_files(self, path, extension):
        old_path = path
        counter = 0
        if extension in path:
            path = self.path_separator.join(path.split(self.path_separator)[:-1])
        for f in os.scandir(path):
            if extension in f.name:
                counter += 1
        if counter >= 1:
            return old_path.replace(extension, f"({counter}){extension}")
        else:
            return old_path

    def __write_file(self, data, path, delimiter: str = ''):
        with open(path, "w") as file:
            datawriter = csv.writer(file, delimiter=delimiter)
            for i in data:
                datawriter.writerow(i)

    def save_csv(self, data: list[list], path: str = None):
        if path:
            path = self.__check_duplicate_files(path, ".csv")
        else:
            path = self.__check_duplicate_files(f"{self.path}/friends_data.csv", ".csv")
        self.__write_file(data, path, delimiter=",")

    def save_tsv(self, data: list[list], path: str = None):
        if path:
            path = self.__check_duplicate_files(path, ".tsv")
        else:
            path = self.__check_duplicate_files(f"{self.path}/friends_data.tsv", ".tsv")
        self.__write_file(data, path, delimiter='\t')

    def save_json(self, data: list[list], path: str = None):
        j = json.dumps(data, indent=4, ensure_ascii=False,)
        if path:
            path = self.__check_duplicate_files(path, ".json")
        else:
            path = self.__check_duplicate_files(f"{self.path}/friends_data.json", ".json")
        with open(path, "w") as json_file:
            json_file.write(j)





