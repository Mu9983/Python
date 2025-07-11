def Examination_01():
    num = input("请输入数字:")
    try:
        numint = int(num[:-1])
        if num[-1] == 'm':
            print(numint / 666.6)
        elif num[-1] == 'u':
            print(numint * 666.6)
        else:
            print("输入有误")
    except Exception:
        print("输入有误")


def Examination_02():
    A = 1.01
    total = A ** 30
    B = (total / (0.995 ** 4)) / 26
    print(B)

def Examination_03():
    class AException(Exception):
        pass

    for i in range(1, 4):
        try:
            password = int(input("请输入密码"))
            if password != 123456 and i == 3: # 假设123456是真实密码
                raise AException
            elif password != 123456:
                print("密码错误，请重新输入")
            else:
                print("业务正在操作中...")
                break
        except AException:
            print("账户冻结")


def Examination_04():
    












