import requests
import xml.etree.ElementTree as ET
import re
from config import API_URL, HEADERS

def create_category(name, parent_category_id=2, lang_id=2):
    link_rewrite = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
    
    # Create the XML payload
    prestashop = ET.Element("prestashop", {"xmlns:xlink": "http://www.w3.org/1999/xlink"})
    category = ET.SubElement(prestashop, "category")

    # Define category fields
    ET.SubElement(category, "id_parent").text = str(parent_category_id)
    ET.SubElement(category, "active").text = "1"

    # Category name with language ID
    name_elem = ET.SubElement(category, "name")
    name_lang = ET.SubElement(name_elem, "language", {"id": str(lang_id)})
    name_lang.text = name

    # Link rewrite
    link_rewrite_elem = ET.SubElement(category, "link_rewrite")
    link_rewrite_lang = ET.SubElement(link_rewrite_elem, "language", {"id": str(lang_id)})
    link_rewrite_lang.text = link_rewrite

    # Meta title, description, and keywords
    meta_title_elem = ET.SubElement(category, "meta_title")
    meta_title_lang = ET.SubElement(meta_title_elem, "language", {"id": str(lang_id)})
    meta_title_lang.text = name

    meta_description_elem = ET.SubElement(category, "meta_description")
    meta_description_lang = ET.SubElement(meta_description_elem, "language", {"id": str(lang_id)})
    meta_description_lang.text = f"{name} description."

    meta_keywords_elem = ET.SubElement(category, "meta_keywords")
    meta_keywords_lang = ET.SubElement(meta_keywords_elem, "language", {"id": str(lang_id)})
    meta_keywords_lang.text = "keyword"

    # Convert the XML tree to string
    category_data = ET.tostring(prestashop, encoding="utf-8", method="xml").decode("utf-8")

    # Send POST request to create the category
    endpoint = f"{API_URL}/categories"

    try:
        response = requests.post(endpoint, headers=HEADERS, data=category_data, verify=False)
        
        if response.status_code == 201:
            # Parse the XML response to get the ID of the newly created category
            response_data = ET.fromstring(response.text)
            category_id = response_data.find('.//id').text  # Extract the ID from the XML
            # print(f"Category '{name}' created successfully with ID: {category_id}")
            return category_id
        else:
            print(f"Failed to create category. Status: {response.status_code}")
            print("Response:", response.text)
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
