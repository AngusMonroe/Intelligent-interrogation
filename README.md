# Intelligent-interrogation
This is an app to give drug advise to user based on his symptom.

This project conclude two parts: **Word2vec** and **Web spider**. 


### Directory Introduction
- **Intelligent-interrogation** directory contains python code and C++ code about the project demo.
 - **pyQT** is the python code of project demo.
 - **QT** is the C++ code of project GUI.
 - **python-LDA** is a demo of LDA model in python.
- **data** directory contains training sets and database(disease information, disease dictionary and drug dictionary).
- **debug** directory contains some python code used to debug or processing data(divide words or adjust data format).
- **spider** directory contains web spiders used to get information online.
- **paper** is the introduction of our project.
- **IMG_8655** is the mind vector of our project.


### Project Functions

The main function of the project is as follows:

- use 'jieba' to divide words
- use TF-IDF to extract keywords
- use Word2vec to build model
- use Levenshtein to searching targets
- use Seq2seq model
- use LDA model
- use SQL Sever



### Requirements
- python 3.6
- PyQt5
- Navicat for SQL Sever
- urllib, urllib2, json, pymssql, word2vec, Levenshtein, jieba, jieba.analyse, xlrd, xlwt
