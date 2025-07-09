from traitor import Traitor, trait, impl
from typing import Protocol


# -------------------------
# Traits to be implemented
# -------------------------

# NOTE: @trait is just syntactic sugar and wraps @runtime_checkable


@trait
class Drivable(Protocol):
    def drive(self) -> str: ...


@trait
class Refuelable(Protocol):
    def refuel(self) -> str: ...


@trait
class Rechargeable(Protocol):
    def charge(self) -> str: ...


# -------------------------------
# Classes implementing the traits
# -------------------------------


@impl(Drivable, Refuelable)
class GasCar(Traitor):
    def __init__(self):
        super().__init__()

    def drive(self) -> str:
        return "Driving with gasoline!"

    def refuel(self) -> str:
        return "Refueling at the gas station."


@impl(Drivable, Rechargeable)
class EV(Traitor):
    def __init__(self):
        super().__init__()

    def drive(self) -> str:
        return "Driving silently on battery."

    def charge(self) -> str:
        return "Charging at the station."


@impl(Drivable, Refuelable, Rechargeable)
class Hybrid(Traitor):
    def __init__(self):
        super().__init__()

    def drive(self) -> str:
        return "Driving with either fuel or battery."

    def refuel(self) -> str:
        return "Refueling the hybrid tank."

    def charge(self) -> str:
        return "Charging the hybrid battery."


# --------------------------------------------------------
# functions acting on classes implementing specific traits
# --------------------------------------------------------

# NOTE: The examples below illustrate how to use Traitor-style traits,
#       and how different type annotations can trigger different LSP errors.
#       This is a side effect of bending Python's Protocol system into something
#       it wasn't quite designed for — there’s currently no clean way around it.


def take_for_a_ride(vehicle: Drivable):
    print(vehicle.drive())


def pit_stop(vehicle: Traitor):
    for result in [
        vehicle.if_implements(Refuelable).refuel(),
        vehicle.if_implements(Rechargeable).charge(),
    ]:
        if result:
            print(result)


if __name__ == "__main__":
    car = Hybrid()
    print(f"Using {car.__class__.__name__}")
    take_for_a_ride(car)
    pit_stop(car)

    print("---------------")

    car = GasCar()
    print(f"Using {car.__class__.__name__}")
    take_for_a_ride(car)
    pit_stop(car)

    print("---------------")

    car = EV()
    print(f"Using {car.__class__.__name__}")
    take_for_a_ride(car)
    pit_stop(car)
