from calendar import c
import json
from tokenize import String
from turtle import clear
from numpy import empty
import requests
import pandas as pd


data = []
variantSKU = []
idSeller = []


def variantSKU_WritterPE(skuVariable):   
    # print(type(skuVariable))
    for newApiRequest in skuVariable:
        print(newApiRequest)
        

        # {Contenido PE}

        url = f"https://api-pe.ripley.com/marketplace/ecommerce/search/v1/pe/products/by-sku/{newApiRequest}"

        payload={}
        headers = {
        'Cookie': '__cf_bm=AkvOddY1jUq5UOOUJZmyaqUF7MKJ2cwH1SxvF3XdrTU-1661547620-0-AS2a70t+0+ZFYrKcz+tW7rycoiwmCoCOoG/5wamUd79INlDGj3p7Qhk2pODv0lk6nDdoOGi80vn+uMmhioGjWl8='
        }

        responseCn = requests.request("GET", url, headers=headers, data=payload)



        # {Contenido}
        # url = f"https://api.ripley.com/marketplace/ecommerce/search/v1/cl/products/by-sku/{newApiRequest}?code=false&filter=false"

        # payload={}
        # headers = {
        # 'Cookie': '__cf_bm=xmkvYQsiDNt3WrA3GcaHROHP_JNwnuc2e9gLmEZ93sY-1650080271-0-AV3GJQdulRGdnGopTca2N1OKlDJxQHeXZZ+hCaVsSNiS0yuL6p/vdDMtbbzH4bdq8FGNvmLzdCfwLR5ggkIkKd4='
        # }

        # responseCn = requests.request("GET", url, headers=headers, data=payload)

        if responseCn.status_code == 200:
            cnData = responseCn.json()
            for item in cnData['related']:
                print(str(item['sku'])) 
                variantSKU.append(str(item['sku']))
                
        if responseCn.status_code == 204:
            print("No hay respuesta desde el sevidor")            
        break

    return variantSKU


def idSeller_WritterPE(skuVariable):   
    # print(type(skuVariable))
    for newApiRequest in skuVariable:
        print(newApiRequest)
        
        # {Contenido}
        url = f"https://api-pe.ripley.com/marketplace/ecommerce/search/v1/pe/products/by-sku/{newApiRequest}"

        payload={}
        headers = {
        'Cookie': '__cf_bm=AkvOddY1jUq5UOOUJZmyaqUF7MKJ2cwH1SxvF3XdrTU-1661547620-0-AS2a70t+0+ZFYrKcz+tW7rycoiwmCoCOoG/5wamUd79INlDGj3p7Qhk2pODv0lk6nDdoOGi80vn+uMmhioGjWl8='
        }

        responseCn = requests.request("GET", url, headers=headers, data=payload)

        
        
        if responseCn.status_code == 200:
            cnData = responseCn.json()
            for item in cnData['related']:
                print(str(item['shop']['id']))
                idSeller.append(str(item['shop']['id']))
                
        if responseCn.status_code == 204:
            print("No hay respuesta desde el sevidor")            
        break

    return idSeller



def variantSKU_WritterCL(skuVariable):   
    # print(type(skuVariable))
    for newApiRequest in skuVariable:
        print(newApiRequest)
        
        # {Contenido}
        url = f"https://api.ripley.com/marketplace/ecommerce/search/v1/cl/products/by-sku/{newApiRequest}?code=false&filter=false"

        payload={}
        headers = {
        'Cookie': '__cf_bm=xmkvYQsiDNt3WrA3GcaHROHP_JNwnuc2e9gLmEZ93sY-1650080271-0-AV3GJQdulRGdnGopTca2N1OKlDJxQHeXZZ+hCaVsSNiS0yuL6p/vdDMtbbzH4bdq8FGNvmLzdCfwLR5ggkIkKd4='
        }

        responseCn = requests.request("GET", url, headers=headers, data=payload)

        if responseCn.status_code == 200:
            cnData = responseCn.json()
            for item in cnData['related']:
                print(str(item['sku'])) 
                variantSKU.append(str(item['sku']))
                
        if responseCn.status_code == 204:
            print("No hay respuesta desde el sevidor")            
        break

    return variantSKU


def idSeller_WritterCL(skuVariable):   
    # print(type(skuVariable))
    for newApiRequest in skuVariable:
        print(newApiRequest)
        
        # {Contenido}
        url = f"https://api.ripley.com/marketplace/ecommerce/search/v1/cl/products/by-sku/{newApiRequest}?code=false&filter=false"

        payload={}
        headers = {
        'Cookie': '__cf_bm=xmkvYQsiDNt3WrA3GcaHROHP_JNwnuc2e9gLmEZ93sY-1650080271-0-AV3GJQdulRGdnGopTca2N1OKlDJxQHeXZZ+hCaVsSNiS0yuL6p/vdDMtbbzH4bdq8FGNvmLzdCfwLR5ggkIkKd4='
        }

        responseCn = requests.request("GET", url, headers=headers, data=payload)

        
        
        if responseCn.status_code == 200:
            cnData = responseCn.json()
            for item in cnData['related']:
                print(str(item['shop']['id']))
                idSeller.append(str(item['shop']['id']))
                
        if responseCn.status_code == 204:
            print("No hay respuesta desde el sevidor")            
        break

    return idSeller