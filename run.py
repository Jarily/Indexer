'''
NAME: run.py
OS:  Windows 7 64 Bit
ENVIRONMENT: Python3.6 (Without External Dependencies) 

INPUT: 从键盘输入关键字
OUTPUT: 返回该关键字的倒排记录表(如果存在)

FUNCTION：
1，计算出以下语料统计量：
词项数量，文档数量，词条数量，文档平均长度
2，从命令行输入关键字，然后返回该关键字的倒排记录表

NOTE：
当从键盘上输入一个关键字的时候，
首先利用getEntrySeq.py程序中的normalize函数将这个关键字规范化
然后在利用compressionAndDecompression.py程序中的字典查询到该关键字在单一字符串中的下标作为Key值
利用这个Key值在最终的倒排索引文件res\FinalInvertedIndex.txt中进行解压输出

'''

import getEntrySeq
import singlePassInMemoryIndexing
import compressionAndDecompression
import os

ITEM=0    # 词项数量
ENTRY=0   # 词条数量
DOCSUM=0  # 文档数量
DOCAVE=0  # 文档平均长度

def GetInf(f1,f2,f3):
    global ITEM
    global ENTRY
    global DOCSUM
    global DOCAVE
    ENTRY=f1.SUM
    DOCSUM=f1.CNT-1
    DOCAVE=int(ENTRY/DOCSUM)
    ITEM=len(f3.d)
    print('语料的词项数量为： %d'%ITEM)
    print('语料的文档数量为： %d'%DOCSUM+' (From 1 to %d)'%DOCSUM)
    print('语料的词条数量为： %d'%ENTRY)
    print('语料的文档平均长度为： %d'%DOCAVE)
    

def Run(f1,f2,f3):
    GetInf(f1,f2,f3)

    #for t in f1.title:
    #    print('第%d个title为：'%t+' '+f1.title[t])
    print()
    print('-----------------！程序开始运行！-----------------')
    while True:
        s1=input("   请输入一个需要检索的内容(单独输入0退出程序)     \n")
        if s1=='0':
            print('-----------------！程序运行结束！-----------------')
            print()
            break
        s1=f1.normalize(s1)
        if f1.JudgeAlphabet(s1)==False:
            print('----------------！请输入有效单词！----------------')
            continue
        s2=s1.split()
        for w in s2:
            if w in f3.dword:
                ind=f3.dword[w]
                #print(f3.d)
                print("   词项 %s 的"%w+"在语料库中出现的频次为: %d"%f3.d[ind][1])
                lst=f3.DeCompressionIndex(f3.d[ind]) # 解压索引表
                print("   词项 %s 的倒排记录表为:"%w)
                print(lst)
                #d[ind]
            else:
                print("   语料库中没有  %s :"%w)
       # print(s2)
        print('--------------------------------------------------')
    

def main(f1,f2,f3):
    # 在当前路径下建立tmp和res文件夹，分别保存临时文件和结果文件
    tmp=''
    res=''
    tmp+=os.getcwd()
    res+=os.getcwd()
    tmp+='//tmp'
    res+='//res'
    if os.path.exists(tmp) == False:
        os.mkdir("tmp")
    if os.path.exists(res) == False:
        os.mkdir("res")
    f1.main()                  # 运行getEntrySeq.py文件
    f2.main()                  # 运行singlePassInMemoryIndexing.py文件
    f3.main()                  # 运行compressionAndDecompression.py文件

    Run(f1,f2,f3)
        
if __name__=='__main__':
    main(getEntrySeq,singlePassInMemoryIndexing,compressionAndDecompression)

