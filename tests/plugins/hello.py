def import_self():
    from dummy.plugins import hello
    return hello


def get_plugin_source():
    from pluginbase import get_plugin_source
    return get_plugin_source()


def demo_func():
    return 42
