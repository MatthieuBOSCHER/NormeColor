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


    def generate_triadic(self, hsv):
        h = hsv[0] * 360
        h += 180
        h0 = h + 60
        h1 = h - 60
        triadic0 = (h0/360, hsv[1], hsv[2])
        triadic1 = (h1/360, hsv[1], hsv[2])

        triadic0_rgb = colorsys.hsv_to_rgb(triadic0[0], triadic0[1], triadic0[2])
        triadic0_rgb = (triadic0_rgb[0]*255, triadic0_rgb[1]*255, triadic0_rgb[2]*255)

        triadic1_rgb = colorsys.hsv_to_rgb(triadic1[0], triadic1[1], triadic1[2])
        triadic1_rgb = (triadic1_rgb[0]*255, triadic1_rgb[1]*255, triadic1_rgb[2]*255)

        return (triadic0_rgb, triadic1_rgb)


    def generate_analogus(self, hsv):
        h = hsv[0] * 360
        h0 = h + 30
        h1 = h - 30
        analogus0 = (h0/360, hsv[1], hsv[2])
        analogus1 = (h1/360, hsv[1], hsv[2])

        analogus0_rgb = colorsys.hsv_to_rgb(analogus0[0], analogus0[1], analogus0[2])
        analogus0_rgb = (analogus0_rgb[0]*255, analogus0_rgb[1]*255, analogus0_rgb[2]*255)

        analogus1_rgb = colorsys.hsv_to_rgb(analogus1[0], analogus1[1], analogus1[2])
        analogus1_rgb = (analogus1_rgb[0]*255, analogus1_rgb[1]*255, analogus1_rgb[2]*255)

        return (analogus0_rgb, analogus1_rgb)


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
