from file_manaher import FileManager
import config


class CommandRunner:
    def __init__(self):
        self.file_manager = FileManager(config.current_dir)

    def run(self):
        while True:
            command = input(f"Текущая директория: {self.file_manager.current_directory}\nДоступные команды (list, cd, create_dir, delete_dir, create_file, read_file, write_to_file, delete_file, copy_file, move_file, rename_file, exit): ")
            if command == 'list':
                self.file_manager.list_directory()

            elif command.startswith('cd '):
                directory = command.split(' ')[1]
                self.file_manager.change_directory(directory)

            elif command.startswith('create_dir '):
                directory = command.split(' ')[1]
                self.file_manager.create_directory(directory)

            elif command.startswith('delete_dir '):
                directory = command.split(' ')[1]
                self.file_manager.delete_directory(directory)

            elif command.startswith('create_file '):
                parts = command.split(' ')
                file_name = parts[1]
                content = ' '.join(parts[2:])
                self.file_manager.create_file(file_name, content)

            elif command.startswith('read_file '):
                file_name = command.split(' ')[1]
                self.file_manager.read_file(file_name)

            elif command.startswith('write_to_file '):
                parts = command.split(' ')
                file_name = parts[1]
                content = ' '.join(parts[2:])
                self.file_manager.write_to_file(file_name, content)

            elif command.startswith('delete_file '):
                file_name = command.split(' ')[1]
                self.file_manager.delete_file(file_name)

            elif command.startswith('copy_file '):
                parts = command.split(' ')
                source_file = parts[1]
                destination_file = parts[2]
                self.file_manager.copy_file(source_file, destination_file)

            elif command.startswith('move_file '):
                parts = command.split(' ')
                source_file = parts[1]
                destination_folder = parts[2]
                self.file_manager.move_file(source_file, destination_folder)

            elif command.startswith('rename_file '):
                parts = command.split(' ')
                old_name = parts[1]
                new_name = parts[2]
                self.file_manager.rename_file(old_name, new_name)

            elif command == 'exit':
                break

            else:
                print('Команды не существует, попробуйте еще раз!')
