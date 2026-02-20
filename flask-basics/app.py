from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    greeting = "Welcome to My Personal Site!"
    highlights = [
        "Python enthusiast & developer",
        "Open-source contributor",
        "Lifelong learner",
        "Coffee-powered coder ☕",
    ]
    return render_template('home.html', greeting=greeting, highlights=highlights)

@app.route('/about')
def about():
    person = {
        "name": "Alex Rivera",
        "age": 25,
        "location": "Almaty, Kazakhstan",
        "bio": (
            "I'm a passionate software developer who loves building "
            "useful things with Python and Flask. When I'm not coding, "
            "you'll find me exploring the mountains or reading a good book."
        ),
    }
    skills = ["Python", "Flask", "HTML & CSS", "SQL", "Git"]
    return render_template('about.html', person=person, skills=skills)

@app.route('/hobbies')
def hobbies():
    hobbies_list = [
        {
            "name": "Hiking",
            "emoji": "🏔️",
            "description": "Exploring trails and summiting peaks whenever the weather allows.",
        },
        {
            "name": "Photography",
            "emoji": "📷",
            "description": "Capturing landscapes and street moments with my mirrorless camera.",
        },
        {
            "name": "Reading",
            "emoji": "📚",
            "description": "Sci-fi, history, and the occasional programming book.",
        },
        {
            "name": "Cooking",
            "emoji": "🍳",
            "description": "Experimenting with new recipes from around the world.",
        },
    ]
    favourite = "Hiking"
    return render_template('hobbies.html', hobbies=hobbies_list, favourite=favourite)

if __name__ == '__main__':
    app.run(debug=True)
