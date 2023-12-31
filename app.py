from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))

@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

#-------------------------------------------------------
# Form to retrivethe user's frozen yogurt order
@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template("froyo_form.html")
    
#-------------------------------------------------------
# Shows the user what frozen yogurt they have ordered
@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_topping = request.args.get('toppings')

    context = {
        'users_froyo_flavor': users_froyo_flavor,
        'users_froyo_topping': users_froyo_topping, 
    }

    return render_template("froyo_results.html", **context)

#-------------------------------------------------------
# Form to retrive user's favorite color, animal and city
@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"> <br/>
        What is your favorite animal? <br/>
        <input type="text" name="animal"> <br/>
        What is your favorite city? <br/>
        <input type="text" name="city"> <br/>
        <input type="submit" name="Submit!">
    </form>
    """

#-------------------------------------------------------
#Show the user's favorite color, animal and city
@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_fav_color = request.args.get('color')
    users_fav_animal = request.args.get('animal')
    users_fav_city = request.args.get('city')
    return f'Wow, I didnt know {users_fav_color} {users_fav_animal} lived in {users_fav_city}!'

#-------------------------------------------------------
# Form to retrive the user's secret message
@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Enter a secret message<br/>
        <input type="text" name="message"><br/>
        <input type="submit" name="Submit!">
    </form>
    """

#-------------------------------------------------------
# Show the user's secret message that is sorted
@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_secret_message = request.form.get('message')
    users_new_message = ''.join(sorted(users_secret_message))
    return f"Here is your secret message! {users_new_message}"

#-------------------------------------------------------
# Form to retrive two numbers and perform math based on the option provided by the user
@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template("calculator_form.html")

#-------------------------------------------------------
# Show the user their results of their calculation
@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    users_operator = request.args.get('operation')
    users_operand_1 = request.args.get('operand1')
    users_operand_2 = request.args.get('operand2')
    # Result of adding two number
    users_operand_result = int(users_operand_1 ) + int(users_operand_2)
    # Result of subtracting two numbers
    users_subtract_result = int(users_operand_1 ) - int(users_operand_2)
    # Result of mulitplying two numbers
    users_product_result = int(users_operand_1 ) * int(users_operand_2)
    # Result of divding two numbers
    users_divide_result = int(users_operand_1 ) / int(users_operand_2)

    if users_operator == "add":
        return f'You chose to add {users_operand_1} and {users_operand_2}. Your result is {users_operand_result}'
    elif users_operator == "subtract":
        return f'You chose to subtract {users_operand_1} and {users_operand_2}. Your result is {users_subtract_result}'
    elif users_operator == "multiply":
        return f'You chose to multiply {users_operand_1} and {users_operand_2}. Your result is {users_product_result}'
    elif users_operator == "divide":
        return f'You chose to divide {users_operand_1} and {users_operand_2}. Your result is: {users_divide_result}'
    else:
        return "Not a valid operation or operand, try again"

#-------------------------------------------------------
# Dictionary with key, value pairs where the horoscope is the key and their personality is the value
HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

#-------------------------------------------------------
# Form to retrive the user's horoscope
@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

#-------------------------------------------------------
# Show the user their personality based on their horoscope
@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""
    # Get the sign the user entered in the form, based on their birthday
    horoscope_sign = request.args.get('horoscope_sign')

    # Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = request.args.get('Tell me my personality!')

    # Generate a random number from 1 to 99
    lucky_number = random.randint(1, 99)

    context = {
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
