import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World

from src.laplace_equation_solver import LaplaceEquationSolver

from src.biot_savart_equation_solver import BiotSavartEquationSolver

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
        Wire((0, 0), (0, 100), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((0, 100), (60, 100), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((60, 100), (80, 100), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((80, 100), (100, 100), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((100, 100), (100, 40), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((100, 40), (100, 20), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((100, 20), (100, 0), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((100, 0), (40, 0), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((40, 0), (20, 0), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((20, 0), (0, 0), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)
    ]
    ground_position = (20, 0)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)

    world.show_circuit(
        {0: (0, 0), 1: (0, 100), 2: (60, 100), 3: (80, 100), 4: (100, 100), 5: (100, 40), 6: (100, 20), 7: (100, 0), 8: (40, 0), 9: (20, 0)}
    )
    world.compute()
    world.show_all()
    """"
    a, b = circuit.get_voltage_and_current_fields(WORLD_SHAPE, [0,0], [6, 6]) #quand c'ai fais X20 je l'ai pas fais ici
    # print(a)  # a est le voltage en tout point = aussi un scalar

    laplace = LaplaceEquationSolver()
    tests =  laplace._solve_in_cartesian_coordinate(a, 1, 1)  # Permet de checker ce qui est retourné par Laplace pour ce circuit
    print(tests)
    """
    #Biot = BiotSavartEquationSolver()
    #Magn =  Biot._solve_in_cartesian_coordinate(b, 1, 1)  # Permet de checker ce qui est retourné par Laplace pour ce circuit
    #print(Magn)
