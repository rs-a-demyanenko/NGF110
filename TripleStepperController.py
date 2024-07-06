import StepperMotor
import DualStepperController

class TripleStepperController(DualStepperController):
    def __init__(self, motor_x, motor_y, motor_z, distance_between_passes_xy, distance_between_passes_z, passes_z):
        super().__init__(motor_x, motor_y, distance_between_passes_xy)
        self.motor_z = motor_z
        self.distance_between_passes_z = distance_between_passes_z
        self.passes_z = passes_z

    def perform_passes(self, speed_xy, speed_z, num_passes_xy, primary_direction):
        # Выполнение проходов в направлениях X и Y
        super().perform_passes(speed_xy, num_passes_xy, primary_direction)

        # Выполнение проходов в направлении Z
        for pass_num in range(self.passes_z):
            direction = 1 if pass_num % 2 == 0 else -1
            self.motor_z.move(self.distance_between_passes_z * direction, speed_z)

# Пример использования:
# motor_x = StepperMotor(step_pin=18, dir_pin=19, steps_per_mm=100, acceleration=0.1)
# motor_y = StepperMotor(step_pin=23, dir_pin=22, steps_per_mm=100, acceleration=0.1)
# motor_z = StepperMotor(step_pin=27, dir_pin=26, steps_per_mm=100, acceleration=0.1)
# motor_x.set_limits(0, 300)  # Установка лимитов для оси X
# motor_y.set_limits(0, 200)  # Установка лимитов для оси Y
# motor_z.set_limits(0, 100)  # Установка лимитов для оси Z

# controller = TripleStepperController(motor_x, motor_y, motor_z, 10, 5, 3)
# controller.perform_passes(speed_xy=5, speed_z=2, num_passes_xy=5, primary_direction='x')