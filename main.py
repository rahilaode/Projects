from flask import Flask, request, jsonify, render_template, url_for



app = Flask(__name__)

@app.route('/')
def man():
   return render_template('index.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)