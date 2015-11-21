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
    html()

def html():
    local('make html')

def pdf():
    local('make latex')
    # The manual PDF build typically throws tons of errors. We should fix them
    # but for now we ignore so the build server job isn't always marked as
    # failed when a mostly-working PDF is generated.
    with settings(warn_only=True):
        with lcd('build/latex'):
            # You need to run pdflatex twice to get the TOC and references
            # right.
            local('pdflatex -interaction=nonstopmode Mixxx-Manual.tex')
            local('pdflatex -interaction=nonstopmode Mixxx-Manual.tex')

@hosts(PROD)
def publish():
    regen()
    project.rsync_project(
        remote_dir=DEST_PATH,
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
