"""
Supply slaves to the plugin by acquiring them in the lego manager and wrapping in the appropriate library.
"""
import contextlib
import importlib


def get_library(lib_name):
    """
    Receives string which represents a library name.
    Returns the library object by importing it.
    """
    *module, lib_class = lib_name.split('.')
    return getattr(importlib.import_module('.'.join(module)), lib_class)


@contextlib.contextmanager
def acquire_slaves(lego_manager, query, exclusive=True):
    """
    Creates salves based on the requested setup.

    Args:
        setup - The requested setup.

    Returns:
        slaves.
    """
    with lego_manager.root.acquire(query, exclusive) as slaves:
        with contextlib.ExitStack() as stack:
            yield [
                stack.enter_context(get_library(library_name)(hostname))
                for hostname, library_name in slaves
            ]