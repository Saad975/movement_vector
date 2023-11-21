import pytest
from course_correction.collision_dector import CollisionDetection
from drone.drone import Drone


@pytest.fixture
def drone():
    return Drone([5, 5, 5], [10, 10, 10])


def test_detect_collision(drone):
    collision_detector = CollisionDetection()

    correction = collision_detector.detect_collision(drone, [11, 5, 5], 0)
    assert drone.collision_detected
    assert correction == 5

    correction = collision_detector.detect_collision(drone, [-1, 5, 5], 0)
    assert drone.collision_detected
    assert correction == 5

    correction = collision_detector.detect_collision(drone, [2, 5, 5], 0)
    assert not drone.collision_detected
    assert correction == 0

    correction = collision_detector.detect_collision(drone, [6, 5, 5], 0)
    assert not drone.collision_detected
    assert correction == 0
