# -*- coding: utf-8 -*-

from os import listdir, remove
from os.path import isdir
from search_google.cli import run
from shutil import rmtree
from tempfile import NamedTemporaryFile, TemporaryDirectory
from unittest import TestCase

import json

class resultsTest(TestCase):

  def setUp(self):
    tempfile = NamedTemporaryFile()
    self.out_path = tempfile.name
    tempfile.close()
    self.out_dir = TemporaryDirectory().name
    
  def test_search(self):
    argv = [
      'cli.py',
      'google',
      '--num=1'
    ]
    run(argv)
  
  def test_search_image(self):
    argv = [
      'cli.py',
      'google',
      '--searchType=image',
      '--num=1'
    ]
    run(argv)
    
  def test_save_links(self):
    argv = [
      'cli.py',
      'google',
      '--num=1',
      '--save_links=' + self.out_path
    ]
    run(argv)
  
  def test_save_metadata(self):
    argv = [
      'cli.py',
      'google',
      '--num=1',
      '--save_metadata=' + self.out_path
    ]
    run(argv)
  
  def test_download_links(self):
    argv = [
      'cli.py',
      'google',
      '--num=1',
      '--save_downloads=' + self.out_dir
    ]
    run(argv)
  
  def test_download_images(self):
    argv = [
      'cli.py',
      'google',
      '--searchType=image',
      '--num=1',
      '--save_downloads=' + self.out_dir
    ]
    run(argv)
    
  def tearDown(self):
    remove(self.out_path)
    rmtree(self.out_dir)
    