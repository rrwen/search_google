# -*- coding: utf-8 -*-

from apiclient.discovery import build
from os import makedirs, path
try:
  from urllib.request import urlopen
except ImportError:
  from urllib import urlopen

import json
import shutil
import requests

class results:
  """Google Custom Search Engine (CSE) API results.
  
  Uses the `Google Custom Search Engine API <https://developers.google.com/api-client-library/python/apis/customsearch/v1>`_ 
  to search webpages and images using queries.
  
  Args:
    buildargs (dict):
      Named arguments for `googleapiclient.build <https://google.github.io/google-api-python-client/docs/epy/googleapiclient.discovery-module.html#build>`_.
    cseargs (dict):
      Named arguments for `cse.list <https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/customsearch_v1.cse.html>`_.
  
  Attributes:
    metadata (dict):
      object returned from `cse.list <https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/customsearch_v1.cse.html>`_.
    buildargs (dict):
      Same as argument ``buildargs`` for reference of inputs.
    csedargs (dict):
      Same as argument ``cseargs`` for reference of inputs.
  
  Examples: 
    ::
    
      # Import the api module for the results class
      import search_google.api
      
      # Define buildargs for api api
      buildargs = {
        "serviceName": "customsearch",
        "version": "v1",
        "developerKey": "your_api_key"
      }
      
      # Define cseargs for search
      cseargs = {
        "q": "keyword query",
        "cx": "your_cse_id",
        "num": 3
      }
      
      # Create a results object
      results = search_google.api.results(buildargs, cseargs)
      
      # Preview the search results
      results.preview()
      
      # Obtain the url links from the search
      # Links are inside results['items'] list
      links = results.get_values('items', 'link')
      
      # Obtain the url links from the search
      links = results.links
      
      # Save the search result metadata to a json file
      results.save_metadata('metadata.json')
      
      # Save the search result links to a text file
      results.save_links('links.txt')
      
      # Download the search results to a directory
      results.download_links('downloads')
  """
  def __init__(
    self,
    buildargs = {
      'serviceName': 'customsearch',
      'version': 'v1',
    },
    cseargs={
      'num': 3,
      'fileType': 'png'
    }):
    self.buildargs = buildargs
    self.cseargs = cseargs
    self.metadata = build(**buildargs).cse().list(**cseargs).execute()
  
  def download_links(self, dir_path):
    """Download web pages or images from search result links.
    
    Args:
      dir_path (str):
        Path of directory to save downloads of :class:`api.results`.links
    """
    links = self.links
    if not path.exists(dir_path):
      makedirs(dir_path)
    for i, url in enumerate(links):
      if 'start' in self.cseargs:
        i += int(self.cseargs['start'])
      ext = self.cseargs['fileType']
      ext = '.html' if ext == '' else '.' + ext
      file_name = self.cseargs['q'].replace(' ', '_') + '_' + str(i) + ext
      file_path = path.join(dir_path, file_name)
      r = requests.get(url, stream=True)
      if r.status_code == 200:
        with open(file_path, 'wb') as f:
          r.raw.decode_content = True
          shutil.copyfileobj(r.raw, f)
    
  def get_values(self, k, v):
    """Get a list of values from the key value metadata attribute.
    
    Args:
      k (str):
        Key in :class:`api.results`.metadata
      v (str):
        Values from each item in the key of :class:`api.results`.metadata
    
    Returns:
      A list containing all the ``v`` values in the ``k`` key for the  :class:`api.results`.metadata attribute.
    """
    metadata = self.metadata
    values = []
    if metadata != None:
      if k in metadata:
        for metav in metadata[k]:
          if v in metav:
            values.append(metav[v])
    return values
    
  def preview(self, n=10, k='items', kheader='displayLink', klink='link', kdescription='snippet'):
    """Print a preview of the search results.
    
    Args:
      n (int):
        Maximum number of search results to preview
      k (str):
        Key in :class:`api.results`.metadata to preview
      kheader (str):
        Key in :class:`api.results`.metadata[``k``] to use as the header
      klink (str):
        Key in :class:`api.results`.metadata[``k``] to use as the link if image search
      kdescription (str):
        Key in :class:`api.results`.metadata[``k``] to use as the description
    """
    if 'searchType' in self.cseargs:
      searchType = self.cseargs['searchType']
    else:
      searchType = None
    items = self.metadata[k]
  
    # (cse_print) Print results
    for i, kv in enumerate(items[:n]):
      if 'start' in self.cseargs:
        i += int(self.cseargs['start'])
      
      # (print_header) Print result header
      header = '\n[' + str(i) + '] ' + kv[kheader]
      print(header)
      print('=' * len(header))
      
      # (print_image) Print result image file
      if searchType == 'image':
        link = '\n' + path.basename(kv[klink])
        print(link)
        
      # (print_description) Print result snippet
      description = '\n' + kv[kdescription]
      print(description)
  
  def save_links(self, file_path):
    """Saves a text file of the search result links.
    
    Saves a text file of the search result links, where each link 
    is saved in a new line. An example is provided below::
      
      http://www.google.ca
      http://www.gmail.com
    
    Args:
      file_path (str):
        Path to the text file to save links to.
    """
    data = '\n'.join(self.links)
    with open(file_path, 'w') as out_file:
      out_file.write(data)
    
  def save_metadata(self, file_path):
    """Saves a json file of the search result metadata.
    
    Saves a json file of the search result metadata from :class:`api.results`.metadata.
    
    Args:
      file_path (str):
        Path to the json file to save metadata to.
    """
    data = self.metadata
    with open(file_path, 'w')  as out_file:
      json.dump(data, out_file)
    
  @property
  def links(self):
    """list of str: Web links to search results using :func:`api.results.get_values`."""
    return self.get_values('items', 'link')
    
