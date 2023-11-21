import os

from drone.command_processor import CommandProcessor
from drone.drone import Drone
from world.world import World


class DroneController:

    def __init__(self, world_dimensions, drone_start_position):
        self.world = World(world_dimensions)
        self.drone = Drone(drone_start_position, world_dimensions)
        self.command_processor = CommandProcessor(self.drone)

    def run_simulation(self):
        self.drone.initialize_drone()
        try:
            self.drone.read_sensor_data()
        except IndexError:
            raise IndexError("Invalid world or drone dimension.'")

        try:
            current_directory = os.path.dirname(os.path.realpath(__file__))
            file_name = os.path.join(current_directory, "commands.txt")

            with open(file_name, 'r') as file:
                for line in file:
                    command = line.strip()
                    if not command:
                        break
                    self.command_processor.process_command(command)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

        self.drone.land()


if __name__ == "__main__":

    world_dimensions = [10, 10, 10]
    drone_start_position = [5, 5, 5]

    drone_controller = DroneController(world_dimensions, drone_start_position)
    drone_controller.run_simulation()
