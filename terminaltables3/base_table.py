"""Base table class. Define just the bare minimum to build tables."""

from typing import Generator, Optional, Sequence, Tuple

from terminaltables3.build import build_border, build_row, flatten
from terminaltables3.width_and_alignment import align_and_pad_cell, max_dimensions


class BaseTable:
    """Base table class.

    :ivar iter table_data: List (empty or list of lists of strings) representing the table.
    :ivar str title: Optional title to show within the top border of the table.
    :ivar bool inner_column_border: Separates columns.
    :ivar bool inner_footing_row_border: Show a border before the last row.
    :ivar bool inner_heading_row_border: Show a border after the first row.
    :ivar bool inner_row_border: Show a border in between every row.
    :ivar bool outer_border: Show the top, left, right, and bottom border.
    :ivar dict justify_columns: Horizontal justification. Keys are column indexes (int). Values are right/left/center.
    :ivar int padding_left: Number of spaces to pad on the left side of every cell.
    :ivar int padding_right: Number of spaces to pad on the right side of every cell.
    """

    CHAR_F_INNER_HORIZONTAL = "-"
    CHAR_F_INNER_INTERSECT = "+"
    CHAR_F_INNER_VERTICAL = "|"
    CHAR_F_OUTER_LEFT_INTERSECT = "+"
    CHAR_F_OUTER_LEFT_VERTICAL = "|"
    CHAR_F_OUTER_RIGHT_INTERSECT = "+"
    CHAR_F_OUTER_RIGHT_VERTICAL = "|"
    CHAR_H_INNER_HORIZONTAL = "-"
    CHAR_H_INNER_INTERSECT = "+"
    CHAR_H_INNER_VERTICAL = "|"
    CHAR_H_OUTER_LEFT_INTERSECT = "+"
    CHAR_H_OUTER_LEFT_VERTICAL = "|"
    CHAR_H_OUTER_RIGHT_INTERSECT = "+"
    CHAR_H_OUTER_RIGHT_VERTICAL = "|"
    CHAR_INNER_HORIZONTAL = "-"
    CHAR_INNER_INTERSECT = "+"
    CHAR_INNER_VERTICAL = "|"
    CHAR_OUTER_BOTTOM_HORIZONTAL = "-"
    CHAR_OUTER_BOTTOM_INTERSECT = "+"
    CHAR_OUTER_BOTTOM_LEFT = "+"
    CHAR_OUTER_BOTTOM_RIGHT = "+"
    CHAR_OUTER_LEFT_INTERSECT = "+"
    CHAR_OUTER_LEFT_VERTICAL = "|"
    CHAR_OUTER_RIGHT_INTERSECT = "+"
    CHAR_OUTER_RIGHT_VERTICAL = "|"
    CHAR_OUTER_TOP_HORIZONTAL = "-"
    CHAR_OUTER_TOP_INTERSECT = "+"
    CHAR_OUTER_TOP_LEFT = "+"
    CHAR_OUTER_TOP_RIGHT = "+"
    CHAR_S_INNER_HORIZONTAL = "-"
    CHAR_S_INNER_INTERSECT = "+"
    CHAR_S_INNER_VERTICAL = "|"
    CHAR_S_OUTER_LEFT_INTERSECT = "+"
    CHAR_S_OUTER_LEFT_VERTICAL = "|"
    CHAR_S_OUTER_RIGHT_INTERSECT = "+"
    CHAR_S_OUTER_RIGHT_VERTICAL = "|"

    def __init__(
        self, table_data: Sequence[Sequence[str]], title: Optional[str] = None
    ):
        """Constructor.

        :param iter table_data: List (empty or list of lists of strings) representing the table.
        :param title: Optional title to show within the top border of the table.
        """
        self.table_data = table_data
        self.title = title
        self.separator_title = None

        self.inner_column_border = True
        self.inner_footing_row_border = False
        self.inner_heading_row_border = True
        self.inner_separators = True
        self.inner_separators_delimiter = "---"
        self.inner_row_border = False
        self.outer_border = True

        self.justify_columns = {}  # {0: 'right', 1: 'left', 2: 'center'}
        self.padding_left = 1
        self.padding_right = 1

    def horizontal_border(
        self, style: str, outer_widths: Sequence[int], title
    ) -> Tuple[str, ...]:
        """Build any kind of horizontal border for the table.

        :param str style: Type of border to return.
        :param iter outer_widths: List of widths (with padding) for each column.

        :return: Prepared border as a tuple of strings.
        :rtype: tuple
        """
        if style == "top":
            horizontal = self.CHAR_OUTER_TOP_HORIZONTAL
            left = self.CHAR_OUTER_TOP_LEFT
            intersect = (
                self.CHAR_OUTER_TOP_INTERSECT if self.inner_column_border else ""
            )
            right = self.CHAR_OUTER_TOP_RIGHT
            title = title
        elif style == "bottom":
            horizontal = self.CHAR_OUTER_BOTTOM_HORIZONTAL
            left = self.CHAR_OUTER_BOTTOM_LEFT
            intersect = (
                self.CHAR_OUTER_BOTTOM_INTERSECT if self.inner_column_border else ""
            )
            right = self.CHAR_OUTER_BOTTOM_RIGHT
            title = title
        elif style == "heading":
            horizontal = self.CHAR_H_INNER_HORIZONTAL
            left = self.CHAR_H_OUTER_LEFT_INTERSECT if self.outer_border else ""
            intersect = self.CHAR_H_INNER_INTERSECT if self.inner_column_border else ""
            right = self.CHAR_H_OUTER_RIGHT_INTERSECT if self.outer_border else ""
            title = title
        elif style == "footing":
            horizontal = self.CHAR_F_INNER_HORIZONTAL
            left = self.CHAR_F_OUTER_LEFT_INTERSECT if self.outer_border else ""
            intersect = self.CHAR_F_INNER_INTERSECT if self.inner_column_border else ""
            right = self.CHAR_F_OUTER_RIGHT_INTERSECT if self.outer_border else ""
            title = title
        elif style == "separator":
            horizontal = self.CHAR_S_INNER_HORIZONTAL
            left = self.CHAR_S_OUTER_LEFT_INTERSECT if self.outer_border else ""
            intersect = self.CHAR_S_INNER_INTERSECT if self.inner_column_border else ""
            right = self.CHAR_S_OUTER_RIGHT_INTERSECT if self.outer_border else ""
            title = title
        else:
            horizontal = self.CHAR_INNER_HORIZONTAL
            left = self.CHAR_OUTER_LEFT_INTERSECT if self.outer_border else ""
            intersect = self.CHAR_INNER_INTERSECT if self.inner_column_border else ""
            right = self.CHAR_OUTER_RIGHT_INTERSECT if self.outer_border else ""
            title = title
        return build_border(outer_widths, horizontal, left, intersect, right, title)

    def gen_row_lines(
        self, row: Sequence[str], style: str, inner_widths: Sequence[int], height: int
    ) -> Generator[Tuple[str, ...], None, None]:
        r"""Combine cells in row and group them into lines with vertical borders.

        Caller is expected to pass yielded lines to ''.join() to combine them into a printable line. Caller must append
        newline character to the end of joined line.

        In:
        ['Row One Column One', 'Two', 'Three']
        Out:
        [
            ('|', ' Row One Column One ', '|', ' Two ', '|', ' Three ', '|'),
        ]

        In:
        ['Row One\nColumn One', 'Two', 'Three'],
        Out:
        [
            ('|', ' Row One    ', '|', ' Two ', '|', ' Three ', '|'),
            ('|', ' Column One ', '|', '     ', '|', '       ', '|'),
        ]

        :param iter row: One row in the table. List of cells.
        :param str style: Type of border characters to use.
        :param iter inner_widths: List of widths (no padding) for each column.
        :param int height: Inner height (no padding) (number of lines) to expand row to.

        :return: Yields lines split into components in a list. Caller must ''.join() line.
        """
        cells_in_row = []

        # Resize row if it doesn't have enough cells.
        if len(row) != len(inner_widths):
            row = row + [""] * (len(inner_widths) - len(row))

        # Pad and align each cell. Split each cell into lines to support multi-line cells.
        for i, cell in enumerate(row):
            align = (self.justify_columns.get(i),)
            inner_dimensions = (inner_widths[i], height)
            padding = (self.padding_left, self.padding_right, 0, 0)
            cells_in_row.append(
                align_and_pad_cell(cell, align, inner_dimensions, padding)
            )

        # Determine border characters.
        if style == "heading":
            left = self.CHAR_H_OUTER_LEFT_VERTICAL if self.outer_border else ""
            center = self.CHAR_H_INNER_VERTICAL if self.inner_column_border else ""
            right = self.CHAR_H_OUTER_RIGHT_VERTICAL if self.outer_border else ""
        elif style == "footing":
            left = self.CHAR_F_OUTER_LEFT_VERTICAL if self.outer_border else ""
            center = self.CHAR_F_INNER_VERTICAL if self.inner_column_border else ""
            right = self.CHAR_F_OUTER_RIGHT_VERTICAL if self.outer_border else ""
        elif style == "separator":
            left = self.CHAR_S_OUTER_LEFT_VERTICAL if self.outer_border else ""
            center = self.CHAR_S_INNER_VERTICAL if self.inner_column_border else ""
            right = self.CHAR_S_OUTER_RIGHT_VERTICAL if self.outer_border else ""
        else:
            left = self.CHAR_OUTER_LEFT_VERTICAL if self.outer_border else ""
            center = self.CHAR_INNER_VERTICAL if self.inner_column_border else ""
            right = self.CHAR_OUTER_RIGHT_VERTICAL if self.outer_border else ""

        # Yield each line.
        yield from build_row(cells_in_row, left, center, right)

    def gen_table(
        self,
        inner_widths: Sequence[int],
        inner_heights: Sequence[int],
        outer_widths: Sequence[int],
    ) -> Generator[Tuple[str, ...], None, None]:
        """Combine everything and yield every line of the entire table with borders.

        :param iter inner_widths: List of widths (no padding) for each column.
        :param iter inner_heights: List of heights (no padding) for each row.
        :param iter outer_widths: List of widths (with padding) for each column.
        :return:
        """
        # Yield top border.
        if self.outer_border:
            yield self.horizontal_border("top", outer_widths, title=self.title)

        # Yield table body.
        row_count = len(self.table_data)
        last_row_index, before_last_row_index = row_count - 1, row_count - 2
        for i, row in enumerate(self.table_data):
            # Yield the row line by line (e.g. multi-line rows).
            if self.inner_heading_row_border and i == 0:
                style = "heading"
            elif self.inner_footing_row_border and i == last_row_index:
                style = "footing"
            elif self.inner_separators and row[0] == self.inner_separators_delimiter:
                style = "separator"
            else:
                style = "row"
            if not style == "separator": # Don't return separator text
                yield from self.gen_row_lines(row, style, inner_widths, inner_heights[i])
            # If this is the last row then break. No separator needed.
            if i == last_row_index:
                break
            # Yield heading separator.
            if style == "heading":
                yield self.horizontal_border("heading", outer_widths, title=None)
            # Yield footing separator.
            elif self.inner_footing_row_border and i == before_last_row_index:
                yield self.horizontal_border("footing", outer_widths, title=None)
            # Yield string-matched row separator.
            elif style == "separator":
                # If the second column exists then pass it as the border title.
                title = row[1] if len(row) > 1 else None
                yield self.horizontal_border("separator", outer_widths, title)
            # Yield grid-style separator.
            elif self.inner_row_border:
                print("Yielding a separator row")
                yield self.horizontal_border("row", outer_widths, title=None)

        # Yield bottom border.
        if self.outer_border:
            yield self.horizontal_border("bottom", outer_widths, title=None)

    @property
    def table(self) -> str:
        """Return a large string of the entire table ready to be printed to the terminal."""
        dimensions = max_dimensions(
            self.table_data, self.padding_left, self.padding_right
        )[:3]
        return flatten(self.gen_table(*dimensions))
