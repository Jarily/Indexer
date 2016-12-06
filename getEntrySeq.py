'''
NAME: getEntrySeq.py
OS:  Windows 7 64 Bit
ENVIRONMENT: Python3.6 (Without External Dependencies) 

INPUT: file(doc\shakespeare-merchant.trec.1 and doc\shakespeare-merchant.trec.1)
OUTPUT: file(res\EntrySeq.txt)

FUNCTION：
将给定的语料词条化
删除影响检索结果的一些特殊词项，例如<DOC>,<speaker>,<title>等等
得出每个词条和它所在的DOC编号的序列
将结果保存在res\EntrySeq.txt.txt文件中
res\getEntrySeq.txt的内容为;
---------------
词条 docId编号
...
...
...
---------------
将每个DOC的标题保存在全局的title字典中，便于后期操作
'''

import os

# 定义全局变量
title={}  # 保存每个DOC的title
CNT=1     # 记录DOC的编号
STR=''    # 纪录所有的输出结果，即每个文档中的单词和它出现的频次
SUM=0     # 记录预料中出现的单词总数
CNTt=1    # 记录title的编号

#包含所有要保留的字符集合
keep={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
      'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
      's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '}#, '-', "'"}

alphabet={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
      'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
      's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}


def JudgeAlphabet(s):      # 判断一个字符串是否一个字母都没有(无效单词)
    for c in s.lower():
        if c in alphabet:
            return True
    return False
    

def normalize(s):          # 把一个字符串格式化，剔除数字等其他符号
    result=''
    for c in s.lower():
        if c in keep:
            result+=c
        else:
            result+=' '
    return result

def getStr(s,str1,str2):   # 获取两个标记符中间的字符串
    ind1=s.find(str1)
    ind2=s.find(str2)
    if ind1==-1 or ind2==-1:  # 查询失败
        return ''
    lens=len(str1)
    s1=s[ind1+lens:ind2]
    #s1=normalize(s1)
    return s1

def deleteMark(s,s1):      # 删除<spearer>等标记符
    ind=s.find(s1)
    if ind==-1:      # 查找失败
        return s
    lens=len(s1)
    s=s[:ind]+s[ind+lens:]
    return s

def deleteSeg(s,s1,s2):    # 删除两个标记符以及之间的字符串
    ind1=s.find(s1)
    ind2=s.find(s2)
    if ind1==-1 or ind2==-1:  # 查找失败
        return s
    lens=len(s2)
    s=s[:ind1]+s[ind2+lens:]
    return s

def solve(fname):
    global STR   # 声明为全局变量
    global CNT   
    global SUM
    global CNTt
    global title
    s=open(fname, 'r').read()
    while s.find('<DOC>')!=-1:  # 以DOC为单位处理每个DOC的内容
        s1=getStr(s,'<DOC>','</DOC>')   # 获取DOC之间的字符串 
        s2=getStr(s1,'<title>','</title>')  # 获取title之间的字符串
        s2=normalize(s2)  # 标准格式化
        title[CNTt]=s2
        CNTt+=1
        s1=deleteSeg(s1,'<DOCNO>','</DOCNO>') # 删掉DOCNO和它们之间的字符串
        s1=deleteMark(s1,'<speaker>')    # 删掉标记符<speaker>
        s1=deleteMark(s1,'</speaker>')
        s1=deleteMark(s1,'<title>')      # 删掉标记符<title>
        s1=deleteMark(s1,'</title>')
        s1=normalize(s1)
        words=s1.split()
        lens=len(words)
        SUM+=lens
        for w in words:
            STR=STR+w+' '+str(CNT)+'\n'
        s=deleteSeg(s,'<DOC>','</DOC>')  # 删除总文件中已处理的DOC段
        CNT+=1
    return

def main():  # 处理两个预料，并将每个DOC中出现的单词和出现的频次保存在文件中
    global STR
    global CNT
    STR=''
    CNT=1
    fnames=''
    fnames+=os.getcwd()         # 获取当前目录
    fnames+='\\doc\\'           # 加上doc文件夹
    f1=f2=fnames
    f1+='shakespeare-merchant.trec.1'      # 加上文件名
    f2+='shakespeare-merchant.trec.2'
    solve(f1)
    solve(f2)
    fnames=''
    fnames+=os.getcwd()         # 获取当前目录
    fnames+='\\res\\'           # 加上res文件夹
    fnames+='EntrySeq.txt'      # 加上文件名
    f=open(fnames,'w+')
    f.writelines(STR)
    f.close()
    '''
    print('总的单词数：%d'%SUM)
    print('tittle：%d'%CNTt)
    print('docId：%d'%CNT)
    for t in title:
        print('第%d个title为：'%t+' '+title[t])
    '''

if __name__=='__main__':
    main()
