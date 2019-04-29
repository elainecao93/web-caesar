from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            Rotate by: <input type="text" name="rot"> <br>
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
"""

@app.route("/", methods=["POST"])
def encrypt():
    try:
        rot = int(request.form["rot"])
        inp = request.form["text"]
        out = rotate_string(inp, rot)
    except:
        out =  "The rotation input was invalid."
    return form.format(out)

@app.route("/")
def index():
    return form.format("")

app.run()