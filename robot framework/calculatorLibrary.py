from robot.api.deco import keyword
import Calculator from calculator

class CalaculatorLibrary(object):
    def __init__(self):
        self.expression = ''
        self.calculator = Calculator

    @keyword('Push button ${button}')
    def push(self, button):
        self.expression += button
        return self.expression

    @keyword('Result should be')
    def result(self, expected_result):
        pass