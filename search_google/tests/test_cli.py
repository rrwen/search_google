# -*- coding: utf-8 -*-

from os import listdir, makedirs, remove
from os.path import isdir
from search_google.cli import run
from shutil import rmtree
from tempfile import TemporaryFile, TemporaryDirectory
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
    with TemporaryFile() as out_file:
      argv = [
        'cli.py',
        'google',
        '--num=1',
        '--save_links=' + out_file.name
      ]
      run(argv)
  
  def test_save_metadata(self):
    with TemporaryFile() as out_file:
      argv = [
        'cli.py',
        'google',
        '--num=1',
        '--save_metadata=' + out_file.name
      ]
      run(argv)
  
  def test_download_links(self):
    with TemporaryDirectory() as out_dir:
      argv = [
        'cli.py',
        'google',
        '--num=1',
        '--save_downloads=' + out_dir
      ]
      run(argv)
  
  def test_download_images(self):
    with TemporaryDirectory() as out_dir:
      argv = [
        'cli.py',
        'google',
        '--searchType=image',
        '--num=1',
        '--save_downloads=' + out_dir
      ]
      run(argv)
    