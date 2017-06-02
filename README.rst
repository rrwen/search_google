search_google
=============

| Richard Wen
| rrwen.dev@gmail.com

* `Documentation <https://rrwen.github.io/search_google>`_
* `PyPi Package <https://pypi.python.org/pypi/search_google>`_

A command line tool and module for Google API web and image search.


Install
-------

1. Install `Python <https://www.python.org/downloads/>`_
2. Install `search_google <https://pypi.python.org/pypi/search-google>`_ via ``pip``

::
  
  pip install search_google
  
For the latest developer version, see `Developer Install`_.
  
Usage
-----

For help in the console::
  
  search_google -h
  
Ensure that a `CSE ID <https://support.google.com/customsearch/answer/2649143?hl=en>`_ and a `Google API developer key <https://developers.google.com/api-client-library/python/auth/api-keys>`_ are set::

  search_google -s cx="your_cse_id"
  search_google -s build_developerKey="your_dev_key"

Search the web for keyword "cat"::
  
  search_google "cat"
  search_google "cat" --save_links=cat.txt
  search_google "cat" --save_downloads=downloads

Search for "cat" images::
  
  search_google cat --searchType=image
  search_google "cat" --searchType=image --save_links=cat_images.txt
  search_google "cat" --searchType=image --save_downloads=downloads
  
Use as a Python module:

.. code-block:: python

  # Import the api module for the results class
  import search_google.api
  
  # Define buildargs for cse api
  buildargs = {
    'serviceName': 'customsearch',
    'version': 'v1',
    'developerKey': 'your_api_key'
  }
  
  # Define cseargs for search
  cseargs = {
    'q': 'keyword query',
    'cx': 'your_cse_id',
    'num': 3
  }
  
  # Create a results object
  results = search_google.api.results(buildargs, cseargs)
  
  # Download the search results to a directory
  results.download_links('downloads')
  
For more usage details, see the `Documentation <https://rrwen.github.io/search_google>`_.

Developer Notes
---------------

Developer Install
*****************

Install the latest developer version with ``pip`` from github::
  
  pip install git+https://github.com/rrwen/search_google
  
Install from ``git`` cloned source:

1. Ensure `git <https://git-scm.com/>`_ is installed
2. Clone into current path
3. Install via ``pip``

::

  git clone https://github.com/rrwen/search_google
  cd search_google
  pip install . -I
  
Tests
*****

1. Ensure `unittest <https://docs.python.org/2.7/library/unittest.html>`_ is available
2. Run tests

::
  
  pip install . -I
  python -m unittest

Documentation Maintenance
*************************

1. Ensure `sphinx <https://github.com/sphinx-doc/sphinx/>`_ is installed ``pip install -U sphinx``
2. Update the documentation in ``docs/``

::
  
  pip install . -I
  sphinx-build -b html docs/source docs

Upload to github
****************

1. Ensure `git <https://git-scm.com/>`_ is installed
2. Add all files and commit changes
3. Push to github

::
  
  git add .
  git commit -a -m "Generic update"
  git push
  
Upload to PyPi
**************

1. Ensure `twine <https://pypi.python.org/pypi/twine>`_ is installed ``pip install twine``
2. Ensure `sphinx <https://github.com/sphinx-doc/sphinx/>`_ is installed ``pip install -U sphinx``
3. Run tests and check for OK status
4. Delete ``dist`` directory
5. Update the version ``search_google/__init__.py``
6. Update the documentation in ``docs/``
7. Create source distribution
8. Upload to `PyPi <https://pypi.python.org/pypi>`_

::
  
  pip install . -I
  python -m unittest
  sphinx-build -b html docs/source docs
  python setup.py sdist
  twine upload dist/*
  
Implementation
**************

This command line tool uses the `Google Custom Search Engine (CSE) <https://developers.google.com/api-client-library/python/apis/customsearch/v1>`_ to perform web and image searches. It relies on `googleapiclient.build <https://google.github.io/google-api-python-client/docs/epy/googleapiclient.discovery-module.html#build>`_ and `cse.list <https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/customsearch_v1.cse.html>`_, where ``build`` was used to create a Google API object and ``cse`` was used to perform the searches.

The class `search_google.api <https://rrwen.github.io/search_google/#module-api>`_ simply passed a dictionary of arguments into ``build`` and ``cse`` to process the returned results with properties and methods. `search_google.cli <https://rrwen.github.io/search_google/#module-cli>`_ was then used to create a command line interface for `search_google.api <https://rrwen.github.io/search_google/#module-api>`_.

In order to use ``build`` and ``cse``, a `Google Developer API Key <https://developers.google.com/api-client-library/python/auth/api-keys>`_ and a `Google CSE ID <https://cse.google.com/all>`_ needs to be created for API access (see `search_google Setup <https://rrwen.github.io/search_google/#setup>`_). Creating these keys also required a `Gmail <https://www.google.com/gmail>`_ account for login access.

::
  
          googleapiclient.build  <-- Google API
                    |                    
                 cse.list        <-- Google CSE
                    |
             search_google.api   <-- search results
                    |
             search_google.cli   <-- command line

A rough example is provided below thanks to the `customsearch example <https://github.com/google/google-api-python-client/blob/master/samples/customsearch/main.py>`_ from Google:

.. code-block:: python
  
  from apiclient.discovery import build
  
  # Set developer key and CSE ID
  dev_key = 'a_developer_key'
  cse_id = 'a_cse_id'
  
  # Obtain search results from Google CSE
  service = build("customsearch", "v1", developerKey=dev_key)
  results = service.cse().list(q='cat', cx=cse_id).execute()
  
  # Manipulate search results after ...
