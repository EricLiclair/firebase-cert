from db import bucket

STORAGE_LOCATION = f"public" # storage/<path to the >/


def check_if_file_already_exists():
  # check if file already exists
  
  return False


def store_image_in_db(certificate_path, event_name, id):
  file_name = f"{STORAGE_LOCATION}/{event_name}/{id}.{certificate_path.split('.')[-1]}"
  blob = bucket.blob(file_name)
  blob.upload_from_filename(certificate_path)
  blob.make_public()

  return blob.public_url
  

