# Indexer
a big project from UCAS Course  Ben He' Modern Information Retrieval 

---------------------------------------------------------------------------------------------
## NAME：            基于Python的索引器实现
## OS:               Windows 7 64 Bit
## ENVIRONMENT:      Python3.6 (Without External Dependencies) 
## DATE：            2016.11.6
---------------------------------------------------------------------------------------------                
### FILE LIST
		  1 getEntrySeq.py
		  2 singlePassInMemoryIndexing.py
	 	  3 compressionAndDecompression.py
		  4 run.py
		  5 main.py
---------------------------------------------------------------------------------------------

### FILE DEPENDENCE
                  doc\shakespeare-merchant.trec.1
             	  doc\shakespeare-merchant.trec.1

---------------------------------------------------------------------------------------------

### RUN		  直接运行main.py程序即可

---------------------------------------------------------------------------------------------
### RUN RESULT FILE
		  tmp\tmp0,tmp1,...
                  res\EntrySeq.txt
                  res\invertedIndex.txt
		  res\SingleString.txt
		  res\FinalInvertedIndex.txt

---------------------------------------------------------------------------------------------
#### getEntrySeq.py
		  将给定的语料词条化
		  将结果保存在res\EntrySeq.txt.txt文件中

#### singlePassInMemoryIndexing.py
		  主要功能是实现了内存式单遍扫描索引构建算法
		  构建的倒排索引保存在res\invertedIndex.txt文件中

#### compressionAndDecompression.py
		  主要功能是对res\invertedIndex.txt的倒排索引进行压缩和解压功能
		  1，词典的单一字符串形式压缩/解压，采用哈希表
		  2，倒排索引的Gamma编码压缩/解压
		  并将压缩后的倒排索引保存在res\FinalInvertedIndex.txt文件中

#### run.py
		  1，计算出以下语料统计量：词项数量，文档数量，词条数量，文档平均长度
		  2，从命令行输入关键字，然后返回该关键字的倒排记录表

#### main.py
		  整个项目的入口程序
		  运行该项目只需要运行该程序即可
---------------------------------------------------------------------------------------------