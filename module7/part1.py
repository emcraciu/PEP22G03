# objects

class Keyboard:
    typed = ''
    shift_pressed = False

    def press_shit(self):
        self.shift_pressed = True

    def release_shit(self):
        self.shift_pressed = False

    def press_a(self):
        if self.shift_pressed:
            self.typed += 'A'
        else:
            self.typed += 'a'  # <- learn how is self

    def how_is_self(self):
        print(id(self))


keyboard = Keyboard()

print(type(keyboard))
print(f'valoarea este: {keyboard.typed}')
keyboard.press_a()
print(f'noua valoarea este: {keyboard.typed}')
keyboard.press_a()
print(f'noua noua valoarea este: {keyboard.typed}')
keyboard.how_is_self()
print(id(keyboard))


# new keyboard

keyboard1 = Keyboard()
print(f'new keyboard - valoarea este: {keyboard1.typed}')
keyboard1.press_shit()
keyboard1.press_a()
keyboard1.release_shit()
print(f'new keyboard - noua valoarea este: {keyboard1.typed}')