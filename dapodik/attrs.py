import attr
from functools import partial


def frozen(_, __, ___):
    """
    Prevent an attribute to be modified.

    .. versionadded:: 20.1.0
    """
    raise attr.exceptions.FrozenAttributeError("Atribut tidak dapat dirubah")


frozen_attrib = partial(attr.ib, on_setattr=frozen)
