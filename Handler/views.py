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
       print(request.data)
       url = f'https://smp.hubtel.com/api/merchants/{Hubtel_Prepaid_Deposit_ID}/send/mobilemoney'
# ###      url = 'https://webhook.site/e8faaf1c-622f-4828-89fe-7b1303af9472'
       key = 'Wm14elFCNTphMjgyMjEyYjVkNzY0NDkzYTY5NzZkNWQwMDk2ZTYzMw=='

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
#    "PrimaryCallbackUrl": "https://webhook.site/ed33a505-d5e4-42c4-83ba-540f3e6ecad4", 
    "PrimaryCallbackUrl": request.data["Url"], 
   "Description": "Withdrawal",
    "ClientReference": request.data["ClientReference"]
      }

       response1 = requests.post(url, headers=header, json=data)
    #   print(response1.json())
     #  print(response1.json()["Data"]["TransactionId"])

       if response1.status_code == 401:
            print("Authentication failed. Check your API key.")
       else:
           print(response1.json())
           Hubtel_Prepaid_Deposit_ID = '2016922'
           url = f' https://smrsc.hubtel.com/api/merchants/{Hubtel_Prepaid_Deposit_ID}/transactions/status?clientReference={response1.json()["Data"]["ClientReference"]}'
           key = 'MFlwelFCRzoyZWU3OGU5YWE2ZTM0NDQ0OGFmMzRjNTI1ODcwNTlkYg=='

           header = {
    'Authorization': f'Basic {key}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Cache-Control': 'no-cache'
           }
           time.sleep(5)
           print("t")
           response = requests.get(url, headers=header)
           print(response.json())
         #  print(response.text)
       return Response(response.json())
 



       # except:
        #   return Response('No')



class New_Recure(APIView):
    def post(self , request):
    
      Hubtel_POS_Sales_ID = '2017154'
      url = f'https://rip.hubtel.com/api/proxy/{Hubtel_POS_Sales_ID}/create-invoice'
#key ='Wm14elFCNTphMjgyMjEyYjVkNzY0NDkzYTY5NzZkNWQwMDk2ZTYzMw=='

      header = {
       'Authorization': 'Basic Wm14elFCNTphMjgyMjEyYjVkNzY0NDkzYTY5NzZkNWQwMDk2ZTYzMw==',
       'Content-Type': 'application/json',
       'Accept':'*/*',
       'Cache-Control': 'no-cache'
      }
      x = request.data
      data = { 
    "orderDate": x["Start_Date"],
    "invoiceEndDate": x["End_Date"],
    "description": x["About"],
    "startTime": x["Time"],
    "paymentInterval": x["Type"],
    "customerMobileNumber": x["Contact"],
    "paymentOption": "MobileMoney",
    "channel": x["Channel"],
    "customerName": x["Name"],
    "recurringAmount": x["Recure"],
    "totalAmount": x["Total"],
    "initialAmount": x["First"],
    "currency": "GHS",
    "callbackUrl": x["Url"]
   # "callbackUrl": "https://www.omall.online/confirm_recure"
    }

        
      response = requests.post(url, headers=header, json=data)   
             
      return Response(response.json())
          
class initialize_transaction(APIView):
    def post(self , request):
      url ='https://rip.hubtel.com/api/proxy/verify-invoice'

      header = {
       'Authorization': 'Basic Wm14elFCNTphMjgyMjEyYjVkNzY0NDkzYTY5NzZkNWQwMDk2ZTYzMw==',
       'Content-Type': 'application/json',
       'Accept':'*/*',
       'Cache-Control': 'no-cache'
      }
      
      x = request.data
      data = { 
    "recurringInvoiceId": x["id_1"],
    "requestId": x["id_2"],
    "otpCode": x["otp"],
    }
      response = requests.post(url, headers=header, json=data)   
      print(response.json())
      return Response(response.json())




class Delete_transaction(APIView):
    def post(self , request):
      x = request.data
      url ='https://rip.hubtel.com/api/proxy/2017154/cancel-invoice/'+x["id"]
      print(url)  
      header = {
       'Authorization': f'Basic Wm14elFCNTphMjgyMjEyYjVkNzY0NDkzYTY5NzZkNWQwMDk2ZTYzMw==',
       'Content-Type': 'application/json',
       'Accept': 'application/json',
       'Cache-Control': 'no-cache'
      }
      x = request.data
      response = requests.delete(url, headers=header)
      print(response)   
      return Response(response
)




class Transfere_Account(APIView):
    def post(self , request):
       url = f'https://trnf.hubtel.com/api/inter-transfers/2017154'
       key = 'MFlwelFCRzoyZWU3OGU5YWE2ZTM0NDQ0OGFmMzRjNTI1ODcwNTlkYg=='

       header = {
    'Authorization': f'Basic Wm14elFCNTphMjgyMjEyYjVkNzY0NDkzYTY5NzZkNWQwMDk2ZTYzMw==',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Cache-Control': 'no-cache'
       }
       uid =str(uuid.uuid1())
       data = {

    "DestinationAccountNumber":'2016922',
    "Amount": request.data["Amount"],
    "PrimaryCallbackUrl": request.data["Url"],
    "Description": "Withdrawal",
    "ClientReference": uid,
      }
       response1 = requests.post(url, headers=header, json=data)
       print(response1.json())
       return Response(response1.text)


class Check_Ref(APIView):
    def post(self , request):
       Hubtel_Prepaid_Deposit_ID = '2016922'
       url = f' https://smrsc.hubtel.com/api/merchants/{Hubtel_Prepaid_Deposit_ID}/transactions/status?clientReference={request.data["Ref"]}'
       key = 'MFlwelFCRzoyZWU3OGU5YWE2ZTM0NDQ0OGFmMzRjNTI1ODcwNTlkYg=='

       header = {
    'Authorization': f'Basic {key}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Cache-Control': 'no-cache'
       }
       
       response = requests.get(url, headers=header)

       if response.status_code == 401:
            print("Authentication failed. Check your API key.")
       else:
           print(response.text)
       return Response(response.json())



class Chech_Number(APIView):
    def post(self , request):
       url=f"https://rnv.hubtel.com/v2/merchantaccount/merchants/2017154/mobilemoney/verify?channel={request.data['channel']}&customerMsisdn={request.data['Contact']}"
       print(url)
       header = {
    'Authorization': f'Basic Wm14elFCNTphMjgyMjEyYjVkNzY0NDkzYTY5NzZkNWQwMDk2ZTYzMw==',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Cache-Control': 'no-cache'
       }
       response = requests.get(url, headers=header)
       print(response)
       if response.status_code == 401:
            print("Authentication failed. Check your API key.")
       else:
           print(response.text)
       return Response(response.text)



class Check_Prepaid(APIView):
    def get(self , request):
       Hubtel_Prepaid_Deposit_ID = '2016922'
       url = f' https://trnf.hubtel.com/api/inter-transfers/prepaid/{Hubtel_Prepaid_Deposit_ID}'
       key = 'MFlwelFCRzoyZWU3OGU5YWE2ZTM0NDQ0OGFmMzRjNTI1ODcwNTlkYg=='

       header = {
    'Authorization': f'Basic {key}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Cache-Control': 'no-cache'
       }

       response = requests.get(url, headers=header)

       if response.status_code == 401:
            print("Authentication failed. Check your API key.")
       else:
           print(response.text)
       return Response(response.json())



class Check_Card(APIView):
    def post(self , request):
       url=f"https://rnv.hubtel.com/v2/merchantaccount/merchants/2017154/idcard/verify?idtype=ghanacard&idnumber={request.data['ID']}"
       print(url)
       header = {
    'Authorization': f'Basic Wm14elFCNTphMjgyMjEyYjVkNzY0NDkzYTY5NzZkNWQwMDk2ZTYzMw==',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Cache-Control': 'no-cache'
       }
       response = requests.get(url, headers=header)
       print(response)
       if response.status_code == 401:
            print("Authentication failed. Check your API key.")
       else:
           print(response.text)
       return Response(response.text)



class Check_Bank(APIView):
    def post(self , request):
       url=f"https://rnv.hubtel.com/v2/merchantaccount/merchants/2017154/bank/verify/{request.data['CODE']}/{request.data['ID']}"
       print(url)
       header = {
    'Authorization': f'Basic Wm14elFCNTphMjgyMjEyYjVkNzY0NDkzYTY5NzZkNWQwMDk2ZTYzMw==',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Cache-Control': 'no-cache'
       }
       response = requests.get(url, headers=header)
       print(response)
       if response.status_code == 401:
            print("Authentication failed. Check your API key.")
       else:
           print(response.text)
       return Response(response.text)




class Check_Meter(APIView):
    def post(self , request):
       Hubtel_Prepaid_Deposit_ID = '2016922'
       url = f'https://cs.hubtel.com/commissionservices/{Hubtel_Prepaid_Deposit_ID}/e6d6bac062b5499cb1ece1ac3d742a84?destination={request.data["Number"]}'
       key = 'MFlwelFCRzoyZWU3OGU5YWE2ZTM0NDQ0OGFmMzRjNTI1ODcwNTlkYg=='

       header = {
    'Authorization': f'Basic {key}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Cache-Control': 'no-cache'
       }

       response = requests.get(url, headers=header)

       if response.status_code == 401:
            print("Authentication failed. Check your API key.")
       else:
           print(response.text)
       return Response(response.json())






class Send_Bank(APIView):
    def post(self , request):
       Hubtel_Prepaid_Deposit_ID = '2016922'
       url = f'https://smp.hubtel.com/api/merchants/{Hubtel_Prepaid_Deposit_ID}/send/bank/gh/{request.data["Bank"]}'
       key = 'MFlwelFCRzoyZWU3OGU5YWE2ZTM0NDQ0OGFmMzRjNTI1ODcwNTlkYg=='

       header = {
    'Authorization': f'Basic {key}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Cache-Control': 'no-cache'
       }

       x = request.data
       data = { 
         "Amount": x["Amount"],
      "BankName": "",
      "BankBranch": "",
      "BankBranchCode": "",
      "BankAccountNumber": x["Account"],
      "BankAccountName": "",
      "ClientReference": x["Ref"],
      "PrimaryCallbackUrl":x["Url"],
      "Description": "Test Deposit",
      "RecipientPhoneNumber": ""

 #"Destination": x["Number"],
  #  "Amount": x["Amount"],
   # "CallbackUrl": "https://webhook.site/cd98263c-b182-443b-ae95-dbdd64511aff",
   # "ClientReference": x["Ref"],
   # "Extradata": {
    #    "bundle": x["Meter"]
   # }


  
    }
       print(x)
       print(data)
       print(url)
       response = requests.post(url, headers=header, json=data)   
       print(response.json())
       return Response(response.json())




class Initialize_Ecg(APIView):
    def post(self , request):
      Hubtel_Prepaid_Deposit_ID = '2016922'
      url = f'https://cs.hubtel.com/commissionservices/{Hubtel_Prepaid_Deposit_ID}/e6d6bac062b5499cb1ece1ac3d742a84'

      header = {
       'Authorization': 'Basic Wm14elFCNTphMjgyMjEyYjVkNzY0NDkzYTY5NzZkNWQwMDk2ZTYzMw==',
       'Content-Type': 'application/json',
       'Accept':'*/*',
       'Cache-Control': 'no-cache'
      }

      x = request.data
      data = { 

 "Destination": x["Number"],
    "Amount": x["Amount"],
    "CallbackUrl": x["Url"],
    "ClientReference": x["Ref"],
    "Extradata": {
        "bundle": x["Meter"]
    }


  
    }
      print(x)
      print(data)
      print(url)
      response = requests.post(url, headers=header, json=data)   
      print(response.json())
      return Response(response.json())




class Dirrect_Transaction(APIView):
    def post(self , request):
        header = {
       'Authorization': 'Basic Wm14elFCNTphMjgyMjEyYjVkNzY0NDkzYTY5NzZkNWQwMDk2ZTYzMw==',
       'Content-Type': 'application/json',
       'Accept':'*/*',
       'Cache-Control': 'no-cache'
      }
        x = request.data
        data = {
     "CustomerName": x["Name"],
      "CustomerMsisdn": x["Number"],
      "CustomerEmail": x["Email"],
      "Channel": x["Channel"],
      "Amount": x["Amount"],
      "PrimaryCallbackUrl": x["Callback"],
      "Description": x["About"],
      "ClientReference": x["Reference"]

      }
        response = requests.post('https://rmp.hubtel.com/merchantaccount/merchants/2017154/receive/mobilemoney', headers=header, json=data)
        print(response)
        return Response(response.text)




class Check_Pos(APIView):
    def get(self , request):
       Hubtel_Pos_ID = '2017154'
       url = f'https://trnf.hubtel.com/api/inter-transfers/{Hubtel_Pos_ID}'
       key = 'MFlwelFCRzoyZWU3OGU5YWE2ZTM0NDQ0OGFmMzRjNTI1ODcwNTlkYg=='

       header = {
    'Authorization': f'Basic {key}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Cache-Control': 'no-cache'
       }

       response = requests.get(url, headers=header)

       if response.status_code == 401:
            print("Authentication failed. Check your API key.")
       else:
           print(response.text)
       return Response(response.json())
