# -*- coding: utf-8 -*-

from os import listdir, makedirs
from os.path import isdir
from search_google.cli import main
from shutil import rmtree
from tempfile import NamedTemporaryFile, mkdtemp
from unittest import TestCase

import json

argv = []

class resultsTest(TestCase):

  def setUp(self):
    self.tempfile = NamedTemporaryFile().name
    self.tempdir = mkdtemp()
    
  def test_search(self):
    argv = [
      'cli.py',
      'google',
      '--build_developerKey=AIzaSyClH2yMLZlf_cs7yHn7gi16MWMkfCeaLZg',
      '--cx=014766831074566761693:ovdpanxgl6o'
      '--num=1'
    ]
    with self.assertRaises(SystemExit):
      main()
  
  def test_search_image(self):
    argv = [
      'cli.py',
      'google',
      '--searchType=image',
      '--build_developerKey=AIzaSyClH2yMLZlf_cs7yHn7gi16MWMkfCeaLZg',
      '--cx=014766831074566761693:ovdpanxgl6o'
      '--num=1'
    ]
    with self.assertRaises(SystemExit):
      main()
    
  def test_save_links(self):
    argv = [
      'cli.py',
      'google',
      '--build_developerKey=AIzaSyClH2yMLZlf_cs7yHn7gi16MWMkfCeaLZg',
      '--cx=014766831074566761693:ovdpanxgl6o'
      '--num=1',
      '--save_links=' + self.tempfile
    ]
    with self.assertRaises(SystemExit):
      main()
  
  def test_save_metadata(self):
    argv = [
      'cli.py',
      'google',
      '--build_developerKey=AIzaSyClH2yMLZlf_cs7yHn7gi16MWMkfCeaLZg',
      '--cx=014766831074566761693:ovdpanxgl6o'
      '--num=1',
      '--save_metadata=' + self.tempfile
    ]
    with self.assertRaises(SystemExit):
      main()
  
  def test_download_links(self):
    argv = [
      'cli.py',
      'google',
      '--build_developerKey=AIzaSyClH2yMLZlf_cs7yHn7gi16MWMkfCeaLZg',
      '--cx=014766831074566761693:ovdpanxgl6o'
      '--num=1',
      '--save_downloads=' + self.tempdir
    ]
    with self.assertRaises(SystemExit):
      main()
  
  def test_download_images(self):
    argv = [
      'cli.py',
      'google',
      '--searchType=image',
      '--build_developerKey=AIzaSyClH2yMLZlf_cs7yHn7gi16MWMkfCeaLZg',
      '--cx=014766831074566761693:ovdpanxgl6o'
      '--num=1',
      '--save_downloads=' + self.tempdir
    ]
    with self.assertRaises(SystemExit):
      main()
    