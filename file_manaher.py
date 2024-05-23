import os
import shutil


class FileManager:
    def __init__(self, current_directory):
        self.current_directory = current_directory

    def list_directory(self):
        files = os.listdir(self.current_directory)
        for file in files:
            print(file)

    def change_directory(self, new_directory):
        new_path = os.path.join(self.current_directory, new_directory)
        if os.path.isdir(new_path):
            self.current_directory = new_path
        else:
            print("Директория не найдена")

    def create_directory(self, directory_name):
        new_directory_path = os.path.join(self.current_directory, directory_name)
        os.mkdir(new_directory_path)

    def delete_directory(self, directory_name):
        directory_path = os.path.join(self.current_directory, directory_name)
        shutil.rmtree(directory_path)

    def create_file(self, file_name, content=""):
        file_path = os.path.join(self.current_directory, file_name)
        if os.path.exists(file_path):
            print("Файл уже есть")
        else:
            with open(file_path, 'w') as file:
                file.write(content)

    def read_file(self, file_name):
        file_path = os.path.join(self.current_directory, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                print(content)
        else:
            print("Файл не найден")

    def write_to_file(self, file_name, content):
        file_path = os.path.join(self.current_directory, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(content)
        else:
            print("Файл не найден")

    def delete_file(self, file_name):
        file_path = os.path.join(self.current_directory, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("Файл не найден")

    def copy_file(self, source_file, destination_file):
        source_path = os.path.join(self.current_directory, source_file)
        destination_path = os.path.join(self.current_directory, destination_file)
        if os.path.exists(source_path):
            shutil.copy(source_path, destination_path)
        else:
            print("Файл для копирования не найден")

    def move_file(self, source_file, destination_folder):
        source_path = os.path.join(self.current_directory, source_file)
        destination_path = os.path.join(self.current_directory, destination_folder)
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
        else:
            print("Файл не найден")

    def rename_file(self, old_name, new_name):
        old_path = os.path.join(self.current_directory, old_name)
        new_path = os.path.join(self.current_directory, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
        else:
            print("Файл не найден")