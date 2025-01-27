from read_json import read_json
from category import create_category
from product import create_product, upload_image
import re
from progress_bar import progress_bar

RESULTS_PATH =  "../scrapper-results/output_json"
CATEGORY_PATH =  f'{RESULTS_PATH}/main_categories.json'


def load_categories(categories, parent_category_id=2): # parent_category_id=2 = Home
    categories_array = []
    categories_len = len(categories)
    counter = 0
    for category in categories:
        counter += 1
        progress_bar(counter, categories_len, prefix='Categories:', suffix='Complete', length=50)

        category_name = category['name'] 
        category_id = create_category(
            name=category_name,
            parent_category_id=parent_category_id
        )

        categories_array.append({"category_id": category_id, "category_name":category_name})
    print("")
    return categories_array


def load_subcategories(category_id, category_name):
    products_array = []
    subcategory_path = f'{RESULTS_PATH}/{category_name}.json'
    subcategories = read_json(path=subcategory_path)
    subcategories_array = subcategories["subcategories"]
    subcategories_len = len(subcategories_array)

    counter = 0
    if subcategories_len == 0: 
        return []

    for subcategory in subcategories_array:
        counter += 1
        progress_bar(counter, subcategories_len, prefix=f'Subcategories for {category_name}:', suffix='Complete', length=50)

        subcategory_name = subcategory["name"]
        subcategory_id = create_category(
            name=subcategory_name,
            parent_category_id=category_id
        )

        products_path = f'{RESULTS_PATH}/{category_name}~{subcategory_name}~produkty.json'
        products = read_json(path=products_path)

        if not products:
            continue
        
        products_array.append({"subcategory_id": subcategory_id, "products": products})
    print("")
    return products_array

        
def load_products(products, subcategory_id):
    products_len = len(products)
    counter = 0
    for product in products:
        counter += 1
        progress_bar(counter, products_len, prefix=f'Products:', suffix='Complete', length=50)

        name = product["name"][:64]
        price = product["price"]
        clean_price = re.sub(r'[^\d,]', '', price).replace(',', '.')
        description_array = product["description"]
        images = product["images"]

        description_acc = ""
        for description in description_array:
            description_acc = description_acc + description 


        # TODO?: add manufacturer
        # manufacturer = product["manufacturer"]

        product_id = create_product(
            category_id=subcategory_id,
            name=name,
            price=clean_price,
            description=description_acc[:512]
        )
        for image in images:
            image_path = f'/Users/tymonmuszynski/Documents/GitHub/pg-biznes/scrapper-results/images_to_jpg/{image}'
            upload_image(
                product_id=product_id,
                image_path=image_path.replace(".webp", ".jpg")
            )
    print("")


categories = read_json(path=CATEGORY_PATH)
categories_array = load_categories(categories=categories)
for category in categories_array:
    products_array = load_subcategories(category_id=category["category_id"], category_name=category["category_name"])
    for products in products_array:
        load_products(products=products["products"], subcategory_id=products["subcategory_id"])
