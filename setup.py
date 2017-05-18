# -*- coding: utf-8 -*-

from setuptools import setup

setup(
  name='search_google',
  version='0.0.0',
  description='A command line tool for Google web and image search.',
  author='Richard Wen',
  author_email='rrwen.dev@gmail.com',
  license='MIT',
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
    'interface'],
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