# Django-bg-projekt
Blog like page with boats, their descriptions etc. Based on Django tutorial by Corey Schafer on [YouTube](https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

~~[bgprojekt.xyz](https://www.bgprojekt.xyz) - Live site hosted on Linode, own configured Linux server~~

Changed hosting to Heroku available at [link](https://django-bg-project.herokuapp.com/).

## Setup
1. clone repo
2. setup venv for repo and activate it. This [link](https://docs.python.org/3/library/venv.html) might be useful.
3. run `pip install -r requirements.txt`
4. run migrations and create superuser 
```bash
  python manage.py migrate
  python manage.py createsuperuser
```
5. run server via thiis command `python manage.py runserver`

## Disclaimers
**Do not run with debug turned on in production!**

## Known bugs
>Heroku free plan does deactivates after 30minutes of inactivity, so added profile pictures will be removed, which causes problems then.

On local development there are not known bugs.

### TODO:
- [ ] make better readme (setup section, pictures etc)
- [ ] add tests
- [ ] add email confirmation on creating account
- [ ] switch to Dockerfile

