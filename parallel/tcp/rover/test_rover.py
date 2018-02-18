"""
TDD for TurtleRover used in exercise 4) of parallelism section

:author: 'Grzegorz Latuszek (Nokia)'
"""
import pytest


def test_rover_is_on_the_position_it_was_set(rover_class):
    assert 30 < rover_class.MAX_X
    assert 80 < rover_class.MAX_Y

    rov = rover_class(x=30, y=50)
    assert rov.x == 30
    assert rov.y == 50

    rov = rover_class(x=0, y=80)
    assert rov.x == 0
    assert rov.y == 80


def test_rover_is_headed_towards_direction_it_was_set(rover_class):
    rov = rover_class(x=30, y=50, direction="N")
    assert rov.direction == "N"

    rov = rover_class(x=30, y=50, direction="W")
    assert rov.direction == "W"


def test_creating_rover_beyond_map_boundaries_raises_BeyondMapError(rover_class):
    from rover import BeyondMapError
    with pytest.raises(BeyondMapError):
        rover_class(x=rover_class.MAX_X+1, y=rover_class.MIN_Y, direction='W')
    with pytest.raises(BeyondMapError):
        rover_class(x=rover_class.MIN_X-1, y=rover_class.MIN_Y, direction='W')
    with pytest.raises(BeyondMapError):
        rover_class(x=rover_class.MIN_X, y=rover_class.MAX_Y+1, direction='W')
    with pytest.raises(BeyondMapError):
        rover_class(x=rover_class.MIN_X, y=rover_class.MIN_Y-1, direction='W')


def test_creating_rover_with_wrong_direction_raises_WrongDirection(rover_class):
    from rover import WrongDirection
    with pytest.raises(WrongDirection):
        rover_class(x=30, y=50, direction="K")
    with pytest.raises(WrongDirection):
        rover_class(x=30, y=50, direction=["W"])
    with pytest.raises(WrongDirection):
        rover_class(x=30, y=50, direction=76)


def test_rover_can_move_forward(rover_class):
    rov = rover_class(x=50, y=50, direction="N")
    rov.move_forward()
    assert rov.x == 50
    assert rov.y == 51

    rov.move_forward()
    assert rov.x == 50
    assert rov.y == 52

    rov = rover_class(x=50, y=50, direction="S")
    rov.move_forward()
    assert rov.x == 50
    assert rov.y == 49

    rov = rover_class(x=50, y=50, direction="W")
    rov.move_forward()
    assert rov.x == 49
    assert rov.y == 50

    rov = rover_class(x=50, y=50, direction="E")
    rov.move_forward()
    assert rov.x == 51
    assert rov.y == 50


def test_rover_can_move_backward(rover_class):
    rov = rover_class(x=50, y=50, direction="N")
    rov.move_backward()
    assert rov.x == 50
    assert rov.y == 49

    rov.move_backward()
    assert rov.x == 50
    assert rov.y == 48

    rov = rover_class(x=50, y=50, direction="S")
    rov.move_backward()
    assert rov.x == 50
    assert rov.y == 51

    rov = rover_class(x=50, y=50, direction="W")
    rov.move_backward()
    assert rov.x == 51
    assert rov.y == 50

    rov = rover_class(x=50, y=50, direction="E")
    rov.move_backward()
    assert rov.x == 49
    assert rov.y == 50


def test_can_rotate_to_the_left(rover_at_50_50_N):
    rov = rover_at_50_50_N
    rov.turn_left()
    assert rov.direction == "W"
    rov.turn_left()
    assert rov.direction == "S"
    rov.turn_left()
    assert rov.direction == "E"
    rov.turn_left()
    assert rov.direction == "N"


def test_can_rotate_to_the_right(rover_at_50_50_N):
    rov = rover_at_50_50_N
    rov.turn_right()
    assert rov.direction == "E"
    rov.turn_right()
    assert rov.direction == "S"
    rov.turn_right()
    assert rov.direction == "W"
    rov.turn_right()
    assert rov.direction == "N"


def test_rover_can_wrap_at_north_boundry(rover_at_MAXX_MAXY_N):
    rov = rover_at_MAXX_MAXY_N
    rov.move_forward()
    assert rov.x == rov.MAX_X
    assert rov.y == rov.MIN_Y


def test_rover_can_wrap_at_west_boundry(rover_at_MINX_MINY_S):
    rov = rover_at_MINX_MINY_S
    rov.turn_right()
    rov.move_forward()
    assert rov.x == rov.MAX_X
    assert rov.y == rov.MIN_Y


def test_rover_can_wrap_at_south_boundry(rover_at_MINX_MINY_S):
    rov = rover_at_MINX_MINY_S
    rov.move_forward()
    assert rov.x == rov.MIN_X
    assert rov.y == rov.MAX_Y


def test_rover_can_wrap_at_east_boundry(rover_at_MAXX_MAXY_N):
    rov = rover_at_MAXX_MAXY_N
    rov.turn_right()
    rov.move_forward()
    assert rov.x == rov.MIN_X
    assert rov.y == rov.MAX_Y


def test_can_interpret_command_move_forward(rover_at_50_50_N):
    command = "f"
    rov = rover_at_50_50_N
    rov.interpret_single_command(command)
    assert rov.x == 50
    assert rov.y == 51


def test_can_interpret_command_move_backward(rover_at_50_50_N):
    command = "b"
    rov = rover_at_50_50_N
    rov.interpret_single_command(command)
    assert rov.x == 50
    assert rov.y == 49


def test_can_interpret_command_turn_left(rover_at_50_50_N):
    command = "l"
    rov = rover_at_50_50_N
    rov.interpret_single_command(command)
    assert rov.direction == "W"


def test_can_interpret_command_turn_right(rover_at_50_50_N):
    command = "r"
    rov = rover_at_50_50_N
    rov.interpret_single_command(command)
    assert rov.direction == "E"


def test_rover_can_interpret_cmd_sequence(rover_at_50_50_N):
    rov = rover_at_50_50_N
    earth_sent_commands = "fbrflfr"
    rov.interpret_commands(earth_sent_commands)
    assert rov.x == 51
    assert rov.y == 51
    assert rov.direction == "E"


def test_rover_can_ignore_incorrect_cmd(rover_at_50_50_N):
    rov = rover_at_50_50_N
    earth_sent_commands = "fbryflhfr"
    rov.interpret_commands(earth_sent_commands)
    assert rov.x == 51
    assert rov.y == 51
    assert rov.direction == "E"


# ------------------------------------ resources


@pytest.fixture
def rover_class():
    from rover import Rover
    return Rover


@pytest.fixture
def rover_at_MINX_MINY_S(rover_class):
    rov = rover_class(x=rover_class.MIN_X, y=rover_class.MIN_Y, direction="S")
    return rov


@pytest.fixture
def rover_at_50_50_N(rover_class):
    rov = rover_class(x=50, y=50, direction="N")
    return rov

@pytest.fixture
def rover_at_MAXX_MAXY_N(rover_class):
    return rover_class(x=rover_class.MAX_X, y=rover_class.MAX_Y, direction='N')
