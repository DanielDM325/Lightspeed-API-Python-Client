import requests

class LightspeedAPIClient:
    API_URL = 'https://api.webshopapp.com/nl/'
    API_key = ''
    API_secret = ''

    def __init__(self, API_key, API_secret):
        self.API_key = API_key
        self.API_secret = API_secret


    def products_get(self, brand = '', limit = 50, page = 1, since_id = 0, created_at_min = '', created_at_max = '', updated_at_min = '', updated_at_max = ''):
        API_url = self.API_URL + 'products.json'
        if brand != '':
            API_url = API_url + '?brand=' + str(brand)
        API_url = API_url + '?limit=' + str(limit)
        API_url = API_url + '?page=' + str(page)
        API_url = API_url + '?since_id' + str(since_id)
        if brand != '':
            API_url = API_url + '?brand=' + str(brand)
        if created_at_min != '':
            API_url = API_url + '?created_at_min=' + str(created_at_min)
        if created_at_max != '':
            API_url = API_url + '?created_at_max=' + str(created_at_max)
        if updated_at_min != '':
            API_url = API_url + '?updated_at_min=' + str(updated_at_min)
        if updated_at_max != '':
            API_url = API_url + '?updated_at_max=' + str(updated_at_max)
        return requests.get(API_url, auth=(self.API_key, self.API_secret)).json()
    

    def products_count(self):
        API_url = self.API_URL + 'products/count.json'
        return requests.get(API_url, auth=(self.API_key, self.API_secret)).json()


    def products_get_id(self, id):
        API_url = self.API_URL + 'products/' + str(id) + '.json'
        return requests.get(API_url, auth=(self.API_key, self.API_secret)).json()
