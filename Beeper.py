from machine import Pin, PWM
import time

class Beeper:
    def __init__(self, pin_number):
        self.beeper = PWM(Pin(pin_number), freq=1000)

    def beep(self, duration_ms=100):
        self.beeper.duty(512)
        time.sleep_ms(duration_ms)
        self.beeper.duty(0)

    def long_beeps(self, count=3, duration_ms=500):
        for _ in range(count):
            self.beep(duration_ms)
            time.sleep_ms(duration_ms)

    def siren(self, cycles=8, duration_ms=100):
        for _ in range(cycles):
            for freq in range(1000, 2000, 100):
                self.beeper.freq(freq)
                self.beep(duration_ms // cycles)
            for freq in range(2000, 1000, -100):
                self.beeper.freq(freq)
                self.beep(duration_ms // cycles)

# Пример использования:
beeper = Beeper(5) # Предполагается, что пищалка подключена к пину 5

# Простой короткий пик
beeper.beep()

# Три длинных пика
beeper.long_beeps()

# Сирена
beeper.siren()