from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('output_user_brief.html')


if __name__ == '__main__':
  app.run(debug=True)