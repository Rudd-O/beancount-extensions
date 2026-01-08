# Beancount future transactions

**Attention:** The project beancount-future-transactions has been superseded by
[beancount-extensions](https://github.com/Rudd-O/beancount-extensions).  This
is the last release of the project as is -- upgrade your Beancount setup to
use the new project.

This is a very simple plugin for Beancount that filters out transactions with a future date, provided they are tagged with the `#future` tag.

To use:

* Install using your favorite Python method — probably `pip` or `python setup.py install`, although you may want to install to your user directory (`pip --user`).
* Include the stanza `plugin "beancount_extensions.future_transactions"` in your Beancount file.

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
