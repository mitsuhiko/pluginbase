import os
import sys
import subprocess


def test_clean_shutdown():
    env = dict(os.environ)
    env['PYTHONPATH'] = '..:.'
    c = subprocess.Popen([sys.executable, '-c', 'import shutdown'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         env=env)
    stdout, stderr = c.communicate()
    assert stdout == b''
    assert stderr == b''
