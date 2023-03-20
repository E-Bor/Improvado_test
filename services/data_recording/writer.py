import csv
import os
import platform
import json


class DataWriter:
    """Data export class in different formats"""
    def __init__(self):
        self.path_separator = "\\" if platform.system() == "Windows" else "/"
        self.path = self.path_separator.join(os.path.dirname(__file__).split(self.path_separator)[:-2])

    # Checking if there are files with the same extension
    def __check_duplicate_files(self, path: str, extension: str) -> str:
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

    # Writing data to a file
    def __write_file(self, data: list, path: str, delimiter: str = ''):
        with open(path, "w") as file:
            datawriter = csv.writer(file, delimiter=delimiter)
            for i in data:
                datawriter.writerow(i)

    # Saving data to csv
    def __save_csv(self, data: list[list], path: str = None):
        if path:
            path = self.__check_duplicate_files(path, ".csv")
        else:
            path = self.__check_duplicate_files(f"{self.path}/report.csv", ".csv")
        self.__write_file(data, path, delimiter=",")

    # Saving data to tsv
    def __save_tsv(self, data: list[list], path: str = None):
        if path:
            path = self.__check_duplicate_files(path, ".tsv")
        else:
            path = self.__check_duplicate_files(f"{self.path}/report.tsv", ".tsv")
        self.__write_file(data, path, delimiter='\t')

    # Saving data to JSON
    def __save_json(self, data: list[list], path: str = None):
        j = json.dumps(data, indent=4, ensure_ascii=False,)
        if path:
            path = self.__check_duplicate_files(path, ".json")
        else:
            path = self.__check_duplicate_files(f"{self.path}/report.json", ".json")
        with open(path, "w") as json_file:
            json_file.write(j)

    #   Selecting the save function
    def save_file(self, data: list[list], path: str = None, extension: str = "csv"):
        extension = path.split(self.path_separator)[-1].split(".")[-1] if "." in path else extension
        if extension:
            if extension.lower() == "tsv":
                self.__save_tsv(data, path)
            if extension.lower() == "json":
                self.__save_json(data, path)
            if extension.lower() == "csv":
                self.__save_csv(data, path)
        else:
            self.__save_csv(data, path)
