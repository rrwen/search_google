# -*- coding: utf-8 -*-

from os import listdir, makedirs, remove
from os.path import isdir
from search_google.cli import run
from shutil import rmtree
from tempfile import NamedTemporaryFile, mkdtemp
from unittest import TestCase

import json

class resultsTest(TestCase):
    
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
    tempfile = NamedTemporaryFile().name
    argv = [
      'cli.py',
      'google',
      '--num=1',
      '--save_links=' + tempfile
    ]
    run(argv)
    remove(tempfile)
  
  def test_save_metadata(self):
    tempfile = NamedTemporaryFile().name
    argv = [
      'cli.py',
      'google',
      '--num=1',
      '--save_metadata=' + tempfile
    ]
    run(argv)
    remove(tempfile)
  
  def test_download_links(self):
    tempdir = mkdtemp()
    argv = [
      'cli.py',
      'google',
      '--num=1',
      '--save_downloads=' + tempdir
    ]
    run(argv)
    rmtree(tempdir)
  
  def test_download_images(self):
    tempdir = mkdtemp()
    argv = [
      'cli.py',
      'google',
      '--searchType=image',
      '--num=1',
      '--save_downloads=' + tempdir
    ]
    run(argv)
    rmtree(tempdir)
    