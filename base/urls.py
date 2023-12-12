from django.urls import path
from .views import home, room, create_room, update_room, delete_room, login_page, logout_user, register_user, \
    delete_message, user_profile, update_user, topics_pages, activity_page

urlpatterns = [
    path("login/", login_page, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", logout_user, name="logout"),
    path("", home, name="home"),
    path("room_page/<str:pk>", room, name="room"),
    path("profile/<str:pk>", user_profile, name="user-profile"),
    path("create-room/", create_room, name="create-room"),
    path("update-room/<str:pk>", update_room, name="update-room"),
    path("delete-room/<str:pk>", delete_room, name="delete-room"),
    path("delete-message/<str:pk>", delete_message, name="delete-message"),
    path("update-user/", update_user, name="update-user"),
    path("topics/", topics_pages, name="topics"),
    path("activity/", activity_page, name="activity"),
]
