import gc
import pytest

from pluginbase import PluginBase


@pytest.fixture(scope='function')
def base():
    return PluginBase(package='dummy.plugins')


@pytest.fixture(scope='function')
def dummy_internal_name():
    return 'pluginbase._internalspace._sp7bb7d8da1d24ae5a5205609c951b8be4'


@pytest.fixture(scope='function')
def source(base):
    return base.make_plugin_source(searchpath=['./plugins'],
                                   identifier='demo')


@pytest.yield_fixture(scope='function', autouse=True)
def run_garbage_collection():
    gc.collect()
    try:
        yield
    finally:
        gc.collect()
