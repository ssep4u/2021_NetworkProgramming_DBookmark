# DBookmark
models -> admin -> views -> templates -> urls
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
    - \_\_str\_\_()
- bookmark/admin Bookmark
- List Bookmark
    - bookmark/views BookmarkListView
    - bookmark/templates/bookmark bookmark_list.html
    - urls; bookmark/urls bookmark:list
- Add Bookmark
    - bookmark/views BookmarkCreateView
    - bookmark/templates/bookmark bookmark_create.html, bookmark_list.html
    - bookmark/urls bookmark:add
- Bookmark Detail
    - bookmark/views BookmarkDetailView
    - bookmark/templates/bookmark bookmark_detail.html, bookmark_list.html
    - bookmark/urls bookmark:detail
- Update Bookmark
    - bookmark/views BookmarkUpdateView
    - bookmark/templates/bookmark bookmark_update.html, bookmark_list.html
    - bookmark/urls bookmark:update
    - bookmark/models get_absolute_url() in Bookmark
- Delete Bookmark
    - bookmark/views BookmarkDeleteView
    - bookmark/templates/bookmark bookmark_confirm_delete.html, bookmark_list.html
    - bookmark/urls bookmark:delete
- 기능완성✨🎉
- config/templates/base.html, extends, block title, block content
---
- startapp accounts
    - python manage.py startapp accounts
    - add 'accounts' in INSTALLED_APPS settings.py
- models, AUTH_USER_MODEL, admin, forms
    - accounts/models CustomUser(AbstractUser)
        1. db.sqlite3 삭제
        1. migrations 폴더에 있는 .py 삭제
        1. python manage.py makemigrations
        1. python manage.py migrate
    - AUTH_USER_MODEL = 'accounts.CustomUser' in settings.py
    - accounts/admin CustomUserAdmin
    - accounts/forms CustomUserCreationForm(UserCreationForm)
- Register
    - accounts/views register
    - templates/accounts register, register_done; templates/bookmark bookmark_list
    - accounts/urls register; config/urls
- Login, Logout
    - accounts/forms LoginForm
    - accounts/views my_login, my_logout
    - templates/accounts login, login_fail; templates/bookmark bookmark_list
    - accounts/urls login, logout
- CustomUser 사용
    - bookmark/models add user in Bookmark
- 로그인 동작
    - 로그인 요구하자
      - FBV: @login_required
      - CBV: LoginRequiredMixin
    - bookmark_list
      - 로그인 하면, 자기 것만 보이기
      - 로그인 안하면, 다 보이기
    - bookmark_create
      - user 초기화