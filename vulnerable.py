from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route("/ping")
def ping():
    host = request.args.get("host")

    # Intentionally vulnerable code for CodeQL testing.
    subprocess.call(f"ping -c 1 {host}", shell=True)

    return "Ping executed"


if __name__ == "__main__":
    app.run()
