import pkg_resources
from subprocess import call
'''pip_update_all
Based on user515656's answer at https://stackoverflow.com/questions/2720014/how-to-upgrade-all-python-packages-with-pip
'''
packages = [dist.project_name for dist in list(pkg_resources.working_set)]
call("pip install --upgrade " + ' '.join(packages), shell=True)