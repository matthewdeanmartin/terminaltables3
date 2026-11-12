=========================
terminaltables3 |version|
=========================

Easily draw tables in terminal/console applications from a list of lists of strings. As easy as:

.. code-block:: pycon

    >>> from terminaltables3 import AsciiTable
    >>> table_data = [
    ... ['Heading1', 'Heading2'],
    ... ['row1 column1', 'row1 column2'],
    ... ['row2 column1', 'row2 column2'],
    ... ['row3 column1', 'row3 column2'],
    ... ]
    >>> table = AsciiTable(table_data)
    >>> print(table.table)
    +--------------+--------------+
    | Heading1     | Heading2     |
    +--------------+--------------+
    | row1 column1 | row1 column2 |
    | row2 column1 | row2 column2 |
    | row3 column1 | row3 column2 |
    +--------------+--------------+

.. figure:: examples.png
    :target: _images/examples.png

    Linux, macOS, and Windows are also supported. View source: :github:`example1.py`, :github:`example2.py`,
    :github:`example3.py`

Features
========

* Multi-line rows: add newlines to table cells and terminaltables3 will handle the rest.
* Table titles: show a title embedded in the top border of the table (not supported by Markdown tables or PorcelainTable, which
  have no top border to hold it).
* Python: Python 3.8+ supported on Linux, macOS, and Windows.
* CJK: Wide Chinese/Japanese/Korean characters displayed correctly.
* RTL: Arabic and Hebrew characters aligned correctly.
* Alignment/Justification: Align individual columns left, center, or right.
* Colored text: colorclass_, colorama_, termcolor_, or just plain `ANSI escape codes`_.

Project Links
=============

* Documentation: https://terminaltables3.readthedocs.io/en/latest/
* Source code: https://github.com/matthewdeanmartin/terminaltables3
* PyPI homepage: https://pypi.org/project/terminaltables3/
* Change log: https://github.com/matthewdeanmartin/terminaltables3/blob/master/CHANGELOG.md

.. toctree::
    :maxdepth: 2
    :caption: General

    install
    quickstart
    settings

.. toctree::
    :maxdepth: 2
    :caption: Table Styles

    asciitable
    singletable
    doubletable
    githubtable

.. toctree::
    :maxdepth: 1
    :caption: Appendix

    changelog

.. _colorclass: https://github.com/Robpol86/colorclass
.. _colorama: https://github.com/tartley/colorama
.. _termcolor: https://pypi.org/project/termcolor/
.. _ANSI escape codes: http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x329.html
