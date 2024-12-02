#!/usr/bin/python3

from typing import Self

class FuelStation:
    """
    A class that manages slot for the fuel types.
    """
    def __init__(self: Self, diesel: int, petrol: int, electric: int) -> None:
        """
        Initializes the FuelStation object and declared the default slots for
        all types of vehicles (diesel, petrol, electric).
        """
        self.empty_slots = {
            "diesel": {
                'total_slots': diesel,
                'remaining': diesel
            },
            "petrol": {
                'total_slots': petrol,
                'remaining': petrol
            },
            "electric": {
                'total_slots': electric,
                'remaining': electric
            },
        }

    def fuel_vehicle(self: Self, fuel_type: str) -> bool:
        """ Check whether fuel slot is empty

        Args:
            fuel_type: Type of fuel string (diesel, petrol, electric).

        Returns:
            bool: If there is empty slot then True otherwise False.
        """

        # Check if there is any empty slot of current fuel type
        fuel_type: str = fuel_type.strip().lower()
        if fuel_type in self.empty_slots and self.empty_slots[fuel_type]['remaining']:
            self.empty_slots[fuel_type]['remaining'] -= 1
            return True
        return False

    def open_fuel_slot(self: Self, fuel_type: str) -> bool:
        """ Check whether fuel slot is full then empty 1 slot

        Args:
            fuel_type: Type of fuel string (diesel, petrol, electric).

        Returns:
            bool: If we can empty any slot then True otherwise False.
        """
        fuel_type: str = fuel_type.strip().lower()
        if fuel_type in self.empty_slots and \
            self.empty_slots[fuel_type]['remaining'] < self.empty_slots[fuel_type]['total_slots']:
            self.empty_slots[fuel_type]['remaining'] += 1
            return True
        return False


fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.fuel_vehicle("petrol"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.fuel_vehicle("electric"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("diesel"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("electric"))
print(fuel_station.open_fuel_slot("electric"))
