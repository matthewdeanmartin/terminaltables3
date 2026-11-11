"""Tuple rows can be padded when later rows contain more columns."""

from terminaltables3.base_table import BaseTable


def test_short_tuple_row_is_padded():
    table = BaseTable([("A",), ("B", "C")])
    assert table.table == (
        "+---+---+\n" "| A |   |\n" "+---+---+\n" "| B | C |\n" "+---+---+"
    )
