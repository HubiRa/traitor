from typing import runtime_checkable, Type, Any, Callable, cast, List, Tuple


def require_traits(obj: Any, *traits: Any) -> None:
    for trait in traits:
        if not isinstance(obj, trait):
            raise TypeError(
                f"{obj.__class__.__name__} does not implement required trait: {trait.__name__}"
            )


class _Noop:
    def __getattr__(self, name):
        def noop(*args, **kwargs):
            return None

        return noop


_NOOP = _Noop()


class Traitor:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        traits = getattr(self, "__impl__", ())
        if not isinstance(traits, (List, Tuple)):
            traits = (traits,)
        require_traits(self, *traits)

    def implements(self, *traits: Type) -> bool:
        return all(trait in getattr(self, "__impl__", ()) for trait in traits)

    def if_implements(self, trait: Type):
        return self if self.implements(trait) else _NOOP


def trait(cls: Any) -> Type[Any]:
    return cast(Type[Any], runtime_checkable(cls))


def impl(*traits: Any) -> Callable[[Type], Type]:
    def wrapper(cls: Type) -> type:
        setattr(cls, "__impl__", traits)
        return cls

    return wrapper
