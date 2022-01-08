from numpy import matrix, dot
from scipy.linalg import solve
from itertools import chain
from typing import List


# generator matrix  the lattice you want to analyze
# possible array cases (0,2(r+1)), (r+1,r+1)), (2r+ 1,1),(r,r+2) for r in N
lattice_matrix = matrix('0 6; 3 3')

# possible isometries coordinates in 2-dimensional lattices
coordinates_isometry_matrix = [
    '1 0; 0 1', '-1 0; 0 -1', '-1 0; 0 1',
    '-1 0; 0 1', '1 0; 0 -1', '0 1; 1 0',
    '0 -1; -1 0', '0 -1; 1 0', '0 1; -1 0'
]

# isometries in matrix form
all_isometry_matrix = [
    matrix(isometry)
    for isometry in coordinates_isometry_matrix
]

# all new lattices generated from isometries
def list_newlattices(
    lattice_matrix: matrix, all_isometry_matrix: List[matrix]
) -> List[matrix]:

    return [
        dot(lattice_matrix, matrix)
        for matrix in all_isometry_matrix
    ]


# checks whether the lines of matrix 2 can be written as integer linear combinations
# of the lines of matrix 1
# here we solve all linear systems and then check if there is one that is not integer
def check_interger_solutions(
    first_matrix: matrix, second_matrix: matrix
) -> bool:

    _system_solutions = [
        solve(first_matrix, row.transpose()).tolist()
        for row in second_matrix
    ]

    _all_elements_solutions = list(chain(*_system_solutions))
    linear_system_solutions = list(chain(*_all_elements_solutions))

    for number in linear_system_solutions:
        if number // 1 != number:
            return False

    return True


# check if the lattices are equal from the generating matrix
def compare_lattice(first_matrix: matrix, second_matrix: matrix) -> bool:
    return (
        True if (
            check_interger_solutions(first_matrix, second_matrix)
            and check_interger_solutions(second_matrix, first_matrix)
        )
        else False
    )


# shows which lattices are the same as the initial and which are not
def show_equals(lattice_matrix: matrix, all_isometry_matrix: List[matrix]) -> None:

    all_lattices = list_newlattices(lattice_matrix, all_isometry_matrix)
    pattern_message = f'O Reticulado gerado pela isometria (phi)'

    for index, lattice in enumerate(all_lattices):
        if compare_lattice(lattice_matrix.transpose(), lattice):
            print(
                f'{pattern_message} {index} {lattice.tolist()} ' 
                f'é igual ao original {lattice_matrix.tolist()}.'
            )
        else:
            print(
                f'{pattern_message} {index} {lattice.tolist()} '
                f'é diferente do original {lattice_matrix.tolist()}.'
            )

    return None


show_equals(lattice_matrix, all_isometry_matrix)
