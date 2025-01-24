import os
from jinja2 import Template

# Template for the portfolio website
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ name }}'s Portfolio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #007BFF;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }
        section {
            margin: 2rem;
            padding: 1rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #007BFF;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            margin: 0.5rem 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to {{ name }}'s Portfolio</h1>
    </header>
    <section>
        <h2>About Me</h2>
        <p>{{ about }}</p>
    </section>
    <section>
        <h2>Skills</h2>
        <ul>
        {% for skill in skills %}
            <li>{{ skill }}</li>
        {% endfor %}
        </ul>
    </section>
    <section>
        <h2>Projects</h2>
        <ul>
        {% for project in projects %}
            <li>
                <strong>{{ project.name }}</strong>: <a href="{{ project.link }}" target="_blank">{{ project.link }}</a>
            </li>
        {% endfor %}
        </ul>
    </section>
</body>
</html>
"""

def generate_portfolio(name, about, skills, projects, output_dir="portfolio"):
    """
    Generate a portfolio website.

    :param name: Name of the user.
    :param about: A short bio about the user.
    :param skills: A list of skills.
    :param projects: A list of projects, each being a dictionary with 'name' and 'link'.
    :param output_dir: Directory to save the portfolio.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Render the HTML template
    template = Template(HTML_TEMPLATE)
    html_content = template.render(name=name, about=about, skills=skills, projects=projects)

    # Write the HTML file
    with open(os.path.join(output_dir, "index.html"), "w") as f:
        f.write(html_content)

    print(f"Portfolio generated in '{output_dir}/index.html'")

# Example usage
if __name__ == "__main__":
    name = "John Doe"
    about = "I am a passionate developer with a love for creating impactful software solutions."
    skills = ["Python", "JavaScript", "HTML & CSS", "Machine Learning", "Web Development"]
    projects = [
        {"name": "Weather App", "link": "https://github.com/johndoe/weather-app"},
        {"name": "Task Tracker", "link": "https://github.com/johndoe/task-tracker"},
        {"name": "Portfolio Generator", "link": "https://github.com/johndoe/portfolio-generator"}
    ]

    generate_portfolio(name, about, skills, projects)
