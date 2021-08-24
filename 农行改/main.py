from service import Action
act=Action()

while True:
    act.welcome()

    chose = input("请输入您的业务：")
    if chose == '1':
        act.addUser()
    elif chose =='2':
        act.saveMoney()
    elif chose== '3':
        act.takeMoney()
    elif chose == '4':
        act.transfer()
    elif chose=='5':
        act.information()
    elif chose=='6':
        break
    else:
        print("输入错误，请重新输入！")