from fabric.api import *
from fabric.operations import local as lrun, run
from fabric.operations import  put
import time
import urllib2
import ConfigParser
import os.path
import json
import yaml
from pprint import pprint
import logging
from fabric.colors import green, red
from random import randint
from fabric.context_managers import cd
env.user = 'vikas'
env.shell = "/bin/sh -c"
env.use_ssh_config = True

def localhost():
  env.run = lrun
  env.hosts = ['localhost']

def deploy_test():
  run('uname -a')
