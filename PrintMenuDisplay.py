class PrintMenuDisplay:
    # Константы класса
    SELECTED_PREFIX = '-> '
    NOT_SELECTED_PREFIX = '   '
    BACK_ITEM = '[назад]'
    SELECTED_ITEM_MESSAGE = 'Выбрано: '
    MENU_SEPARATOR = '---\n'
    KEY_VALUE_FORMAT = '{:<15}: {}\n'

    def init(self, menu_items=None, descriptions=None, values=None):
        self.menu_items = [self.BACK_ITEM] + menu_items if menu_items is not None else [self.BACK_ITEM]
        self.descriptions = descriptions if descriptions is not None else []
        self.values = values if values is not None else []
        self.current_index = 0
        self.items_per_page = 4
        self.display_key_values()

    def display_menu(self):
        # Вывод меню с обозначением выбранного пункта стрелкой
        menu_text = ''
        start_index = (self.current_index // self.items_per_page) * self.items_per_page
        end_index = start_index + self.items_per_page
        for index in range(start_index, min(end_index, len(self.menu_items))):
            prefix = self.SELECTED_PREFIX if index == self.current_index else self.NOT_SELECTED_PREFIX
            menu_text += f'{prefix}{self.menu_items[index]}\n'
        menu_text += self.MENU_SEPARATOR if end_index < len(self.menu_items) else ''
        print(menu_text)

    def display_key_values(self):
        # Вывод информации в формате ключ-значение
        key_value_text = ''
        for description, value in zip(self.descriptions, self.values):
            key_value_text += self.KEY_VALUE_FORMAT.format(description, value)
        print(key_value_text)

    def next_item(self):
        # Переход к следующему пункту меню
        self.current_index = (self.current_index + 1) % len(self.menu_items)
        self.display_menu()

    def previous_item(self):
        # Переход к предыдущему пункту меню
        self.current_index = (self.current_index - 1) % len(self.menu_items)
        self.display_menu()

    def select_item(self):
        # Вывод выбранного пункта меню
        selected_item = self.menu_items[self.current_index]
        print(f'{self.SELECTED_ITEM_MESSAGE}{selected_item}')

    def update_menu_items(self, new_menu_items):
        # Обновление пунктов меню
        self.menu_items = [self.BACK_ITEM] + new_menu_items
        self.display_menu()

    def update_descriptions(self, new_descriptions):
        # Обновление описаний
        self.descriptions = new_descriptions
        self.display_key_values()

    def update_values(self, new_values):
        # Обновление значений
        self.values = new_values
        self.display_key_values()

# Пример использования:
# menu_items = ['Пункт 1', 'Пункт 2', 'Пункт 3', 'Пункт 4', 'Пункт 5']
# descriptions = ['Температура', 'Давление', 'Влажность', 'Скорость ветра']
# values = ['22°C', '1 атм', '50%', '5 м/с']

# print_menu_display = PrintMenuDisplay(menu_items=menu_items, descriptions=descriptions, values=values)

# print_menu_display.display_menu()           Выведет первые четыре пункта меню
# print_menu_display.display_key_values()     Выведет информацию в формате ключ-значение
# print_menu_display.next_item()              Переключит на следующий пункт
# print_menu_display.previous_item()          Переключит на предыдущий пункт
# print_menu_display.select_item()            Выведет выбранный пункт


# Обновление пунктов меню
# new_menu_items = ['Пункт A', 'Пункт B', 'Пункт C']
# print_menu_display.update_menu_items(new_menu_items)

# Обновление описаний
# new_descriptions = ['Новая температура', 'Новое давление']
# print_menu_display.update_descriptions(new_descriptions)

# Обновление значений
# new_values = ['25°C', '1.2 атм']
# print_menu_display.update_values(new_values)