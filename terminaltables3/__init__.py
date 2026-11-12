"""Generate simple tables in terminals from a nested list of strings.

Use SingleTable or DoubleTable instead of AsciiTable for box-drawing characters.

https://github.com/Robpol86/terminaltables3
https://pypi.python.org/pypi/terminaltables3
"""

from terminaltables3.ascii_table import AsciiTable  # noqa
from terminaltables3.github_table import GithubFlavoredMarkdownTable  # noqa
from terminaltables3.other_tables import DoubleTable  # noqa
from terminaltables3.other_tables import PorcelainTable  # noqa
from terminaltables3.other_tables import SingleTable  # noqa

__author__ = "@Robpol86, @matthewdeanmartin"
__license__ = "MIT"
__version__ = "4.1.0"
