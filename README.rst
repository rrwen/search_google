search_google
=============

| Richard Wen
| rrwen.dev@gmail.com
  
  
A command line tool for Google web and image search.
  
Install
-------

1. Install `Python <https://www.python.org/downloads/>`_
2. Install search_google via ``pip``

::
  
  pip install search_google
  
For the latest developer version, see `Developer Install`_.
  
Usage
-----

For usage details, refer to the `documentation <https://rrwen.github.io/search_google>`_.

::
  
  search_google -h
  search_google cat
  search_google cat --searchType=image
  search_google cat --save_links=cat.txt

Developer Notes
---------------

Developer Install
*****************

Install the latest developer version from github::
  
  pip install git+https://github.com/rrwen/search_google
  
Install from cloned source::

  git clone https://github.com/rrwen/search_google
  cd search_google
  pip install . -I

Documentation Maintenance
*************************

1. Ensure `sphinx <https://github.com/sphinx-doc/sphinx/>`_ is installed ``pip install -U sphinx``
2. Generate the documentation in ``docs/``

::
  
  pip install . -I
  sphinx-build -b html docs/source docs
  
Uploading to PyPi
*****************

1. Ensure `twine <https://pypi.python.org/pypi/twine>`_ is installed ``pip install twine``
2. Ensure `wheel <https://pypi.python.org/pypi/wheel>`_ is installed ``pip install wheel``
3. Create source distribution
4. Create wheels
5. Upload to `PyPi <https://pypi.python.org/pypi>`_

::
  python setup.py sdist
  python setup.py bdist_wheel
  python setup.py bdist_wheel --universal
  twine upload dist/*
  
Implementation
**************

This command line tool used the `Google Custom Search Engine (CSE) <https://developers.google.com/api-client-library/python/apis/customsearch/v1>`_ to perform web and image searches. It relied on `googleapiclient.build <https://google.github.io/google-api-python-client/docs/epy/googleapiclient.discovery-module.html#build>`_ and `cse.list <https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/customsearch_v1.cse.html>`_, where ``build`` was used to create a Google API object and ``cse`` was used to perform the searches. The class `search_google.cse <https://rrwen.github.io/search_google/#module-cse>`_ simply passed a dictionary of arguments onto ``build`` and ``cse`` and manipulated the results using properties and methods. `search_google.cli <https://rrwen.github.io/search_google/#module-cli>`_ was then used to create a command line interface for `search_google.cse <https://rrwen.github.io/search_google/#module-cse>`_. In order to use ``build`` and ``cse``, a `Google Developer API Key <https://developers.google.com/api-client-library/python/auth/api-keys>`_ and a `Google CSE ID <https://cse.google.com/all>`_ must be created to have access (see `search_google Setup <https://rrwen.github.io/search_google/#setup>`_). Creating these keys required a `Gmail <https://www.google.com/gmail>`_ account for login access.
