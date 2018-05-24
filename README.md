# PluginBase

PluginBase is a module for Python that enables the
development of flexible plugin systems in Python.

Step 1:
```python
from pluginbase import PluginBase
plugin_base = PluginBase(package='yourapplication.plugins')
```

Step 2:
```python
plugin_source = plugin_base.make_plugin_source(
    searchpath=['./path/to/plugins', './path/to/more/plugins'])
```

Step 3:
```python
with plugin_source:
    from yourapplication.plugins import my_plugin
my_plugin.do_something_cool()
```

Or alternatively:
```python
my_plugin = plugin_source.load_plugin('my_plugin')
my_plugin.do_something_cool()
```
