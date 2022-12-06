from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('classes/', views.classes, name='classes'),
    path('classes/<int:class_id>/', views.class_detail, name='detail'),

    path('membership/create/', views.MembershipCreate.as_view(), name='membership_create'),
    path('membership/<int:user_id>/', views.membership, name='membership'),
    path('membership/<int:user_id>/update/', views.MembershipUpdate.as_view(), name='membership_update'),
    path('membership/<int:membership_id>/assoc_class/<int:class_id>/', views.assoc_class, name='assoc_class'),
    path('membership/<int:membership_id>/unassoc_class/<int:class_id>/', views.unassoc_class, name='unassoc_class'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]