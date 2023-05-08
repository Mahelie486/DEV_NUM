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
        Wire((0, 0), (0, 5), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((0, 5), (3, 5), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((3, 5), (4, 5), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((4, 5), (5, 5), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((5, 5), (5, 2), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((5, 2), (5, 1), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((5, 1), (5, 0), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((5, 0), (2, 0), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((2, 0), (1, 0), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((1, 0), (0, 0), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)
    ]
    ground_position = (1, 0)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (0, 0), 1: (0, 5), 2: (3, 5), 3: (5, 5), 4: (5, 2), 5: (5, 1), 6: (5, 0), 7: (2, 0), 8: (1, 0)}
    )
    world.compute()
    world.show_all()