from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {
        "NAME": u"Mom",
        "Number": u"+91 912345678",
        "done": False,
        "id": 1
    },
    {
        "NAME": u"Add Numbers",
        "NUMBER": u"+91 987654321",
        "done": False,
        "id": 1,
    },
]
@app.route("/")
def contact():
    return "Contact List"
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the required information",

        }, 400)
    task = {
        "id": tasks[-1]["id"]+1,
        "title": request.json["Name"],
        "description": request.json.get("NUMBER",""),
        "done": False
    }
    tasks.append(task)
    return jsonify({
        "status": "Success",
        "message": "contact stored successfully",
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })
if (__name__== "__main__"):
    app.run(debug = True)