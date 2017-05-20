# -*- coding: utf-8 -*-

from setuptools import setup
from search_google import __version__

def readme():
  with open('README.rst') as f:
    for i in range(11):
      next(f)
    return f.read()[1:]
        
setup(
  name='search_google',
  version=__version__,
  description='A command line tool and module for Google API web and image search.',
  long_description=readme(),
  author='Richard Wen',
  author_email='rrwen.dev@gmail.com',
  license='MIT',
  url='https://github.com/rrwen/search_google',
  download_url='https://github.com/rrwen/search_google/archive/master.zip',
  keywords = [
    'google',
    'api',
    'custom',
    'web',
    'image',
    'search',
    'engine',
    'cli',
    'cse',
    'command', 
    'line',
    'interface',
    'tool',
    'module'],
  entry_points={
      'console_scripts': ['search_google=search_google.cli:main']
  },
  packages=['search_google'],
  package_data={
    'search_google': ['config.json']
  },
  install_requires=[
    'argparse',
    'google-api-python-client'
  ]
)