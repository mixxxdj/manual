from fabric.api import *
import fabric.contrib.project as project
import os

from source import conf

PROD = 'stacktrace.org'
# Format the path using the version in the Sphinx config.
DEST_PATH = '/home/mixxx/public_html/manual/%s' % conf.version
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DEPLOY_PATH = os.path.join(ROOT_PATH, 'build/html')
env.user = 'mixxx'

def clean():
    local('make clean')

def regen():
    clean()
    local('make html')

@hosts(PROD)
def publish():
    regen()
    project.rsync_project(
        remote_dir=DEST_PATH,
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
