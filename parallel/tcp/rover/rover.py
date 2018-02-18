"""
Tool to be used during parallelism exercises
    Base class for TurtleRover used in exercise 4)

:author: 'Grzegorz Latuszek (Nokia)'
"""


class Rover(object):
    ALLOWED_DIRECTIONS = ('N', 'E', 'S', 'W')
    MIN_Y = 0
    MAX_Y = 99
    MIN_X = 0
    MAX_X = 99

    def __init__(self, x, y, direction="N"):
        Rover._raise_error_if_coordinates_out_of_boundaries(x, y)
        Rover._raise_error_if_direction_not_allowed(direction)
        self.x = x
        self.y = y
        self.direction = direction

    def move_forward(self):
        shift_by_direction = {'N': (0, 1),
                              'E': (1, 0),
                              'S': (0, -1),
                              'W': (-1, 0)}
        (dx, dy) = shift_by_direction[self.direction]
        self.x += dx
        self.y += dy
        self._correct_coordinates_on_boundry_wrap()

    def move_backward(self):
        self.turn_left()
        self.turn_left()
        self.move_forward()
        self.turn_left()
        self.turn_left()

    def turn_right(self):
        rotation_shift = {'N': 'E',
                          'E': 'S',
                          'S': 'W',
                          'W': 'N'}
        new_direction = rotation_shift[self.direction]
        self.direction = new_direction

    def turn_left(self):
        self.turn_right()
        self.turn_right()
        self.turn_right()

    def interpret_single_command(self, command):

        command_to_function = {'l': self.turn_left,
                               'r': self.turn_right,
                               'f': self.move_forward,
                               'b': self.move_backward}
        try:
            rover_move = command_to_function[command]
            rover_move()
        except KeyError:
            err = WrongCommand(command)
            # raise err  # we just ignore it
            print(err)

    def interpret_commands(self, commands):
        for cmd in commands:
            self.interpret_single_command(cmd)

    @staticmethod
    def _raise_error_if_coordinates_out_of_boundaries(x_coord, y_coord):
        if (x_coord > Rover.MAX_X) or (x_coord < Rover.MIN_X):
            raise BeyondMapError
        if (y_coord > Rover.MAX_Y) or (y_coord < Rover.MIN_Y):
            raise BeyondMapError

    @staticmethod
    def _raise_error_if_direction_not_allowed(direction):
        if direction not in Rover.ALLOWED_DIRECTIONS:
            raise WrongDirection

    def _correct_coordinates_on_boundry_wrap(self):
        if self.y < Rover.MIN_Y:
            self.y = Rover.MAX_Y
        elif self.y > Rover.MAX_Y:
            self.y = Rover.MIN_Y
        elif self.x < Rover.MIN_X:
            self.x = Rover.MAX_X
        elif self.x > Rover.MAX_X:
            self.x = Rover.MIN_X


class BeyondMapError(Exception):
    pass


class WrongDirection(Exception):
    pass


class WrongCommand(Exception):
    def __init__(self, command):
        self.command = command

    def __str__(self):
        return "Wrong '%s' command" % self.command
