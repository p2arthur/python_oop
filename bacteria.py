class Bacterium:
    def __init__(self, name, shape, flagella, cell_wall, x, y, life_points):
        self.shape = shape
        self.flagella = flagella
        self.cell_wall = cell_wall
        self.name = name
        self.x = x
        self.y = y
        self.life_points = life_points


bacteria_1 = Bacterium('Mohammend', 'Cylindrical', True, True, 1, 2)
bacteria_2 = Bacterium('Carmel', 'Spiral', True, False, 1, 2)
bacteria_3 = Bacterium('Samara', 'Circle', False, False, 6, 12)
