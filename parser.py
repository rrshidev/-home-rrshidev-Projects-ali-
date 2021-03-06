import xml.etree.ElementTree as ET

tree_client = ET.parse('clientFile.xml');
root_client = tree_client.getroot()
tree_our = ET.parse('ourFile.xml');
root_our = tree_our.getroot()
cnt = 1
cntt = 1
test_list = [0]
dict_our_id, dict_client_id, dict_our_price,dict_client_price, dict_quantity = {}, {}, {}, {}, {}
list_our_id, list_client_id, list_our_price, list_client_price, list_quantity = [], [], [], [], []

# составили словарь айдишек
for offer in root_our.iter('offer'):
    pars = offer.attrib.get('id')
    dict_our_id = dict(id = pars)
    list_our_id.append(dict_our_id) #лепим список из словаря, чтобы устроить сравнение
for product in root_client.iter('product'):
    test = product.attrib.get('prodID')
    dict_client_id = dict(id = test)
    list_client_id.append(dict_client_id)

# составили словарь цен
for price_our in root_our.iter('price'):
    pars_BaseRetailPrice = price_our.attrib.get('BaseRetailPrice')
    pars_BaseWholePrice = price_our.attrib.get('BaseWholePrice')
    pars_RetailPrice = price_our.attrib.get('RetailPrice')
    pars_WholePrice = price_our.attrib.get('WholePrice')
    dict_our_price = dict(BaseRetailPrice = pars_BaseRetailPrice, BaseWholePrice = pars_BaseWholePrice, RetailPrice = pars_RetailPrice, WholePrice = pars_WholePrice)
    list_our_price.append(dict_our_price)
for price_client in root_client.iter('price'):
    pars_BaseRetailPrice = price_client.attrib.get('BaseRetailPrice')
    pars_BaseWholePrice = price_client.attrib.get('BaseWholePrice')
    pars_RetailPrice = price_client.attrib.get('RetailPrice')
    pars_WholePrice = price_client.attrib.get('WholePrice')
    dict_client_price = dict(BaseRetailPrice=pars_BaseRetailPrice, BaseWholePrice=pars_BaseWholePrice,
                          RetailPrice=pars_RetailPrice, WholePrice=pars_WholePrice)
    list_client_price.append(dict_client_price)

# Словарь остатков
for quantity in root_client.iter('assort'):
    pars_sklad = quantity.attrib.get('sklad')
    dict_quantity = dict(quantity=pars_sklad)
    list_quantity.append(dict_quantity)

#Собственно сам парсинг
for id in list_our_id:
    for prod_id in zip(list_client_id):
        if id == prod_id:
            index_id = list_our_id.index(id)
            index_prod_id = list_client_id.index(prod_id)
            list_our_price[index_id] = list_client_price[index_prod_id]


#заливаем list_our_price в наш xml
for price, i, quantity, n in zip(root_our.iter('price'), list_our_price, root_our.iter('quantity'), list_quantity):
    a, b, d = '', '', ''
    for c, f in zip(i.items(), n.items()):
        j = str(c)

        if j.isalpha() is True:
            a = a + j

        elif j.isdigit() is True:
            b = b + j
        g = str(f)
        if g.isdigit() is True:
            d = d + g

    price.set(a, b)
    quantity.text(d)



tree_our.write('ourFile.xml')
