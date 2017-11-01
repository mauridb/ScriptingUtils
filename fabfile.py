from __future__ import with_statement
from fabric.api import *


# fab prerelease_master:'BRANCH-MASTER-MESSAGE'
def prerelease_master(msg):
	local('git add .')
	local('git commit -m "{}"'.format(msg))
	local('git push origin master')

# fab release:'RELEASE-tag version'
def release(msg):
	local('git checkout release')
	local('git merge master')
	local('git tag -a {} -m "RELEASE: last version {}"'.format(msg,msg))
	local('git push origin release')
	local('git checkout master')
