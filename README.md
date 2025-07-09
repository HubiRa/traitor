# Traitor

A small experiment in trait-like composition using Python’s `Protocol`, inspired by Rust's traits
(while being a lot less powerful — and arguably less useful).

I never said it was a good idea! Implemented just for fun.

---

## How to try it out

This project uses [uv](https://docs.astral.sh/uv/) out of habit (ok, it's overkill here...)

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

Then run the example:

```bash
python example.py
```

## What is this?

Traitor is a tiny Python library inspired by Rust's traits, built on top of Python's `Protocol`.

It lets you:

- Declare traits using `@trait` (a thin `@runtime_checkable` wrapper)
- Mark classes as implementing traits with `@impl(...)`
- Enforce trait conformance at runtime via a base class (`Traitor`)
- Compose behavior in a declarative way

Example:

```python
from traitor import trait, impl, Traitor
from typing import Protocol

@trait
class Loggable(Protocol):
    def log(self) -> None: ...

@impl(Loggable)
class MyClass(Traitor):
    def log(self): print("hello")

MyClass().if_implements(Loggable).log()  # prints "hello"
```

---

### Why the name?

Because it betrays Rust traits just as much as Python inheritance.
