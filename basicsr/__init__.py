# https://github.com/xinntao/BasicSR
# flake8: noqa
import sys as _sys

# Ensure absolute imports like `import basicsr` work when bundled as a custom node.
_sys.modules.setdefault("basicsr", _sys.modules[__name__])

from .version import __gitsha__, __version__

__all__ = ["__gitsha__", "__version__"]
