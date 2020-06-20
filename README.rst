# sphinx-test
 Sphinx test

Testing glossary options

Caveats:
========
- Careful: if the glossary abbreviation file is changed and included from main-content files, sphinx build apparently does not automatically rebuild these files. One needs to `touch` all the files including manually. Update: I tried again, and now it does? Need to check
- Links: Apparently _ in section name gets turned into - in HTML anchor, consider this when adding raw HTML link
- sphinx.ext.autosectionlabel was used to automatically create labels from sections, otherwise labels would have needed to be added manually
- sphinx.ext.autosectionlabel: line `autosectionlabel_prefix_document = True` in `conf.py` yields the reference name of the type `file:header` (`gltest_glossary:replace_hoverxref`); otherwise the label `replace_hoverxref` would have been generated
