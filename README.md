# Beancount extensions by Rudd-O

This package contains a number of Beancount plugins.  To use:

* From a source checkout of this repository: put the folder in your `PYTHONPATH` environment variable, then launch Beancount or Fava under that environment.
* Installing into your local Python environment: clone this repo, then run `python3 setup.py bdist_wheel`, then use `pip3` to install the resulting wheel under the `dist/` subfolder.

## `beancount_extensions.future_transactions`

A very simple plugin for Beancount that filters out transactions with a future date, provided they are tagged with the `#future` tag.

To use, add the the stanza `plugin "beancount_extensions.future_transactions"` to your main Beancount file.

That's it.

From this point on, any transaction with a future tagged `#future` will not appear in your reports and queries.

If you want to suppress **all** future-dated entries, add the option `suppress_all_future_entries` to your plugin stanza:

```
; beancount.bean

plugin "beancount_extensions.future_transactions" "suppress_all_future_entries"
```

if you want to suppress entries taggedwith a different tag, say, `#excludenow`, then you can use the following option:

```
; beancount.bean

plugin "beancount_extensions.future_transactions" "tag_to_suppress=excludenow"
```
## `beancount_extensions.auto_open_subaccounts`

This plugin will automatically create open account directives for any account you mention in a transaction, provided that one of the parent accounts has a special marker metadata entry allowing subaccounts to be automatically opened.

To use, first load the plugin in your main Beancount file:

```
; beancount.bean

plugin "beancount_extensions.auto_open_subaccounts"
```

Now mark the account you want subaccounts to be automatically opened for, as follows:

```
; beancount.bean

2025-01-01 open Expenses:Gifts
  auto_open_subacconuts: "true"
```

Presto!  Now you can expect all transactions mentioning any subaccount under `Expenses:Gifts` to auto-create open account directives for you.
