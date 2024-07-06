import serial

class SerialMenuDisplay:
    # Константы класса
    SELECTED_PREFIX = '-> '
    NOT_SELECTED_PREFIX = '   '
    BACK_ITEM = '[назад]'
    SELECTED_ITEM_MESSAGE = 'Выбрано: '
    MENU_SEPARATOR = '---\n'
    KEY_VALUE_FORMAT = '{:<15}: {}\n'

    def __init__(self, port, baudrate=9600, menu_items=None, descriptions=None, values=None):
        self.serial_port = serial.Serial(port, baudrate)
        self.menu_items = [self.BACK_ITEM] + menu_items if menu_items is not None else [self.BACK_ITEM]
        self.descriptions = descriptions if descriptions is not None else []
        self.values = values if values is not None else []
        self.current_index = 0
        self.items_per_page = 4

    def display_menu(self):
        # Отправка меню с обозначением выбранного пункта стрелкой
        menu_text = ''
        start_index = (self.current_index // self.items_per_page) * self.items_per_page
        end_index = start_index + self.items_per_page
        for index in range(start_index, min(end_index, len(self.menu_items))):
            prefix = self.SELECTED_PREFIX if index == self.current_index else self.NOT_SELECTED_PREFIX
            menu_text += f'{prefix}{self.menu_items[index]}\n'
        menu_text += self.MENU_SEPARATOR if end_index < len(self.menu_items) else ''
        self.serial_port.write(menu_text.encode())

    def display_key_values(self):
        # Отправка информации в формате ключ-значение
        key_value_text = ''
        for description, value in zip(self.descriptions, self.values):
            key_value_text += self.KEY_VALUE_FORMAT.format(description, value)
        self.serial_port.write(key_value_text.encode())

    def next_item(self):
        # Переход к следующему пункту меню
        self.current_index = (self.current_index + 1) % len(self.menu_items)
        self.display_menu()

    def previous_item(self):
        # Переход к предыдущему пункту меню
        self.current_index = (self.current_index - 1) % len(self.menu_items)
        self.display_menu()

    def select_item(self):
        # Отправка выбранного пункта меню в COM порт
        selected_item = self.menu_items[self.current_index]
        self.serial_port.write(f'{self.SELECTED_ITEM_MESSAGE}{selected_item}\n'.encode())

# Пример использования:
menu_items = ['Пункт 1', 'Пункт 2', 'Пункт 3', 'Пункт 4', 'Пункт 5']
descriptions = ['Температура', 'Давление', 'Влажность', 'Скорость ветра']
values = ['22°C', '1 атм', '50%', '5 м/с']

serial_menu_display = SerialMenuDisplay('COM3', menu_items=menu_items, descriptions=descriptions, values=values)  # Замените 'COM3' на ваш COM порт

serial_menu_display.display_menu()  # Отобразит первые четыре пункта меню
serial_menu_display.display_key_values()  # Отобразит информацию в формате ключ-значение
serial_menu_display.next_item()     # Переключит на следующий пункт
serial_menu_display.previous_item() # Переключит на предыдущий пункт
serial_menu_display.select_item()   # Отправит выбранный пункт