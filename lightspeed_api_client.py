import requests
import base64


class LightspeedAPIClient:
    API_URL = 'https://api.webshopapp.com/nl/'
    credentials = None

    def __init__(self, API_key, API_secret):
        self.credentials = (API_key, API_secret)

    def products_get(self, brand='', limit=50, page=1, since_id=0, created_at_min='', created_at_max='', updated_at_min='', updated_at_max=''):
        API_url = self.API_URL + 'products.json?'
        if brand != '':
            API_url = API_url + 'brand=' + str(brand) + '&'
        API_url = API_url + 'limit=' + str(limit) + '&'
        API_url = API_url + 'page=' + str(page) + '&'
        API_url = API_url + 'since_id' + str(since_id) + '&'
        if brand != '':
            API_url = API_url + 'brand=' + str(brand) + '&'
        if created_at_min != '':
            API_url = API_url + 'created_at_min=' + str(created_at_min) + '&'
        if created_at_max != '':
            API_url = API_url + 'created_at_max=' + str(created_at_max) + '&'
        if updated_at_min != '':
            API_url = API_url + 'updated_at_min=' + str(updated_at_min) + '&'
        if updated_at_max != '':
            API_url = API_url + 'updated_at_max=' + str(updated_at_max) + '&'
        return requests.get(API_url, auth=self.credentials).json()

    def products_count(self):
        API_url = self.API_URL + 'products/count.json'
        return requests.get(API_url, auth=self.credentials).json()

    def products_get_id(self, id):
        API_url = self.API_URL + 'products/' + str(id) + '.json'
        return requests.get(API_url, auth=self.credentials).json()

    def variants_get(self, product='', article_code='', ean='', sku='', hs='', limit=50, page=1, since_id=0, created_at_min='', created_at_max='', updated_at_min='', updated_at_max=''):
        API_url = self.API_URL + 'variants.json?'
        if product != '':
            API_url = API_url + 'product=' + str(product) + '&'
        if article_code != '':
            API_url = API_url + 'article_code=' + str(article_code) + '&'
        if ean != '':
            API_url = API_url + 'ean=' + str(ean) + '&'
        if sku != '':
            API_url = API_url + 'sku=' + str(sku) + '&'
        if hs != '':
            API_url = API_url + 'product=' + str(hs) + '&'
        API_url = API_url + 'limit=' + str(limit) + '&'
        API_url = API_url + 'page=' + str(page) + '&'
        API_url = API_url + 'since_id=' + str(since_id) + '&'
        if created_at_min != '':
            API_url = API_url + 'created_at_min=' + str(created_at_min) + '&'
        if created_at_max != '':
            API_url = API_url + 'created_at_max=' + str(created_at_max) + '&'
        if updated_at_min != '':
            API_url = API_url + 'updated_at_min=' + str(updated_at_min) + '&'
        if updated_at_max != '':
            API_url = API_url + 'updated_at_max=' + str(updated_at_max) + '&'
        return requests.get(API_url, auth=self.credentials).json()

    def variants_count(self):
        API_url = self.API_URL + 'variants/count.json'
        return requests.get(API_url, auth=self.credentials).json()

    def variants_get_id(self, id):
        API_url = self.API_URL + 'variants/' + str(id) + '.json'
        return requests.get(API_url, auth=self.credentials).json()

    def metafields_get(self, limit=50, page=1, since_id=0, created_at_min='', created_at_max='', updated_at_min='', updated_at_max=''):
        API_url = self.API_URL + 'metafields.json?'
        API_url = API_url + 'limit=' + str(limit) + '&'
        API_url = API_url + 'page=' + str(page) + '&'
        API_url = API_url + 'since_id=' + str(since_id) + '&'
        if created_at_min != '':
            API_url = API_url + 'created_at_min=' + str(created_at_min) + '&'
        if created_at_max != '':
            API_url = API_url + 'created_at_max=' + str(created_at_max) + '&'
        if updated_at_min != '':
            API_url = API_url + 'updated_at_min=' + str(updated_at_min) + '&'
        if updated_at_max != '':
            API_url = API_url + 'updated_at_max=' + str(updated_at_max) + '&'
        return requests.get(API_url, auth=self.credentials).json()

    def metafields_count(self):
        API_url = self.API_URL + 'metafields/count.json'
        return requests.get(API_url, auth=self.credentials).json()

    def metafields_get_id(self, id):
        API_url = self.API_URL + 'metafields/' + str(id) + '.json'
        return requests.get(API_url, auth=self.credentials).json()

    def metafields_create(self, owner_type, owner_id, key, value):
        API_url = self.API_URL + 'metafields.json'
        payload = {'metafield[ownerType]' : owner_type, 'metafield[ownerId]' : str(owner_id), 'metafield[key]' : str(key), 'metafield[value]' : str(value), 'metafield[ownerResource]' : str(owner_id)}
        print(payload)
        return requests.post(API_url, data=payload, auth=self.credentials).json()
    
    def product_images_get(self, id):
        API_url = self.API_URL + 'products/' + str(id) + '/images.json'
        return requests.get(API_url, auth=self.credentials).json()

    def product_images_create(self, id, image_path, file_name):
        API_url = self.API_URL + 'products/' + str(id) + '/images.json'
        image = open(image_path, mode='rb').read()
        attachment = base64.b64encode(image)
        payload = {'productImage[attachment]' : attachment, 'productImage[filename]' : file_name}
        return requests.post(API_url, data=payload, auth=self.credentials).json()
    
    def product_images_delete(self, id, product_image_id):
        API_url = self.API_URL + 'products/' + str(id) + '/images/' + str(product_image_id) + '.json'
        return requests.delete(API_url, auth=self.credentials)

    def product_images_update(self, id, product_image_id, sorting_order):
        API_url = self.API_URL + 'products/' + str(id) + '/images/' + str(product_image_id) + '.json'
        payload = {'productImage[sortOrder]' : str(sorting_order)}
        return requests.put(API_url, data=payload, auth=self.credentials).json()


def number_of_pages(number_of_items, page_size=50):
    return int(number_of_items / page_size) + 1
