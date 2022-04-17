from asyncio import events
import json

# import requests


def lambda_handler(event, context):

    print(event)
    personId = event['queryStringParameters']['personId']
    # personId = event['test']
    # personId = "TestingCloudFormation"
    # myfirstname = event.name
    # mylastname = event.lastname
   

    return {
        "statusCode": 200,
        "body": json.dumps({
            # "name": myfirstname + " " + mylastname +" from Lambda" ,
             "personId": personId + " from Lambda"
        }),
    }
