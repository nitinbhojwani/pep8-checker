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
Below are 2 intuitive commands supported:

### 1. To check syntax and linting in directory(ies) or file(s)

* ```fab check:dir1,dir2,filepath1```
It will check all .py files inside both the directories dir1 and dir2. Also it will check file at filepath1 if its .py

* ```fab check:filepath1,filepath2```
It will check both files at filepath1 and filepath2

* ```fab check```
It will check all .py files inside current directory

### 2. To auto-correct to PEP8 standards in case of directory(ies) or file(s)

* ```fab auto_clean:dir1,dir2,filepath1```
It will remove .pyc files and auto-correct all the .py files(to certain extent), inside both the directories dir1 and dir2 and also file at filepath1 if it's .py

* ```fab auto_clean```
It will remove .pyc files and auto-correct all .py files(to certain extent), inside current directory
