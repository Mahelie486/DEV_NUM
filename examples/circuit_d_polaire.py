import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World

from src.laplace_equation_solver import LaplaceEquationSolver

from src.biot_savart_equation_solver import BiotSavartEquationSolver

from numpy import pi

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

    wires = [
        Wire((20, pi / 24), (80, pi / 24), horizontal_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((80, pi / 24), (80, pi/7), vertical_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((80, pi/7), (80, 2*pi/9), vertical_eqs, polar_variables, HIGH_WIRE_RESISTANCE),
        Wire((80, 2*pi/9), (80, pi / 3), vertical_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((80, pi / 3), (20, pi / 3), horizontal_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((20, pi / 3), (20, 2*pi/9), vertical_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((20, 2*pi/9), (20, pi/7), vertical_eqs, polar_variables, BATTERY_VOLTAGE),
        Wire((20, pi/7), (20, pi / 24), vertical_eqs, polar_variables, LOW_WIRE_RESISTANCE),
    ]
    ground_position = (20, pi/7)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.POLAR, shape=WORLD_SHAPE)
    
    world.show_circuit(
        {0: (20, pi / 24),
        1: (80, pi / 24),
        2: (80, pi/7),
        3: (80, 2*pi/9), 
        4: (80, pi / 3), 
        5: (20, pi / 3), 
        6: (20, 2*pi/9),
        7: (20, pi/7)}
    )
    world.compute()
    world.show_all()
