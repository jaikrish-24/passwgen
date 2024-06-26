from flask import Flask, render_template, request, jsonify
import random
import array

app = Flask(__name__)

# Maximum length of password needed
PASSWORD_LENGTH = 12

# Declare arrays of the characters that we need in our password
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOWERCASE_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPPERCASE_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SPECIAL_CHARACTERS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

def build_combined_list(preferences):
    combined_list = []
    if 1 in preferences:
        combined_list.extend(UPPERCASE_LETTERS)
    if 2 in preferences:
        combined_list.extend(LOWERCASE_LETTERS)
    if 3 in preferences:
        combined_list.extend(NUMBERS)
    if 4 in preferences:
        combined_list.extend(SPECIAL_CHARACTERS)
    if 5 in preferences:
        combined_list.append(' ')
    return combined_list

def get_random_character(character_list):
    return random.choice(character_list)

def generate_initial_password(combined_list):
    initial_password = ""
    if UPPERCASE_LETTERS[0] in combined_list:
        initial_password += get_random_character(UPPERCASE_LETTERS)
    if LOWERCASE_LETTERS[0] in combined_list:
        initial_password += get_random_character(LOWERCASE_LETTERS)
    if NUMBERS[0] in combined_list:
        initial_password += get_random_character(NUMBERS)
    if SPECIAL_CHARACTERS[0] in combined_list:
        initial_password += get_random_character(SPECIAL_CHARACTERS)
    if ' ' in combined_list:
        initial_password += ' '
    return initial_password

def extend_password(initial_password, combined_list, password_length):
    while len(initial_password) < password_length:
        initial_password += get_random_character(combined_list)
    return initial_password

def shuffle_password(password):
    password_array = array.array('u', password)
    random.shuffle(password_array)
    return ''.join(password_array)

def generate_password(preferences, password_length):
    combined_list = build_combined_list(preferences)
    if not combined_list:
        return ""
    
    initial_password = generate_initial_password(combined_list)
    extended_password = extend_password(initial_password, combined_list, password_length)
    final_password = shuffle_password(extended_password)
    return final_password

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        preferences = request.form.getlist('preferences')
        password_length = int(request.form.get('password_length', 12))
        if preferences:  # Check if any preferences are selected
            preferences = [int(pref) for pref in preferences]
            password = generate_password(preferences, password_length)
    return render_template("index.html", password=password)

@app.route("/generate_password", methods=["POST"])
def generate_password_route():
    data = request.get_json()
    preferences = data.get('preferences', [])
    password_length = data.get('password_length', 12)
    password = generate_password(preferences, password_length)
    return jsonify(password)

if __name__ == "__main__":
    app.run(debug=True)
