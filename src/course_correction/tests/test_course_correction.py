from ..course_correction import CourseCorrection
from ...drone.drone import Drone


def test_correct_course():
    drone = Drone(start_position=[0, 0, 0], world_dimensions=[10, 10, 10])

    course_correction = CourseCorrection()

    drone.movement_vectors = [20, 0, 0]
    axis_index = 0
    direction = "left"
    distance = 10

    course_correction.correct_course(drone, axis_index, direction, distance)
    expected_vectors = [-10, 0, 0]

    assert drone.movement_vectors == expected_vectors

    drone.movement_vectors = [20, 0, 0]
    axis_index = 0
    direction = "right"
    distance = 10

    course_correction.correct_course(drone, axis_index, direction, distance)
    expected_vectors = [10, 0, 0]

    assert drone.movement_vectors == expected_vectors
