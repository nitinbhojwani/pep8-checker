from fabric.api import local, task, settings


@task
def check(dirs=None):
    with settings(warn_only=True):
        if dirs:
            dirs = dirs.split(',')
            for directory in dirs:
                if directory:
                    directory = directory[:-
                                          1] if directory[-1] == '/' else directory
                    result = local('flake8 ' + str(directory) + '/*.py')
            return
        result = local('flake8 *.py')
        if not result:
            print('Please fix the Errors')
        return


@task
def check_files(files=None):
    with settings(warn_only=True):
        if files:
            files = files.split(',')
            for file_name in files:
                if not '.py' in file_name:
                    print (file_name + " is not .py file")
                    continue
                result = local('flake8 ' + str(file_name))
            if not result:
                print('Please fix the Errors')
            return
        else:
            print('format - fab check_files:filepath/filename1.py,filename2.py')
        return


@task
def auto_clean(dirs=None):
    with settings(warn_only=True):
        if dirs:
            dirs = dirs.split(',')
            for directory in dirs:
                local('find ' + str(directory) +
                      ' -name "*.pyc" -exec rm -rf {} \;')
                directory = directory[:-
                                      1] if directory[-1] == '/' else directory
                result = local('autopep8 --in-place ' +
                               str(directory) + '/*.py')
            return
        else:
            print('removing .pyc files')
            local('find . -name "*.pyc" -exec rm -rf {} \;')
            result = local('find . -name \'*.py\' -exec autopep8 --in-place '{}' \;')
            if not result:
                print('Please fix the Errors')
            return


@task
def auto_clean_files(files=None):
    with settings(warn_only=True):
        if files:
            files = files.split(',')
            for file_name in files:
                if not '.py' in file_name:
                    print (file_name + " is not .py file")
                    continue
                result = local('autopep8 --in-place ' +
                               str(file_name))
            return
