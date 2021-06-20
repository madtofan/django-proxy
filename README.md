# django-proxy
Using django as an authentication proxy

# install required packages
- Run command 'pip install -r requirements.txt'

# running the proxy
- Run command 'python manage.py runserver'

# managing the proxy
- Proxy is managed under the app 'api'
- urls.py and views.py for the reverse proxy redirection handling
- permissions.py for the permission handling for each view