from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
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
      <!-- create your form here -->
      <form id="myForm" action="/encrypt" method="post">
        <label for="rotate" >Rotate by: </label>
        <input id="rotate" type="text" name="rot" value="0">
        <textarea type="text" name="text">{0}</textarea>
        <input type="submit">
        <input type="reset" value="Reset Form">
      </form>
    </body>
</html>
"""

@app.route("/encrypt", methods=['POST'])
def encrypt():
  rotation = int(request.form["rot"])
  text = request.form["text"]
  encrypted = rotate_string(text, rotation)
  
  return form.format(encrypted)



@app.route("/")
def index():
    return form.format("")

app.run()