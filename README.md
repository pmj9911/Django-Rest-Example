This is an example app which demonstrated the usage of Django Rest Framework.
###Functions:
##Module Account:
Create User -
1. creates a user in DB
2. returns created User in the response with a unique id.

Get User -
1. fetchs user from DB using the id given either as a query or path param.
2. If a user doesn't exist, returns a proper error message.
3. The response should be "User"

##Usage:
1. Creating a virtual env:
virtualenv venv
source vene/bin/activate
2. Installing the dependencies:
pip3 install -r requirements.txt
3. Running the server
python3 manage.py runserver

If asked, the also run 
python3 manage.py migrate
to run the migrations.
