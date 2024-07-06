class MachineConfig:
    def __init__(self):
        # Определение пинов для шаговых двигателей
        self.stepper_pins = {
            'X': {'step': 2, 'dir': 3},
            'Y': {'step': 4, 'dir': 5},
            'Z': {'step': 6, 'dir': 7}
        }
        
        # Определение пинов для LCD
        self.lcd_pins = {
            'rs': 8, 'en': 9, 'd4': 10, 'd5': 11, 'd6': 12, 'd7': 13
        }
        
        # Определение пинов для энкодера
        self.encoder_pins = {'clk': 14, 'dt': 15}
        
        # Определение пинов для 7-сегментного индикатора
        self.seven_segment_pins = {'data': 16, 'cs': 17, 'clk': 18}
        
        # Определение пинов для кнопок
        self.button_pins = {'start': 19, 'stop': 20}
        
        # Определение пинов для пищалки
        self.buzzer_pin = 21
        
        # Стандартные скорости и ускорения
        self.default_speed = 100  # мм/мин
        self.default_acceleration = 50  # мм/с^2
        
        # Шаги на мм для различных осей
        self.steps_per_mm = {
            'X': 80,
            'Y': 80,
            'Z': 400
        }

    def get_stepper_pins(self, axis):
        return self.stepper_pins[axis]

    def get_lcd_pins(self):
        return self.lcd_pins

    def get_encoder_pins(self):
        return self.encoder_pins

    def get_seven_segment_pins(self):
        return self.seven_segment_pins

    def get_button_pins(self):
        return self.button_pins

    def get_buzzer_pin(self):
        return self.buzzer_pin

    def get_default_speed(self):
        return self.default_speed

    def get_default_acceleration(self):
        return self.default_acceleration

    def get_steps_per_mm(self, axis):
        return self.steps_per_mm[axis]

# Пример использования:
config = MachineConfig()
x_stepper_pins = config.get_stepper_pins('X')
lcd_pins = config.get_lcd_pins()