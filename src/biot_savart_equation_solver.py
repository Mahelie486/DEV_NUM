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
    # Version préliminaire manque méthode pour aller chercher distance du point avec el.courant
    def _solve_in_cartesian_coordinate(
    self,
    electric_current: VectorField,
    delta_x: float,
     delta_y: float
    ) -> VectorField:
        # extrait dimensions de matrice
        position, current = [], []
        dim_x, dim_y, dim_z = electric_current.shape
        magnetic_field = np.zeros((dim_x, dim_y, dim_z))
        return magnetic_field
        """"
        # remplace intégration en couvrant espaces en bond de delta
        for i in range(0, dim_x, delta_x):
            for j in range(0, dim_y, delta_y):
                current_x, current_y, current_z = electric_current[i, j][0], electric_current[i, j][1], electric_current[i, j][2]
                if current_x != 0 or current_y != 0 or current_z != 0:
                    champ = np.zeros((dim_x, dim_y, dim_z))  # Maybe not useful for this new technique
                    # am
                    position.append((i, j, 0))
                    current.append(i)
                if (i, j, 0) not in position:  # 0 if in pos et initialized with 0s
                    # distance (from all current elements?)
                    r = np.array(['something', 'something'])  # Besoin de faire diff the dist avec chaque élément de courant
                    r_norm = (np.linalg.norm(r, axis=1))
                    # portion perpendiculaire(champs perpendiculaire au courant)
                    cross_part = np.cross(current, r)
                    # Calcul biot savard: sum de tout élément champs rpl int.
                    magnetic_field[i, j] = [0, 0, np.sum(mu_0 * cross_part[:,2]/(4*pi*r_norm*3))]
        return VectorField(magnetic_field)
        """
        """"
                    for k in range(0, dim_x, delta_y):
                        for l in range(0, dim_y, delta_y):
                            if electric_current[k, l][0] == 0 or electric_current[k, l][1] == 0 or electric_current[k, l][2] == 0:
                                rx = i-k
                                ry = j-l
                                norme_r = math.sqrt(rx**2 + ry**2)
                                vecteur_r = np.array([rx, ry, 0])
                                I_x_r = np.cross(electric_current[i, j], vecteur_r)
        return VectorField(magnetic_field)
        """

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
        # On convertit les coordonnées polaires et les deltas en catésien
        # extrait dimensions de matrice
        position, current = [], []
        dim_r, dim_thet = electric_current.shape
        magnetic_field = np.zeros((dim_r, dim_thet))
        # remplace intégration en couvrant espaces en bond de delta
        for i in range(0, dim_r, delta_r):
            for j in range(0, dim_thet, delta_theta):
                current_r, current_theta = electric_current[i, j][0], electric_current[i, j][1]
                # current_x = electric_current[i, j][0]*math.cos(electric_current[i, j][1])
                # current_y = electric_current[i, j][0]*math.sin(electric_current[i, j][1])
                if current_r != 0 or current_theta != 0:
                    position.append((i, j))
                    current.append(i)
                if (i, j) not in position:  # 0 if in pos et initialized with 0s
                    # distance (from all current elements?)
                    r = np.array(['something en cartésien', 'something_cartésien'])  # Besoin de faire diff the dist avec chaque élément de courant
                    r_norm = (np.linalg.norm(r, axis=1))
                    # portion perpendiculaire(champs perpendiculaire au courant)
                    cross_part = np.cross(current, r)
                    # Calcul biot savard: sum de tout élément champs rpl int.
                    magnetic_field[i, j] = [0, 0, np.sum(mu_0 * cross_part[:,2]/(4*pi*r_norm*3))]
        return VectorField(magnetic_field)
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
