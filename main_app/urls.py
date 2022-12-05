from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('classes/', views.classes, name='classes'),
    path('classes/<int:class_id>/', views.class_detail, name='detail'),

    path('membership/create/', views.MembershipCreate.as_view(), name='membership_create'),
    path('membership/<int:user_id>/', views.membership, name='membership'),
    path('membership/<int:user_id>/update/', views.MembershipUpdate.as_view(), name='membership_update'),

    # path('login/', views.login, name='login'),
    # path('signup/', views.signup, name='signup')
]