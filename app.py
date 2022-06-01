from flask import Flask, render_template, request, redirect
import create_palete as plt
from flask_bootstrap import Bootstrap
from flask_colorpicker import colorpicker
import re

app = Flask(__name__)

Bootstrap(app)
colorpicker(app)

@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


def get_palette(input_color="#00B2FF"):

    if not re.search('([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$', input_color):
        input_color = "#00B2FF"
    input_color = input_color.lstrip('#')
    input_color = tuple(int(input_color[i:i + 2], 16) for i in (0, 2, 4))
    input_color = plt.Color(input_color[0], input_color[1], input_color[2])

    split_complementary = input_color.generate_split_complementary(input_color.hsv)
    splitA = plt.create_color(split_complementary[0])
    splitB = plt.create_color(split_complementary[1])

    analogus = input_color.generate_analogus(input_color.hsv)
    analogusA = plt.create_color(analogus[0])
    analogusB = plt.create_color(analogus[1])


    complement = plt.create_color(input_color.generate_complementary(input_color.hsv))

    palette = {"splitA": splitA, "splitB": splitB, "analogusA": analogusA, "analogusB": analogusB,
               "complement": complement, "input_color": input_color}

    return palette
    return False


@app.route('/color', methods=['POST'])
def color():
    input_color = request.form.get('hex')
    palete = get_palette(input_color)
    return render_template("index.html", complement=palete.get("complement").get_hexvalue(), splitA=palete.get('splitA').get_hexvalue(),
                           splitB=palete.get("splitB").get_hexvalue(), analogusB=palete.get('analogusB').get_hexvalue(),
                           analogusA=palete.get('analogusA').get_hexvalue(),
                           input_color=palete.get("input_color").get_hexvalue())



if __name__ == '__main__':
    app.run()
