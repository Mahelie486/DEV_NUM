import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World

if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
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
        VoltageSource((0, 0), (0, 2), vertical_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((0, 2), (0, 6), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((0, 6), (6, 6), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((6, 6), (6, 2), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((6, 2), (6, 0), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((6, 0), (0, 0), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)

    ]
    ground_position = (0, 0)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (0, 0), 1: (0, 2), 2: (0, 6), 3: (6, 6), 4: (6, 2), 5: (6, 0)}
    )
    world.compute()
    world.show_all()
