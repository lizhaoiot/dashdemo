import os
import platform
import itertools
import time

class MakePassword(object):
    def __init__(self):
        self.rawList=[]
        self.denyList=['',' ','@']
        self.pwList=[]
        self.minLen=6
        self.maxLen=16
        self.timeout=3
        self.flag=0
        self.run={
            '0':exit,
            '1':self.addDenyList,
            '2':self.addDenyList,
            '3':self.clearRawList,
            '4':self.setRawList,
            '5':self.modifyPAsswordLen,
            '6':self.createPasswordList,
            '7':self.showPassword,
            '8':self.createPasswordFile
        }
        self.main()

    def main(self):
        '''主程序'''
        while True:
            self.mainMenu()
            op=input("输入选项:")
            if op in map(str,range()):
                self.run.get(op)()
            else:
                self.tipMainMenuInputError()
                continue
            
    def  mainMenu(self):
        self.clear()
        print("||")
        print('='*40)
        print('||')
        print('|| 0:退出程序')
        print('|| 1:输入密码原始字符串')
        print('|| 2:添加非法字符到列表')
        print('|| 3:清空原始密码列表')
        print('|| 4:整理原始密码列表')
        print('|| 5:改变默认密码长度(%d-%d)'%(self.minLen,self.maxLen))
        print('|| 6:创建密码列表')
        print('|| 7:显示所有密码')
        print('|| 8:创建字典文件')
        print('||')
        print('='*40)
        print('||')
        print("当前非法字符为：%s"%self.denyList)
        print('当前原始密码元素为：%s'%self.rawList)
        print('共有密码%d个'%len(self.pwList))
        if self.flag:
            print("已在当前目录创建密码文件dic.txt")
        else:
            print("尚未创建密码文件")
        
        
    def clear(self):
        OS=platform.system()
        if OS ==u'Windows':
            os.system('cls') 
        else:
            os.system('clear')        
        
        
    def tipMainMenuInputError(self):
        self.clear()
        print("只能输入0-8的整数，等待%d秒后重新输入"%self.timeout)
        time.sleep(self.timeout)
        
        
        
    def getRawList(self):
        self.clear()
        print("输入回车后直接退出")
        print("当前原始密码列表为:%s"%self.rawList)
        st=None
        while not st =="":
            st=input("请输入密码元素字符串：")
            if st in self.denyList:
                print("这个字符串预先设定的非法字符串")
                continue
            else:
                self.rawList.append(st)
                self.clear()
                print("输入回车后直接退出")
                print("当前原始密码列表为：%s"%self.rawList)
                
        
        
    def addDenyList(self):
        self.clear()
        print("输入回车后直接退出")
        print("当前非法字符为：%s"%self.denyList)
        st=None
        while not st =="":
            st = input("请输入需要添加的非法字符串：")
            self.denyList.append(st)
            self.clear()
            print("输入回车后直接退出")
            print("当前非法字符列表为：%s"%self.denyList)
        
        
        
    
    def clearRawList(self):
        self.rawList=[]
    
    def setRawList(self):
        a=set(self.rawList)
        b=set(self.denyList)
        self.rawList=[]
        for str in set(a-b):
            self.rawList.append(str)
            
            
        
    def modifyPAsswordLen(self):
        self.clear()
        while True:
            print("当前密码长度为%d-%d" %(self.minLen,self.maxLen))
            min = input("请输入密码最小长度：")
            max = input("请输入密码最大长度: ")
            try:
                self.minLen= int(min)
                self.maxLen= int(max)
            except ValueError:
                print("密码长队只能输入数字[6-18]")
                break
            
            if self.minLen not in range(6,19) or self.maxLen not in range(6,19):
                print("密码长度只能输入数字[6-18]")
                self.minLen =6 
                self.maxLen =16
                continue
            
            if  self.minLen == self.maxLen:
                res = input("确定将密N码长度设定为%d吗?(Yy/Nn)")
                if res not in list('yYNn'):
                    print("输入错误，请重新输入")
                    continue
                elif res in list('yY'):
                    print("好吧。你确定就好")
                    break
                else:
                    print("给个机会吧，改一下吧")
                    continue
            elif self.minLen > self.maxLen:
                print("最小长度比最大长度还长，请重新输入")
                self.minLen =6 
                self.maxLen =16
                continue
            else:
                print("设置完毕，等待%d秒后回主菜单"%self.timeout)
                time.sleep(self.timeout)
                break
                
    def createPasswordList(self):
        titleList=[]
        swapcaseList=[]
        for st in self.rawList:
            swapcaseList.append(st.swapcase())
            titleList.append(st.title())
        sub1=[]
        sub2=[]
        for st in set(self.rawList +titleList+swapcaseList):
            sub1.append(st)
            for i in range(2,len(sub1)+1):
                sub2+=list(itertools.permutations(sub1,i))#罗列所有情况
            for tup in sub2:
                PW=''
                for subPW in tup:
                    PW +=subPW
                if len(PW) in range(self.minLen,self.maxLen):
                    self.pwList.append(PW)
                else:
                    pass
                
    def showPassword(self):
        for i  in range(len(self.pwList)):
            if i%4==0:
                print("%s\n" % self.pwList[i])
            else:
                print("%s\t" % self.pwList[i])
        
        print("\n")
        print("显示%d秒，回到主菜单" %self.timeout)
        time.sleep(self.timeout)
        
    def createPasswordFile(self):
        print("当前目录下创建字典文件:dic.txt")
        time.sleep(self.timeout)
        with open('./dic.txt','w+') as fp:
            for PW in self.pwList:
                fp.write(PW)
                fp.write('\n')
        self.flag=1
            


if __name__ == '__main__':
    mp= MakePassword()
    
