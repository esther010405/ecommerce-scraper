import requests
from bs4 import BeautifulSoup

def get_products():
    
    url = "https://www.jumia.com.ng/"
    data=[]
    headers= {
        "User-Agent":
        "Mozilla/5.0"
    }
    response= requests.get(url, headers=headers)

    print( response.status_code)
    soup= BeautifulSoup (
        response.text,
        "html.parser"
    )
    
    products =soup.find_all("article", class_= "prd")

    
    for product in products :
        nom_tag= product.find( "div" , class_= "name")
        prix_tag= product.find("div", class_= "prc")

        if not nom_tag or not prix_tag:
            continue

        nom= nom_tag.text.strip()
        prix= prix_tag.text.strip()
        img= product.find("img")
        if img:
            image= img.get("data-src", "")
        else :
            image= ""

        data.append({
            "Nom": nom,
            "Prix":prix,
            "image": image
        })
    print( data )

    return data
get_products()