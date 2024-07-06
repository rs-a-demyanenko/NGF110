from machine import Pin, PWM
import time

class StepperMotor:
    def __init__(self, step_pin, dir_pin, steps_per_mm, acceleration):
        self.step_pin = PWM(Pin(step_pin))  # ШИМ для управления шагами
        self.dir_pin = Pin(dir_pin, Pin.OUT)  # Пин для управления направлением
        self.position = 0
        self.steps_per_mm = steps_per_mm
        self.acceleration = acceleration
        self.limit_start = None
        self.limit_end = None

    def set_limits(self, start, end):
        self.limit_start = start
        self.limit_end = end

    def move(self, mm, speed_mm_per_sec):
        if self.limit_start is not None and self.position + mm < self.limit_start:
            print("Ошибка: перемещение за пределы начального лимита")
            return
        if self.limit_end is not None and self.position + mm > self.limit_end:
            print("Ошибка: перемещение за пределы конечного лимита")
            return

        steps = int(mm * self.steps_per_mm)
        self.dir_pin.value(1 if mm > 0 else 0)  # Установка направления

        # Расчет периода ШИМ сигнала на основе скорости
        pwm_freq = int(self.steps_per_mm * speed_mm_per_sec)
        self.step_pin.freq(pwm_freq)

        # Активация ШИМ для выполнения шагов
        self.step_pin.duty(512)  # 50% скважность
        for _ in range(steps):
            time.sleep(1 / pwm_freq)  # Пауза соответствует частоте ШИМ
        self.step_pin.duty(0)  # Отключение ШИМ

        self.position += mm

    def get_position(self):
        return self.position

# Пример использования:
# motor = StepperMotor(step_pin=18, dir_pin=19, steps_per_mm=100, acceleration=0.1)
# motor.set_limits(0, 200)
# motor.move(50, 5)
# print("Текущее положение двигателя:", motor.get_position())