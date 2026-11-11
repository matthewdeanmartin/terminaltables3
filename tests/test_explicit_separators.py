"""Optional separators preserve the existing table behavior by default."""

from collections.abc import Sequence

import pytest

from terminaltables3 import (
    AsciiTable,
    DoubleTable,
    GithubFlavoredMarkdownTable,
    SingleTable,
)


@pytest.mark.parametrize("table_type", [AsciiTable, SingleTable, DoubleTable])
def test_marker_is_data_until_separators_are_enabled(table_type):
    table = table_type([["Head"], ["---"], ["Body"]], title="Title")

    assert table.inner_separators is False
    assert "---" in table.table


@pytest.mark.parametrize("table_type", [AsciiTable, SingleTable, DoubleTable])
def test_opt_in_separator_uses_existing_border_style(table_type):
    marked = table_type([["alpha"], ["---"], ["bravo"]], title="Title")
    grid = table_type([["alpha"], ["bravo"]], title="Title")
    marked.inner_separators = True
    marked.inner_heading_row_border = False
    grid.inner_heading_row_border = False
    grid.inner_row_border = True

    assert marked.table == grid.table


def test_separator_title_does_not_replace_table_title():
    table = AsciiTable(
        [["Header", "Col"], ["First", "1"], ["---", "Group"], ["Second", "2"]],
        title="Table",
    )
    table.inner_separators = True

    lines = table.table.splitlines()
    assert "Table" in lines[0]
    assert "First" in lines[3]
    assert "Group" in lines[4]
    assert "Second" in lines[5]


def test_custom_delimiter_and_empty_rows():
    table = AsciiTable([["A"], [], ["==", "Group"], ["B"]])
    table.inner_separators = True
    table.inner_separators_delimiter = "=="

    assert "Group" in table.table


def test_two_argument_border_call_still_works():
    table = AsciiTable([["abc"]], title="Top")

    assert "".join(table.horizontal_border("top", [5])) == "+Top--+"
    assert "".join(table.horizontal_border("row", [5])) == "+-----+"
    assert "".join(table.horizontal_border("row", [5], "Group")) == "+Group+"


def test_markdown_override_accepts_optional_title():
    table = GithubFlavoredMarkdownTable([["Head"], ["---"], ["Body"]])

    assert "---" in table.table
    assert "".join(table.horizontal_border("heading", [6], title=None)) == "|------|"


def test_inner_row_borders_do_not_write_to_stdout(capsys):
    table = AsciiTable([["A"], ["B"]])
    table.inner_row_border = True

    assert "A" in table.table
    assert capsys.readouterr().out == ""


def test_existing_custom_sequence_needs_no_slice_support():
    class Rows(Sequence):
        def __init__(self):
            self.rows = [["A"], ["B"]]

        def __len__(self):
            return len(self.rows)

        def __getitem__(self, index):
            if isinstance(index, slice):
                raise TypeError("slicing is unsupported")
            return self.rows[index]

    assert "B" in AsciiTable(Rows()).table
