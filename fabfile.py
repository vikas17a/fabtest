from fabric.api import run
from fabric.operations import local
def host_type():
    local('uname -s')
