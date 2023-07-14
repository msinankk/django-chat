# django-chat
Django chat app using socket programming and channels.
##  Chat Project Using Django
### Pull from git
```
git pull https://github.com/msinankk/django-chat.git main
```

### Create virtual environment
```
python -m venv venv
```
### Activate virtual venv
#### - Windows
```
venv/Scripts/activate
```
#### - Lynx/max os
```
source venv/bin/activate
```

### Install requirement txt
```
pip install -r requirements.txt
```
### Run migrations
```
python manage.py migrate
```
### Create admin users
Create multiple admin users to chat with each others.
```
python manage.py createsuperuser
```
### Run the server
#### - localhost
```
python manage.py runserver
```
 Then navigate to http://localhost:8000/admin/login and login with your account, then come back to http://localhost:8000/ start chat with the other users. Enjoy!
#### - local n/w
```
python manage.py runserver 0.0.0.0:8000
```
To run within the local network run this instead and do the stuff described in runserver method.
