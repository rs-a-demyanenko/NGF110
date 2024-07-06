from machine import Pin
import time

class Encoder:
    def __init__(self, pin_clk, pin_dt):
        self.pin_clk = Pin(pin_clk, Pin.IN)
        self.pin_dt = Pin(pin_dt, Pin.IN)
        self.last_time = time.ticks_ms()
        self.position = 0
        self.multiplier = 1
        self.counter = 0

    def read(self):
        current_time = time.ticks_ms()
        if self.pin_clk.value() == 1:
            if self.pin_dt.value() == 0:
                # Вращение по часовой стрелке
                self.position += self.multiplier
                self.counter += self.multiplier
            else:
                # Вращение против часовой стрелки
                self.position -= self.multiplier
                self.counter -= self.multiplier

            # Вычисляем время между импульсами
            time_diff = current_time - self.last_time
            self.last_time = current_time

            # Увеличиваем множитель в зависимости от скорости вращения
            if time_diff < 200:  # Если время меньше 200 мс
                self.multiplier *= 2  # Удваиваем множитель
            elif time_diff > 500:  # Если время больше 500 мс
                self.multiplier = 1  # Сбрасываем множитель

            # Ограничиваем максимальное значение множителя
            if self.multiplier > 128:
                self.multiplier = 128

        return self.position

    def reset_counter(self):
        self.counter = 0

    def get_counter(self):
        return self.counter

# Пример использования:
encoder = Encoder(14, 12)  # Предполагается, что CLK подключен к пину 14, а DT - к пину 12

# Сброс счетчика импульсов
encoder.reset_counter()

# В основном цикле программы
while True:
    position = encoder.read()
    print("Текущая позиция:", position)
    print("Количество импульсов с последнего сброса:", encoder.get_counter())
    time.sleep_ms(10)