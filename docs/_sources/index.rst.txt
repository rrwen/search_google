search_google
=============

.. toctree::
   :maxdepth: 2

| Richard Wen
| rrwen.dev@gmail.com

A command line tool and module for Google API web and image search.

Tested for Python 2.6 and 3.5 using `Anaconda 4.3.1 <https://www.continuum.io/downloads>`_.

::
  
  search_google -h
  search_google cats
  search_google cats --searchType=image

Install
-------

1. Install `Python <https://www.python.org/downloads/>`_
2. Install `search_google <https://pypi.python.org/pypi/search-google>`_ via ``pip``

::
  
  pip install search_google

Setup
-----

* A `CSE ID <https://support.google.com/customsearch/answer/2649143?hl=en>`_ and a `Google API developer key <https://developers.google.com/api-client-library/python/auth/api-keys>`_ are required to use this package
* A `Gmail <https://www.google.com/gmail>`_ account will also be required to create and access the ID and developer key
* When asked to sign in, use your Gmail account for access

*Note: Instructions and links were written on May 20, 2017, and are subject to change depending on Google's website and API.*

Google Custom Search Engine
***************************

A `Google Custom Search Engine (CSE) <https://developers.google.com/api-client-library/python/apis/customsearch/v1>`_ and a `CSE ID <https://support.google.com/customsearch/answer/2649143?hl=en>`_ can be setup with the following instructions:

1. Go to the `CSE Control Panel <http://cse.google.com/manage/all>`_
2. Click **Add**
3. Enter a website in the box under **Sites to search** such as "www.google.com"
4. Click **Create**
5. Go back to the `CSE Control Panel <http://cse.google.com/manage/all>`_
6. Select your created search engine
7. Turn on **Image search**
8. For **Sites to search**, select **Search the entire web but emphasize included sites**
9. Under **Sites to search**, click checkbox next to **Site**
10. Under **Sites to search**, click **Delete**
11. Under **Details**, click **Search engine ID**
12. Set ``cx`` by replacing "your_cse_id" with the **Search engine ID**

::
  
  search_google -s cx="your_cse_id"

Google API
**********

An `API developer key <https://developers.google.com/api-client-library/python/auth/api-keys>`_ for the `Google Application Programming Interface (API) <https://developers.google.com/api-client-library/python/>`_ can be setup with the following instructions:

1. Enable `Google Custom Search Engine <https://console.developers.google.com/apis/api/customsearch.googleapis.com>`_
2. Go to `Google API Console Credentials <https://console.developers.google.com/apis/credentials>`_
3. Click **Create Credentials -> API Key**
4. Set ``build_developerKey`` by replacing "your_dev_key" with the **API Key**

::
  
  search_google -s build_developerKey="your_dev_key"

Usage
-----

For help in the console, use::
  
  search_google -h
  
Please that the `Setup`_ section was completed::
  
  search_google -s cx="your_cse_id"
  search_google -s build_developerKey="your_dev_key"

Web and Image Search
********************

Perform a web search::
  
  search_google cat
  search_google "cat with hat"

Perform an image search::

  search_google cat --searchType=image
  search_google "cat with hat" --searchType=image

Search for ``20`` results::

  search_google cat --n=20
  search_google cat --searchType=image --n=20
  
Preview all 20 results::

  search_google cat --n=20 --option_preview=20
  search_google cat --searchType=image --n=20 --option_preview=20
  
Links and Metadata
******************

Save metadata::
  
  search_google cat --save_metadata=cat.json
  search_google cat --searchType=image --save_metadata=cat_images.json

Save URL links::
  
  search_google cat --save_links=cat.txt
  search_google cat --searchType=image --save_links=cat_images.txt

Save links and metadata::
  
  search_google cat --save_links=cat.txt --save_metadata=cat.json
  search_google cat --searchType=image --save_links=cat_images.txt --save_metadata=cat_images.json

Default Arguments
*****************

Default arguments persist even after the console is closed. Defaults enable user customization of the search_google command without a long list of arguments every call.  
  
View the defaults::
  
  search_google -v

Increase number of search results previewed to ``20``::

  search_google -s option_preview=20
  
Turn off preview of search results::

  search_google -s option_silent=True
  
Set the ``searchType`` argument to default to ``image`` search::

  search_google -s searchType=image
  
Set the ``fileType`` argument to default to ``jpg`` images::
  
  search_google -s fileType=jpg

Set to save a text file named ``links.txt`` with search result links whenever used::
  
  search_google -s save_links=links.txt

Remove default arguments::

  search_result -r option_preview
  search_google -r option_silent
  search_google -r searchType
  search_google -r fileType
  search_google -r save_links
  
Reset the defaults::
  
  search_google -d

After resetting defaults, the developer and CSE ID keys will have to be set again::

  search_google -s cx="your_cse_id"
  search_google -s build_developerKey="your_dev_key"

Additional Arguments
********************

A number of optional arguments defined using ``--`` are not shown when using ``search_google -h``. These can be used with the same names as the arguments passed to `Google's CSE method <https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/customsearch_v1.cse.html>`_::

  search_google -a

For example, the index of the first result to return can be set by argument ``start`` which is a named argument in `Google's CSE method <https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/customsearch_v1.cse.html>`_::
  
  search_google cat --start=2
  search_google cat --lr=lang_en
  search_google cat --searchType=image --imgType=photo
  search_google cat --searchType=image --imgDominantColor=brown
  
Module Import
*************

The `search_google <https://pypi.python.org/pypi/search-google>`_ package may also be used as a `Python module <https://docs.python.org/2/tutorial/modules.html>`_::
  
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

For more details on module usage, see the example in `api`_.
  
Modules
-------

api
***

.. automodule:: api
   :members:

cli
***

.. autofunction:: cli.main
   