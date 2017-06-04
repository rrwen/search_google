# -*- coding: utf-8 -*-

from os import listdir, makedirs, remove, rmtree
from os.path import isdir
from search_google.cli import run
from shutil import rmtree
from tempfile import NamedTemporaryFile, mkdtemp
from unittest import TestCase

import json

class resultsTest(TestCase):

	def setUp(self):
		self.tempfile = NamedTemporaryFile().name
		self.tempdir = mkdtemp()
		
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
		remove(self.tempfile)
		rmtree(self.tempdir)
		