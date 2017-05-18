# -*- coding: utf-8 -*-

from setuptools import setup

def readme():
  with open('README.rst') as f:
    for i in range(9):
      next(f)
    return f.read()[1:]
        
setup(
  name='search_google',
  version='1.0.2',
  description='A command line tool for Google web and image search.',
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
    'tool'],
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