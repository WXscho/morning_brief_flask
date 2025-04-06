from flask import Flask, render_template
import os
print(os.listdir('templates'))
app = Flask(__name__)

@app.route('/')
def brief():
  return render_template('base.html')


if __name__ == '__main__':
  app.run(debug=True)