from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My Portfolio</h1>
    <p>Hi, I’m <b>Your Name</b>, a passionate developer!</p>
    <a href='/about'>About</a> | <a href='/projects'>Projects</a>
    """

@app.route("/about")
def about():
    return """
    <h1>About Me</h1>
    <p>I’m a developer specializing in Python, Flask, and web technologies.</p>
    <a href='/'>Home</a> | <a href='/projects'>Projects</a>
    """

@app.route("/projects")
def projects():
    return """
    <h1>My Projects</h1>
    <ul>
        <li><b>Project 1:</b> Flask Web App</li>
        <li><b>Project 2:</b> Machine Learning Model</li>
        <li><b>Project 3:</b> Personal Blog</li>
    </ul>
    <a href='/'>Home</a> | <a href='/about'>About</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
