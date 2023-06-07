from flask import Flask, render_template, request
import requests

app = Flask(__name__)

clients = []


@app.route("/", methods=["GET", "POST"])
def dash():
    if request.method == "POST":
        numbers = request.form.get("numbers")
        message = request.form.get("message")
        client = request.form.get("client")

        # Send the form data to google.com
        response = requests.post(
            f"{client}:5001",
            data={"numbers": numbers, "message": message, "client": client},
        )
        if response.status_code == 200:
            return "Form data posted successfully!"
        else:
            return "Failed to post form data."

    # List of clients for the select option
    # clients = ["client1", "client2"]

    return render_template("dash.html", clients=clients)


@app.route("/ping")
def ping():
    client_ip = request.remote_addr

    if client_ip not in clients:
        clients.append(client_ip)

    print(clients)
    return "Ping received successfully!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
