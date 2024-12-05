from bs4 import BeautifulSoup
import json
import requests




url = 'https://www.immoweb.be/en/classified/house/for-sale/waremme/4300/20311579'
url2= "https://www.immoweb.be/en/classified/house/for-sale/aalst-9300/9300/20313535"
response = requests.get(url2, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"})
response_text = response.text

soup = BeautifulSoup(response_text, 'html.parser')
script_tag = soup.find('script', string=lambda text: text and 'av_items' in text)

# Extract the JavaScript content from the script tag
script_content = script_tag.string

# Extract the av_items JSON from the script content using string manipulation

import re

def extract_energy_certificate(script_content):
    # Regex to find energy_certificate value
    match = re.search(r'"energy_certificate"\s*:\s*"([^"]*)"', script_content)
    
    if match:
        return match.group(1)
    
    return None

energy = extract_energy_certificate(script_content)
print(energy)

"""# Parse the JSON string into a Python object
av_items = json.loads(av_items_json)

# Now you can work with the av_items dictionary
print(av_items)
"""