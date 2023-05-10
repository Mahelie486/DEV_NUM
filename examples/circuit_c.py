import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from math import cos, sin, sqrt

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World

# Essai paramètres cartésien pour cercle
if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    # dpl le long du rayon = dpl selon eqn d'une ligne
    expression_dpl_x = x
    expression_dpl_y = y*x  # bullshit maybe mais but est d'avoir eqn d'une ligne avec taux de variation
    rayon_eqn = (expression_dpl_x, expression_dpl_y)

    expression_dpl_x = x
    expression_dpl_y = sqrt(sqrt(x**2 + y**2) - x**2)
    theta_eqn = (expression_dpl_x, expression_dpl_y)

# on trace juste un cercle pour les tests => apres update de nouvelles eqns pas sur ça marche
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
