from flask import Flask, render_template
import create_palete as plt

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", complement=plt.complement.get_hexvalue())


if __name__ == '__main__':
    app.run()
