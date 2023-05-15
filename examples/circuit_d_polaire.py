import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World

import numpy as np


if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    polar_variables = Symbol("r"), Symbol("theta")
    r, theta = polar_variables

    r_expression_vertical = 0 * r
    theta_expression_vertical = theta
    vertical_eqs = (r_expression_vertical, theta_expression_vertical)

    r_expression_horizontal = r
    theta_expression_horizontal = 0 * theta
    horizontal_eqs = (r_expression_horizontal, theta_expression_horizontal)

    r_expression_diagonal = r
    theta_expression_diagonal = theta
    diagonal_eqs = (r_expression_diagonal, theta_expression_diagonal)

    theta_1 = np.pi / 24
    theta_2 = np.pi / 3

    wires = [
        Wire((20, theta_1), (80, theta_1), horizontal_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((80, theta_1), (80, np.pi/7), vertical_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((80, np.pi/7), (80, 2*np.pi/9), vertical_eqs, polar_variables, HIGH_WIRE_RESISTANCE),
        Wire((80, 2*np.pi/9), (80, theta_2), vertical_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((80, theta_2), (20, theta_2), horizontal_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((20, theta_2), (20, 2*np.pi/9), vertical_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((20, 2*np.pi/9), (20, np.pi/7), vertical_eqs, polar_variables, BATTERY_VOLTAGE),
        Wire((20, np.pi/7), (20, theta_1), vertical_eqs, polar_variables, LOW_WIRE_RESISTANCE),
    ]
    ground_position = (20, np.pi/7)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.POLAR, shape=WORLD_SHAPE)

    world.show_circuit(
        {0: (20, theta_1),
        1: (80, theta_1),
        2: (80, np.pi/7),
        3: (80, 2*np.pi/9), 
        4: (80, theta_2), 
        5: (20, theta_2), 
        6: (20, 2*np.pi/9),
        7: (20, np.pi/7)}
    )
    world.compute()
    world.show_all()

    
    #Biot = BiotSavartEquationSolver()
    # print(len(b[0]))
    # print(b)
    #Magn =  Biot._solve_in_polar_coordinate(b, 1, 1)  # Permet de checker ce qui est retourné par Laplace pour ce circuit
    #print(Magn)
    