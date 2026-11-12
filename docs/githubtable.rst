.. _githubtable:

===========================
GithubFlavoredMarkdownTable
===========================

GithubFlavoredMarkdownTable was initially added in the original project's pull request bcho_. It produces a
`GitHub Flavored Markdown`_ formatted table.

Table titles are ignored because the Markdown table format has no place for them. The ``outer_border`` and
``inner_column_border`` toggles are not supported by this format; leave them at their defaults.

.. image:: githubtable.png
    :target: _images/githubtable.png

.. image:: githubtable_rendered.png
    :target: _images/githubtable_rendered.png

API
===

.. autoclass:: terminaltables3.GithubFlavoredMarkdownTable
    :members: column_max_width, column_widths, ok, table_width, table

.. _bcho: https://github.com/Robpol86/terminaltables/pull/12
.. _GitHub Flavored Markdown: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables
