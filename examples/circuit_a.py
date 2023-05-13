import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World

from src.laplace_equation_solver import LaplaceEquationSolver

if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 4.0
    HIGH_WIRE_RESISTANCE = 2.0  # Probablement carrément une résistance -AM
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
    """
    world.show_circuit(
        {0: (0, 0), 1: (0, 5), 2: (3, 5), 3: (4, 5), 4: (5, 5), 5: (5, 2), 6: (5, 1), 7: (5, 0), 8: (2, 0), 9: (1, 0)}
    )
    world.compute()
    world.show_all()
    """
    a, b = circuit.get_voltage_and_current_fields(WORLD_SHAPE, [60,60], [101, 101])
    # print(a)  # a est le voltage en tout point = aussi un scalar
    laplace = LaplaceEquationSolver()
    tests =  laplace._solve_in_cartesian_coordinate(a, 1, 1)  # Permet de checker ce qui est retourné par Laplace pour ce circuit
    print(tests)