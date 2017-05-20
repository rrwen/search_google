# -*- coding: utf-8 -*-

from setuptools import setup

import search_google

def readme():
  with open('README.rst') as f:
    for i in range(11):
      next(f)
    return f.read()[1:]
        
setup(
  name=search_google.__name__,
  version=search_google.__version__,
  description=search_google.__description__,
  long_description=readme(),
  author=search_google.__author__,
  author_email=search_google.__email__,
  license=search_google.__license__,
  url=search_google.__url__,
  download_url=search_google.__download_url__,
  keywords =search_google. __keywords__,
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
