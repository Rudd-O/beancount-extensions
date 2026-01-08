"""
Various Beancount plugins.
"""

__author__ = "Manuel Amador (Rudd-O)"
__plugins__ = ("auto_open_subaccounts",)

import time
import sys

from beancount.core import data

DEBUG = 0


def auto_open_subaccounts(entries, options_map, *optional_args):
    start_time = time.time()
    errors = []
    new_entries = []

    opens = [e for e in entries if isinstance(e, data.Open)]
    enabled_for = dict()
    opened = set()
    auto_opened = 0

    for entry in opens:
        for m in entry.meta:
            if m == "auto_open_subaccounts" and entry.meta[m].strip().lower() == "true":
                enabled_for[entry.account] = entry
        opened.add(entry.account)

    for entry in entries:
        if isinstance(entry, data.Transaction):
            for posting in entry.postings:
                if posting.account not in opened:
                    account_fragments = posting.account.split(":")
                    matching_parent_open = None
                    for k, v in enabled_for.items():
                        potential_match = k.split(":")
                        if account_fragments[:len(potential_match)] == potential_match:
                            matching_parent_open = v
                            break
                    if matching_parent_open is not None:
                        new_entries.append(data.Open(
                            matching_parent_open.meta,
                            entry.date,
                            posting.account,
                            matching_parent_open.currencies,
                            matching_parent_open.booking
                        ))
                        opened.add(posting.account)
                        auto_opened += 1

    new_entries = entries + new_entries

    if DEBUG:
        elapsed_time = time.time() - start_time
        print("%s: Took %.2f. Discovered %d open accounts.  %d of them have auto open subtree.  Auto-opened %d accounts." % (__name__, elapsed_time, len(opened), len(enabled_for), auto_opened), file=sys.stderr)

    return new_entries, errors
