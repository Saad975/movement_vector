from src.drone.drone import Drone
from course_correction.course_correction import CourseCorrection



def test_move_with_collision_detection():
    drone = Drone(start_position=[5, 5, 5], world_dimensions=[10, 10, 10])

    drone.collision_detected = False
    drone.total_distance = 0
    drone.course_correction = CourseCorrection()
    drone.move("left", 1)
    expected_current_position = [4, 5, 5]

    assert drone.current_position == expected_current_position
    assert drone.total_distance == 1

    drone.reset_movement()
    drone.move("right", 20)
    expected_current_position = [10, 5, 5]

    assert drone.current_position == expected_current_position
    assert drone.total_distance == 7
