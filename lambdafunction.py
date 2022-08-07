
def elidgible_for_cse():
    
    
if event["currentIntent"]["slots"]["marks"] == "marks">90 :
    
    
return "You are elidgible to take admission in CSE."

else :
    
    return "Sorry !!..You are not elidgible to take admission in CSE."
    
    



def elidgible_for_eee():

if event["currentIntent"]["slots"]["marks"] == 80>"marks">90 :
    
return "You are elidgible to take admission in EEE."


 
else :
    
    return "Sorry !!..You are not elidgible to take admission in EEE."




def lambda_handler(event, context):
response = {
    "dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
        "message": {
          "contentType": "PlainText"
        }
    }
}
print(event)

    if event["currentIntent"]["slots"]["branch"] == "cse":
        
        response["dialogAction"]["message"]["content"] = elidgible_for_cse()
    else:
        response["dialogAction"]["message"]["content"] = elidgible_for_eee()
        
        
return response
