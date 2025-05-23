import pycuber as pc

def solve_white_cross(scramble):
    cube = pc.Cube()
    formula = pc.Formula(scramble)
    cube(formula)

    moves = []

    def apply(m):
        nonlocal cube, moves
        cube(pc.Formula(m))
        moves.append(m)

    def move_white_edge_to_down(face_name, pos):
        color = str(cube.get_face(face_name)[pos[0]][pos[1]])
        if color != 'W':
            return

        if face_name == 'U':
            if pos == (0, 1): apply("U'"); apply("L'"); apply("D"); apply("L")
            elif pos == (1, 0): apply("U"); apply("B'"); apply("D"); apply("B")
            elif pos == (1, 2): apply("U'"); apply("F'"); apply("D"); apply("F")
            elif pos == (2, 1): apply("U"); apply("R'"); apply("D"); apply("R")
        elif face_name == 'F':
            if pos == (0, 1): apply("F'"); apply("U'"); apply("R'"); apply("U"); apply("R"); apply("F")
            elif pos == (1, 0): apply("L'"); apply("U"); apply("L")
            elif pos == (1, 2): apply("R"); apply("U'"); apply("R'")
            elif pos == (2, 1): apply("F"); apply("F")
        elif face_name == 'R':
            if pos == (0, 1): apply("R'"); apply("U'"); apply("B'"); apply("U"); apply("B"); apply("R")
            elif pos == (1, 0): apply("F'"); apply("U"); apply("F")
            elif pos == (1, 2): apply("B"); apply("U'"); apply("B'")
            elif pos == (2, 1): apply("R"); apply("R")
        elif face_name == 'L':
            if pos == (0, 1): apply("L'"); apply("U'"); apply("F'"); apply("U"); apply("F"); apply("L")
            elif pos == (1, 0): apply("B'"); apply("U"); apply("B")
            elif pos == (1, 2): apply("F"); apply("U'"); apply("F'")
            elif pos == (2, 1): apply("L"); apply("L")
        elif face_name == 'B':
            if pos == (0, 1): apply("B'"); apply("U'"); apply("L'"); apply("U"); apply("L"); apply("B")
            elif pos == (1, 0): apply("R'"); apply("U"); apply("R")
            elif pos == (1, 2): apply("L"); apply("U'"); apply("L'")
            elif pos == (2, 1): apply("B"); apply("B")

    for face in ['U', 'F', 'R', 'L', 'B']:
        for pos in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            move_white_edge_to_down(face, pos)

    return ' '.join(moves)
