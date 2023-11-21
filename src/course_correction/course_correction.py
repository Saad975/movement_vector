class CourseCorrection:

    def __init__(self):
        pass

    def correct_course(self, drone, axis_index, direction, distance):
        print(f"({drone.movement_vectors[0]}, {drone.movement_vectors[1]}, {drone.movement_vectors[2]}) -> "
              f"CRASH IMMINENT: AUTOMATIC COURSE CORRECTION")

        if direction.lower() in ["left", "backward", "down"]:
            drone.movement_vectors[axis_index] = -distance
        else:
            drone.movement_vectors[axis_index] = distance
