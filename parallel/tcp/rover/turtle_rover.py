"""
Tool to be used during parallelism exercises
    rover with GUI to be used in exercise 4)

:author: 'Grzegorz Latuszek (Nokia)'
"""
import turtle
from rover import Rover


class TurtleRover(Rover):
    _mars_initialized = False

    def __init__(self, x, y, direction="N", color="red"):
        super(TurtleRover, self).__init__(x, y, direction)
        self.color = color
        self._set_mars_space()
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.color("grey")
        for point in self.grid_points:
            self.turtle.setposition(point[0]-0.5, point[1]-0.5)
        self.turtle.speed('normal')
        self.turtle.hideturtle()
        self.turtle.penup()
        self._set_position_and_direction()
        self.turtle.color(self.color)
        self.turtle.down()
        self.turtle.showturtle()

    @classmethod
    def _set_mars_space(cls):
        if not cls._mars_initialized:
            turtle.reset()
            turtle.title("Welcome on Mars")
            turtle.setworldcoordinates(cls.MIN_X, cls.MIN_Y, cls.MAX_X+1, cls.MAX_Y+1)
            cls.grid_points = TurtleRover._get_grid_points(cls.MIN_X, cls.MIN_Y, cls.MAX_X, cls.MAX_Y)
            cls._mars_initialized = True

    @staticmethod
    def _get_grid_points(min_x, min_y, max_x, max_y):
        points = []
        for x in range(min_x, max_x+1):
            bottom_point = (x, min_y)
            top_point = (x, max_y)
            if x % 2 == 0:
                points.append(bottom_point)
                points.append(top_point)
            else:
                points.append(top_point)
                points.append(bottom_point)
        for y in range(min_y, max_y+1):
            left_point = (min_x, y)
            right_point = (max_x, y)
            if y % 2 == 0:
                points.append(left_point)
                points.append(right_point)
            else:
                points.append(right_point)
                points.append(left_point)
        return points

    def _set_position_and_direction(self):
        direction2angle = {"E": 0, "N": 90, "W": 180, "S": 270}
        self.turtle.setheading(direction2angle[self.direction])
        self.turtle.setpos(self.x, self.y)

    def interpret_single_command(self, command):
        super(TurtleRover, self).interpret_single_command(command)
        self._set_position_and_direction()
        self.turtle.down()

    def _correct_coordinates_on_boundry_wrap(self):
        old_x = self.x
        old_y = self.y
        super(TurtleRover, self)._correct_coordinates_on_boundry_wrap()
        if (old_x != self.x) or (old_y != self.y):
            self.turtle.penup()

if __name__ == '__main__':
    rov = TurtleRover(50, 50, "N", "violet")
    rov.interpret_commands("frflfrflffflf")
    raw_input("rover>")
