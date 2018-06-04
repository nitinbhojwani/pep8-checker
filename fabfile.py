from fabric.api import local, task, settings


def get_exclude_dirs_str(exclude):
    if exclude:
        return "-not -path './" +\
               "/*' -not -path './".join(exclude.split(',')) + "/*'"
    else:
        return ""


def get_find_command(dirs, find='*.py'):
    dirs = ' '.join(set(dirs.split(','))) if dirs else '.'
    return "find %s -name \'%s\'" % (dirs.replace(',', ' '), find)


@task
def check(dirs=None, exclude=None):
    with settings(warn_only=True):
        exit(local('%s %s | xargs flake8' % (get_find_command(
            dirs), get_exclude_dirs_str(exclude))).return_code)


@task
def auto_clean(dirs=None, exclude=None):
    with settings(warn_only=True):
        commands = [
            {'cmd': 'rm -rf', 'msg': 'remove .pyc files', 'find': '*.pyc'},
            {'cmd': 'autopep8 --in-place', 'msg': 'run autopep8'},
            {'cmd': 'sed -i "" -e s/[[:space:]]*$//',
                'msg': 'remove trailing whitespaces'}
        ]

        for command in commands:
            print(command['msg'], '...')
            local('%s %s -exec %s {} \;'
                  % (get_find_command(dirs, find=command.get('find', '*.py')),
                     get_exclude_dirs_str(exclude),
                     command['cmd']))
    return
