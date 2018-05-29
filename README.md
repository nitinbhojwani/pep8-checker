# pep8-checker

[![Build Status](https://travis-ci.org/nitinbhojwani/pep8-checker.svg?branch=master)](https://travis-ci.org/nitinbhojwani/pep8-checker)

Fabfile to
* Check syntax and lint the python code based on PEP8 standard 
* Auto-correct according to PEP8 standard(to certain extent) and remove .pyc files

## Prerequisites
* ```requirements-python2.txt```
It contains the pip dependencies, which were used to test script with Python 2.7.13

* ```requirements-python3.txt```
It contains the pip dependencies, which were used to test script with Python 3.5.3

## Installation
* pip install -r requirements-python2.txt

OR

* pip install -r requirements-python3.txt

## Usage
This includes fabfile.py which contains the neccessary functions
Below are 4 intuitive commands supported:

### 1. To check syntax and linting in director-y(ies)

* ```fab check:dir1,dir2```
It will check all .py files inside both the directories dir1 and dir2

* ```fab check```
It will check all .py files inside current directory

### 2. To check syntax and linting in file(s)

* ```fab check_files:file1.py,file2.py```
It will check both the files - file1.py and file2.py

### 3. To auto-correct to PEP8 standards in case of director-y(ies)

* ```fab auto_clean:dir1,dir2```
It will remove .pyc files and auto-correct all the .py files(to certain extent), inside both the directories dir1 and dir2

* ```fab auto_clean```
It will remove .pyc files and auto-correct all .py files(to certain extent), inside current directory

### 4. To auto-correct to PEP8 standards in case of file(s)

* ```fab auto_clean_files:file1.py,file2.py```
It will auto-correct both files - file1.py and file2.py
