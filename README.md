--> Portfolio web app using flask 

A simple Flask web application that takes a user message via a form and displays it back on the page.  
This project demonstrates Flask routing, HTML rendering, and form handling.

---

-->  Features
- Accepts user input from an HTML form.
- Displays the submitted message on the same page.
- Handles empty input gracefully with a default message.
- Uses a templates folder for HTML and static folder for CSS.

---

--> project Structure
│── app.py # Main Python file
│── templates/ 
│ └── index.html 
| └── contact.html
│── static/
│ └── style.css 

--> How to run
- python portfolio.py
- flask run