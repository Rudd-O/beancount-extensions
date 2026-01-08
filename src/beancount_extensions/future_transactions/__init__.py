"""A plugin that suppresses future transactions when enabled.
"""

__author__ = "Manuel Amador (Rudd-O)"
__plugins__ = ("future_transactions_plugin",)
__version__ = "0.0.7"

import datetime
from beancount.core import data

# The name of the metadata field that indicates this is a future transaction
# that should be filtered out if it is past today's date.
DEFAULT_TAG = "future"
OPT_TAG_TO_SUPPRESS = "tag_to_suppress"

# Suppress all future entries or only entries tagged with OPT_TAG_TO_SUPPRESS.
OPT_SUPPRESS_ALL_FUTURE_ENTRIES = "suppress_all_future_entries"

__plugins__ = ("future_transactions_plugin",)


# If "suppress_all_future_entries" in options_map, skips all future-dated entries
# else only transactions tagged #future
def future_transactions_plugin(entries, options_map, *optional_args):
    options = {
        OPT_SUPPRESS_ALL_FUTURE_ENTRIES: False,
        OPT_TAG_TO_SUPPRESS: DEFAULT_TAG,
    }
    if optional_args:
        for argval in optional_args[0].split(","):
            arg, dv, val = argval.partition("=")
            if not dv:
                arg = argval
                val = "true"
            if val.lower() == "true":
                val = True
            elif val.lower() == "false":
                val = False
            options[arg] = val

    errors = []
    new_entries = []
    today = datetime.date.today()

    def skip(entry):
        if entry.date <= today:
            return False
        return (options[OPT_SUPPRESS_ALL_FUTURE_ENTRIES]) or (
            isinstance(entry, data.Transaction)
            and options[OPT_TAG_TO_SUPPRESS] in entry.tags
        )

    for eindex, entry in enumerate(entries):
        if not skip(entry):
            new_entries.append(entry)

    return new_entries, errors
