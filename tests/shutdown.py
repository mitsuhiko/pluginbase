from pluginbase import PluginBase

base = PluginBase(package='dummy.modules')
plugin_source = base.make_plugin_source(
    searchpath=['./plugins'])

# This dangles around.  This will be collected when the interpreter
# shuts down.
hello = plugin_source.load_plugin('hello')
