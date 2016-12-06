'''
NAME: main.py
OS:  Windows 7 64 Bit
ENVIRONMENT: Python3.6 (Without External Dependencies) 

FUNCTION：
整个项目的入口程序
运行该项目只需要运行该程序即可
首先调用run.py中的run.main函数开始整个程序的运行
然后由run.py中的run.main函数控制其他程序的运行

'''
import getEntrySeq                      # 导入getEntrySeq.py文件
import singlePassInMemoryIndexing       # 导入singlePassInMemoryIndexing.py文件
import compressionAndDecompression      # 导入compressionAndDecompression.py文件
import run                              # 导入run.py文件

def main(f1,f2,f3,f4):
    f4.main(f1,f2,f3)             # 运行run.py的main函数
        
if __name__=='__main__':
    main(getEntrySeq,singlePassInMemoryIndexing,compressionAndDecompression,run)
