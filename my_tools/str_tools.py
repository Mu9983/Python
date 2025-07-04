def str_reverse(str):
    return str[::-1]

def substr(str, x, y):
    return str[x:y]

if __name__ == '__main__':
    print(str_reverse("12341234"))
    print(substr("12341234", 2, 5))