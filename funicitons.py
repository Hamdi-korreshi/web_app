def get_tasks(file_path='todo.txt'):
    """ Opens the default file to read and return the list of tasks"""
    with open(file_path, 'r') as file_local:
        read = file_local.readlines()
    return read


def write_file(to_be_written, file_path='todo.txt'):
    """ Write the task list into the text file"""
    with open(file_path, 'w') as file:
        file.writelines(to_be_written)


if __name__ == '__main__':
    print(get_tasks())
