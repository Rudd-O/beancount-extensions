import unittest

import datetime

from beancount.core import data
from beancount_extensions import future_transactions as mod


class TestTransactions(unittest.TestCase):
    def test_basic(self):
        entries = [
            data.Transaction(
                "", datetime.date.today(), "*", "payee", "narration", [], [], []
            )
        ]
        ret, errs = mod.future_transactions_plugin(entries, None)
        assert len(ret) == 1, ret
        assert len(errs) == 0, errs
