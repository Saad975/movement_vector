class CommandProcessor:
    def __init__(self, drone):
        self.drone = drone

    def process_command(self, command):
        """
        Order: int
        Direction: string (left, right, forward, backward, up, down)
        Distance: int
        :param command:
        :return:
        """
        split_command = command.split()
        if len(split_command) == 3:
            order, direction, distance = split_command
            distance = int(distance)
            self.drone.move(direction, distance)

        else:
            print("Invalid command format. Please use 'Order Direction Distance.'")


