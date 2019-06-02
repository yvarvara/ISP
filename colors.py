import random


class ColorsMethods:
    @staticmethod
    def rgb_to_hex(r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)

    @staticmethod
    def hex_to_rgb(hex_color):
        h = hex_color.lstrip('#')
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def color_inverse(hex_color):
        r, g, b = ColorsMethods.hex_to_rgb(hex_color)
        clr = ColorsMethods.rgb_to_hex(255 - r, 255 - g, 255 - b)
        return clr

    @staticmethod
    def get_rand_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        return ColorsMethods.rgb_to_hex(r, g, b)