import os
import platform
import itertools
import time

def main():
    '''主程序'''
    global rawList #原始数据列表
    rawList=[]
    global denyList #非法单词列表
    denyList =[' ','','@']
    global pwList  #最终的密码列表
    pwList =[]
    global minLen #密码的最小长度
    minLen =6
    global maxLen #密码的最大长度
    maxLen =16
    global timeout
    timeout =3
    global flag
    flag =0
    run ={
    '0':exit,
    '1':getRawList,
    '2':addDenyList,
    '3':clearRawList,
    '4':setRawList,
    '5':modifyPasswordLen,
    '6':createPasswordList,
    '7':showPassword,
    '8':createPasswordFile
    }

    while True:
        mainMenu()
        op=input('输入选项：')
        if op in map(str,range(len(run))):
            run.get(op)()
        else:
            tipMainMenyinputError()
            continue

def mainMenu():
    '''主菜单'''
    global denyList
    global rawList
    global pwList
    global flag
    clear()
    print('||')
    print('||'*40)
    print('||')
    print('||0:退出程序')
    print('||1:输入密码原始字符串')
    print('||2:添加非法字符到列表')
    print('||3:清空原始密码列表')
    print('||4:整理原始密码列表')
    print('||5:改变默认密码长度(%d-$d)'%(minLen,maxLen))
    print('||6:创建密码列表')
    print('||7:显示所有密码')
    print('||8:创建字典文件')
    print('||')
    print('||'*40)
    print('||')
    print('当前非法字符为：%s'%denyList)
    print('当前原始密码元素为：%s'%rawList)
    print('共有密码%d个'%len(pwList))
    if flag:
        print("已在当前目录创建密码文件dic.txt")
    else:
        print("尚未创建密码文件")





def clear():
    '''清屏函数'''
    OS =platform.system()
    if (OS ==u'Windows'):
        os.system('cls')
    else:
        os.system('clear')


def tipMainMenyinputError():
    '''错误信息'''
    clear()
    print("只能输入0-7的整数，等待%d秒后重新输入"%timeout)
    time.sleep(timeout)


def getRawList():
    '''获取原始数据列表'''
    clear()
    global denyList
    global rawList
    print("输入回车后直接退出")
    print("当前原始密码列表为：%s"%rawList)
    st=None
    while not st =="":
        st= input("请输入密码元素字符串:")
        if st in denyList:
            print("此字符串中存在预先设定的非法字符串")
            continue
        else:
            rawList.append(st)
            clear()
            print("输入回车后直接退出")
            print("当前原始密码列表：%s"%rawList)

def addDenyList():
    '''增加非法词'''
    clear()
    global denyList
    print("输入回车后直接退出")
    print("当前非法字符为：%s"%denyList)
    st=None
    while not st =="":
        st=input("请输入需要添加的非法字符串:")
        denyList.append(st)
        clear()
        print("输入回车后直接退出")
        print("当前非法字符列表为：%s" %denyList)


def clearRawList():
    '''清空原始数据列表'''
    global rawList
    rawList=[]
    
def setRawList():
    '''整理原始数据列表'''
    global rawList
    global denyList
    a=set(rawList)
    b=set(denyList)
    rawList=[]
    for str in set(a-b):
        rawList.append(str)
        
def modifyPassword():
    '''修改默认密码的长度'''
    clear()
    global maxLen
    global minLen
    while True:
        print("当前密码长度为%d-%d" %(minLen,maxLen))
        min = input("请输入密码的最小长度：")
        max = input("请输入密码的最大长度：")
        try:
            minLen =int(min)
            maxLen =int(max)
        except ValueError:
            print("密码长度只能输入数字[6-18]")
            break
        if minLen not in range(6,19) or maxLen not in range(6,19):
            print("密码长度只能输入数字[6-18]")
            minLen =6
            maxLen =16
            continue
        if minLen == maxLen:
            res = input("确认将密码长度设定为%d吗？(Yy/Nn)" %maxLen)
            if res not in list('yYnN'):
                print("")
                
            
            
            
def createPasswordList():
    '''创建密码列表'''

def showPassword():
    '''显示创建的密码'''

def createPasswordFile():
    '''创建密码字典文件'''

if __name__ == '__main__':
    main()