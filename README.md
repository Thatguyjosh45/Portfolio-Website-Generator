# Portfolio Generator

A simple Python script to generate a portfolio website using the Jinja2 templating engine. This project helps developers and professionals create a static portfolio showcasing their skills, projects, and a brief bio. It's a great starting point for anyone looking to build a personal website with minimal effort.

# Features

Automatically generates a responsive portfolio website.

Customizable sections for:

About Me

Skills

Projects

Uses Jinja2 for dynamic templating.

Lightweight and easy to use.

# Installation

Clone this repository:

git clone https://github.com/yourusername/portfolio-generator.git

Navigate to the project directory:

cd portfolio-generator

Install the required dependencies:

pip install -r requirements.txt

# Usage

Open the script portfolio_generator.py and update the example usage section with your details:

name = "John Doe"
about = "I am a passionate developer with a love for creating impactful software solutions."
skills = ["Python", "JavaScript", "HTML & CSS", "Machine Learning", "Web Development"]
projects = [
    {"name": "Weather App", "link": "https://github.com/johndoe/weather-app"},
    {"name": "Task Tracker", "link": "https://github.com/johndoe/task-tracker"},
    {"name": "Portfolio Generator", "link": "https://github.com/johndoe/portfolio-generator"}
]

Run the script:

python portfolio_generator.py

Your portfolio will be generated in the portfolio directory as index.html.

Open portfolio/index.html in your browser to view the portfolio.

# Example Output

The generated portfolio will include the following sections:

About Me: A brief introduction.

Skills: A list of technical or professional skills.

Projects: A list of projects with names and GitHub links.

# Customization

Template Styling: Update the inline CSS in the HTML_TEMPLATE string to change the look and feel of your portfolio.

Additional Sections: Modify the HTML_TEMPLATE or the Python script to add new sections as needed.

# Dependencies

Python 3.6 or later

Jinja2: Install via pip install Jinja2

# Contribution

Feel free to fork this repository, submit pull requests, or suggest new features. Contributions are welcome
