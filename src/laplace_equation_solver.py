import numpy as np

from src.coordinate_and_position import CoordinateSystem
from src.fields import ScalarField

from math import pi


class LaplaceEquationSolver:
    """
    A Laplace equation solver used to compute the resultant potential field P in 2D-space generated by a constant
    voltage field V (for example due to wires).
    """

    def __init__(self, nb_iterations: int = 1000):
        """
        Laplace solver constructor. Used to define the number of iterations for the relaxation method.

        Parameters
        ----------
        nb_iterations : int
            Number of iterations performed to obtain the potential by the relaxation method (default = 1000).
        """
        self.nb_iterations = nb_iterations

    def _solve_in_cartesian_coordinate(
            self,
            constant_voltage: ScalarField,
            delta_x: float,
            delta_y: float
    ) -> ScalarField:
        """
        Solve the Laplace equation to compute the resultant potential field P in 2D-space.

        Parameters
        ----------
        constant_voltage : ScalarField
            A scalar field V : ℝ² → ℝ ; (x, y) → V(x, y), where V(x, y) is the electrical components' voltage at a
            given point (x, y) in space.
        delta_x : float
            Small discretization of the x-axis.
        delta_y : float
            Small discretization of the y-axis.

        Returns
        -------
        potential : ScalarField
            A scalar field P : ℝ² → ℝ ; (x, y) → P(x, y), where P(x, y) is the electric potential at a given point
            (x, y) in space. The difference between P and V is that P gives the potential in the whole world, i.e inside
            the electrical components and in the empty space between the electrical components, while the field V
            always gives V(x, y) = 0 if (x, y) is not a point belonging to an electrical component of the circuit.
        """
        # nb. Les delta sont déjà considérés pour tte les valeurs contenues dans constant_voltage
        
        # Crée une deuxième matrice de même taille avec les mêmes valeurs pour éviter de modifier la matrice initiale
        potential = constant_voltage.copy()

        # On itère pour raffiner les valeurs de potentiels à chaque points selon les points qui l'entoure
        for _ in range(self.nb_iterations):

            # Ajouter des 0 sur le contour permet d'avoir des matrices toujours de bonne tailles pour le calcul
            potential = np.pad(potential,[(1, 1), (1, 1)], mode='constant')

            # Equation obtenue avec discrétisation de Laplace avec des matrices pour tous les points
            potential = 1/4 * (potential[:-2, 1:-1] + potential[2:, 1:-1] + potential[1:-1, :-2] + potential[1:-1, 2:])

            # On reporte le tout dans la matrice initiale pour recommencer la boucle et étendre les valeurs
            np.copyto(potential, constant_voltage, where=constant_voltage != 0)

        return ScalarField(potential)

    def _solve_in_polar_coordinate(
            self,
            constant_voltage: ScalarField,
            delta_r: float,
            delta_theta: float
    ) -> ScalarField:
        """
        Solve the Laplace equation to compute the resultant potential field P in 2D-space.

        Parameters
        ----------
        constant_voltage : ScalarField
            A scalar field V : ℝ² → ℝ ; (r, θ) → V(r, θ), where V(r, θ) is the electrical components' voltage at a
            given point (r, θ) in space.
        delta_r : float
            Small discretization of the r-axis.
        delta_theta : float
            Small discretization of the θ-axis.

        Returns
        -------
        potential : ScalarField
            A scalar field P : ℝ² → ℝ ; (r, θ) → P(r, θ), where P(r, θ) is the electric potential at a given point
            (r, θ) in space. The difference between P and V is that P gives the potential in the whole world, i.e inside
            the electrical components and in the empty space between the electrical components, while the field V
            always gives V(r, θ) = 0 if (r, θ) is not a point belonging to an electrical component of the circuit.
        """
        # nb. Les delta sont déjà considérés pour tte les valeurs contenues dans constant_voltage
        
        # Crée une deuxième matrice de même taille avec les mêmes valeurs pour éviter de modifier la matrice initiale       
        potential = constant_voltage.copy()

        # Nécessaire pour déterminer les indices et au bout du compte le r
        pot_modif = np.copy(constant_voltage)
        N, M = constant_voltage.shape
        
        # Déterminer les constantes pour l'équation trouvé dans la discrétisation
        r = (np.indices(pot_modif.shape)[0])*delta_r
        A_1 = ((r**2 * delta_theta**2)/((2* r**2 * delta_theta**2) + (2 * delta_r**2)))
        A_2 = ((r * delta_r * delta_theta**2)/ ((r**2 * delta_theta**2) + delta_r**2))[1:-1, 1:-1]
        A_3 = (delta_r**2 / (2*r*delta_theta**2) + 2*delta_r**2)[1:-1, 1:-1]

        # On itère pour raffiner les valeurs de potentiels à chaque points selon les points qui l'entoure
        for _ in range(self.nb_iterations):

            # Ajouter des 0 sur le contour permet d'avoir des matrices toujours de bonne tailles pour le calcul
            potential = np.pad(potential,[(1, 1), (1, 1)], mode='constant')

            # Equation obtenue avec discrétisation de Laplace avec des matrices pour tous les points
            potential = (potential[:-2, 1:-1] + potential[2:, 1:-1]) * A_1
            + (potential[:-2, 1:-1] - potential[2:, 1:-1]) *  A_2
            + (potential[1:-1, :-2]+ potential[1:-1, 2:]) * A_3

            # On reporte le tout dans la matrice initiale pour recommencer la boucle et étendre les valeurs
            np.copyto(potential, constant_voltage, where=constant_voltage != 0)
        return ScalarField(potential)


    def solve(
            self,
            constant_voltage: ScalarField,
            coordinate_system: CoordinateSystem,
            delta_q1: float,
            delta_q2: float
    ) -> ScalarField:
        """
        Solve the Laplace equation to compute the resultant potential field P in 2D-space.

        Parameters
        ----------
        constant_voltage : ScalarField
            A scalar field V : ℝ² → ℝ representing a constant voltage field.
        coordinate_system : CoordinateSystem
            Coordinate system.
        delta_q1 : float
            Small discretization of the first axis.
        delta_q2 : float
            Small discretization of the second axis.

        Returns
        -------
        potential : ScalarField
            A scalar field P : ℝ² → ℝ  representing the potential in the 2D world.
        """
        if coordinate_system == CoordinateSystem.CARTESIAN:
            return self._solve_in_cartesian_coordinate(constant_voltage, delta_q1, delta_q2)
        elif coordinate_system == CoordinateSystem.POLAR:
            return self._solve_in_polar_coordinate(constant_voltage, delta_q1, delta_q2)
        else:
            raise NotImplementedError("Only the cartesian and polar coordinates system are implemented.")
