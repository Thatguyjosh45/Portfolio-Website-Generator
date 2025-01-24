import os
from jinja2 import Template

# Template for the portfolio website (HTML)
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ name }}'s Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <div class="left">
                <a href="#about-section">{{ name }}</a>
            </div>
            <div class="right">
                <a href="#about-section">About</a>
                <a href="#projects-section">Projects</a>
                <a href="#skills-section">Skills</a>
                <a href="#leave-message-section">Leave a Message!</a>
            </div>
        </nav>
    </header>

    <section id="about-section">
        <h2>Hey, I'm {{ name }}!</h2>
        <div class="bio">
            <p>{{ about }}</p>
        </div>
    </section>

    <div class="divider"></div>

    <section id="projects-section">
        <h2>Projects</h2>
        <div class="project-subsection">
            <h3>Software</h3>
            <div class="projects-scroll-container">
                {% for project in projects %}
                    <div class="project-box">
                        <a href="{{ project.link }}" target="_blank">
                            <h4>{{ project.name }}</h4>
                            <p>{{ project.description }}</p>
                        </a>
                    </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <div class="divider"></div>

    <section id="skills-section">
        <h2>Skills</h2>
        <div class="skills-container">
            {% for skill in skills %}
                <i class="fa-brands fa-{{ skill }}"></i>
            {% endfor %}
        </div>
    </section>

    <div class="divider"></div>

    <section id="leave-message-section">
        <h2>Leave a Message!</h2>
        <p>coming soon :)</p>
    </section>

    <footer>
        <p>&copy; {{ year }} {{ name }}. All Rights Reserved.</p>
    </footer>
</body>
</html>
"""

# CSS for the portfolio website
CSS_CONTENT = """/* Base Styles */
:root {
    --text-color: #1a1c20;
    --link-color: #ffffff;
    --background-color: #eeeff1;
    font-size: 14px; /* Set the base font size */
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
    scroll-padding-top: 5rem; /* Adjust this value based on the height of your nav bar */
}

body {
    font-family: 'Steph', sans-serif;
    background-color: var(--background-color);
}

a {
    color: var(--text-color);
    text-decoration: none;
}

nav {
    background-color: #bfd6c4;
    display: flex;
    justify-content: space-between;
    padding: 0 3.125rem;
    height: 4rem;
    align-items: center;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
    background-color: rgba(191, 214, 196, 0.9);
    backdrop-filter: blur(5px);
}

nav .left a {
    color: var(--text-color);
    font-size: 1.5rem;
    font-weight: 600;
}

nav .right a {
    color: var(--text-color);
    font-size: 1.375rem;
    margin: 0 0.625rem;
}

nav .right a:hover {
    color: var(--link-color);
    transition: color 0.3s ease-in-out;
}

section {
    padding: 8rem 2rem;
    min-height: 80vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 2rem;
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

section h2 {
    font-size: 3rem;
    font-weight: 700;
    color: var(--text-color);
}

.project-box {
    border: 1px solid #d7dbd8;
    border-radius: 0.5rem;
    padding: 1rem;
    background-color: #f9f9f9;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.skills-container {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
}

.skills-container i {
    font-size: 3rem;
    color: #588061;
    transition: transform 0.3s ease, color 0.3s ease;
}

.skills-container i:hover {
    transform: scale(1.2);
    color: #a5d6b0;
}
"""

def generate_portfolio(name, about, skills, projects, output_dir="portfolio"):
    """
    Generate a portfolio website.

    :param name: Name of the user.
    :param about: A short bio about the user.
    :param skills: A list of skills (as icons).
    :param projects: A list of projects, each being a dictionary with 'name', 'link', and 'description'.
    :param output_dir: Directory to save the portfolio.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Render the HTML template
    template = Template(HTML_TEMPLATE)
    html_content = template.render(name=name, about=about, skills=skills, projects=projects, year=2025)

    # Write the HTML file
    with open(os.path.join(output_dir, "index.html"), "w") as f:
        f.write(html_content)

    # Write the CSS file
    with open(os.path.join(output_dir, "styles.css"), "w") as f:
        f.write(CSS_CONTENT)

    print(f"Portfolio generated in '{output_dir}/index.html' and '{output_dir}/styles.css'")

# Example usage
if __name__ == "__main__":
    name = "John doe"
    about = "Hey! I'm John, a high school student passionate about software development and UX design."
    skills = ["python", "html5", "javascript", "css3-alt", "figma", "java"]
    projects = [
        {"name": "Floppy Fish", "link": "https://github.com/stephanieran/floppy-fish", "description": "Floppy Fish is a spinoff of Flappy Bird built in Java."},
        {"name": "Circles", "link": "https://github.com/stephanieran/circles", "description": "A photo sharing app with daily prompts."},
        {"name": "Github Issues", "link": "https://github.com/stephanieran/github-issues", "description": "An iOS app to streamline GitHub Issues access."}
    ]

    generate_portfolio(name, about, skills, projects)
