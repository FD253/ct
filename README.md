# Twitter Poster
### Server
* Clone repo
* Use virtualenv (py3)
* `pip install -r requirements.txt`
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py createsuperuser` (needed for getting the ApiKey for using the api)
* `python manage.py runserver`
* In another shell (inside the ct directory) run: `celery -A tw worker -l info`
### Client
* Populate credentials.py with your 4 twitter keys & secrets and username
* Run `python client.py` once to generate your ApiKey (look for it in admin)
* Add your ApiKey to credentials.py
* Run `python client.py` with up to 5 args (1st arg is the tweet text and the other 4 are paths to images in your system). 
Examples:
`python client.py text [img1] [img2] [img3] [img4]`
`python client.py 'this is the text' /home/user/Pictures/01.jpg /home/user/Pictures/02.jpg`
To tweet only images just put '' instead of a text:
`python client.py '' /home/user/Pictures/01.jpg`
