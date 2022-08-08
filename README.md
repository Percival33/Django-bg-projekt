# Django-bg-projekt

Blog like page with boats, their descriptions etc. Based on Django tutorial by Corey Schafer on [YouTube](https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p).

## Setup

1. clone repo
2. setup venv for repo and activate it. This [link](https://docs.python.org/3/library/venv.html) might be useful.
3. run `pip install -r requirements.txt`
4. create new secret key using this command (with virtualenv active)

```
python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
```

5. run migrations and create superuser

```bash
  python manage.py migrate
  python manage.py createsuperuser
```

6. run server via thiis command `python manage.py runserver`

## Disclaimers

**Do not run with debug turned on in production!**

## Known bugs

There are not known bugs.

### TODO:

- [ ] make better readme (setup section, pictures etc)
- [ ] add tests
- [ ] add email confirmation on creating account
- [ ] switch to Dockerfile
