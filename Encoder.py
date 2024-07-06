from machine import Pin

class Encoder:
    def init(self, pin_clk, pin_dt):
        self.pin_clk = Pin(pin_clk, Pin.IN)
        self.pin_dt = Pin(pin_dt, Pin.IN)
        self.position = 0
        self.last_time = time.ticks_us()
        self.last_state = self.pin_clk.value()

        # Настройка прерываний
        self.pin_clk.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self._update)

    def _update(self, pin):
        current_time = time.ticks_us()
        time_difference = time.ticks_diff(current_time, self.last_time)
        self.last_time = current_time

        # Рассчитываем приращение position
        increment = max(1, int(1000000 / time_difference)) # Пример прогрессии

        current_state = self.pin_clk.value()
        dt_state = self.pin_dt.value()
        if current_state != self.last_state:
            if dt_state != current_state:
                self.position += increment  # Увеличиваем position
            else:
                self.position -= increment  # Уменьшаем position
        self.last_state = current_state

    def read(self):
        # Возвращает текущее положение
        return self.position

# Пример использования:
# pin_clk = 14  # Замените на реальный GPIO пин
# pin_dt = 12   # Замените на реальный GPIO пин

# encoder = Encoder(pin_clk, pin_dt)

# В основном цикле программы
# while True:
#     position = encoder.read()
#     print(f"Положение: {position}")
#     time.sleep(0.1)  # Добавляем небольшую задержку для удобства чтения