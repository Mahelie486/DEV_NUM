import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World

from src.laplace_equation_solver import LaplaceEquationSolver

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

    x_expression_diagonal = x
    y_expression_diagonal = y
    diagonal_eqs = (x_expression_diagonal, y_expression_diagonal)

    wires = [
        VoltageSource((40, 10), (60, 10), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((60, 10), (80, 20), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((80, 20), (90, 40), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((90, 40), (90, 60), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((90, 60), (80, 80), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((80, 80), (60, 90), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((60, 90), (40, 90), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((40, 90), (20, 80), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((20, 80), (10, 60), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((10, 60), (10, 40), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((10, 40), (20, 20), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((20, 20), (40, 10), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
    ]
    ground_position = (40, 10)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    
    world.show_circuit(
        {0: (40, 10), 1: (60, 10), 2: (80, 20), 3: (90, 40), 4: (90, 60), 5: (80, 80), 6: (60, 90), 7: (40, 90), 8: (
        20, 80), 9: (10, 60), 10: (10, 40), 11: (20, 20)}
    )
    world.compute()
    world.show_all()
    

    a, b = circuit.get_voltage_and_current_fields(WORLD_SHAPE, [60,60], [101, 101])
    # print(a)  # a est le voltage en tout point = aussi un scalar
    #laplace = LaplaceEquationSolver()
    #tests =  laplace._solve_in_cartesian_coordinate(a, 1, 1)  # Permet de checker ce qui est retourné par Laplace pour ce circuit
    #print(tests)
