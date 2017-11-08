# -*- coding: utf-8 -*-

__name__ = 'search_google'
__author__ = 'Richard Wen'
__email__ = 'rrwen.dev@gmail.com'
__version__ = '1.2.1'
__license__ = 'MIT'
__description__ = 'A command line tool and module for Google API web and image search.'
__keywords__ = [
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
  'module']
__url__ = 'https://github.com/rrwen/search_google'
__download_url__ = 'https://github.com/rrwen/search_google/archive/master.zip'
__install_requires__ = [
  'google-api-python-client',
  'kwconfig',
  'requests'
]
__packages__ = ['search_google']
__package_data__ = {'search_google': ['config.json']}
__entry_points__ = {'console_scripts': ['search_google=search_google.cli:run']}
