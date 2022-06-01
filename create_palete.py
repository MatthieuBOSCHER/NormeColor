import colorsys


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        r, g, b = map(lambda x: x/255, [self.r, self.g, self.b])
        self.hsv = colorsys.rgb_to_hsv(r, g, b)


    def get_hexvalue(self):
        return '#'+'%02x%02x%02x' % (int(self.r), int(self.g) , int(self.b))


    def generate_split_complementary(self, hsv):
        h = hsv[0] * 360
        h += 180
        h0 = h + 30
        h1 = h - 30
        splitcomplement0 = (h0/360, hsv[1], hsv[2])
        splitcomplement1 = (h1/360, hsv[1], hsv[2])

        splitcomplement0_rgb = colorsys.hsv_to_rgb(splitcomplement0[0], splitcomplement0[1], splitcomplement0[2])
        splitcomplement0_rgb = (splitcomplement0_rgb[0]*255, splitcomplement0_rgb[1]*255, splitcomplement0_rgb[2]*255)

        splitcomplement1_rgb = colorsys.hsv_to_rgb(splitcomplement1[0], splitcomplement1[1], splitcomplement1[2])
        splitcomplement1_rgb = (splitcomplement1_rgb[0]*255, splitcomplement1_rgb[1]*255, splitcomplement1_rgb[2]*255)

        return (splitcomplement0_rgb, splitcomplement1_rgb)


    def generate_complementary(self, hsv):
        h = hsv[0] * 360
        h += 180

        complement = (h / 360, hsv[1], hsv[2])

        complement_rgb = colorsys.hsv_to_rgb(complement[0], complement[1], complement[2])
        complement_rgb = (complement_rgb[0] * 255, complement_rgb[1] * 255, complement_rgb[2] * 255)

        return complement_rgb


    def print_rgb_color(self):
        print("R:", self.r, 'G:', self.g, 'B:', self.b)


    def get_rgb_value(self):
        return self.r, self.g, self.b


    def print_hsv_color(self):
        print("hsv: ", self.hsv)


def create_color(rgb):
    return Color(rgb[0], rgb[1], rgb[2])



# complement.print_rgb_color()


# print(complement.get_rgb_value())
# print(complement.get_hexvalue())

