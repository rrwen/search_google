# -*- coding: utf-8 -*-

from os import listdir, remove
from os.path import isdir, isfile
from search_google.cli import run
from shutil import rmtree
from tempfile import NamedTemporaryFile, TemporaryDirectory
from unittest import TestCase

import json

class cliTest(TestCase):

  def setUp(self):
    tempfile = NamedTemporaryFile()
    self.tempfile = tempfile.name
    tempfile.close()
    self.tempdir = TemporaryDirectory().name
    
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
      '--save_links=' + self.tempfile
    ]
    run(argv)
  
  def test_save_metadata(self):
    argv = [
      'cli.py',
      'google',
      '--num=1',
      '--save_metadata=' + self.tempfile
    ]
    run(argv)
  
  def test_download_links(self):
    argv = [
      'cli.py',
      'google',
      '--num=1',
      '--save_downloads=' + self.tempdir
    ]
    run(argv)
  
  def test_download_images(self):
    argv = [
      'cli.py',
      'google',
      '--searchType=image',
      '--num=1',
      '--save_downloads=' + self.tempdir
    ]
    run(argv)
    
  def tearDown(self):
    if isfile(self.tempfile):
      remove(self.tempfile)
    if isdir(self.tempdir):
      rmtree(self.tempdir)
    