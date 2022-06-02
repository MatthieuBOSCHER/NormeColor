from flask import Flask, render_template, request, redirect, url_for
import create_palete as plt
from flask_bootstrap import Bootstrap
from flask_colorpicker import colorpicker
import re
import random

app = Flask(__name__)

Bootstrap(app)
colorpicker(app)


@app.route('/')
def index():  # put application's code here
    random_color = lambda: random.randint(0, 255)
    random_color = '#%02X%02X%02X' % (random_color(),random_color(),random_color())
    palete = get_palette(random_color)
    return render_template("index.html", complement=palete.get("complement").get_hexvalue(),
                           triadicA=palete.get('triadicA').get_hexvalue(),
                           triadicB=palete.get("triadicB").get_hexvalue(),
                           analogusB=palete.get('analogusB').get_hexvalue(),
                           analogusA=palete.get('analogusA').get_hexvalue(),
                           input_color=palete.get("input_color").get_hexvalue())


def get_palette(input_color="#00B2FF"):

    if not re.search('([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$', input_color):
        input_color = "#00B2FF"
    input_color = input_color.lstrip('#')
    input_color = tuple(int(input_color[i:i + 2], 16) for i in (0, 2, 4))
    input_color = plt.Color(input_color[0], input_color[1], input_color[2])

    triadic_complementary = input_color.generate_triadic(input_color.hsv)
    triadicA = plt.create_color(triadic_complementary[0])
    triadicB = plt.create_color(triadic_complementary[1])

    analogus = input_color.generate_analogus(input_color.hsv)
    analogusA = plt.create_color(analogus[0])
    analogusB = plt.create_color(analogus[1])


    complement = plt.create_color(input_color.generate_complementary(input_color.hsv))

    palette = {"triadicA": triadicA, "triadicB": triadicB, "analogusA": analogusA, "analogusB": analogusB,
               "complement": complement, "input_color": input_color}

    return palette
    return False


@app.route('/', methods=['POST'])
def color():
    input_color = request.form.get('hex')
    # print(request)
    palete = get_palette(input_color)
    return render_template("index.html", complement=palete.get("complement").get_hexvalue(), triadicA=palete.get('triadicA').get_hexvalue(),
                           triadicB=palete.get("triadicB").get_hexvalue(), analogusB=palete.get('analogusB').get_hexvalue(),
                           analogusA=palete.get('analogusA').get_hexvalue(),
                           input_color=palete.get("input_color").get_hexvalue())

# @app.after_request
# def printrequest(response):
#     print(response)


if __name__ == '__main__':
    app.run()
