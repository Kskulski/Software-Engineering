from enum import Enum
<<<<<<< HEAD
from assignment5.subject import Subject
=======
from subject.py import Subject

>>>>>>> 8c64d1c319c2e805cd0f21895f34bb214f5f6baa

class State(Enum):
    START = 0
    COLLECT_NUM1 = 1
    COLLECT_NUM2 = 2

<<<<<<< HEAD
=======

>>>>>>> 8c64d1c319c2e805cd0f21895f34bb214f5f6baa
class CalculatorModel(Subject):
    def __init__(self):
        self._N1 = '0'
        self._N2 = '0'
        self._operation = None
        self._state = State.START
        Subject.attach(self)

    def attach(self, observer: Observer) -> None:
        self.append(observer)
        pass

    def _evaluate(self):
        return eval('{} {} {}'.format(int(self._N1), self._operation, int(self._N2)))


    def handle_digit(self, d: str):
        if self._state == State.START:
            self._state = State.COLLECT_NUM1
            self._N1 = d

        elif self._state == State.COLLECT_NUM1:
            self._N1 += d

        elif self._state == State.COLLECT_NUM2:
            self._N2 += d

    def handle_operation(self, operation: str):
        if operation not in '+-*/':
            raise ValueError()

        if self._state == State.COLLECT_NUM1:
            self._state = State.COLLECT_NUM2
            self._operation = operation

        elif self._state == State.COLLECT_NUM2:
            # order of following two statements is critical, maybe should refactor to eliminate fragility

            self._N1 = str(self._evaluate())
            self._operation = operation
            self._N2 = '0'

    def handle_CE(self):
        if self._state == State.COLLECT_NUM1:
            self._N1 = '0'

        elif self._state == State.COLLECT_NUM2:
            self._N2 = '0'

    def get_result(self):
        return int(self._N1)

    def get_expr(self):
        return '{} {} {}'.format(self._N1.lstrip('0'), self._operation, self._N2.lstrip('0'))

    def handle_equal(self):
        if self._state == State.COLLECT_NUM2:
            self._N1 = self._evaluate()
            self._state == State.COLLECT_NUM1
            self._N2 = 0

if __name__ == '__main__':
    calculator = CalculatorModel()

    calculator.handle_digit('1')
    calculator.handle_digit('2')
    calculator.handle_operation('+')
    calculator.handle_digit('2')
    calculator.handle_digit('0')
    calculator.handle_operation('*')
    calculator.handle_digit('2')
    calculator.handle_CE()
    calculator.handle_digit('3')
    print(calculator.get_expr())
    calculator.handle_operation('/')
    print(calculator.get_result())
