# SOURCE URL -  https://app.currencyapi.com/api-keys
# api key="cur_live_UUXBKuIuX0t5oBlEOBIUQ76QqHWHXsEhoDBS3kXH" 

import requests
import json

response=requests.get("https://api.currencyapi.com/v3/latest?apikey=cur_live_UUXBKuIuX0t5oBlEOBIUQ76QqHWHXsEhoDBS3kXH")
print(response.status_code)            # 200 if all well
data=response.json()
print(data)
show_data=json.dumps(data,indent=4)   # to show in pretty or easily understandable way
print(show_data)
print(data["data"]["INR"]["value"])   # print a specific value
print()

def currency_converter(amount_in_INR):
    try:
        amount_in_USD=amount_in_INR/ data["data"]["INR"]["value"]
        if amount_in_INR==int or float :
            print(f'The amount is {amount_in_USD}USD')
    except Exception as e:
        print("Enter a valid integer or float value for amount.") 
    
# currency_converter([2,3])  
currency_converter(100)