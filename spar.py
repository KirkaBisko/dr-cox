import requests

seznam_izdelkov = ['olje', 'kruh', 'moka', 'kis', 'sladkor', 'testenine', 'riž']


seznam = {}
      
for name in seznam_izdelkov:
    url = 'https://search-spar.spar-ics.com/fact-finder/rest/v4/search/products_lmos_si?query=' \
          'IZDELEK&page=1&hitsPerPage=10&useAsn=false&fbclid=IwAR16c5cYQcUWc7LeqE3c_uWTzSpPWeq83aNTjjhQIb_xwjDZz_N9GOnZzjE'      
    link = url.replace('IZDELEK', name)
    html = requests.get(link)
    jsonResponse = html.json()
    hits = jsonResponse.get('hits')
    for hit in hits:
        title = hit.get('masterValues').get('title')
        price = hit.get('masterValues').get('price')
        seznam[title] = price
