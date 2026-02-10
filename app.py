from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

# Create instance of app
app = Flask(__name__)
# Create empty list to store books user inputs
user_books = []


# Deocrator for Home Dashboard
@app.route("/")
def home_dashboard():
    # Render html file for Home Dashboard
    return render_template("home.html")


# Decorator for Add Book page
# Initialize GET and POST methods for form
@app.route("/add/book", methods=["GET", "POST"])
def add_book():
    # Check if user has submitted form
    if request.method == "POST":
        # Get all book info user submitted in form
        title = request.form.get("title")
        author = request.form.get("author")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")

        # Convert date values into Python objects, remove time portion
        starting_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        ending_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        # Calculate how many days it took to finish book
        duration = (ending_date - starting_date).days + 1

        # Add book info to list that was created earlier
        user_books.append({
            "title": title,
            "author": author,
            "start_date": start_date,
            "end_date": end_date,
            "duration": duration
        })
        # Redirect user to calendar page after submitting form
        return redirect(url_for("calendar"))
    # Render html file for Add Book page
    return render_template("add_book.html")


# Decorator for Calendar page
@app.route("/calendar")
def calendar():
    # Render html file for Calendar page & send data to page
    return render_template("calendar.html", books=user_books)


# decorator for Help page
@app.route("/help")
def help():
    # Render html file for Help page
    return render_template("help.html")


if __name__ == "__main__":
    app.run(debug=True)
