# Intelligent-interrogation
This is an app to give drug advise to user based on his symptom.

![屏幕快照 2018-06-01 上午9.13.29.png](https://i.loli.net/2018/06/01/5b109de99a546.png)


### Directory Introduction
- **Intelligent-interrogation** directory contains python code and C++ code about the project demo.
- **data** directory contains training sets and database(disease information, disease dictionary and drug dictionary).
- **debug** directory contains some python code used to debug or processing data(divide words or adjust data format).
- **spider** directory contains web spiders used to get information online.
- **framework** is the mind vector of our project.


### Project Functions

The main function of the project is as follows:

- use 'jieba' to divide words
- use TF-IDF to extract keywords
- use Word2vec to build model
- use Levenshtein to searching targets
- use Seq2seq model
- use LDA model
- use SQL Sever
- use django framework



### Requirements
- python 3.6
- Navicat for SQL Sever
- urllib, urllib2, json, pymssql, word2vec, Levenshtein, jieba, jieba.analyse, xlrd, xlwt, django


### Usage

1. run http sever
	
	```
	cd Intelligent-interrogation/Intelligent-interrogation/IISever
	python manage.py runserver
	```
	
2. Open `http://127.0.0.1:8000/` in browser