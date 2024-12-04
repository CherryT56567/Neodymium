import time

class Motor:
    def __init__(self, id):
        self.motor_speed = 0
        self.motor_id = id
        self.initialize_motor();
        print("Motor initialized")

    def initialize_motor(self):
        # TODO
        print(f"Motor {self.motor_id} initialized")
        
    def set_speed(self, speed):
        self.motor_speed = speed
        print(f"Motor speed set to {self.motor_speed}")
        
    def return_speed(self):
        return self.motor_speed

    def start(self):
        # TODO: Start Motor
        print("Motor running")
        
    def stop(self):
        # TODO: Stop Motor
        print("Motor stopping")

class Sensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self.value = 0
        
    def initialize_sensor(self):
        # TODO
        Print(f"Sensor {self.sensor_id} initialized")

    def read_value(self):
        # TODO
        print(f"Sensor {self.sensor_id} value read: {value}")
        return value
    
    def emulate_value(self, value):
        self.value = value
        print(f"Sensor {self.sensor_id} value emulated: {value}")

class Robot:
    def __init__(self):
        # Initialization of motors, sensors, and other components
        self.motor1 = Motor(1) # LEFT
        self.motor2 = Motor(2) # LEFT
        self.motor3 = Motor(3) # RIGHT
        self.motor4 = Motor(4) # RIGHT
        self.sensor1 = Sensor(1)
        self.pSpeed = 0
        print("Robot initialized")

    def start(self):
        # TODO
        print("Robot starting")

    def set_speed(self, speed):
        self.pSpeed = speed
        self.motor1.set_speed(speed)
        self.motor2.set_speed(speed)
        self.motor3.set_speed(speed)
        self.motor4.set_speed(speed)
        
    def move(self):
        self.motor1.start()
        self.motor2.start()
        self.motor3.start()
        self.motor4.start()

    def turn(self, left):
        if left:
            self.motor1.set_speed(speed) # 1 2 + == Right
            self.motor2.set_speed(speed)
            self.motor3.set_speed(-speed)
            self.motor4.set_speed(-speed)
        else:
            self.motor1.set_speed(-speed) # 1 2 + == Right
            self.motor2.set_speed(-speed)
            self.motor3.set_speed(speed)
            self.motor4.set_speed(speed)
        self.motor1.start()
        self.motor2.start()
        self.motor3.start()
        self.motor4.start()

    def stop(self):
        self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()

# Example of creating a Robot instance and starting it
if __name__ == "__main__":
    robot = Robot()
    robot.start()
