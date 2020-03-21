"""
Type hint
 1. Ayuda a auto-documentar el código
 2. Ayuda a alas herramientas de calidad del código y editores
 3. Ayuda a pensar mejor tu código
"""

from typing import List

# hello
# this is working
def square(elements: List[int]) -> List[int]:
    """
    Eleva todos los elementos al cuadrado
    """
    return [x*x for x in elements]

square([1, 2, 3, 4])

# square([1, 'a', 'b'])
