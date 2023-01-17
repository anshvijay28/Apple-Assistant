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
### canvasAPIKey
To get this API Key go to XXXXX.instructure.com > Account > Settings > Generate New Token  

The generate new Token Button will look like this  

![New Canvas Token Picture](/pictures/New_Access_Token.png?raw=true "Cavas Access Token")  
  
 After you click New Access Token you will be prompted to create an expiration date and specify the purpose. Specifying the purpose has no effect on the program it is just for organizational purposes if you have multiple access tokens. For the expiration date you can create one at your discretion, I did not create an expiration date for less maintence, but if you are concerned for the security of the program go ahead and create one.
 
![Generate Token Picture](/pictures/Generate_Token.png?raw=true "Cavas Access Token")  
