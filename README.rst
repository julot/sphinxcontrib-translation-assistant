###################################
sphinxcontrib.translation_assistant
###################################

Sphinx extension to view
`Translation Assistant <http://joeglens.com/translation-assistant-tool>`__
file.

To use this extension, you should download the chapter in text format then copy
paste the content to Translation Assistant.
This is because the extension search for tab to indicate content and title.

The link to download the text format is available at the bottom of the page at
each chapter.


Format
======

This extension is only for Syosetsu format.

Since I didn't know the rule of Syosetsu format,
this is the result of my investigation after seeing the text format download.

Separator
  Lines with 4 or more asterisk character.

  This line separate content and note.

Content
  First line starts with ideographic space and the rest of the lines until
  separator.

Title
  First line without ideographic space before the first line of content.

Notes
  Lines before or after separator depending on content.

  Pre notes is lines before separator and content,
  post notes is lines after content and separator.


Without Author's Notes
----------------------

.. code-block:: text

  Title

    Content.

    Content.

    Content.


With Author's Post-Notes
------------------------

.. code-block:: text

  Title

    Content.

    Content.

    Content.

  ********************************************

  Notes.


With Author's Pre-Notes
-----------------------

.. code-block:: text

  Notes.

  ********************************************

  Title

    Content.

    Content.

    Content.


With Author's Note
------------------

.. code-block:: text

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

  .. translation-assistant:: chapter-01.txt


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
