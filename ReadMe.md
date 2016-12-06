# Indexer
a big project from UCAS Course  Ben He' Modern Information Retrieval 

---------------------------------------------------------------------------------------------
## NAME��            ����Python��������ʵ��
## OS:               Windows 7 64 Bit
## ENVIRONMENT:      Python3.6 (Without External Dependencies) 
## DATE��            2016.11.6
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

### RUN		  ֱ������main.py���򼴿�

---------------------------------------------------------------------------------------------
### RUN RESULT FILE
		  tmp\tmp0,tmp1,...
                  res\EntrySeq.txt
                  res\invertedIndex.txt
		  res\SingleString.txt
		  res\FinalInvertedIndex.txt

---------------------------------------------------------------------------------------------
#### getEntrySeq.py
		  �����������ϴ�����
		  �����������res\EntrySeq.txt.txt�ļ���

#### singlePassInMemoryIndexing.py
		  ��Ҫ������ʵ�����ڴ�ʽ����ɨ�����������㷨
		  �����ĵ�������������res\invertedIndex.txt�ļ���

#### compressionAndDecompression.py
		  ��Ҫ�����Ƕ�res\invertedIndex.txt�ĵ�����������ѹ���ͽ�ѹ����
		  1���ʵ�ĵ�һ�ַ�����ʽѹ��/��ѹ�����ù�ϣ��
		  2������������Gamma����ѹ��/��ѹ
		  ����ѹ����ĵ�������������res\FinalInvertedIndex.txt�ļ���

#### run.py
		  1���������������ͳ�����������������ĵ������������������ĵ�ƽ������
		  2��������������ؼ��֣�Ȼ�󷵻ظùؼ��ֵĵ��ż�¼��

#### main.py
		  ������Ŀ����ڳ���
		  ���и���Ŀֻ��Ҫ���иó��򼴿�
---------------------------------------------------------------------------------------------