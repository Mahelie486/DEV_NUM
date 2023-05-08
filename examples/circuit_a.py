import env_examples

import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World

# import time

# tests/essaies

if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0  # Probablement carrément une résistance -AM
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    x_expression_vertical = 0 * x
    y_expression_vertical = y
    vertical_eqs = (x_expression_vertical, y_expression_vertical)

    x_expression_horizontal = x
    y_expression_horizontal = 0 * y
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    wires = [
        Wire((0, 100), (0, 0), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((80, 100), (0, 100), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((100, 100), (80, 100), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((100, 60), (100, 100), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((100, 40), (100, 60), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((100, 0), (100, 40), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((20, 0), (100, 0), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((0, 0), (20, 0), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE)
    ]
    ground_position = (0, 0)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit()
    world.compute()
    world.show_all()