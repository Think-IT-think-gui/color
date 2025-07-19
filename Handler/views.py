from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import uuid
import requests

class Transaction(APIView):
    def post(self , request):
        data = {
    "RecipientName": "Name",
    "RecipientMsisdn":"Number",
    "CustomerEmail": "Email",
    "Channel": "Type",
    "Amount": "Amount",
    "PrimaryCallbackUrl": "	https://webhook.site/d4549a7d-32d1-4f22-b99f-12c28377fec4",
    "Description": "Withdrawal",

      }
        response = requests.post('https://webhook.site/6b3ae430-950e-414f-8533-29f2ece7dfec', json=data)
        return Response(response.text)
     

class Pay_Transaction(APIView):
    def post(self , request):
       Hubtel_Prepaid_Deposit_ID = '2016922'
       url = f'https://smp.hubtel.com/api/merchants/{Hubtel_Prepaid_Deposit_ID}/send/mobilemoney'
       url = 'https://webhook.site/e8faaf1c-622f-4828-89fe-7b1303af9472'
       key = 'MFlwelFCRzoyZWU3OGU5YWE2ZTM0NDQ0OGFmMzRjNTI1ODcwNTlkYg=='

       header = {
    'Authorization': f'Basic {key}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Cache-Control': 'no-cache'
       }

       data = {
    "RecipientName": request.data["Name"],
    "RecipientMsisdn": request.data["Number"],
    "CustomerEmail": request.data["Email"],
    "Channel": request.data["Type"],
    "Amount": request.data["Amount"],
    "PrimaryCallbackUrl": "	https://webhook.site/d4549a7d-32d1-4f22-b99f-12c28377fec4",
    "Description": "Withdrawal",
    "ClientReference": f"Ref-{str(uuid.uuid1())}"
      }

       response = requests.post(url, headers=header, json=data)

       if response.status_code == 401:
            print("Authentication failed. Check your API key.")
       else:
           print(response.text)
       return Response(response.text)




       # except:
        #   return Response('No')
