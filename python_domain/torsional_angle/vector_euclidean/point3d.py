class Point_3d(object):
    """
    @parameters: one list of 3 coordinates

    returns a tuple in form of (x, y, z) coordinates

    @ToDo: add incorrect x,y,z input handling
    """
    def __init__(self, l):
        # set point's coordinates
        # l is an iterable (list or )
        self.x, self.y, self.z = map(float, l)
        self.coords = (self.x, self.y, self.z)

    def __add__(self, no):
        return None

    def __sub__(self, no):
        # substracting point substracts CORRESPONDING coordinates' values
        return [m_i - n_i for m_i, n_i in zip(self.coords, no.coords)]
