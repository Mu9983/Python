def print_file_info(file_name):
    try:
        file = open(file_name, 'r', encoding='UTF-8')
        print(file.read())
    except Exception as e:
        print(e)
    else:
        file.close()

def append_to_file(file_name, data):
    try:
        file = open(file_name, 'a', encoding='UTF-8')
        file.write(data)
    except Exception as e:
        print(e)
    else:
        file.close()

if __name__ == '__main__':
    print_file_info("D:\\DevelopingSoftware\\Pycharm\\PythonProject\\test.txt")
    append_to_file("D:\\DevelopingSoftware\\Pycharm\\PythonProject\\test.txt", "\nHello")
    print_file_info("D:\\DevelopingSoftware\\Pycharm\\PythonProject\\test.txt")