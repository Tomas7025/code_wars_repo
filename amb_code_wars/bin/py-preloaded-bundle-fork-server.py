#!"/home/tomas/Área de Trabalho/code_wars/amb_code_wars/bin/python3"
# EASY-INSTALL-ENTRY-SCRIPT: 'preloaded==1.20230516.122456','console_scripts','py-preloaded-bundle-fork-server.py'
import re
import sys

# for compatibility with easy_install; see #2198
__requires__ = 'preloaded==1.20230516.122456'

try:
    from importlib.metadata import distribution
except ImportError:
    try:
        from importlib_metadata import distribution
    except ImportError:
        from pkg_resources import load_entry_point


def importlib_load_entry_point(spec, group, name):
    dist_name, _, _ = spec.partition('==')
    matches = (
        entry_point
        for entry_point in distribution(dist_name).entry_points
        if entry_point.group == group and entry_point.name == name
    )
    return next(matches).load()


globals().setdefault('load_entry_point', importlib_load_entry_point)


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(load_entry_point('preloaded==1.20230516.122456', 'console_scripts', 'py-preloaded-bundle-fork-server.py')())
