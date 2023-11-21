from course_correction.collision_dector import CollisionDetection
from course_correction.course_correction import CourseCorrection


class Drone:
    def __init__(self, start_position, world_dimensions):
        self.collision_detected = False
        self.total_distance = 0
        self.movement_vectors = [0, 0, 0]
        self.current_position = start_position
        self.world_dimensions = world_dimensions

    def initialize_drone(self):
        print("==== VoloDrone Initialising")

    def read_sensor_data(self):
        print("==== VoloDrone Sensors Data read")
        print(
            f"World: (x=range(0, {self.world_dimensions[0]}), y=range(0, {self.world_dimensions[1]}), z=range(0, {self.world_dimensions[2]}))")
        print(f"Drone starts at: ({self.current_position[0]}, {self.current_position[1]}, {self.current_position[2]})")

    def take_off(self):
        print("==== Volodrone Take Off")

    def get_axis_index(self, direction):
        direction_mapping = {
            "left": 0,
            "right": 0,
            "up": 1,
            "down": 1,
            "forward": 2,
            "backward": 2
        }
        return direction_mapping.get(direction.lower())

    def update_movement_vectors(self, direction, distance):
        axis_index = self.get_axis_index(direction)

        if axis_index is not None:
            # breakpoint()
            if direction.lower() in ["left", "backward", "down"]:
                self.movement_vectors[axis_index] -= distance
            else:
                self.movement_vectors[axis_index] += distance

    def calculate_new_position(self):
        return [current + movement for current, movement in zip(self.current_position, self.movement_vectors)]

    def move(self, direction, distance):
        axis_index = self.get_axis_index(direction)

        if axis_index is not None:

            self.update_movement_vectors(direction, distance)

            new_position = self.calculate_new_position()

            correction = self.handle_collision(new_position, axis_index)

            if correction != 0 or self.collision_detected:
                course_correction = CourseCorrection()
                course_correction.correct_course(self, axis_index, direction, correction)

            self.current_position = new_position
            self.total_distance += correction if self.collision_detected else distance

        else:
            raise ValueError(
                "Invalid direction. Direction Should be 'left', 'right', 'forward', 'backward', 'up', or 'down'.")

        self.dectect_movement(self.total_distance)
        self.reset_movement()

    def handle_collision(self, new_position, axis_index):
        collision_detector = CollisionDetection()
        correction = collision_detector.detect_collision(self, new_position, axis_index)
        return correction

    def dectect_movement(self, total_distance):
        print(f"({self.movement_vectors[0]}, {self.movement_vectors[1]}, {self.movement_vectors[2]}) -> "
              f"({self.current_position[0]}, {self.current_position[1]}, {self.current_position[2]}) [{total_distance}]")

    def reset_movement(self):
        self.movement_vectors = [0, 0, 0]
        self.collision_detected = False

    def land(self):
        print("==== Volodrone Landing")
