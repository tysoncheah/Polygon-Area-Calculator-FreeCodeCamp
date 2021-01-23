# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main

rect = shape_calculator.Rectangle(3, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_diagonal())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(3)
print(sq.get_diagonal())
print(sq)

print(rect.get_amount_inside(sq))

# Run unit tests automatically
main(module='test_module', exit=False)