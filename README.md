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
### Canvas API Key
Go to XXXXX.instructure.com > Account > Settings > Generate New Token  

The generate new Token Button will look like this  

![New Canvas Token Picture](/pictures/New_Access_Token.png?raw=true "New Access Token")  
  
 After you click New Access Token you will be prompted to create an expiration date and specify the purpose. Specifying the purpose has no effect on the program it is just for organizational purposes if you have multiple access tokens. For the expiration date you can create one at your discretion, I did not create an expiration date for less maintence, but if you are concerned for the security of the program go ahead and create one.
 
![Generate Token Picture](/pictures/Generate_Token.png?raw=true "Generate Token")  
### OpenAi API Key  
Go to this [link](https://openai.com/api/) and create an account. Once you have made an account, go to the upper right hand corner and click "View API Keys". 

![View API Keys](/pictures/OpenAI_View_Keys.png?raw=true "View Keys")  

Once clicked you simply press "Create new secret key". Make sure to note it down some place because once you click off the pop up you will no longer have access to the key and will have to make a new one.  

### Openweathermap API Key  
Go to this [link](https://openweathermap.org/api) and create an account. Once you have made an account, again go to the upper right hand corner and click "My API keys".  

![My API Keys](/pictures/Manage_openweathermap_key.png?raw=true "My Keys")  

Then give your key a name (again the name of the key doesn't effect its functionality) and press generate.  

![Generate Openweathermapkey](/pictures/Generate_openweathermap_key.png?raw=true "Generate Key")  


