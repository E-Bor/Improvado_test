# Get started #

## Step 1. Need to upload the folder with the project ##

## Step 2. Need to get an access token
To get a token, you need to follow the authorization link. The mini app number is already built into the link, you don't 
need to change anything.
Copy this link and paste it into your browser:

    https://oauth.vk.com/authorize?client_id=51581575&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.52

Next, you will be redirected to a blank page. Please note that the url in the search bar has changed.

    https://oauth.vk.com/blank.html#access_token=vk1.a.N5A8r9cMdGb0dsRS-dGc1e7RKfuKHxZr9dFBs8l1Ywo6_ctoCFhOyQGwQRRXl6XVuoaI8VeCnSv2FFbJPV8EQcocpJQR54jiuIych8cy-w2d3bQGBp9eEL1yuhxYeaVO_AeHykei8xilj1-CufkwpigLCrtrW5g0XvMG0PjAdljS7JuQX-GuVv64AK-TJeOX&expires_in=86400&user_id=12134214

You need to copy the part that comes after "access_token=" and before "&expires_in=". You will get a string like this

    vk1.a.N5A8r9cMdGb0dsRS-dGc1e7RKfuKHxZr9dFBs8l1Ywo6_ctoCFhOyQGwQRRXl6XVuoaI8VeCnSv2FFbJPV8EQcocpJQR54jiuIych8cy-w2d3bQGBp9eEL1yuhxYeaVO_AeHykei8xilj1-CufkwpigLCrtrW5g0XvMG0PjAdljS7JuQX-GuVv64AK-TJeOX

This is your token. Next, you need to go to the project folder, find the config.py file and copy this token there (inside the quotes after token = )

## Step 3. You must specify the user id whose friends will be analyzed ##

Specify the user id inside quotes after "user_id ="

## Step 4. Next, you need to install all the necessary components. ##

    pip install -r requirements.txt
    

## Step 5. Launch ##

Open a terminal inside the project folder and run the command.
    
    python3 main.py

Next, the file with all the data will be saved in csv format in the current folder under the name "report.csv"

## At the end ##
You can change the output file path or extension. Also, all reports will not overwrite each other. If there are files with the same extension, "(number)" will be appended to the name. (Made so that no report is lost)