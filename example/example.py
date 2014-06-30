import os
from functools import partial
from pluginbase import PluginBase


# For easier usage calculate the path relative to here.
here = os.path.abspath(os.path.dirname(__file__))
get_path = partial(os.path.join, here)


# Setup a plugin base for "example.modules" and make sure to load
# all the default built-in plugins from the builtin_plugins folder.
plugin_base = PluginBase(package='example.plugins',
                         searchpath=[get_path('./builtin_plugins')])


class Application(object):
    """Represents a simple example application."""

    def __init__(self, name):
        # Each application has a name
        self.name = name

        # And a dictionary where it stores "formatters".  These will be
        # functions provided by plugins which format strings.
        self.formatters = {}

        # and a source which loads the plugins from the "app_name/plugins"
        # folder.
        self.source = plugin_base.make_plugin_source(
            searchpath=[get_path('./%s/plugins' % name)])

        # Here we list all the plugins the source knows about, load them
        # and the use the "setup" function provided by the plugin to
        # initialize the plugin.
        for plugin_name in self.source.list_plugins():
            plugin = self.source.load_plugin(plugin_name)
            plugin.setup(self)

    def register_formatter(self, name, formatter):
        """A function a plugin can use to register a formatter."""
        self.formatters[name] = formatter


def run_demo(app, source):
    """Shows all formatters in demo mode of an application."""
    print('Formatters for %s:' % app.name)
    print('       input: %s' % source)
    for name, fmt in sorted(app.formatters.items()):
        print('  %10s: %s' % (name, fmt(source)))
    print('')


def main():
    # This is the demo string we want to format.
    source = 'This is a cool demo text to show this functionality.'

    # Set up two applications.  One loads plugins from ./app1/plugins
    # and the second one from ./app2/plugins.  Both will also load
    # the default ./builtin_plugins.
    app1 = Application('app1')
    app2 = Application('app2')

    # Run the demo for both
    run_demo(app1, source)
    run_demo(app2, source)

    # And just to show how the import system works, we also showcase
    # importing plugins regularly:
    with app1.source:
        from example.plugins import secret
        print('Plugin module: %s' % secret)


if __name__ == '__main__':
    main()
