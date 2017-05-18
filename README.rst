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

Developer Notes
---------------

Documentation Maintenance
*************************

1. Ensure `Python <https://www.python.org/downloads/>`_ is installed
2. Ensure `sphinx <https://github.com/sphinx-doc/sphinx/>`_ is installed ``pip install -U sphinx``
2. Generate the documentation in ``docs/``

::
  
  pip install . -I
  sphinx-build -b html docs/source docs
  
