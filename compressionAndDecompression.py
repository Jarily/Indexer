'''
NAME: compressionAndDecompression.py
OS:  Windows 7 64 Bit
ENVIRONMENT: Python3.6 (Without External Dependencies) 

INPUT: file(res\invertedIndex.txt)
OUTPUT: file(res\FinalInvertedIndex.txt and res\SingleString.txt)

FUNCTION：
主要功能是实现倒排索引的压缩和解压功能
1，词典的单一字符串形式压缩/解压，采用哈希表
2，倒排索引的Gamma编码压缩/解压
根据singlePassInMemoryIndexing.py程序获取的索引文件res\invertedIndex.txt
实现其上述两种压缩和解压功能
最终将压缩后的倒排记索引保存在res\FinalInvertedIndex.txt

NOTE：
由于词典采用单一字符串形式压缩，故将词典组成的单一字符串保存在res\SingleString.txt中
索引时，采用Python的字典功能查询词项，维护了一个全局的字典dword
dword 的 key值为词项，value值为该词项在单一字符串中的起始下标
压缩后的倒排索引的键值则为该词项在单一字符串中的起始下标

倒排索引的记录压缩：
第一个值为第一个文档的gamma编码，
第二个值则为第二个文档和第一个文档的差的gamma编码
...
（由于在SPIMI算法中的实现顺序和合并顺序，可以保证获取的文档序列是增序）

最终压缩后的倒排索引表的存储形式为：
起始下标  词项长度 频次  gamma编码压缩后的记录序列

'''


# compressionAndDecompression.py
import struct
import pickle
import sys
import os
words=''
dword={}
d={}

def GetGammaCode(a):   # gamma压缩
    if a==0:
        return '0'
    s1=bin(a)
    offset=s1[3:]   # 偏移 0bxxxxx 去掉前三位即去掉高位的1
    lens=len(offset)
    length='1'*lens+'0'       # 长度部分的一元码
    gamma=length+offset  # 最终的gamma编码
    return gamma
'''
def DeGammaCompression(gamma):  # gamma解压
    lst=[]
    for g in gamma:
        if g=='0':
            lst.append('1')
        elseif 
    lens=len(gamma)
    length=int(lens/2)
    s1='0b1'
    s1+=gamma[length+1:]
    a=int(s1,2)
    return a
'''

def DeGammaCompressionSeg(gamma):  # 一段gamma编码解压
    lst=[]
    lens=len(gamma)
    i=0
    flag=0
    tmp=-1
    while i<lens:
        if gamma[i]=='0':
            if flag==0:
                tmp=1
                lst.append(str(tmp))
                flag=1
            else:
                tmp=tmp+1
                lst.append(str(tmp))
            i+=1
        else:
            j=i
            while gamma[j+1]=='1':
                j+=1
            leng=j-i+1
            s1='0b1'
            s1+=gamma[j+2:j+leng+2]
            a=int(s1,2)
            if flag==0:
                tmp=a
                lst.append(str(tmp))
                flag=1
            else:
                tmp=tmp+a
                lst.append(str(tmp))
            i=i+leng*2+1
    return lst


def DeCompressionIndex(lst):  # 解压索引文档序列，为list类型
    l=[]
    l=DeGammaCompressionSeg(lst[2])
    '''
    #l.append(lst[1])
    # a=DeGammaCompression(lst[2])
    l.append(str(a))
    tmp=a
    print(a)
    print(lst)
    for ll in lst[3:]:
        tt=DeGammaCompressionSeg(ll)
        #tmp+=a
        l.append(tt)
    '''
    return l


def SaveFile(d,fname):  # 保存当前字典为文件，写入文件夹res中
    fnames=''
    fnames+=os.getcwd() # 获取当前目录
    fnames+='\\res\\'   # 加上res文件夹
    fnames+=fname       # 加上文件名
    #print(fnames) 
    f=open(fnames,'w+')
    # print("\n词项"+" 频次  "+"倒排文档")
    lines=''
    for w in d:
        s1=''
        s1=' '.join(d[w][2:])   # 将list文件用' '分隔连接成一个字符串
    #    print(w+' '+str(d[w][0])+": "+s1)
        lines+=str(w)+' '+str(d[w][0])+" "+str(d[w][1])+' '+s1+'\n'
    f.write(lines)
    f.close


def GetInvertedIndex(fname):    # 将倒排索引压缩后保存在'res\FinalInvertedIndex.txt'
    global words
    global d
    global dword
    fnames=''
    fnames+=os.getcwd() # 获取当前目录
    fnames+='\\res\\'   # 加上res文件夹
    fnames+=fname       # 加上文件名
    f=open(fnames,'r')     
    lines=f.readlines()
    d={}
    for line in lines:
        lists=line.split()
        str1=lists[0]
        freq=int(lists[1])       # 词项频率
        len1=len(words)          # 当前词项在单一字符串中的起始位置
        len2=len(str1)           # 词项长度
        dword[str1]=len1
        words+=str1
        d.setdefault(len1,[]).append(len2)
        d.setdefault(len1,[]).append(freq)
        #d1.setdefault(str1,[]).append(freq)
        #tmp0=lists[2]
        tmp1=int(lists[2])
        tmp=''
        tmp+=GetGammaCode(tmp1)
        #d.setdefault(len1,[]).append(tmp)  # 保存第一个文档的ID
        for l in lists[3:]:
            ll=int(l)
            tmp2=ll-tmp1                   # 文档的差值
            tmp+=GetGammaCode(tmp2)         # gamma压缩
            #d.setdefault(len1,[]).append(tmp)
            tmp1=ll
        d.setdefault(len1,[]).append(tmp)
    f.close
    SaveFile(d,'FinalInvertedIndex.txt')
    fnames=''
    fnames+=os.getcwd()           # 获取当前目录
    fnames+='\\res\\'             # 加上res文件夹
    fnames+='SingleString.txt'    # 加上文件名
    f=open(fnames,'w+')
    f.write(words)
    f.close
    
def main():
    GetInvertedIndex('invertedIndex.txt')

if __name__=='__main__':
    GetInvertedIndex('invertedIndex.txt')
