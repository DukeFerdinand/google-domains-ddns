import os
from requests import get
from dotenv import load_dotenv

from settings import Settings

load_dotenv()

setup = Settings()
setup.configure(os.environ)

ip = get(os.environ['PUBLIC_IP_SERVICE']).text

url = f'https://{setup.USERNAME}:{setup.PASSWORD}@domains.google.com/nic/update?hostname={setup.DOMAIN}&myip={ip}'
print("Updating public IP...")

res = get(url)
print(res.text)
