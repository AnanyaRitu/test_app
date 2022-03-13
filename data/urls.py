from django.urls import path

from . import views

urlpatterns = [
    path('',  views.log_in, name='log_in'),
    path('parent_registration/', views.parent_registration, name='parent_registration'),
    path('child_registration/', views.child_registration, name='child_registration'),
    path('logout/', views.log_out, name='log_out'),

    path('parent_home/', views.parent_home, name='parent_home'),
    path('parent_create_data_view/', views.parent_create_data_view, name='parent_create_data_view'),
    path('parent_update_data_view/', views.parent_update_data_view, name='parent_update_data_view'),

    path('child_home/', views.child_home, name='child_home'),
    path('child_create_data_view/', views.child_create_data_view, name='child_create_data_view'),
    path('child_update_data_view/', views.child_update_data_view, name='child_update_data_view'),

    #api urls
    path('parent_username_list/', views.parent_username_list, name="parent_username_list"),
    path('parent_data_create/<str:parent>', views.parent_data_create, name="parent_data_create"),
    path('parent_data_update/<str:parent>', views.parent_data_update, name="parent_data_update"),
    path('parent_data_delete/<str:parent>', views.parent_data_delete, name="parent_data_delete"),

    path('child_username_list/', views.child_username_list, name="child_username_list"),
    path('child_data_create/<str:child>', views.child_data_create, name="child_data_create"),
    path('child_data_update/<str:child>', views.child_data_update, name="child_data_update"),
    path('child_data_delete/<str:child>', views.child_data_delete, name="child_data_delete"),
]