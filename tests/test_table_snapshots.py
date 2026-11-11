"""Golden output for the public table formats."""

from pathlib import Path

import pytest

from terminaltables3 import (
    AsciiTable,
    DoubleTable,
    GithubFlavoredMarkdownTable,
    PorcelainTable,
)


@pytest.mark.parametrize(
    "table_type",
    [AsciiTable, DoubleTable, GithubFlavoredMarkdownTable, PorcelainTable],
)
def test_basic_table_snapshot(table_type, snapshot):
    snapshot.snapshot_dir = Path(__file__).parent / "snapshots" / "basic_tables"
    rows = [["Name", "Value"], ["alpha", "1"], ["beta", "2"]]
    snapshot.assert_match(table_type(rows).table, table_type.__name__ + ".txt")
