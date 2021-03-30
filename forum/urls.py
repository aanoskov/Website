from django.urls import path
from . import views
urlpatterns = [
    path("", views.get_blog_list, name="index"),
    path('create_section', views.create_section, name="create_section"),
    path('<int:blog_id>', views.blog, name="blog_by_id"),
    path('login', views.log_in, name="login"),
    path('signup', views.sign_up, name="signup"),
    path('logout', views.log_out, name="logout"),
    path('<int:blog_id>/create_post', views.create_post, name="create_post"),
    path('buy_tickets/', views.buy_tickets, name="buy_tickets"),
    path("main_front", views.index_page, name="index"),
    path("card", views.card_page, name="card"),
    path("economy", views.economy_page, name="economy"),
    path("rules", views.rules_page, name="rules"),
    path("contacts", views.contacts_page, name="contacts"),
]

