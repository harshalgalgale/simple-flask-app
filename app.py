from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return {'data': 'Hello, World! Welcome to Flask'}


@app.route('/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User {}'.format(username)


@app.route('/add/<numbers>')
def add(numbers):
    # show the user profile for that user
    numbers = split_numbers(numbers)
    return 'Add {}'.format(int(numbers[0])+int(numbers[1]))


def split_numbers(numbers):
    numbers = numbers.split(',')
    return numbers
