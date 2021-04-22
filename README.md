# DBookmark

- 프로젝트 시작
    - django-admin startproject config .
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py runserver
- bookmark 앱 시작
    - python manage.py startapp bookmark
    - 'bookmark', in INSTALLED_APPS
- bookmark/models Bookmark
    - python manage.py makemigrations bookmark
    - python manage.py migrate
- bookmark/admin Bookmark
    