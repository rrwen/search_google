# -*- coding: utf-8 -*-

from os import listdir, makedirs
from os.path import isdir
from search_google import cse
from shutil import rmtree
from tempfile import NamedTemporaryFile, mkdtemp
from unittest import TestCase

import json

class resultsTest(TestCase):

  def setUp(self):
    buildargs = {
      'serviceName': 'customsearch',
      'version': 'v1',
      'developerKey': 'AIzaSyClH2yMLZlf_cs7yHn7gi16MWMkfCeaLZg'
    }
    cseargs = {
      'q': 'google',
      'cx': '014766831074566761693:ovdpanxgl6o',
      'num': 1
    }
    self.results = cse.results(buildargs, cseargs)
    self.tempfile = NamedTemporaryFile().name
    self.tempdir = mkdtemp()
  
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
    if not isdir(self.tempdir):
      makedirs(self.tempdir)
    results.download_links(self.tempdir)
    nfiles = len(listdir(self.tempdir))
    rmtree(self.tempdir)
    self.assertTrue(nfiles == 1)
    