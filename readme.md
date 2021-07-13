# Geeky-chat
Command-line real-time chat app using python

# Created Using Python-socketio and Typer
Only dependencies to run this project are python3.6+ , python-socketio and typer *** You will also need to have colorama installed inorder to have coloured outputs during chat ***

# Proof of Concept project Not Recommended for any sort of Production
This project has been created in a span of a single day . So i wont recommend to use this for production . Currently we are not having any user authentication also.

# how to get start 
Clone the repo and install the requirements.txt  \
  ```` pip install requirements.txt ````

currently  I have hardcoded only only 2 users in the server viz umar and aabid .

### start the server 

```` python server.py  ````

This will start the aiohttp server . 

### start the clients to chat with each other 

````  
python geeky_chat.py --sender umar --reciever aabid  

````

````

python geeky_chat.py --sender aabid --reciever umar

```` 


####  Now we are good to geek now 😊😊


start the repo and stay connected
Thanks .

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.



## License
[MIT](https://choosealicense.com/licenses/mit/)