import numpy as np
import math
from scipy.constants import mu_0, pi

from src.coordinate_and_position import CoordinateSystem
from src.fields import VectorField


class BiotSavartEquationSolver:
    """
    A Biot–Savart law solver used to compute the resultant magnetic field B in 2D-space generated by a constant current
    field I (for example due to wires).
    """

    def _solve_in_cartesian_coordinate(
            self,
            electric_current: VectorField,
            delta_x: float,
            delta_y: float
    ) -> VectorField:
       """
        Solve the Biot–Savart equation to compute the magnetic field given an electric current field.

        Parameters
        ----------
        electric_current : VectorField
            A vector field I : ℝ² → ℝ³ ; (x, y) → (I_x(x, y), I_y(x, y), I_z(x, y)), where I_x(x, y), I_y(x, y) and
            I_z(x, y) are the 3 components of the electric current vector at a given point (x, y) in space. Note that
            I_z = 0 is always True in our 2D world.
        delta_x : float
            Small discretization of the x-axis.
        delta_y : float
            Small discretization of the y-axis.

        Returns
        -------
        magnetic_field : VectorField
            A vector field B : ℝ² → ℝ³ ; (x, y) → (B_x(x, y), B_y(x, y), B_z(x, y)), where B_x(x, y), B_y(x, y) and
            B_z(x, y) are the 3 components of the magnetic vector at a given point (x, y) in space. Note that
            B_x = B_y = 0 is always True in our 2D world.
        """

        x, y, z = electric_current.shape
        champ_total = np.zeros((x, y, z))

        for i in range(0, x, delta_x):
            for j in range(0, x, delta_y):
                if electric_current[i, j][0] != 0 or electric_current[i, j][1] != 0 or electric_current[i, j][2] != 0:
                    champ = np.zeros((x, y, z))
                    for k in range(0, x, delta_y):
                        for l in range(0, y, delta_y):
                            if electric_current[k, l][0] == 0 or electric_current[k, l][1] == 0 or electric_current[k, l][2] == 0:
                                rx = i-k
                                ry = j-l
                                norme_r = math.sqrt(rx**2 + ry**2)
                                vecteur_r = np.array([rx, ry, 0])
                                I_x_r = np.cross(electric_current[i, j], vecteur_r)
        return VectorField(champ_total)


    def _solve_in_polar_coordinate(
            self,
            electric_current: VectorField,
            delta_r: float,
            delta_theta: float
    ) -> VectorField:
        """
        Solve the Biot–Savart equation to compute the magnetic field given an electric current field.

        Parameters
        ----------
        electric_current : VectorField
            A vector field I : ℝ² → ℝ³ ; (r, θ) → (I_r(r, θ), I_θ(r, θ), I_z(r, θ)), where I_r(r, θ), I_θ(r, θ) and
            I_z(r, θ) are the 3 components of the electric current vector at a given point (r, θ) in space. Note that
            I_z = 0 is always True in our 2D world.
        delta_r : float
            Small discretization of the r-axis.
        delta_theta : float
            Small discretization of the θ-axis.

        Returns
        -------
        magnetic_field : VectorField
            A vector field B : ℝ² → ℝ³ ; (r, θ) → (B_r(r, θ), B_θ(r, θ), B_z(r, θ)), where B_r(r, θ), B_θ(r, θ) and
            B_z(r, θ) are the 3 components of the magnetic vector at a given point (r, θ) in space. Note that
            B_r = B_θ = 0 is always True in our 2D world.
        
        B_r = 0
        B_θ = 0
        magnetic_field = np.array([B_r, B_θ])
        
        for i in range(self.nb_iterations):
            B_r += (mu_0*electric_current / 4*pi) * (delta_r*np.cos(delta_theta))/(delta_r**2 + delta_theta**2)
            B_θ += (mu_0*electric_current / 4*pi) * (np.sin(delta_theta))/(delta_r**2 + delta_theta**2)
        return VectorField(magnetic_field)
        """
        # row = radius
        # colmn = theta
        # introduire conversion entre polar et cartésien et utiliser la même méthode, nb ne pas oublier de considérer les delta en premier pour avoir vrai distance
        position, current = [], []
        for row, j in enumerate(electric_current):
            for colmn, i in enumerate(j):
                if i[0] or i[1] != 0:
                    # vrai position
                    position.append((row*delta_r, colmn*delta_theta, 0))  # même si en polair on ajoute composante e  z pour faciliter écriture champs tto
                    current.append(i)
        magnetic_field_shape = np.shape(electric_current)
        magnetic_field = np.zeros(magnetic_field_shape)


        for row, j in enumerate(magnetic_field):
            for colmn, i in enumerate(j):
                if (row*delta_r, colmn*delta_theta, 0) not in position:  # En terme de vrai position
                    # on devrait soustraire distance entre 2 point, plus facile en cartésien donc convertir and get back?
                    r = np.array([row*delta_r, colmn*delta_theta, 0]) - np.array(position)
                    r_norm = (np.linalg.norm(r, axis=1))
                    cross_part = np.cross(current, r)
                    magnetic_field[row, colmn] = [0, 0, np.sum(mu_0 * cross_part[:,2]/(4*pi*r_norm*3))]

    def solve(
            self,
            electric_current: VectorField,
            coordinate_system: CoordinateSystem,
            delta_q1: float,
            delta_q2: float
    ) -> VectorField:
        """
        Solve the Biot–Savart equation to compute the magnetic field given an electric current field.

        Parameters
        ----------
        electric_current : VectorField
            A vector field I : ℝ² → ℝ³ representing currents in the 2D world.
        coordinate_system : CoordinateSystem
            Coordinate system.
        delta_q1 : float
            Small discretization of the first axis.
        delta_q2 : float
            Small discretization of the second axis.

        Returns
        -------
        magnetic_field : VectorField
            A vector field B : ℝ² → ℝ³ representing the magnetic field in the 2D world.
        """
        if coordinate_system == CoordinateSystem.CARTESIAN:
            return self._solve_in_cartesian_coordinate(electric_current, delta_q1, delta_q2)
        elif coordinate_system == CoordinateSystem.POLAR:
            return self._solve_in_polar_coordinate(electric_current, delta_q1, delta_q2)
        else:
            raise NotImplementedError("Only the cartesian and polar coordinates solvers are implemented.")
