from flask import Flask, request
from db import app
from Certificate import Certificate
app = Flask(__name__)


@app.route('/generate_certificate', methods=['POST'])
def generate_certificate():
    data = request.get_json()
    certificate = Certificate(
        name=data["name"],
        certificate_id=data["certificate_id"],
        date=data["date"],
        event_name=data["event_name"],
    )
    response = request.get_json()
    response["certificate_url"] = certificate.get_certificate_url()
    return response


if __name__ == "__main__":
    app.run()
