from flask import Flask, render_template

app = Flask("Test App")


@app.route('/api/saysomething')
def say_something():
    # return """
    # <p>Hello World</p>
    # <hr>
    # <button>Click me</button>
    # """
    my_data = {"username": "user1", "role": "admin"}
    return render_template("template1.html", data_variable=my_data)


if __name__ == "__main__":
    print("Start App")
    app.run("localhost", port=5000)
