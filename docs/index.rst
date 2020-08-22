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

<script>
  (function(d,t) {
    var BASE_URL = "https://app.chatwoot.com";
    var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
    g.src= BASE_URL + "/packs/js/sdk.js";
    s.parentNode.insertBefore(g,s);
    g.onload=function(){
      window.chatwootSDK.run({
        websiteToken: '54gXN1MxgKGN2HUs7UzjCQE2',
        baseUrl: BASE_URL
      })
    }
  })(document,"script");
</script>

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
