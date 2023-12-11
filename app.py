from flask import Flask, render_template, jsonify

app = Flask(__name__)

DOGS = [
    {
        'id':
        1,
        'name':
        "Beignet",
        'gender':
        'Female',
        'breed':
        'Sheperd/Husky',
        'age':
        '8 months',
        'size':
        '30 lbs',
        'Time on Shelter':
        '30 days',
        'Good with dogs':
        'Yes',
        'Good with cats':
        'Yes',
        'Good with children':
        'Yes',
        'Housetrained':
        'Yes',
        'Spayed/Neutered':
        'Yes',
        'Description':
        'Beignet is a happy sweet girl. She is friendly with cats, kids, dogs, leash, and crate/house trained!'
    },
    {
        'id':
        2,
        'name':
        "Billy Joe",
        'gender':
        'Male',
        'breed':
        'Border Collie/Chihuahua',
        'age':
        '20 weeks',
        'size':
        '16 lbs',
        'Time on Shelter':
        '1 day',
        'Good with dogs':
        'Yes',
        'Good with cats':
        'Unknown',
        'Good with children':
        'Unknown',
        'Housetrained':
        'Selective',
        'Spayed/Neutered':
        'Yes',
        'Description':
        'Like all puppies Billy Joe is energetic, but also very sweet and loves attention, hugs and snuggles. He has been great with all the new adults he has encountered. Billy Joe has not interacted with any children, but he is a puppy and should be fine with respectful kids. He plays well with other dogs, but has not been cat tested. Billy Joe does well in his crate and is working hard on his house training. He is going to make a wonderful addition to any household.'
    },
    {
        'id':
        3,
        'name':
        "Blair",
        'gender':
        'Female',
        'breed':
        'Hound/Mix',
        'age':
        '7 months',
        'size':
        '51 lbs',
        'Time on Shelter':
        '4 weeks',
        'Good with dogs':
        'Yes',
        'Good with cats':
        'Unknown',
        'Good with children':
        'Unknown',
        'Housetrained':
        'Yes',
        'Spayed/Neutered':
        'Yes',
        'Description':
        """Blair is a true sweetheart! She doesnt hesitate to give every human she passes a gentle hug! She loves to play with her doggie friends but also has no problem entertaining herself with toys of all kinds, she especially loves squeaky toys! she knows a few basic manners but knows her sweet face can help her get away with anything! Blair would make an amazing addition to any household who's active to keep up with her little bursts of energy!
    """
    },
]


@app.route('/')
def hello_world():
  return render_template('home.html', dogs=DOGS)

@app.route('/dogs')
def list_dogs():
  return jsonify(DOGS)

if __name__ == '__main__': app.run(host='0.0.0.0', debug=True)
