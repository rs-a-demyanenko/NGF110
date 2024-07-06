import StepperMotor

class DualStepperController:
    def __init__(self, motor_x, motor_y, distance_between_passes):
        self.motor_x = motor_x
        self.motor_y = motor_y
        self.distance_between_passes = distance_between_passes

    def perform_passes(self, speed, num_passes, primary_direction):
        if primary_direction not in ['x', 'y']:
            print("Ошибка: основное направление должно быть 'x' или 'y'")
            return

        for pass_num in range(num_passes):
            # Определение направления для этого прохода
            direction = 1 if pass_num % 2 == 0 else -1

            # Выполнение прохода в основном направлении
            primary_motor = self.motor_x if primary_direction == 'x' else self.motor_y
            secondary_motor = self.motor_y if primary_direction == 'x' else self.motor_x

            start_limit = primary_motor.limit_start if direction == 1 else primary_motor.limit_end
            end_limit = primary_motor.limit_end if direction == 1 else primary_motor.limit_start
            distance = abs(end_limit - start_limit)

            primary_motor.move(distance * direction, speed)

            # Перемещение на расстояние между проходами, если это не последний проход
            if pass_num < num_passes - 1:
                secondary_motor.move(self.distance_between_passes, speed)

# Пример использования:
motor_x = StepperMotor(step_pin=18, dir_pin=19, steps_per_mm=100, acceleration=0.1)
motor_y = StepperMotor(step_pin=23, dir_pin=22, steps_per_mm=100, acceleration=0.1)
motor_x.set_limits(0, 300)  # Установка лимитов для оси X
motor_y.set_limits(0, 200)  # Установка лимитов для оси Y

controller = DualStepperController(motor_x, motor_y, 10)  # Расстояние между проходами 10 мм
controller.perform_passes(speed=5, num_passes=5, primary_direction='x')