V = [0, 0, 0]
B = [0, 0, 0]

def initialisation_contour ( V0 ):
    """ Initialise les bords de la grille a la valeur V0 """
    V [: ,0] = V0
    V [: , -1] = V0
    V [0 ,:] = V0
    V [ -1 ,:] = V0
    B [: ,0] = True
    B [: , -1] = True
    B [0 ,:] = True
    B [ -1 ,:] = True
