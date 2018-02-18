BUTTONS = '1234567890()-=*/C'

class Calculator(object):
    def __init__(self):
        self._expression = ''

    def push(self, button):
        if button not in BUTTONS:
            raise Exception('invalid input')
        elif button == 'C':
            self._expression = ''
        elif button == '=':
            self._expression = self._calculate()
        else:
            self._expression += button

    def _calculate(self):
        try:
            return enval(self._expression)
        except ZeroDivisionError:
            pass

    def result_should_be(self, expected_result):
        #assert to do
        pass