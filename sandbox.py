
import requests
from pypardot import client
from dotenv import load_dotenv
from typing import Dict, Optional, List
import os

load_dotenv()

config = dict(
    business_unit_id=os.getenv('business_unit_id'),
    domain=os.getenv('domain'),
    client_id=os.getenv('client_id'),
    client_secret=os.getenv('client_secret')
)

p = client.PardotAPI(**config)
p.authenticate_sp()

records = p.visitors.query(created_after='2025-06-23 12:00:00', only_identified = False)

print(records)
