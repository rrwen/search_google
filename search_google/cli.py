# -*- coding: utf-8 -*-

"""
  Usage:
    search_google [q] [--optional]
    search_google [-positional] ...
  
  A command line tool for Google web and image search.
  
  Positional arguments:
    q                 keyword query
    -h                show this help message and exit
    -i                show documentation in browser
    -a                show optional arguments in browser
    -s <arg>=<value>  set default optional arguments
    -r <arg>          remove default arguments
    -v                view default arguments
    -d                reset default arguments
  
  Optional arguments:
    --num             num of results (default: 3)
    --searchType      'image' or unassigned for web search
    --dateRestrict    time period of search
    --start           index of first result
    --fileType        format for image search (default: png)
    --save_links      path for text file of links
    --save_metadata   path for metadata JSON file
    --save_downloads  path for directory of link downloads
    --option_silent   'True' to disable preview
    --option_preview  num of results to preview
    
    For more arguments use: search_google -a
    
  Examples:
    
    Set developer and search engine key arguments
      > search_google -s build_developerKey="dev_key"
      > search_google -s cx="cse_key"
    
    Web search for keyword "cat"
      > search_google cat
    
    Search for "cat" images
      > search_google cat --searchType=image
    
    Download links to directory
      > search_google cat --save_downloads=downloads
  
  For more information visit use: search_google -i
"""

from os.path import isfile
from pkg_resources import resource_filename, Requirement
from pprint import pprint
from sys import argv
from webbrowser import open_new_tab

import json
import kwconfig
import search_google.api

_doc_link = 'https://github.com/rrwen/search_google'
_cse_link = 'https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/customsearch_v1.cse.html'
    
def run(argv=argv):
  """Runs the search_google command line tool.
  
  This function runs the search_google command line tool 
  in a terminal. It was intended for use inside a py file 
  (.py) to be executed using python.
  
  Notes:
    * ``[q]`` reflects key ``q`` in the ``cseargs`` parameter for :class:`api.results`
    * Optional arguments with ``build_`` are keys in the ``buildargs`` parameter for :class:`api.results`
  
    For distribution, this function must be defined in the following files::
      
      # In 'search_google/search_google/__main__.py'
      from .cli import run
      run()
      
      # In 'search_google/search_google.py'
      from search_google.cli import run
      if __name__ == '__main__':
        run()
      
      # In 'search_google/__init__.py'
      __entry_points__ = {'console_scripts': ['search_google=search_google.cli:run']}
  
  Examples::
    
    # Import google_streetview for the cli module
    import search_google.cli
    
    # Create command line arguments
    argv = [
      'cli.py',
      'google',
      '--searchType=image',
      '--build_developerKey=your_dev_key',
      '--cx=your_cx_id'
      '--num=1'
    ]
    
    # Run command line
    search_google.cli.run(argv)
    
  """
  config_file = kwconfig.manage(
    file_path=resource_filename(Requirement.parse('search_google'), 'search_google/config.json'),
    defaults={
      'build_serviceName': 'customsearch',
      'build_version': 'v1',
      'num': 3,
      'fileType': 'png',
      'option_silent': 'False',
      'option_preview' : 10})
  
  # (commands) Main command calls
  if len(argv) > 1:
    if argv[1] == '-i': # browse docs
      open_new_tab(_doc_link)
      exit()
    elif argv[1] == '-a': # browse arguments
      open_new_tab(_cse_link)
      exit()
  config_file.command(argv, i=1, doc=__doc__, quit=True, silent=False)
  
  # (parse_args) Parse command arguments into dict
  kwargs = kwconfig.parse(argv[2:])
  kwargs['q'] = argv[1]
  kwargs = config_file.add(kwargs)
  
  # (split_args) Split args into build, cse, and save arguments
  buildargs = {}
  cseargs = {}
  saveargs = {}
  optionargs = {}
  for k, v in kwargs.items():
    if 'build_' == k[0:6]:
      buildargs[k[6:]] = v
    elif 'save_' == k[0:5]:
      saveargs[k[5:]] = v
    elif 'option_' == k[0:7]:
      optionargs[k[7:]] = v
    else:
      cseargs[k] = v
  
  # (cse_results) Get google api results
  results = search_google.api.results(buildargs, cseargs)
  
  # (cse_print) Print a preview of results
  if 'silent' in optionargs:
    if optionargs['silent'].lower() != 'true':
      results.preview(n=int(optionargs['preview']))
  
  # (cse_save) Save links and metadata
  if 'links' in saveargs:
    results.save_links(saveargs['links'])
  if 'metadata' in saveargs:
    results.save_metadata(saveargs['metadata'])
  
  # (cse_download) Download links
  if 'downloads' in saveargs:
    results.download_links(saveargs['downloads'])
    