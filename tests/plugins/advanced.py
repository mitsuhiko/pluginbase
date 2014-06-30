from pluginbase import get_plugin_source


def get_app():
    rv = get_plugin_source(stacklevel=1)
    if rv is not None:
        return rv.app


def get_app_name():
    return get_app().name
