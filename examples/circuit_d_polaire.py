import env_examples

#from src import Circuit, Current, Wire, World
#import time
#!!en polaire aussi celui-ci!!
#polaire + cartésien
import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from math import cos, sin, pi, sqrt, asin

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


# Essai paramètres polaire pour cercle
if __name__ == "__main__":
    WORLD_SHAPE = (100, 2*pi)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    polar_variables = Symbol("r"), Symbol("theta")
    r, theta = polar_variables

    # Eqn pour dpl rayon
    expression_dpl_rayon = r
    expression_dpl_theta = theta*0
    rayon_eqn = (expression_dpl_rayon, expression_dpl_theta)

    # Eqn dpl circum
    expression_dpl_rayon = 0 * r
    expression_dpl_theta = theta
    theta_eqn = (expression_dpl_rayon, expression_dpl_theta)

# on trace juste un cercle pour les tests
    wires = [
        Wire((2, pi/2), (2, pi), theta_eqn, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((2, pi), (1, pi), rayon_eqn, polar_variables, HIGH_WIRE_RESISTANCE),
        Wire((1, pi), (1, pi/2), theta_eqn, polar_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((1, pi/2), (2, pi/2), rayon_eqn, polar_variables, BATTERY_VOLTAGE)
    ]
    ground_position = (2, pi/2)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.POLAR, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (2, pi/2), 1: (2, pi), 2: (1, pi), 3: (1, pi/2)}
    )
    world.compute()
    world.show_all()