"""Code from https://stackoverflow.com/a/55677007
"""
import typing


if hasattr(typing, "_GenericAlias"):
    # python 3.7
    def _get_base_generic(cls):
        # subclasses of Generic will have their _name set to None, but
        # their __origin__ will point to the base generic
        if cls._name is None:
            return cls.__origin__
        else:
            return getattr(typing, cls._name)


else:
    # python <3.7
    def _get_base_generic(cls):
        try:
            return cls.__origin__
        except AttributeError:
            pass

        name = type(cls).__name__
        if not name.endswith("Meta"):
            raise NotImplementedError("Cannot determine base of {}".format(cls))

        name = name[:-4]
        try:
            return getattr(typing, name)
        except AttributeError:
            raise NotImplementedError("Cannot determine base of {}".format(cls))


if hasattr(typing.List, "__args__"):
    # python 3.6+
    def _get_subtypes(cls):
        subtypes = cls.__args__

        if _get_base_generic(cls) is typing.Callable:
            if len(subtypes) != 2 or subtypes[0] is not ...:
                subtypes = (subtypes[:-1], subtypes[-1])

        return subtypes


else:
    # python 3.5
    def _get_subtypes(cls):
        if isinstance(cls, typing.CallableMeta):  # pylint: disable=no-member
            if cls.__args__ is None:
                return ()

            return cls.__args__, cls.__result__

        for name in ["__parameters__", "__union_params__", "__tuple_params__"]:
            try:
                subtypes = getattr(cls, name)
                break
            except AttributeError:
                pass
        else:
            raise NotImplementedError("Cannot extract subtypes from {}".format(cls))

        subtypes = [typ for typ in subtypes if not isinstance(typ, typing.TypeVar)]
        return subtypes
