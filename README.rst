###################################
sphinxcontrib.translation_assistant
###################################

Sphinx extension to view
`Translation Assistant <http://joeglens.com/translation-assistant-tool>`__
file.

To use this extension, it is recommended that you download the chapter then
copy paste the content to Translation Assistant.

The link to text format download is available at the bottom of the page at each
chapter.

.. important::

  - Tab is not ASCII 9, but Unicode 3000 "Ideographic Space".
  - Separator is line with 44 asterisk character, rendered as horizontal line.


Format
======

This extension is only for Syosetsu format.

Since I didn't know the rule of Syosetsu format,
this is the result of my investigation after seeing the text format download.


Content
  Lines starting with tab.

Title
  First line without tab.

  The complicated part is that this line can be after of before separator.
  But it seems that this line is always the line right before the line with
  tab.

Notes
  Lines before or after separator depending on lines with tab.


Without Author Notes
--------------------

.. code-block:: none

  Title

    Content.

    Content.

    Content.


With Author Notes
-----------------

After content.

.. code-block:: none

  Title

    Content.

    Content.

    Content.

  ********************************************

  Notes.

Before content.

.. code-block:: none

  Notes.

  ********************************************

  Title

    Content.

    Content.

    Content.

Before and after content.

.. code-block:: none

  Notes.

  ********************************************

  Title

    Content.

    Content.

    Content.

  ********************************************

  Notes.



Installation
============

.. code-block:: bat

  (.venv) > pip install sphinxcontrib-translation-assistant

Setup extension in ``conf.py`` file.

.. code-block:: python

  extensions = ['sphinxcontrib.translation_assistant']


Usage
=====

.. code-block:: rst

  .. translation-assistant:: /src/chapter-01.txt


Changes
=======

0.2.0
-----

* Revamp to Syosetsu format.
* incompatible with version 0.1.#


0.1.2
-----

* Add equal and asterisk sign as horizontal line.


0.1.1
-----

* Turn 4 or more soft hyphen (minus) character into horizontal line.
* Fix ignored blank line.


0.1.0
-----

* First public release.
