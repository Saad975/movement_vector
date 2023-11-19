from command_processor import CommandProcessor
from drone import Drone
from world import World


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
            while True:
                command = input("Enter Command (e.g: '01 Left 01'): ")

                if not command:
                    break

                self.command_processor.process_command(command)

        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            pass

        self.drone.land()


if __name__ == "__main__":
    world_dimensions = input("Enter World Dimension in Integer, Seprated By Space (e.g: 10 10 10): ")
    drone_dimensions = input("Enter Drone Start Position in Integer, Seprated By Space (e.g: 5 5 5): ")

    world_dimensions = world_dimensions.split()
    drone_start_position = drone_dimensions.split()

    drone_controller = DroneController(world_dimensions, drone_start_position)

    drone_controller.run_simulation()
