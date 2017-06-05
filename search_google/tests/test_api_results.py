# -*- coding: utf-8 -*-

from os import listdir, remove
from os.path import isdir, isfile
from pkg_resources import resource_filename, Requirement
from shutil import rmtree
from tempfile import TemporaryFile, TemporaryDirectory
from unittest import TestCase

import json
import search_google.api

class resultsTest(TestCase):

  def setUp(self):
    file_path = resource_filename(Requirement.parse('search_google'), 'search_google/config.json')
    with open(file_path, 'r') as in_file:
      defaults = json.load(in_file)
    buildargs = {
      'serviceName': 'customsearch',
      'version': 'v1',
      'developerKey': defaults['build_developerKey']
    }
    cseargs = {
      'q': 'google',
      'num': 1,
      'cx': defaults['cx']
    }
    self.results = search_google.api.results(buildargs, cseargs)
    tempfile = TemporaryFile()
    self.tempfile = tempfile.name
    tempfile.close()
    self.tempdir = TemporaryDirectory().name
    
  def test_preview(self):
    results = self.results
    expected = None
    self.assertTrue(expected == results.preview())
    
  def test_get_values(self):
    results = self.results
    values = results.get_values('items', 'link')
    self.assertTrue(isinstance(values, list))
    
  def test_links(self):
    results = self.results
    expected = results.get_values('items', 'link')
    self.assertTrue(expected == results.links)
    
  def test_save_links(self):
    results = self.results
    open(self.tempfile, 'w').close()
    results.save_links(self.tempfile)
    with open(self.tempfile) as f:
      nlinks = len(f.readlines())
    self.assertTrue(nlinks == 1)
  
  def test_save_metadata(self):
    results = self.results
    open(self.tempfile, 'w').close()
    results.save_metadata(self.tempfile)
    with open(self.tempfile, 'r') as f:    
      metadata = json.load(f)
    self.assertTrue(metadata == results.metadata)
  
  def test_download_links(self):
    results = self.results
    results.download_links(self.tempdir)
    nfiles = len(listdir(self.tempdir))
    rmtree(self.tempdir)
    self.assertTrue(nfiles == 1)
  
  def tearDown(self):
    if isfile(self.tempfile):
      remove(self.tempfile)
    if isdir(self.tempdir):
      rmtree(self.tempdir)
    