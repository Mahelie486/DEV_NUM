import env_examples

#from src import Circuit, Current, Wire, World
#import time
#!!en polaire aussi celui-ci!!
#polaire + cartésien
import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from math import cos, sin, pi, sqrt, asin

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World

"""
# Essaie en cartésien
if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    # On triche equation pour que paramètres polaire donne dpl cartésien, donc donne vrai x et y
    # En bref ça fait les lignes droites
    dpl_rayon_x= x
    dpl_rayon_y = x*sin(theta)
    dpl_rayon = (dpl_rayon_x, dpl_rayon_y)  # dpl le long rayon, mais fait en cartésien

    dpl_cicum = theta/2*pi
    y_expression_horizontal = 0 * y
    dpl_circum = (x_expression_horizontal, y_expression_horizontal)
"""
# Essai paramètres cartésien pour cercle
if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables
    expression_dpl_rayon = sqrt(x**2 + y**2)
    expression_dpl_theta = 0
    rayon_eqn = (expression_dpl_rayon, expression_dpl_theta)

    expression_dpl_rayon = 0
    expression_dpl_theta = asin(x/(sqrt(x**2 + y**2)))
    theta_eqn = (expression_dpl_rayon, expression_dpl_theta)
# on trace juste un cercle pour les tests
    wires = [
        Wire((2, 2), (3, 1), theta_eqn, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((3, 1), (2, 0), theta_eqn, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((2, 0), (1, 1), theta_eqn, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((1, 1), (2, 2), theta_eqn, cartesian_variables, LOW_WIRE_RESISTANCE)
    ]
    ground_position = (2, 2)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (2, 2), 1: (3, 1), 2: (2, 0), 3: (1, 1)}
    )
    world.compute()
    world.show_all()