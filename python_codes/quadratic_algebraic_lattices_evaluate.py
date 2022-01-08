import cmath as cm

from numpy import sqrt, multiply, conjugate
from numpy import array, imag, real, dot, matrix
from numpy.linalg import det

from typing import List


def interger_ring_basis(algebraic_number: float) -> List[float]:

    def _interger_ring_basis(number: float) -> List[float]:
        return [1, number]

    if algebraic_number % 4 in [2, 3]:
        return _interger_ring_basis(algebraic_number)

    sqrt_algebraic_number = sqrt(algebraic_number)
    primitive_element = (1+sqrt_algebraic_number)/2

    return _interger_ring_basis(primitive_element)


def interger_principal_ideal_basis(
    coeficient: float,
    interger_ring_basis: List[float]
) -> List[float]:
    return multiply(interger_ring_basis, coeficient)


def real_lattice_quadratic_basis(
    algebraic_number: float, coeficient: float
) -> List[float]:

    def _create_real_lattice(
        coeficient: float, number1: float, number2: float
    ) -> List[float]:
        return multiply([[1, 1], [number1, number2]], coeficient)

    sqrt_algebraic_number = sqrt(algebraic_number)

    if algebraic_number % 4 in [2, 3]:
        return _create_real_lattice(
            coeficient, 
            sqrt_algebraic_number, 
            -sqrt_algebraic_number
        )

    primitive_element = (1+sqrt_algebraic_number)/2
    conjugate_real_number = (1-sqrt_algebraic_number)/2

    return _create_real_lattice(coeficient, primitive_element, conjugate_real_number)


def imaginary_lattice_quadratic_basis(
    algebraic_number: float, coeficient: complex
) -> List[float]:

    def _create_imaginary_lattice(
        coeficient: float, number1: float, number2: float
    ) -> List[float]:

        return array([
            [real(coeficient), imag(conjugate(coeficient))],
            [real(coeficient*number1), imag(coeficient*number2)]
        ])

    sqrt_algebraic_number = cm.sqrt(algebraic_number)
    if algebraic_number % 4 in [2, 3]:
        return _create_imaginary_lattice(
            coeficient, sqrt_algebraic_number, -sqrt_algebraic_number
        )

    primitive_element = (1+sqrt_algebraic_number)/2
    conjugate_imaginary_number = (1-sqrt_algebraic_number)/2

    return _create_imaginary_lattice(
        coeficient, 
        primitive_element, 
        conjugate_imaginary_number
    )


def evaluate_lattice_volume(matrix: matrix) -> float:
    return sqrt(det(matrix))
