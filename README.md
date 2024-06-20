# Comments Service

API service for comments management.


## Installing using GitHub

```shell
git clone https://github.com/artemgrishko/comments.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
copy .env from .env.samplate and create POSTGRES_DB_URL(you can create it by yourself or use my:postgres://fxunierw:V4bCF69VqtGYcKu_G_q_V6ohm3FyXkWU@cornelius.db.elephantsql.com/fxunierw), SECRET_KEY
python manage.py migrate
python manage.py runserver
```

## Run with docker

Docker should be installed

```shell
docker-compose build
docker-compose up
```

## Getting access for creating new comments

<ul>
  <li>create user via /api/user/register</li>
  <li>get access token via /api/user/token</li>
  <li>add token to local storage</li>
</ul>

## Features

<ul>
  <li>JWT authenticated</li>
  <li>Admin panel /admin/</li>
  <li>Creating comments</li>
  <li>Sorting comments by date, user_name, email</li>
  <li>Captcha</li>
</ul>
