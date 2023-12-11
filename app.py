from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def load_dogs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM dogs"))
    dogs = []
    for row in result.all():
      dogs.append(dict(row._mapping))
  return dogs

@app.route('/')
def hello_world():
  dogs = load_dogs_from_db()
  return render_template('home.html', dogs=dogs)

@app.route('/dogs')
def list_dogs():
  return jsonify(DOGS)

if __name__ == '__main__': app.run(host='0.0.0.0', debug=True)
