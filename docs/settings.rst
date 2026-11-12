.. _settings:

========
Settings
========

AsciiTable, SingleTable, and DoubleTable share the settings below to change the way the table is displayed. These
attributes are available after instantiation. Two other styles differ:

* :ref:`githubtable` supports only ``table_data`` and ``justify_columns``. Titles, borders, and separators are not
  supported.
* ``PorcelainTable`` is an AsciiTable that turns off ``outer_border``, ``inner_heading_row_border``, and
  ``inner_footing_row_border`` in its constructor. Because it has no outer border, titles are never shown.

.. py:attribute:: Table.table_data

    The actual table data to render. This must be a sequence (such as a list or tuple) of rows, where each row is a
    sequence of cells (aka columns in that row). Cells are usually strings, but any other value is converted with
    ``str()`` when rendered. Rows shorter than the widest row are padded with empty cells. The outer sequence holds the
    rows and the inner sequences hold the cells.

    Example:

    .. code-block:: python

        table.table_data = [
            ['Name', 'Color', 'Type'],
            ['Avocado', 'green', 'nut'],
            ['Tomato', 'red', 'fruit'],
            ['Lettuce', 'green', 'vegetable'],
        ]

.. py:attribute:: Table.title

    Optional title to show within the top border of the table. This is ignored if None or a blank string.

.. py:attribute:: Table.inner_column_border

    Toggles the column dividers. Set to **False** to disable these vertically dividing borders.

.. py:attribute:: Table.inner_footing_row_border

    Show a horizontal dividing border before the last row. If **True** this defines the last row as the table footer.

.. py:attribute:: Table.inner_heading_row_border

    Show a horizontal dividing border after the first row. If **False** this removes the border so the first row is no
    longer considered a header row. It'll look just like any other row.

.. py:attribute:: Table.inner_row_border

    If **True** terminaltables3 will show dividing borders between every row.

.. py:attribute:: Table.inner_separators

    If **True** rows whose first cell equals ``inner_separators_delimiter`` are rendered as horizontal separators
    instead of data rows. Disabled by default, so existing tables are unaffected. Not supported by
    :ref:`githubtable`, which renders every row as data.

    Example:

    .. code-block:: pycon

        >>> table = AsciiTable([['Name'], ['Ada'], ['---', 'Group B'], ['Bob']])
        >>> table.inner_separators = True
        >>> print(table.table)
        +------+---------+
        | Name |         |
        +------+---------+
        | Ada  |         |
        +Group B---------+
        | Bob  |         |
        +------+---------+

.. py:attribute:: Table.inner_separators_delimiter

    The first-cell value that marks a row as a separator when ``inner_separators`` is enabled. Defaults to
    ``'---'``. An optional second cell in the marker row supplies a title for the separator.

.. py:attribute:: Table.outer_border

    Toggles the four outer borders. If **False** the top, left, right, and bottom borders will not be shown.

.. py:attribute:: Table.justify_columns

    Aligns text in entire columns. The keys in this dict are column integers (0 for the first column) and the values
    are either 'left', 'right', or 'center'. Left is the default.

    Example:

    .. code-block:: pycon

        >>> table.justify_columns[0] = 'right'  # Name column.
        >>> table.justify_columns[1] = 'center'  # Color column.
        >>> print(table.table)
        +---------+-------+-----------+
        |    Name | Color | Type      |
        +---------+-------+-----------+
        | Avocado | green | nut       |
        |  Tomato |  red  | fruit     |
        | Lettuce | green | vegetable |
        +---------+-------+-----------+

.. py:attribute:: Table.padding_left

    Number of spaces to pad on the left side of every cell. Default is **1**. Padding adds spacing between the cell text
    and the column border.

.. py:attribute:: Table.padding_right

    Number of spaces to pad on the right side of every cell. Default is **1**. Padding adds spacing between the cell
    text and the column border.
