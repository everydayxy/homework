from collections import OrderedDict

userdict = OrderedDict()
userdict[" name "] = [" age "," tel "]

# 删除用户信息


def deleteuser():
    name = input("plaese enter the user you want delete>>")
    userdict.pop(name,"user not exist")
    return

# 添加用户信息


def adduser():
    addperson = input("please enter follow format name:age:tel>>:")
    s = addperson.split(":")
    s[1], s[2] = int(s[1]), int(s[2])
    userdict[s[0]] = list(s[1:])
    return






# 查找用户信息


def finduser():
    findername = input("please enter the username of you want find:")

    if findername not in userdict:
        print("user not exist")
    else:
        print("{} : {} : {}".format(findername, userdict[findername][0],userdict[findername][1]))


# 显示所有用户信息


def showusers():
    for k,v in userdict.items():
        print("{:^10}:{:^5}:{:^}".format(k, v[0], v[1]))



# 更新用户信息
def userupdate():
    new_info = input("please enter follow format name:age:tel")
    s = new_info.split(":")
    s[1], s[2] = int(s[1]), int(s[2])
    if s[0] not in userdict.keys():
        print("the user not exist")
    else:
        userdict.update({s[0]:[s[1],s[2]]})


#在考虑把命令组成字典然后和函数结合起来，但是试了几次没有实现
# cmd_dict = {1:"deletuser",2:"adduser",3:"finduser",4:"showuser",5:"updateuser"}
# cmd_dict = {1:delete,2:affuser,3:finduser,4:showuser}这种不能组成字典
# choice = input(the num you choice is:)
# if int(choice) in cmd_dict:
#     cmd_dict[int(choice)]()  调用选择的函数
# 请问一下老师这种方法能实现吗？


count = 0
while True:
    if count == 0 or len(userdict) < 2:
        print("第一次登录请添加用户")
        adduser()
    count += 1
    print("""
    1:删除
    2：添加
    3：查找
    4：显示用户信息
    5：更新用户信息
    6：保存并推出
    """)
    choice = int(input("请输入您的选项："))

    if int(choice) == 6:
        print("will save the change and quit system")
        break
    if int(choice) == 1:
        deleteuser()
    if int(choice) == 2:
        adduser()
    if int(choice) == 3:
        finduser()
    if int(choice) == 4:
        showusers()
    if int(choice) == 5:
        userupdate()
    else:
        print("输入错误，请重新输入")