####################################
sphinxcontrib.transalation_assistant
####################################

Sphinx extension to view
`Translation Assistant <http://joeglens.com/translation-assistant-tool>`__
file.

Example:

::

  .. translation-assistant:: /src/chapter-01.txt
    :no-title:
    :no-raw:

Available options:

no-title
  Flag indicating that the first line of the file is not a title.

  Please note that this option will skip 2 first line of the file.

  Line starting with ``$`` sign in not counted.

no-raw
  flag indicating that the raw text should not be rendered.


Changes
=======


0.1.0
-----

* First public release.
