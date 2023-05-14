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
        Wire((10, 10), (10, 90), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((10, 90), (58, 90), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((58, 90), (74, 90), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((74, 90), (90, 90), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((90, 90), (90, 42), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((90, 42), (90, 26), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((90, 26), (90, 10), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((90, 10), (42, 10), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((42, 10), (26, 10), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((26, 10), (10, 10), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)
    ]
    ground_position = (26, 10)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    
    world.show_circuit(
        {0: (10, 10), 1: (10, 90), 2: (58, 90), 3: (74, 90), 4: (90, 90), 5: (90, 42), 6: (90, 26), 7: (90, 10), 8: (42, 10), 9: (26, 10)}
    )
    world.compute()
    world.show_all()
