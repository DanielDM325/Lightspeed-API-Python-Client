import requests
import time


class LightspeedAPIClient:
    API_URL = 'https://api.webshopapp.com/nl/'
    credentials = None
    rate_limit_remaining = None
    rate_limit_reset = None
    status_code = None

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
        response = requests.get(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_count(self):
        API_url = self.API_URL + 'products/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_get_id(self, id):
        API_url = self.API_URL + 'products/' + str(id) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None

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
        response = requests.get(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def variants_count(self):
        API_url = self.API_URL + 'variants/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def variants_get_id(self, id):
        API_url = self.API_URL + 'variants/' + str(id) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None

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
        response = requests.get(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def metafields_count(self):
        API_url = self.API_URL + 'metafields/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def metafields_get_id(self, id):
        API_url = self.API_URL + 'metafields/' + str(id) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def metafields_create(self, owner_type, owner_id, key, value):
        API_url = self.API_URL + 'metafields.json'
        payload = {'metafield[ownerType]': owner_type, 'metafield[ownerId]': str(owner_id), 'metafield[key]': str(key), 'metafield[value]': str(value), 'metafield[ownerResource]': str(owner_id)}
        response = requests.post(API_url, data=payload, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def metafields_update(self, metafield_id, owner_type, owner_id, key, value):
        API_url = self.API_URL + 'metafields/' + str(metafield_id) + '.json'
        payload = {'metafield[ownerType]': owner_type, 'metafield[ownerId]': str(owner_id), 'metafield[key]': str(key), 'metafield[value]': str(value), 'metafield[ownerResource]': str(owner_id)}
        response = requests.put(API_url, data=payload, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def metafields_delete(self, metafield_id):
        API_url = self.API_URL + 'metafields/' + str(metafield_id) + '.json'
        response = requests.delete(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 204:
            return response.json()
        else:
            return None

    def product_images_get(self, id):
        API_url = self.API_URL + 'products/' + str(id) + '/images.json'
        response = requests.get(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def product_images_create(self, id, image, file_name):
        API_url = self.API_URL + 'products/' + str(id) + '/images.json'
        payload = {'productImage[attachment]': image, 'productImage[filename]': file_name}
        response = requests.post(API_url, data=payload, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 201:
            return response.json()
        else:
            print(response.status_code)
            return None

    def product_images_delete(self, id, product_image_id):
        API_url = self.API_URL + 'products/' + str(id) + '/images/' + str(product_image_id) + '.json'
        response = requests.delete(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 204:
            return response.text
        else:
            return None

    def product_images_update(self, id, product_image_id, sorting_order):
        API_url = self.API_URL + 'products/' + str(id) + '/images/' + str(product_image_id) + '.json'
        payload = {'productImage[sortOrder]': str(sorting_order)}
        response = requests.put(API_url, data=payload, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def categories_product_get(self):
        API_url = self.API_URL + 'categories/products.json'
        response = requests.get(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def categories_product_count(self):
        API_url = self.API_URL + 'categories/products/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def categories_product_get_id(self, id):
        API_url = self.API_URL + 'categories/products/' + str(id) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code
        if response.status_code == 200:
            return response.json()
        else:
            return None


    def sleep_reset(self):
        if self.rate_limit_remaining[0] == '-1':
            print("Waiting for reset")
            for t in reversed(range(1, int(self.rate_limit_reset[0]) + 1)):
                print(t, end="\r")
                time.sleep(1)
            print(0, end="\r")
            print("Restarting requests")
        elif self.rate_limit_remaining[1] == '-1':
            print("Waiting for reset")
            for t in reversed(range(1, int(self.rate_limit_reset[1]) + 1)):
                print(t, end="\r")
                time.sleep(1)
            print(0, end="\r")
            print("Restarting requests")
        elif self.rate_limit_remaining[2] == '-1':
            print("Waiting for reset")
            for t in reversed(range(1, int(self.rate_limit_reset[2]) + 1)):
                print(t, end="\r")
                time.sleep(1)
            print(0, end="\r")
            print("Restarting requests")
    
    
def number_of_pages(number_of_items, page_size=50):
    return int(number_of_items / page_size) + 1
