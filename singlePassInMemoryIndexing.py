'''
NAME: singlePassInMemoryIndexing.py
OS:  Windows 7 64 Bit
ENVIRONMENT: Python3.6 (Without External Dependencies) 

INPUT: file(res\EntrySeq.txt)
OUTPUT: file(tmp\tmp0.txt,tmp1.txt,... and res\invertedIndex.txt)

FUNCTION：
主要功能是实现了内存式单遍扫描索引构建算法（SPIMI : Single pass in memeory indexing）
采用SPIMI算法将一个文档集分割成多个大小相等的部分，
参考标准就是分成的每个块可以一次性的装入内存
将处理每个块产生的索引写入磁盘文件(tmp\tmp0.txt,tmp1.txt,...)，
对于下一个块则重新采用新的索引。
只要硬盘空间足够大，SPIMI就能索引任何大小的文档集。
最后将多个块合并成最后的倒排索引写入磁盘文件(res\invertedIndex.txt)

NOTE：
由于给定的语料比较小,为了体现出SPIMI算法的思想，故将每块划分为100K
即当内存大小超过100K后即将当前索引写入临时文件tmp中，然后继续索引
'''
import sys
import os

SIZE=100*1024  # 给定外部排序的内存块大小，语料太小，故设定为100KB

TMP=0          # 临时文件的个数

d={}           # 存储倒排索引的字典


def saveInFile(d,flag):  # 保存当前字典为文件，flag=0临时文件，flag=1为最终文件
    fnames=''
    fnames+=os.getcwd()        # 获取当前目录
    if flag==0:
        global TMP
        fnames+='\\tmp\\'                # 加上tmp文件夹
        tmps='tmp'+str(TMP)+'.txt'       # 临时的倒排索引文件，依次为tmp0.txt,tmp1.txt, ...
        fnames+=tmps                     # 加上文件名
        TMP+=1
    else:
        fnames+='\\res\\'                # 加上res文件夹
        fnames+='invertedIndex.txt'      # 压缩前的倒排索引文件  invertedIndex.txt
    f1=open(fnames,'w+')
    # print("\n词项"+" 频次  "+"倒排文档")
    lines=''
    for w in d:
        s1=''
        s1=' '.join(d[w][1:])   # 将list文件用' '分隔连接成一个字符串
    #    print(w+' '+str(d[w][0])+": "+s1)
        lines+=w+' '+str(d[w][0])+" "+s1+'\n'
    f1.write(lines)
    f1.close

    
# Algorithm SPIMI : Single pass in memeory indexing

def SPMIMI(fname):        # 内存式单遍扫描索引构建方法  块设定为SIZE
    fnames=''
    fnames+=os.getcwd()         # 获取当前目录
    fnames+='\\res\\'           # 加上res文件夹
    fnames+=fname      # 加上文件名
    f=open(fnames)
    global SIZE
    global TMP
    d={}
    d.clear()
    while True:         
        line=f.readline()     # 从文件中逐行读入内存
        if line=='':          # 文件已读完
            saveInFile(d,0)   # 保存临时文件
            d.clear()         # 清空字典
            break
        #print(line)
        if sys.getsizeof(d)>=SIZE:  # 超过给定内存块大小，保存临时文件并清空当前字典
            saveInFile(d,0)         # 保存临时文件
            d.clear()               # 清空字典
        s=line.split()        
        str1=s[0]       # 取出词项
        doc=s[1]        # 取出文档ID
        if str1 in d:   # 该词项已经在倒排索引中   
            d[str1][0]+=1    # 频次加1
            if doc in d[str1]:  # 文档ID已经在倒排记录中
                pass    
            else:               # 否则将该文档ID添加进入倒排记录
                d.setdefault(str1,[]).append(doc)   
        else:           # 该词项第一次出现
            d.setdefault(str1,[]).append(1)    # 频次置为1
            d.setdefault(str1,[]).append(doc)  # 添加文档ID
    f.close
    # print('字典的内存为： '+str(sys.getsizeof(d)))
    

def mergeDict(d1,d2):  # 将d2中的倒排索引合并到d1中
    for w2 in d2:      
        if w2 in d1:   # d2中的词项在d1中存在
            d1[w2][0]+=d2[w2][0]  # 频次相加
            for l2 in d2[w2][1:]: # 扫描d2中的文档ID，如果d1中没有则添加到末尾
                if l2 in d1[w2]:  
                    pass
                else:
                    d1[w2].append(l2)
        else:           # d2中的词项在d1中不存在，则直接copy给d1
            d1[w2]=d2[w2].copy()
    return d1

def mergeSeq():        # 合并多个倒排索引并写入文件保存
    global TMP
    d={}
    for i in range(0,TMP):   # 扫描每一个临时文件，并且把每个临时文件中的倒排索引转化为字典存储
        fnames=''
        fnames+=os.getcwd()              # 获取当前目录
        tmps='tmp'+str(i)+'.txt'
        fnames+='\\tmp\\'                # 加上tmp文件夹
        fnames+=tmps                     # 加上tmp文件名
        f=open(fnames,'r')     
        lines=f.readlines()
        d1={}
        for line in lines:
            lists=line.split()
            str1=lists[0]
            freq=int(lists[1])
            d1.setdefault(str1,[]).append(freq)
            for l in lists[2:]:
                d1.setdefault(str1,[]).append(l)
        d=mergeDict(d, d1)   # 合并两个倒排索引的字典
        
    saveInFile(d,1)   # 保存最终结果
    f.close
    
def main():
    global TMP
    SPMIMI('EntrySeq.txt')
    mergeSeq()
    #print('TMP==%d'%TMP)

if __name__=='__main__':
    main()
