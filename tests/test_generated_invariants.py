"""Deterministic generated checks for table rendering invariants."""

import random

from terminaltables3.base_table import BaseTable
from terminaltables3.width_and_alignment import visible_width


def test_generated_tables_have_consistent_rendered_line_widths():
    """Rendered lines should have equal visible widths across varied table shapes."""
    generator = random.Random(0)
    cells = ("", "x", "界", "one\ntwo")

    for row_count in range(6):
        for column_count in range(6):
            rows = []
            for _ in range(row_count):
                row_length = generator.randrange(column_count + 1)
                rows.append(
                    [generator.choice(cells) for _ in range(row_length)]
                )

            for outer_border in (False, True):
                for inner_column_border in (False, True):
                    table = BaseTable(rows)
                    table.outer_border = outer_border
                    table.inner_column_border = inner_column_border

                    lines = table.table.splitlines()
                    widths = {visible_width(line) for line in lines}

                    assert len(widths) <= 1, (rows, outer_border, inner_column_border)

