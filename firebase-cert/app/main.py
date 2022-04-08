from flask import Flask, request
from db import app
from Certificate import Certificate
app = Flask(__name__)


@app.route('/generate_certificate', methods=['POST'])
def generate_certificate():
  data = request.get_json()
  certificate = Certificate(**data)
  certificate.generate_and_upload_certificate()
  return certificate.get_certificate_details()


if __name__ == "__main__":
  app.run()


