import requests
import time
from discord import SyncWebhook
import discord

msgsender_webhook_url = ""
message = ""

def messageSenderStart():
  i = input("Continue? [Y,N] ")
  if i.lower() == str.lower("Y"):
    messageSenderWebhook()
  elif i.lower() == str.lower("N"):
    return
  else:
    print("Not a valid option")
    messageSenderStart()

def messageSenderWebhook():
  global stresser_webhook_url
  i = input("Enter the webhook url: \n")
  if i.startswith("https://discord.com/api/webhooks/"):
    print("Successfully set '" + i + "' as webhook")
    stresser_webhook_url = i
    message()
  else:
    print("ERROR! Make sure the webhook adress starts with '" + "https://discord.com/api/webhooks/" + "'")
    messageSenderWebhook()

def message():
  global message
  i = input("Input the message that should be sent: ")
  if i.lower() == "":
    print("Please add at least a space as message :)")
    message()
  else:
    message = i
    messageSenderFinish()

def messageSenderFinish():
  global message
  global stresser_webhook_url
  print("Webhook: " + stresser_webhook_url)
  print("\n")
  print("Message: " + message)
  i = input("Is everything right? [Y,N] ")
  if i.lower() == str.lower("Y"):
        print("Sending Message")
        response = requests.post(stresser_webhook_url, json={"content": message})
        if response.status_code == 204:
            print("Message sent successfully")
            options()
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            time.sleep(1)
  elif i.lower() == str.lower("N"):
        print("Canceled")
        messageSenderStart()
  else:
        print("Not a valid option")
        messageSenderFinish()




deleter_webhook_url = 'https://discord.com/api/webhooks/1125479565268099192/ZzXxb9UJisrallWGz9puTODa7lKLKxG9eLy47dvxB3ifxb5IgPcPj49jycBLyxVB3IGu'

client = SyncWebhook.from_url(deleter_webhook_url)



def deleterStart():
    i = input("Continue? [Y,N] ")
    if i.lower() == str.lower("Y"):
        removerWebhook()
    elif i.lower() == str.lower("N"):
        print("Disconnecting from discord services...")
        return
    else:
        print("Option doesn't exist?")
        deleterStart()

def removerWebhook():
    global deleter_webhook_url
    global client
    i = input("Enter webhook url: ")
    if i.startswith("https://discord.com/api/webhooks/"):
        print("Successfully set webhook_url to '" + i + "'")
        deleter_webhook_url = i
        client = SyncWebhook.from_url(deleter_webhook_url)
        removerFinish()
    else:
        print("ERROR! Make sure the webhook adress starts with '" + "https://discord.com/api/webhooks/" + "'")
        removerWebhook()

def removerFinish():
    i = input("Remove webhook? [Y,N] ")
    if i.lower() == str.lower("Y"):
        try:
         client.delete()
         print('Webhook deleted successfully.')
         options()
        except discord.NotFound:
         print('Webhook not found.')
        except discord.HTTPException as e:
         print(f'Error occurred while deleting webhook: {e}')
    elif i.lower() == str.lower("N"):
        print("Disconnecting from discord services...")
        return
    else:
        print("Option doesn't exist?")
        removerFinish()

name_webhook_url = "https://discord.com/api/webhooks/1125738043081490472/AXXO3_OAHhMPEfkxZQcaiCv0w85Ay1eqhAauIAQtYNkOjZwObFZarh5wV5KTfP0d59IP"
new_name = ""

nameRequestPayload = {
    'name': new_name
}

def nameStart():
   global name_webhook_url
   i = input("Enter webhook url: ")
   if i.startswith("https://discord.com/api/webhooks/"):
        print("Successfully set webhook_url to '" + i + "'")
        name_webhook_url = i
        nameFinish()
   else:
        print("ERROR! Make sure the webhook adress starts with '" + "https://discord.com/api/webhooks/" + "'")
        nameStart()

def nameFinish():
   global nameRequestPayload
   global new_name
   i = input("New name: ")
   if i.lower() == str.lower(""):
      print("Atleast make the name a SPACE")
      nameFinish()
   else:
      new_name = i
      nameRequestPayload = {
         'name': new_name
     }
      response = requests.patch(name_webhook_url, json=nameRequestPayload)
      if response.status_code == 200:
        print("Successfully changed name!")
        options()
      else:
        print("Failed to update the webhook's name.")
        options()





def options():
   i = input("Deleter [D] , Sender [S] , NameChanger [NC] ")
   if i.lower() == str.lower("D"):
      deleterStart()
   elif i.lower() == str.lower("S"):
      messageSenderStart()
   elif i.lower() == str.lower("NC"):
      nameStart()
   else:
      print("Invalid option?")
      options()

options()