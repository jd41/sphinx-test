.. sphinx-playground documentation master file, created by
   sphinx-quickstart on Fri Jun 12 21:29:38 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: gltest_glossary_include.rst

test abbr+replace+include+rawhtml+link: |replace_abbr_include_rawhtml_link|

test abbr+replace+include: |replace_abbr_include|

Test hoverxref+include: :hoverxref:`text_hoverxref<gltest_glossary:replace_hoverxref>`

Test hoverxref+include+replace: |replace_hoverxref|

Test reference to something unresolved: |thisdoesntexist|

End gltest_file.rst

.. raw:: html
  :file: livechat.html

Welcome to sphinx-playground's documentation!
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
