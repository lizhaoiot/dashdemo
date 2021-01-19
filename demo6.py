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
            
        }
        self.main()

    def main(self):
        '''主程序'''
        while True:
            
    
            


if __name__ == '__main__':
    mp= MakePassword()
    
