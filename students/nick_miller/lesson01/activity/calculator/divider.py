""" This module provides a division operator."""

from .exceptions import ZeroDivision


class Divider:

    @staticmethod
    def calc(operand_1, operand_2):
        try:
            return operand_1 / operand_2
        except ZeroDivisionError:
            raise ZeroDivision
