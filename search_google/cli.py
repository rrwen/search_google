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
      > search_google cat --save-downloads=downloads
  
  For more information visit use: search_google -i
"""

from os.path import isfile
from pkg_resources import resource_filename, Requirement
from pprint import pprint
from search_google import cse
from sys import argv
from webbrowser import open_new_tab
 
import argparse
import json

_doc_link = 'https://github.com/rrwen/search_google'
_cse_link = 'https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/customsearch_v1.cse.html'

class config:
  """Configuration file manipulation for default arguments.
  
  Manipulates a configuration file in JSON format to specify default arguments for
  the  command line. Each key in the json represents an argument and
  each value represents the default setting. The unmodified default arguments are shown below::
    
    {
      'build_serviceName': 'customsearch',
      'build_version': 'v1',
      'num': 3,
      'save_links': None,
      'save_metadata': None,
      'option_silent': 'False',
      'option_preview': 10
    } 
  
  Notes:
    Creates a configuration file with the defaults if the ``file_path`` does not exist.
    
  Args:
    file_path (str):
      Path to the configuration file in JSON format.
    defaults (dict):
      Dictionary of default arguments in key-value format.
  
  Attributes:
    file_path (str):
      Path to the configuration file in JSON format.
  
  Examples: 
    ::
    
      # Import the cse module for the results class
      from search_google import cli
      
      # Specify a file path for creating config object
      config = cli.config('path_to_config.json')
      
      # Update the config file with a new default named "fileType"
      config.update({'fileType': 'jpg'})
      
      # Add defaults if not already set
      # Here the default "num" arg will remain 5
      # While all defaults in "config" are added to "other_config"
      other_config = {'num': 5}
      other_config = config.add(other_config)
      
      # Write new default arguments using key-value dict
      config.overwrite({
        'build_serviceName': 'customsearch',
        'build_version': 'v1',
        'num': 5,
        'save_links': None,
        'save_metadata': None,
        'option_silent': 'False',
        'option_preview': 2})
        
      # Obtain a dict of the default arguments
      arguments = config.read()
      
      # Remove the default argument named "fileType"
      config.remove('fileType')
      
      # Reset to defaults
      config.reset()
  """
  def __init__(
    self,
    file_path, 
    defaults={
      'build_serviceName': 'customsearch',
      'build_version': 'v1',
      'num': 3,
      'option_silent': 'False',
      'option_preview': 10}):
    self.file_path = file_path
    self.defaults = defaults
    if not isfile(file_path):
      self.reset()
      
  def add(self, other_config):
    """Add default arguments to another configuration dictionary.
    
    Adds the default arguments from :class:`cli.config`.file_path 
    to another configuration dictionary if it is not already set.
    
    Args:
      other_config (dict):
        The other configuration dictionary of key-value arguments.
    """
    for k, v in self.read().items():
      if k not in other_config:
        other_config[k] = v
    return other_config
  
  def overwrite(self, new_config):
    """Overwrite default arguments for configuration file.
    
    Overwrites the contents of :class:`cli.config`.file_path with ``new_config``.
    
    Args:
      new_config (dict):
        The new default arguments as a key-value dictionary.
    """
    with open(self.file_path, 'w') as out_file:
      json.dump(new_config, out_file)
      
  def read(self):
    """Read default arguments from configuration file.
    
    Reads the configuration file content into a key-value dictionary.
    
    Returns:
      A dict of the default arguments from :class:`cli.config`.file_path.
    """
    with open(self.file_path, 'r') as in_file:    
      config = json.load(in_file)
    return config
  
  def remove(self, k):
    """Remove default arguments from configuration file.
    
    Removes a default argument from :class:`cli.config`.file_path.
    
    Args:
      k (str):
        The default argument name to remove from :class:`cli.config`.file_path.
    """
    config = self.read()
    config.pop(k, None)
    self.overwrite(config)
    
  def reset(self):
    """Reset default arguments for configuration file.
    
    Resets the contents of :class:`cli.config`.file_path with :class:`cli.config`.defaults.
    """
    with open(self.file_path, 'w') as out_file:
      json.dump(self.defaults, out_file)
    
  def update(self, arguments):
    """Update default arguments for configuration file.
    
    Updates the contents of :class:`cli.config`.file_path with ``arguments``.
    
    Args:
      arguments (dict):
        Key-value dictionary of default arguments with their respective settings to update.
    """
    config = self.read()
    config.update(arguments)
    self.overwrite(config)
    
def main():
  """Runs the search_google command line tool.
  
  This function runs the search_google command line tool 
  in a terminal. It was intended for use inside a py file 
  (.py) to be executed using python.
  
  Notes:
    * ``[q]`` reflects key ``q`` in the ``cseargs`` parameter for :class:`cse.results`
    * Optional arguments with ``build_`` are keys in the ``buildargs`` parameter for :class:`cse.results`
  
    For distribution, this function must be defined in the following files::
      
      # In 'search_google/search_google/__main__.py'
      from .cli import main
      main()
      
      # In 'search_google/search_google.py'
      from search_google.cli import main
      if __name__ == '__main__':
        main()
      
      # In 'search_google/setup.py'
      setup(
        ...
        entry_points={
          'console_scripts' : ['search_google=search_google.cli:main']
        }
        ...
      )
  """
  config_file = config(resource_filename(Requirement.parse('search_google'),  'search_google/config.json'))
  
  # (commands) Main command calls
  if len(argv) > 1:
    if argv[1] == '-h': # show help
      print(__doc__)
      exit()
    elif argv[1] == '-i': # browse docs
      open_new_tab(_doc_link)
      exit()
    elif argv[1] == '-a': # browse arguments
      open_new_tab(_cse_link)
      exit()
    elif argv[1] == '-s': # set defaults
      k, v = argv[2].split("=", maxsplit=1)
      config_file.update({k: v})
      print('\nSet "' + k + '" default to ' + '"' + v + '"')
      exit()
    elif argv[1] == '-r': # remove defaults
      config_file.remove(argv[2])
      print('\n Removed "' + argv[2] + '" default')
      exit()
    elif argv[1] == '-v': # show defaults
      print('\nConfig file at: \n\t' + config_file.file_path + '\n')
      pprint(config_file.read())
      exit()
    elif argv[1] == '-d': # reset defaults
      config_file.reset()
      print('\n Reset defaults')
      exit()
  else:
    print(__doc__)
    exit()
  
  # (argparse) Create argument parser
  parser = argparse.ArgumentParser(usage=__doc__, add_help=False)
  parser.add_argument('q')

  # (parse_args) Parse command arguments into dict
  for kv in argv[2:]:
    k = kv.split('=', maxsplit=1)[0]
    parser.add_argument(k) # add arg
  kwargs = vars(parser.parse_args())
  
  # (default_args) Default arguments from json
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
  
  # (cse_results) Get google cse results
  results = cse.results(buildargs, cseargs)
  
  # (cse_print) Print a preview of results
  if optionargs['silent'].lower() != 'true':
    results.preview(n=optionargs['preview'])
  
  # (cse_save) Save links and metadata
  if 'links' in saveargs:
    results.save_links(saveargs['links'])
  if 'metadata' in saveargs:
    results.save_metadata(saveargs['metadata'])
  
  # (cse_download) Download links
  if 'downloads' in saveargs:
    results.download_links(saveargs['downloads'])
    