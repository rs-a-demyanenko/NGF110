class LCD2004:
    def __init__(self, i2c, address=0x27):
        self.lcd = I2C_LCD_driver.lcd(i2c, address)
        self.max_chars = 20  # Максимальное количество символов в строке
        self.menu_items = []
        self.current_index = 0

    def display_text(self, left_text, right_text):
        if not (len(left_text) == len(right_text) == 4):
            raise ValueError("Массивы должны содержать ровно 4 элемента.")
        
        for i in range(4):
            total_chars = len(left_text[i]) + len(right_text[i])
            if total_chars > self.max_chars:
                raise ValueError(f"Суммарное количество символов в строке {i+1} превышает лимит.")
            
            # Выравнивание текста справа
            right_aligned_text = right_text[i].rjust(self.max_chars - len(left_text[i]))
            self.lcd.lcd_display_string(left_text[i] + right_aligned_text, i+1)

    def clear_screen(self):
        self.lcd.lcd_clear()

    def display_menu(self):
        self.clear_screen()
        start_index = self.current_index - self.current_index % 4
        for i in range(4):
            item_index = start_index + i
            if item_index < len(self.menu_items):
                line = self.menu_items[item_index]
                # Добавление стрелочки для текущего выбора
                if item_index == self.current_index:
                    line += ' <-'
                self.lcd.lcd_display_string(line, i+1)

    def menu_down(self):
        self.current_index = (self.current_index + 1) % len(self.menu_items)
        if self.current_index % 4 == 0 and self.current_index != 0:
            # Смещение пунктов меню вверх
            self.display_menu()

    def menu_up(self):
        if self.current_index == 0:
            self.current_index = len(self.menu_items) - 1
        else:
            self.current_index -= 1
        if self.current_index % 4 == 3 or self.current_index == len(self.menu_items) - 1:
            # Смещение пунктов меню вниз
            self.display_menu()

lcd = LCD2004(i2c, address=0x27)
lcd.menu_items = ['Пункт 1', 'Пункт 2', 'Пункт 3', 'Пункт 4', 'Пункт 5']
lcd.display_menu()  # Отображение меню
lcd.menu_down()     # Перемещение вниз по меню
lcd.menu_up()       # Перемещение вверх по меню