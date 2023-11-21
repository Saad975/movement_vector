class CollisionDetection:

    def __init__(self):
        pass

    def detect_collision(self, drone, new_position, axis_index):
        if new_position[axis_index] < 0:
            new_position[axis_index] = 0
            distance = drone.current_position[axis_index] - new_position[axis_index]
            drone.collision_detected = True
            return distance
        elif new_position[axis_index] > drone.world_dimensions[axis_index]:
            new_position[axis_index] = drone.world_dimensions[axis_index]
            distance = new_position[axis_index] - drone.current_position[axis_index]
            drone.collision_detected = True
            return distance
        else:
            drone.collision_detected = False
            return 0
