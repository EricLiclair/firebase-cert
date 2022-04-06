from datetime import date
import os
from time import sleep
from dateutil.parser import parse

from db_utils import store_image_in_db


cwd = os.getcwd()


class Certificate:
  def __init__(self, 
  name: str, 
  id: int, 
  date: date
  ) -> None:
      self.name = name
      self.id = id
      self.date = parse(date)
      self.certificate_url = None
  
  

  def _upload_generated_certificate(self, certificate_path):
    print('uploading certificate...', self.id)
    file_stored = store_image_in_db(certificate_path, self.id)
    print('file uploaded at', file_stored)
    print('deleting temporary image at', certificate_path)
    return file_stored


  def generate_certificate(self):
    print('generating certificate...')
    sleep(1)
    print('details - ', self.name, self.id, self.date)
    generated_certificate_path = cwd + f"/app/assets/testimg.jpg"
    return generated_certificate_path

  
  def generate_and_upload_certificate(self):
    certificate_path = self.generate_certificate()
    generated_certificate_url = self._upload_generated_certificate(certificate_path=certificate_path)
    self.certificate_url = generated_certificate_url

  
  def get_certificate_details(self):

    return {
      "name": self.name,
      "id": self.id,
      "date": self.date,
      "certificate_url": self.certificate_url
    }

    