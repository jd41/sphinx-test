.. sphinx-playground documentation master file, created by
   sphinx-quickstart on Fri Jun 12 21:29:38 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Start gltest_file.rst:

This is a glossary test

.. This is a substitution.

test abbr+subst+include+rawhtml+link: |subst_abbr_include_rawhtml_link|

test abbr+substitution+include: |subst_abbr_include|

test abbr substitution: |substabbr|

Test hoverxrefs: :hoverxref:`substhoverxref <gltest_glossary:substhoverxref>`

:abbr:`substabbr (hint)`

:abbr: `substabbr (hint)`

test hoverxref: |substhoverxref|

End gltest_file.rst

.. include:: gltest_glossary.rst

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
