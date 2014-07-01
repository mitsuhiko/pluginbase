import pytest


def test_custom_state(base):
    class App(object):
        name = 'foobar'
    source = base.make_plugin_source(searchpath=['./plugins'])
    source.app = App()

    plg = source.load_plugin('advanced')
    assert plg.get_app_name() == 'foobar'


def test_plugin_resources(source):
    with source.open_resource('withresources', 'hello.txt') as f:
        contents = f.read()
    assert contents == b'I am a textfile.\n'

    with pytest.raises(IOError):
        source.open_resource('withresources', 'missingfile.txt')
