import sys
import os
current = os.path.abspath(os.getcwd())
parent = current.find('universal-geocoder')
# print(current[:parent + len('scripts')] + '/')
sys.path.insert(0, current[:parent + len('universal-geocoder')])
DIRECTORIES = ['core', 'support', 'preproc', 'tests', 'data', 'analysis']
for directory in DIRECTORIES:
    path = os.path.join(current[:parent + len('universal-geocoder')] + '/', directory)
    # print(path)
    sys.path.insert(0, path)
