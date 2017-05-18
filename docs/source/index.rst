search_google
=============

.. toctree::
   :maxdepth: 2

| Richard Wen
| rrwen.dev@gmail.com

A command line tool for Google web and image search.

Tested for Python 2.6 and 3.5 using `Anaconda 4.3.1 <https://www.continuum.io/downloads>`_.

::
  
  search_google -h
  search_google cats
  search_google cats --searchType=image

Install
-------

1. Install `Python <https://www.python.org/downloads/>`_
2. Install search_google via ``pip``

::
  
  pip install search_google

Setup
-----

A `CSE ID <https://support.google.com/customsearch/answer/2649143?hl=en>`_ and a `Google API developer key <https://developers.google.com/api-client-library/python/auth/api-keys>`_ are required to use this package. A `Gmail <https://www.google.com/gmail>`_ account will also be required to create and access the ID and developer key.

When prompted, use your Gmail account for login access.

*Note: Instructions and links were written on May 17, 2017, and are subject to change depending on Google's website.*

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

Modules
-------

cse
***

.. automodule:: cse
   :members:

cli
***

.. autofunction:: cli.main

.. autoclass:: cli.config
   :members:
   