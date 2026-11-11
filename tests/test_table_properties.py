"""Property checks across varied table shapes and plain text cells."""

from hypothesis import given, settings
from hypothesis import strategies as st

from terminaltables3 import AsciiTable, GithubFlavoredMarkdownTable, PorcelainTable
from terminaltables3.width_and_alignment import visible_width

cell = st.text(alphabet="abc 012", min_size=0, max_size=8)
rows = st.lists(st.lists(cell, min_size=1, max_size=4), min_size=1, max_size=5)


@settings(max_examples=100, deadline=None)
@given(rows)
def test_ascii_lines_keep_same_visible_width(table_data):
    table = AsciiTable(table_data)
    widths = {visible_width(line) for line in table.table.splitlines()}
    assert len(widths) == 1


@settings(max_examples=100, deadline=None)
@given(rows)
def test_markdown_rows_have_consistent_column_count(table_data):
    table = GithubFlavoredMarkdownTable(table_data)
    lines = table.table.splitlines()
    assert len({line.count("|") for line in lines}) == 1


@settings(max_examples=100, deadline=None)
@given(rows)
def test_porcelain_has_no_outer_border(table_data):
    table = PorcelainTable(table_data)
    assert table.outer_border is False
    assert table.inner_heading_row_border is False
    assert table.inner_footing_row_border is False
