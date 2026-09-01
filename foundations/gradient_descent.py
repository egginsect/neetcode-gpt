import sys
class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        minimizer=init
        for _ in range(iterations):
            minimizer-=(2*minimizer)*learning_rate
        return round(minimizer, 5)

    