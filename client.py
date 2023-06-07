from flask import Flask, request
import requests
import schedule
import time
import threading

app = Flask(__name__)


@app.route("/send_msg", methods=["POST"])
def send_msg():
    numbers = request.form.get("numbers")
    message = request.form.get("message")
    client = request.form.get("client")
    sim_num = request.form.get("sim_num")

    # Do something with the form data
    # For this example, we are printing the received data
    print(f"Received message for client {client}:")
    print(f"Numbers: {numbers}")
    print(f"Message: {message}")

    return "Message received successfully!"


def ping_google():
    try:
        response = requests.get("http://192.168.1.102:5000/ping")
        print("Ping success ....")
    except:
        print("Ping Failed")


def run_background_thread():
    schedule.every(30).seconds.do(ping_google)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    # Start the background thread for pinging google.com
    background_thread = threading.Thread(target=run_background_thread)
    background_thread.start()

    app.run(host="0.0.0.0", port=5001)
