# Apple-Assistant

Python script utilizing the Twilio SMS API and many others to create a virtual assistant that will set reminders, tell you the weather, utilize openai's technology, and much more!

## Setup

After cloning the project establish a .env file with these credientials: 
```
canvasAPIKey = XXXXXXXXXXXXXXX
canvasUserNumber = XXXXXXXXXXXXXXX
numberFrom = XXXXXXXXXXXXXXX
numberTo = XXXXXXXXXXXXXXX
openaiApiKey = XXXXXXXXXXXXXXX
twilioAccountSid = XXXXXXXXXXXXXXX
twilioAuthToken = XXXXXXXXXXXXXXX
```
### Twilio Account
This is what powers the whole application. Without Twilio there would be no phone number to text or SMS messages to send. To make an account go [here](https://www.twilio.com/). Once completed you can go to your console and you will see your Account SID, Authentication Token, and Twilio Phone Number.  

<p align = "center">
    <img width = "auto" height = "400" src = "https://github.com/anshvijay28/Apple-Assistant/blob/main/pictures/Twilio_Account_Information.png">
</p>

### Canvas API Key
Go to XXXXX.instructure.com > Account > Settings > Generate New Token  

The generate new Token Button will look like this  

<p align = "center">
    <img width = "auto" height = "300" src = "https://github.com/anshvijay28/Apple-Assistant/blob/main/pictures/New_Access_Token.png">
</p>
  
 After you click New Access Token you will be prompted to create an expiration date and specify the purpose. Specifying the purpose has no effect on the program it is just for organizational purposes if you have multiple access tokens. For the expiration date you can create one at your discretion, I did not create an expiration date for less maintence, but if you are concerned for the security of the program go ahead and create one.
 
<p align = "center">
    <img width = "350" height = "auto" src = "https://github.com/anshvijay28/Apple-Assistant/blob/main/pictures/Generate_Token.png">
</p>



### OpenAi API Key  
Go to this [link](https://openai.com/api/) and create an account. Once you have made an account, go to the upper right hand corner and click "View API Keys". 

<p align = "center">
    <img width = "350" height = "auto" src = "https://github.com/anshvijay28/Apple-Assistant/blob/main/pictures/OpenAI_View_Keys.png">
</p>

Once clicked you simply press "Create new secret key". Make sure to note it down some place because once you click off the pop up you will no longer have access to the key and will have to make a new one.  

### Openweathermap API Key  
Go to this [link](https://openweathermap.org/api) and create an account. Once you have made an account, again go to the upper right hand corner and click "My API keys".  

<p align = "center">
    <img width = "350" height = "auto" src = "https://github.com/anshvijay28/Apple-Assistant/blob/main/pictures/Manage_openweathermap_key.png">
</p>

Then give your key a name (again the name of the key doesn't effect its functionality) and press generate.  

<p align = "center">
    <img width = "350" height = "auto" src = "https://github.com/anshvijay28/Apple-Assistant/blob/main/pictures/Generate_openweathermap_key.png">
</p>

## Hosting the code  
This program is based upon a flask application. As such, it must be hosted somewhere either locally or externally. I recommend hosting your code externally as you wouldn't have to burdern your device with running the application 24/7. To host on AWS (as I did) watch this tutorial by Caleb Curry! 

[![Apple-Assistant](https://img.youtube.com/vi/4tDjVFbi31o/0/jpg)](https://www.youtube.com/watch?v=4tDjVFbi31o)  

If you want to host your code locally then follow this [tutorial](https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment#create-a-simple-flask-application) by the Twilio team about Ngrok!  

Once you are through the process of hosting your code then you will be left with a url. To finally connect your code to Twilio head over to this [Twilio's Website](https://console.twilio.com/) and click Phone Numbers > Manage > Active Numbers and click on your number in the console (it should be in blue text). Then scroll all the way down and paste your link where I have in this picture.  

<p align = "center">
    <img width = "auto" height = "100" src = "https://github.com/anshvijay28/Apple-Assistant/blob/main/pictures/Twilio_Webhook.png">
</p>
  
Make sure
1. The end of your url is appended with '/sms'
2. You are configuring the "A message comes in" webhook
3. The webhook is set to HTTP POST 

## Commands  
- "hi" --> "Hey there!"
- "gpt: "  --> Whatever is put after the colon will be put through ChatGPT using the OpenAI's API and the user will get the appropriate response 
- "weather" --> Will output the current temperature, high and low of the day, and what time the sun will set 
- "picture: " --> Whatever is put after the colon will be put through DALLE 2 using OpenAI's API and the user will get the appropriate response 
- "balance" --> If using Twilio's free account it will output how much money is left in the account 