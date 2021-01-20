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
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_count(self):
        API_url = self.API_URL + 'products/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_get_id(self, product_id):
        API_url = self.API_URL + 'products/' + str(product_id) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_create(self, visibility='hidden', data_01='', data_02='', data_03='', title='', full_title='', description='', content='', brand_id=None,
                        supplier_id=None, delivery_date_id=None):
        API_url = self.API_URL + 'products.json'
        payload = {
            'product': {
                'visibiliy': visibility,
                'data01': str(data_01),
                'data02': str(data_02),
                'data03': str(data_03),
                'title': title,
                'fulltitle': full_title,
                'description': description,
                'content': content,
                'brand': brand_id,
                'supplier': supplier_id,
                'deliverydate': delivery_date_id
            }
        }
        response = requests.post(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def products_update(self, product_id, data01=None, content=None, title=None, full_title=None, brand=None, supplier=None):
        API_url = self.API_URL + 'products/' + str(product_id) + '.json'
        payload = dict()
        if data01:
            payload['product[data01]'] = data01
        if content:
            payload['product[content]'] = content
        if title:
            payload['product[title]'] = title
        if full_title:
            payload['product[fulltitle]'] = full_title
        if brand:
            payload['product[brand]'] = brand
        if supplier:
            payload['product[supplier]'] = supplier
        response = requests.put(API_url, data=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_attribute_get(self, product_id):
        API_url = self.API_URL + 'products/' + str(product_id) + '/attributes.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_attribute_count(self, product_id):
        API_url = self.API_URL + 'products/' + str(product_id) + '/attributes/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_attribute_update(self, product_id, product_attribute_id, value):
        API_url = self.API_URL + 'products/' + str(product_id) + '/attributes/' + str(product_attribute_id) + '.json'
        payload = {'productAttribute[value]': str(value)}
        response = requests.put(API_url, data=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_attribute_delete(self, product_id, product_attribute_id):
        API_url = self.API_URL + 'products/' + str(product_id) + '/attributes/' + str(product_attribute_id) + '.json'
        response = requests.delete(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 204:
            return response.text
        else:
            return None

    def products_metafield_get(self, metafield_id, limit=50, page=1, since_id=0, created_at_min='', created_at_max='', updated_at_min='', updated_at_max=''):
        API_url = self.API_URL + 'products/' + str(metafield_id) + '/metafields.json?'
        API_url = API_url + 'limit=' + str(limit) + '&'
        API_url = API_url + 'page=' + str(page) + '&'
        API_url = API_url + 'since_id' + str(since_id) + '&'
        if created_at_min != '':
            API_url = API_url + 'created_at_min=' + str(created_at_min) + '&'
        if created_at_max != '':
            API_url = API_url + 'created_at_max=' + str(created_at_max) + '&'
        if updated_at_min != '':
            API_url = API_url + 'updated_at_min=' + str(updated_at_min) + '&'
        if updated_at_max != '':
            API_url = API_url + 'updated_at_max=' + str(updated_at_max) + '&'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_metafield_count(self, product_id):
        API_url = self.API_URL + 'products/' + str(product_id) + '/metafields/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_metafield_create(self, product_id, key, value):
        API_url = self.API_URL + 'products/' + str(product_id) + '/metafields.json'
        payload = {
            'productMetafield': {
                'key': key,
                'value': value
            }
        }
        response = requests.post(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def products_metafield_update(self, product_id, metafield_id, key, value):
        API_url = self.API_URL + 'products/' + str(product_id) + '/metafields/' + str(metafield_id) + '.json'
        payload = {
            'productMetafield': {
                'key': key,
                'value': value
            }
        }
        response = requests.put(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_metafield_delete(self, product_id, metafield_id):
        API_url = self.API_URL + 'products/' + str(product_id) + '/metafields/' + str(metafield_id) + '.json'
        response = requests.delete(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 204:
            return response.text
        else:
            return None

    def variants_get(self, product='', article_code='', ean='', sku='', hs='', limit=50, page=1, since_id=0, created_at_min='', created_at_max='', updated_at_min='', updated_at_max=''):
    def products_relation_get(self, product_id):
        API_url = self.API_URL + 'products/' + str(product_id) + '/relations.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_relation_count(self, product_id):
        API_url = self.API_URL + 'products/' + str(product_id) + '/relations/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_relation_get_id(self, product_id, product_id_relation):
        API_url = self.API_URL + 'products/' + str(product_id) + '/relations/' + str(product_id_relation) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_relation_create(self, product_id, product_id_relation):
        API_url = self.API_URL + 'products/' + str(product_id) + '/relations.json'
        payload = {
            'productRelation': {
                'relatedProduct': product_id_relation
            }
        }
        response = requests.post(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def products_relation_delete(self, product_id, product_id_relation):
        API_url = self.API_URL + 'products/' + str(product_id) + '/relations/' + str(product_id_relation) + '.json'
        response = requests.delete(API_url, auth=self.credentials)
        print(response.text)
        self.update_status(response)
        if response.status_code == 204:
            return response.text
        else:
            return None

        API_url = self.API_URL + 'variants.json?'
        if product != '':
            API_url = API_url + 'product=' + str(product) + '&'
        if article_code != '':
            API_url = API_url + 'article_code=' + str(article_code) + '&'
        if ean != '':
            API_url = API_url + 'ean=' + str(ean) + '&'
        if sku:
            API_url = API_url + 'sku=' + str(sku) + '&'
        if hs != '':
            API_url = API_url + 'hs=' + str(hs) + '&'
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
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def variants_count(self):
        API_url = self.API_URL + 'variants/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def variants_get_id(self, variant_id):
        API_url = self.API_URL + 'variants/' + str(variant_id) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
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
    def variants_update(self, variant_id, is_default=None, sort_order=None, article_code=None, ean=None, sku=None, hs=None, price_excl=None, price_incl=None, price_cost=None,
                        old_price_excl=None, old_price_incl=None, stock_tracking=None, stock_level=None, stock_alert=None, stock_minimum=None, stock_sold=None,
                        stock_buy_minimum=None, stock_buy_maximum=None, weight=None, volume=None, colli=None, size_X=None, size_Y=None, size_Z=None, title=None, tax_id=None):
        API_url = self.API_URL + 'variants/' + str(variant_id) + '.json?'
        payload = {
            'variant': {
                'isDefault': is_default,
                'sortOrder': sort_order,
                'articleCode': article_code,
                'ean': ean,
                'sku': sku,
                'hs': hs,
                'priceExcl': price_excl,
                'priceIncl': price_incl,
                'priceCost': price_cost,
                'oldPriceExcl': old_price_excl,
                'oldPriceIncl': old_price_incl,
                'stockTracking': stock_tracking,
                'stockLevel': stock_level,
                'stockMinimum': stock_minimum,
                'stockSold': stock_sold,
                'stockBuyMinimum': stock_buy_minimum,
                'stockBuyMaximum': stock_buy_maximum,
                'weight': weight,
                'volume': volume,
                'colli': colli,
                'sizeX': size_X,
                'sizeY': size_Y,
                'sizeZ': size_Z,
                'title': title,
                'tax': tax_id,
            }
        }
        response = requests.put(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def variants_create(self, product_id, is_default=False, article_code='', ean='', sku='', price_excl=0, price_incl=0, price_cost=0, old_price_excl=0, stock_tracking='disabled',
                        stock_level=100, stock_alert=0, stock_minimum=0, stock_sold=0, stock_buy_minimum=1, stock_buy_maximum=10000, weight=0, volume=0, colli=1, size_X=0,
                        size_Y=0, size_Z=0, title='Default', tax_id=None):
        API_url = self.API_URL + 'variants.json'
        payload = {
            'variant': {
                'isdefault': is_default,
                'articleCode': article_code,
                'ean': ean,
                'sku': sku,
                'priceExcl': price_excl,
                'priceIncl': price_incl,
                'priceCost': price_cost,
                'oldPriceExcl': old_price_excl,
                'stockTracking': stock_tracking,
                'stockLevel': stock_level,
                'stockAlert': stock_alert,
                'stockMinimum': stock_minimum,
                'stockSold': stock_sold,
                'stockBuyMinimum': stock_buy_minimum,
                'stockByMaximum': stock_buy_maximum,
                'weight': weight,
                'volume': volume,
                'colli': colli,
                'sizeX': size_X,
                'sizeY': size_Y,
                'sizeZ': size_Z,
                'title': title,
                'tax': tax_id,
                'product': product_id
            }
        }
        response = requests.post(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

            API_url = API_url + 'created_at_min=' + str(created_at_min) + '&'
        if created_at_max != '':
            API_url = API_url + 'created_at_max=' + str(created_at_max) + '&'
        if updated_at_min != '':
            API_url = API_url + 'updated_at_min=' + str(updated_at_min) + '&'
        if updated_at_max != '':
            API_url = API_url + 'updated_at_max=' + str(updated_at_max) + '&'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def metafields_count(self):
        API_url = self.API_URL + 'metafields/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def metafields_get_id(self, metafield_id):
        API_url = self.API_URL + 'metafields/' + str(metafield_id) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def metafields_create(self, owner_type, owner_id, key, value):
        API_url = self.API_URL + 'metafields.json'
        payload = {'metafield[ownerType]': owner_type, 'metafield[ownerId]': str(owner_id), 'metafield[key]': str(key), 'metafield[value]': str(value), 'metafield[ownerResource]': str(owner_id)}
        response = requests.post(API_url, data=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def metafields_update(self, metafield_id, owner_type, owner_id, key, value):
        API_url = self.API_URL + 'metafields/' + str(metafield_id) + '.json'
        payload = {'metafield[ownerType]': owner_type, 'metafield[ownerId]': str(owner_id), 'metafield[key]': str(key), 'metafield[value]': str(value), 'metafield[ownerResource]': str(owner_id)}
        response = requests.put(API_url, data=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def metafields_delete(self, metafield_id):
        API_url = self.API_URL + 'metafields/' + str(metafield_id) + '.json'
        response = requests.delete(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 204:
            return response.json()
        else:
            return None

    def product_images_get(self, product_id):
        API_url = self.API_URL + 'products/' + str(product_id) + '/images.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def product_images_create(self, product_id, image, file_name):
        API_url = self.API_URL + 'products/' + str(product_id) + '/images.json'
        payload = {
            'productImage': {
                'attachment': image,
                'filename': file_name
            }
        }
        response = requests.post(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    """
    def product_images_create(self, id, image, image_path, image_name):
        API_url = self.API_URL + 'products/' + str(id) + '/images.json'
        headers = {'content-type': 'multipart/form-data'}
        files = {'productImage[attachment]': (image_path, image), 'productImage[filename]': (None, image_name)}
        response = requests.post(API_url, headers=headers, files=files, auth=self.credentials)
        self.update_status(response)
        print(response.status_code)
        if response.status_code == 201:
            return response.json()
        else:
            return None
    """

    def product_images_delete(self, product_id, product_image_id):
        API_url = self.API_URL + 'products/' + str(product_id) + '/images/' + str(product_image_id) + '.json'
        response = requests.delete(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 204:
            return response.text
        else:
            return None

    def product_images_update(self, product_id, product_image_id, sorting_order):
        API_url = self.API_URL + 'products/' + str(product_id) + '/images/' + str(product_image_id) + '.json'
        payload = {'productImage[sortOrder]': str(sorting_order)}
        response = requests.put(API_url, data=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def categories_product_get(self):
        API_url = self.API_URL + 'categories/products.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def categories_product_count(self):
        API_url = self.API_URL + 'categories/products/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def categories_product_get_id(self, category_id):
        API_url = self.API_URL + 'categories/products/' + str(category_id) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def webhook_get(self, limit=50, page=1, since_id=0, created_at_min='', created_at_max='', updated_at_min='', updated_at_max=''):
    def categories_product_create_bulk(self, product_id, category_ids):
        API_url = self.API_URL + 'categories/products/bulk.json'
        payload = {
            'categoriesProduct': {
                'categories': category_ids,
                'product': product_id
            }
        }
        response = requests.post(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def webhook_get(self, limit=50, page=1, since_id=0, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None):
        API_url = self.API_URL + 'webhooks.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def webhook_count(self):
        API_url = self.API_URL + 'webhooks/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def webhook_get_id(self, webhook_id):
        API_url = self.API_URL + 'webhooks/' + str(webhook_id) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def webhook_create(self, is_active, item_group, item_action, address, language='nl', _format='json'):
        API_url = self.API_URL + 'webhooks.json'
        payload = {
            'isActive': is_active,
            'itemGroup': item_group,
            'itemAction': item_action,
            'language': language,
            'format': _format,
            'address': address
        }
        response = requests.post(API_url, data=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def webhook_update(self, webhook_id, is_active, item_group, item_action, address, _format='json'):
        API_url = self.API_URL + 'webhooks/' + str(webhook_id) + '.json'
        payload = {
            'isActive': is_active,
            'itemGroup': item_group,
            'itemAction': item_action,
            'format': _format,
            'address': address
        }
        response = requests.put(API_url, data=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def webhook_delete(self, webhook_id):
        API_url = self.API_URL + 'webhooks/' + str(webhook_id) + '.json'
        response = requests.delete(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def category_image_get(self, category_id):
        API_url = self.API_URL + 'categories/' + str(category_id) + '/image.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def category_image_post(self, category_id, attachment, file_name):
        API_url = self.API_URL + 'categories/' + str(category_id) + '/image.json'
        payload = {
            'categoryImage': {
                'attachment': attachment,
                'filename': file_name
            }
        }
        response = requests.post(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def category_image_delete(self, category_id):
        API_url = self.API_URL + 'categories/' + str(category_id) + '/image.json'
        response = requests.delete(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 204:
            return response.text
        else:
            return None

    def category_get(self, parent):
        API_url = self.API_URL + 'categories.json?fields=id,title'
        if parent:
            API_url = API_url + '&parent=' + str(parent)
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def category_get_id(self, category_id):
        API_url = self.API_URL + 'categories/' + str(category_id) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def category_count(self):
        API_url = self.API_URL + 'categories/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def category_create(self, parent, title, full_title, is_visible=True, _type='category', description='', content=''):
        API_url = self.API_URL + 'categories.json'
        payload = {
            'category': {
                'parent': parent,
                'isVisible': is_visible,
                'type': _type,
                'title': title,
                'full_title': full_title,
                'description': description,
                'content': content
            }
        }
        response = requests.post(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def redirect_get(self):
        API_url = self.API_URL + 'redirects.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def redirect_count(self):
        API_url = self.API_URL + 'redirects/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def redirect_get_id(self, redirect_id):
        API_url = self.API_URL + 'redirects/' + str(redirect_id) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def redirect_create(self, is_permanent, url, target):
        API_url = self.API_URL + 'redirects.json'
        data = {
            'redirect[isPermanent]': is_permanent,
            'redirect[url]': url,
            'redirect[target]': target
        }
        response = requests.post(API_url, data=data, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def brands_count(self):
        API_url = self.API_URL + 'brands/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def brands_get(self, limit=50, page=1,):
        API_url = self.API_URL + 'brands.json?'
        API_url = API_url + 'limit=' + str(limit) + '&'
        API_url = API_url + 'page=' + str(page)
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def suppliers_count(self):
        API_url = self.API_URL + 'metafields/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json
        else:
            return None

    def suppliers_get(self, limit=50, page=1):
        API_url = self.API_URL + 'suppliers.json?'
        API_url = API_url + 'limit=' + str(limit) + '&'
        API_url = API_url + 'page=' + str(page)
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def taxes_get(self):
        API_url = self.API_URL + 'taxes.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def taxes_create(self, rate, title, is_default=False):
        API_url = self.API_URL + 'taxes.json'
        payload = {
            'tax': {
                'isDefault': is_default,
                'rate': rate,
                'title': title
            }
        }
        response = requests.post(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def order_get(self, number=None, page=1, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None):
        API_url = self.API_URL + 'orders.json?'
        if number:
            API_url + API_url + 'number=' + str(number) + '&'
        API_url = API_url + 'page=' + str(page) + '&'
        if created_at_min:
            API_url = API_url + 'created_at_min=' + created_at_min + '&'
        if created_at_max:
            API_url = API_url + 'created_at_max=' + created_at_max + '&'
        if updated_at_min:
            API_url = API_url + 'updated_at_min=' + updated_at_min + '&'
        if updated_at_max:
            API_url = API_url + 'updated_at_max=' + updated_at_max
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def checkout_get(self):
        API_url = self.API_URL + 'checkouts.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def checkout_get_id(self, checkout_id):
        API_url = self.API_URL + 'checkouts/' + str(checkout_id) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def checkout_create_add_product(self, checkout_id, variant_id, quantity=1):
        API_url = self.API_URL + 'checkouts/' + str(checkout_id) + '/products.json'
        payload = {
            'variant_id': variant_id,
            'quantity': quantity
        }
        response = requests.post(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def checkout_create_update_shipping_method(self, checkout_id, delivery_date, delivery_time):
        API_url = self.API_URL + 'checkouts/' + str(checkout_id) + '.json'
        payload = {
            'shipment_method': {
                'id': 'external',
                'title': 'Node Development Migration',
                'price_incl': 0.0,
                'tax_rate': 0.0,
                'data': {
                    'delivery_date': delivery_date,
                    'delivery_time': delivery_time,
                }
            }
        }
        response = requests.put(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def checkout_create_update_payment_method(self, checkout_id):
        API_url = self.API_URL + 'checkouts/' + str(checkout_id) + '.json'
        payload = {
            'payment_method': {
                'id': 'external',
                'title': 'Node Development Migration',
                'price_incl': 0.0,
                'tax_rate': 0.0
            }
        }
        response = requests.put(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def checkout_validate(self, checkout_id):
        API_url = self.API_URL + 'checkouts/' + str(checkout_id) + '/validate.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def checkout_finish(self, checkout_id):
        API_url = self.API_URL + 'checkouts/' + str(checkout_id) + '/order.json'
        response = requests.post(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def customers_get(self, page=1, limit=50):
        API_url = self.API_URL + 'customers.json'
        filters = {
            'page': page,
            'limit': limit
        }
        response = requests.get(API_url, params=filters, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def customers_count(self):
        API_url = self.API_URL + 'customers/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def customers_get_id(self, customer_id):
        API_url = self.API_URL + 'customers/' + str(customer_id) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def customers_create(self, e_mail, first_name, last_name, is_confirmed=True, referral_id='', gender='', birth_date='', national_id='', password='', middle_name='',
                         phone='', mobile='', is_company=False, company_name='', company_coc_number='', company_vat_number='', address_billing_name='', address_billing_street='',
                         address_billing_street_2='', address_billing_number='', address_billing_extenion='', address_billing_zip_code='', address_billing_city='',
                         address_billing_region='', address_billing_country='nl', address_shipping_company='', address_shipping_name='', address_shipping_street='',
                         address_shipping_street_2='', address_shipping_number='', address_shipping_extension='', address_shipping_zip_code='', address_shipping_city='',
                         address_shipping_region='', address_shipping_country='nl', memo='', do_notify_registered=False, do_notify_confirmed=False, do_notify_password=False):
        API_url = self.API_URL + 'customers.json'
        payload = {
            'customer': {
                'isConfirmed': is_confirmed,
                'referralId': referral_id,
                'gender': gender,
                'birthDate': birth_date,
                'nationalId': str(national_id),
                'email': e_mail,
                'password': ''.join((random.choice(string.ascii_letters + string.digits) for i in range(password))) if type(password) is int else password,
                'firstname': first_name,
                'middlename': middle_name,
                'lastname': last_name,
                'phone': phone,
                'mobile': mobile,
                'isCompany': is_company,
                'companyName': company_name,
                'companyCoCNumber': str(company_coc_number),
                'companyVatNumber': str(company_vat_number),
                'addressBillingName': address_billing_name,
                'addressBillingStreet': address_billing_street,
                'addressBillingStreet2': address_billing_street_2,
                'addressBillingNumber': str(address_billing_number),
                'addressBillingExtension': str(address_billing_extenion),
                'addressBillingZipcode': address_billing_zip_code,
                'addressBillingCity': address_billing_city,
                'addressBillingRegion': address_billing_region,
                'addressBillingCountry': address_billing_country,
                'addressShippingCompany': address_shipping_company,
                'addressShippingName': address_shipping_name,
                'addressShippingStreet': address_shipping_street,
                'addressShippingstreet2': address_shipping_street_2,
                'addressShippingNumber': str(address_shipping_number),
                'addressShippingExtension': str(address_shipping_extension),
                'addressShippingZipcode': address_shipping_zip_code,
                'addressShippingCity': address_shipping_city,
                'addressShippingRegion': address_shipping_region,
                'addressShippingCountry': address_shipping_country,
                'memo': memo,
                'doNotifyRegistered': do_notify_registered,
                'doNotifyConfirmed': do_notify_confirmed,
                'doNotifyPassword': do_notify_password
            }
        }
        response = requests.post(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def customers_delete(self, customer_id):
        API_url = self.API_URL + 'customers/' + str(customer_id) + '.json'
        response = requests.delete(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 204:
            return response.text
        else:
            return None

    def discounts_get(self):
        API_url = self.API_URL + 'discounts.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def discounts_count(self):
        API_url = self.API_URL + 'discounts/count.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def discounts_get_id(self, discount_id):
        API_url = self.API_URL + 'discounts/' + str(discount_id) + '.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def discounts_create(self, code, is_active=True, start_date='today', end_date='+1 month', _type='percentage', discount=10, apply_to='all', categories='', products='',
                         shipment='default', usage_limit=10, times_used=0, minimum_amount=0, before_tax=False, minimum_after=True):
        API_url = self.API_URL + 'discounts.json'
        payload = {
            'discount': {
                'code': code,
                'isActive': is_active,
                'startDate': start_date,
                'endDate': end_date,
                'type': _type,
                'discount': discount,
                'applyTo': apply_to,
                'categories': categories,
                'products': products,
                'shipment': shipment,
                'usageLimit': usage_limit,
                'timesUsed': times_used,
                'minimumAmount': float(minimum_amount),
                'before_tax': before_tax,
                'minimum_after': minimum_after
            }
        }
        response = requests.post(API_url, json=payload, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 201:
            return response.text
        else:
            return None

    def account_permissions(self):
        API_url = self.API_URL + 'account/permissions.json'
        response = requests.get(API_url, auth=self.credentials)
        self.update_status(response)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def update_status(self, response):
        self.rate_limit_remaining = response.headers['X-RateLimit-Remaining'].split('/')
        self.rate_limit_reset = response.headers['X-RateLimit-Reset'].split('/')
        self.status_code = response.status_code

    def sleep_reset(self, verbose=False):
        if self.rate_limit_remaining[0] == '-1':
            if verbose:
                print("Waiting for reset")
            for t in reversed(range(1, int(self.rate_limit_reset[0]) + 2)):
                if verbose:
                    print(t, end="\r")
                time.sleep(1)
            if verbose:
                print(0, end="\r")
                print("Restarting requests")
        elif self.rate_limit_remaining[1] == '-1':
            if verbose:
                print("Waiting for reset")
            for t in reversed(range(1, int(self.rate_limit_reset[1]) + 2)):
                if verbose:
                    print(t, end="\r")
                time.sleep(1)
            if verbose:
                print(0, end="\r")
                print("Restarting requests")
        elif self.rate_limit_remaining[2] == '-1':
            if verbose:
                print("Waiting for reset")
            for t in reversed(range(1, int(self.rate_limit_reset[2]) + 2)):
                if verbose:
                    print(t, end="\r")
                time.sleep(1)
            if verbose:
                print(0, end="\r")
                print("Restarting requests")


def number_of_pages(number_of_items, page_size=50):
    return int(number_of_items / page_size) + 1
