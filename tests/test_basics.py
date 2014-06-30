import gc
import sys

from pluginbase import get_plugin_source


def test_basic_plugin(source, dummy_internal_name):
    # When the source is active the import gives us a module
    with source:
        from dummy.plugins import hello

    # Which because of a stable identifier has a predictable name.
    assert hello.__name__ == dummy_internal_name + '.hello'

    # And can continue to import from itself.
    assert hello.import_self() is hello

    # On the other hand without a source will fall flat on the floor.
    try:
        from dummy.plugins import hello
    except RuntimeError:
        pass
    else:
        assert False, 'Expected a runtime error but managed to ' \
            'import hello (%s)' % hello


def test_fetching_plugin_source(source):
    # Finding the plugin source outside of a plugin and without a with
    # block of a plugin source returns None.
    assert get_plugin_source() is None

    # Inside a source block we can find the source through mere calling.
    with source:
        assert get_plugin_source() is source

    # A module can always find its own source as well (the hello module
    # calls get_plugin_source() itself).
    with source:
        from dummy.plugins import hello
    assert hello.get_plugin_source() is source

    # Last but not least the plugin source can be found by module names
    # (in a plugin source block by the import name and in any case by
    # the internal name)
    with source:
        assert get_plugin_source('dummy.plugins.hello') is source
    assert get_plugin_source(hello.__name__) is source

    # As well as by module object.
    assert get_plugin_source(hello) is source


def test_cleanup(base):
    new_source = base.make_plugin_source(searchpath=['./plugins'])
    mod_name = new_source.mod.__name__
    assert sys.modules.get(mod_name) is new_source.mod

    with new_source:
        from dummy.plugins import hello

    new_source = None
    gc.collect()
    assert sys.modules.get(mod_name) is None
    assert hello.import_self is None


def test_persist(base):
    new_source = base.make_plugin_source(searchpath=['./plugins'],
                                         persist=True)
    mod_name = new_source.mod.__name__
    assert sys.modules.get(mod_name) is new_source.mod

    with new_source:
        from dummy.plugins import hello

    new_source = None
    assert sys.modules.get(mod_name) is not None
    assert hello.import_self is not None
    sys.modules[mod_name].__pluginbase_state__.source.cleanup()
    assert sys.modules.get(mod_name) is None
    assert hello.import_self is None


def test_list_plugins(source):
    plugins = source.list_plugins()
    hello_plugins = [x for x in plugins if x.startswith('hello')]
    assert hello_plugins == ['hello', 'hello2']


def test_load_plugin(source):
    hello = source.load_plugin('hello')
    assert hello.demo_func() == 42
