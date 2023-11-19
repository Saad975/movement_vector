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
        """
        World's width, depth and height should be positive integer.
        :return:
        """
        print("==== VoloDrone Sensors Data read")
        print(
            f"World: (x=range(0, {self.world_dimensions[0]}), y=range(0, {self.world_dimensions[1]}), z=range(0, {self.world_dimensions[2]}))")
        print(f"Drone starts at: ({self.current_position[0]}, {self.current_position[1]}, {self.current_position[2]})")

    def take_off(self):
        print("==== Volodrone Take Off")

    def move(self, direction, distance):
        direction_maping = {
            "left": 0,
            "right": 0,
            "up": 1,
            "down": 1,
            "forward": 2,
            "backward": 2
        }

        axis_index = direction_maping.get(direction.lower())

        if axis_index is not None:

            if direction.lower() in ["left", "backward", "down"]:
                self.movement_vectors[axis_index] -= distance

            else:
                self.movement_vectors[axis_index] += distance

            new_position = self.current_position.copy()
            new_position = [int(current) + int(movement) for current, movement in
                                     zip(new_position, self.movement_vectors)]

            if new_position[axis_index] < 0:
                self.collision_detected = True

            else:
                self.current_position = new_position
                self.total_distance += distance

        else:
            raise ValueError(
                "Invalid direction. Direction Should be 'left', 'right', 'forward', 'backward', 'up', or 'down'.")

        self.dectect_movement(self.total_distance)
        self.movement_vectors = [0, 0, 0]
        self.collision_detected = False

    def dectect_movement(self, total_distance):
        if self.collision_detected:
            print(f"({self.movement_vectors[0]}, {self.movement_vectors[1]}, {self.movement_vectors[2]}) -> "
                  f"CRASH IMMINENT: AUTOMATIC COURSE CORRECTION")

        else:
            print(f"({self.movement_vectors[0]}, {self.movement_vectors[1]}, {self.movement_vectors[2]}) -> "
                  f"({self.current_position[0]}, {self.current_position[1]}, {self.current_position[2]}) [{total_distance}]")

    def land(self):
        print("==== Volodrone Landing")
