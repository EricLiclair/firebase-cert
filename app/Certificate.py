from datetime import date
import os
from time import sleep
from dateutil.parser import parse

from db_utils import store_image_in_db

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont




cwd = os.getcwd()


class Certificate:
  def __init__(self, 
  name: str, 
  id: str, 
  date: date,
  event_name: str
  ) -> None:
      self.name = name
      self.id = id
      self.date = parse(date)
      self.certificate_url = None
      self.event_name = event_name
      self.certificate_path = None
  
  

  def _upload_generated_certificate(self, certificate_path):
    print('uploading certificate...', self.id)
    file_stored = store_image_in_db(certificate_path, self.event_name, self.id)
    print('file uploaded at', file_stored)
    self.delete_folder()
    print('deleting temporary image at', certificate_path)
    return file_stored

# here i have given a particular path to create a folder 
  
  def create_os(self) :
      directory = "certificates"
      parent_dir = cwd + "/app/der1"
      path = os.path.join(parent_dir, directory) 
      try :
          os.mkdir(path)
          return path
      except :
          return path

  def delete_folder(self):
    path_end = os.path.join(temp, self.id)
    #list_dir = os.listdir(temp)
    #print(list_dir)
    os.remove(f"{path_end}.png")
    os.rmdir(temp)
    print("temporary folder deleted")
    

  def generate_certificate(self):
    print('generating certificate...')
    im = Image.open(cwd + "/app/der1/Kotlin.png")
    draw= ImageDraw.Draw(im)
    myfont = ImageFont.truetype(cwd + "/app/der1/Google-sans-Font-Family/ProductSans-Black.ttf",size = 50)
    myfont2 = ImageFont.truetype(cwd + "/app/der1/Google-sans-Font-Family/ProductSans-Regular.ttf",size = 25)
    W,H = im.size
    w , h =draw.textsize(self.name , font=myfont)
    draw.text(((W-w)/2 ,297) , self.name ,font = myfont ,  fill=(71,218 ,136))
    draw.text((100,100) , self.id , font = myfont2 , fill = (71,218,136))
    global temp
    temp = self.create_os()
    file_path = f"{temp}/{self.id}.png"
    im.save(file_path)
    print('details - ', self.name, self.id, self.date)
    generated_certificate_path = file_path
    return generated_certificate_path

  
  def generate_and_upload_certificate(self):
    certificate_path = self.generate_certificate()
    print(certificate_path)
    generated_certificate_url = self._upload_generated_certificate(certificate_path=certificate_path)
    self.certificate_url = generated_certificate_url

  
  def get_certificate_details(self):

    return {
      "name": self.name,
      "id": self.id,
      "date": self.date,
      "certificate_url": self.certificate_url
    }

    