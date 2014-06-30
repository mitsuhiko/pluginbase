def test_custom_state(base):
    class App(object):
        name = 'foobar'
    source = base.make_plugin_source(searchpath=['./plugins'])
    source.app = App()

    plg = source.load_plugin('advanced')
    assert plg.get_app_name() == 'foobar'
