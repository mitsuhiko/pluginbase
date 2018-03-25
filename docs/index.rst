PluginBase
==========

.. module:: pluginbase

Ever tried creating a plugin system for a Python application and you
discovered fighting against the import system?  Me too.  This is where
PluginBase comes in.

PluginBase is a module for Python which extends the import system for
the most common form of plugin usage which is providing a consistent
import experience for plugins from a variety of sources.  Essentially it
allows you to build very flexible plugin based applications which pull in
plugins from bundled sources as well as application specific ones without
bypassing the Python import system.

How does it work?  It's super simple:

Step 1:

    Create a "plugin base" object.  It defines a pseudo package under
    which all your plugins will reside.  For instance it could be
    ``yourapplication.plugins``::

        from pluginbase import PluginBase
        plugin_base = PluginBase(package='yourapplication.plugins')

Step 2:

    Now that you have a plugin base, you can define a plugin source
    which is the list of all sources which provide plugins::

        plugin_source = plugin_base.make_plugin_source(
            searchpath=['./path/to/plugins', './path/to/more/plugins'])

Step 3:

    To import a plugin all you need to do is to use the regular import
    system.  The only change is that you need to import the plugin
    source through the ``with`` statement::

        with plugin_source:
            from yourapplication.plugins import my_plugin
        my_plugin.do_something_cool()

    Alternatively you can also import plugins programmatically instead of
    using the import statement::

        my_plugin = plugin_source.load_plugin('my_plugin')

For a more complex example see the one from the git repo:
`pluginbase-example <https://github.com/mitsuhiko/pluginbase/tree/master/example>`__.

Installation
------------

You can get the library directly from PyPI::

    pip install pluginbase


FAQ
---

Q: Why is there a plugin base and a plugin source class?

    This decision was taken so that multiple applications can co-exist
    together.  For instance imagine you have an application that
    implements a wiki but you want multiple instances of that wiki
    to exist in the same Python interpreter.  The plugin sources split
    out the load paths of the different applications.

    Each instance of the wiki would have its own plugin source and they
    can work independently of each other.

Q: Do plugins pollute ``sys.modules``?

    While a plugin source is alive the plugins do indeed reside in
    ``sys.modules``.  This decision was made consciously so that as little
    as possible of the Python library ecosystem breaks.  However when the
    plugin source gets garbage collected all loaded plugins will
    also get garbage collected.

Q: How does PluginBase deal with different versions of the same plugin?

    Each plugin source works independently of each other.  The way this
    works is by internally translating the module name.  By default that
    module name is a random number but it can also be forced to a hash of
    a specific value to make it stable across restarts which allows
    pickle and similar libraries to work.

    This internal module renaming means that
    ``yourapplication.module.foo`` will internally be called
    ``pluginbase._internalspace._sp7...be4`` for instance.  The same
    plugin loaded from another plugin source will have a different
    internal name.

Q: What happens if a plugin wants to import other modules?

    All fine.  Plugins can import from itself as well as other plugins
    that can be located.

Q: Does PluginBase support pickle?

    Yes, pickle works fine for plugins but it does require defining a
    stable identifier when creating a plugin source.  This could for
    instance be a file system path::

        plugin_source = base.make_plugin_source(
            searchpath=[app.plugin_path],
            identifier=app.config_filename)

Q: What happens if I import from the plugin module without the
plugin source activated through the ``with`` statement?

    The import will fail with a descriptive error message explaining
    that a plugin source needs to be activated.

Q: Can I automatically discover all modules that are available?

    Yes you can.  Just use the :meth:`PluginSource.list_plugins` method
    which returns a list of all plugins that a source can import.

Q: Why would I use this over setuptools based plugins?

    PluginBase and setuptools based plugins solve very different problems
    and are incompatible on an architectural point of view.  PluginBase
    does not solve plugin distribution through PyPI but allows plugins to
    be virtualized from each other.  Setuptools on the other hand is based
    on PyPI based distribution but piggybacks on top of the regular import
    system.

    There are advantages and disadvantages to both of them.  Setuptools
    based plugins are very useful to extend libraries from other
    libraries.  For instance the Jinja2 template engine hooks into the
    Babel library for internationalization through setuptools.

    On the other hand applications distributed to users can benefit from a
    PluginBase based system which allows them to take control over how
    plugins are distributed and full separation from each other.


API
---

High Level
``````````

.. autoclass:: PluginBase
   :members:

.. autoclass:: PluginSource
   :members:

.. autofunction:: get_plugin_source

.. autofunction:: get_searchpath

Import Hook Control
```````````````````

.. autofunction:: pluginbase.import_hook.enable

.. autofunction:: pluginbase.import_hook.disable

.. data:: pluginbase.import_hook.enabled

   Indicates if the import hook is currently active or not.

Internals
`````````

.. autodata:: pluginbase._internalspace

   This module is where pluginbase keeps track of all loaded plugins.
   Generally one can completely ignore the existence of it, but in some
   situations it might be useful to discover currently loaded modules
   through this when debugging.
