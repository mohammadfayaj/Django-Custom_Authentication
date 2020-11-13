from django.urls import path
from django.urls import reverse_lazy
from .import views
from django.contrib.auth import views as auth_views
from users import views as user_views



urlpatterns = [
    path('address_info/',  views.address_info , name='users-address-info'),

    path('',  views.register , name='users-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='users-logout'),
    path('profile/', views.profile , name='users-profile'),
    path('profile_info/', views.profile_info , name='users-profile-info'),


    path('change-password/', auth_views.PasswordChangeView.as_view
    (template_name='users/change-password.html'), name = 'password_change'),

    path('change-password/done/', auth_views.PasswordChangeDoneView.as_view
    (template_name='users/change-password-done.html'), name = 'password_change_done'),

    path('password-reset/',auth_views.PasswordResetView.as_view
    (template_name='users/password_reset.html'),name='password_reset'),

    path('password-reset/done',auth_views.PasswordResetDoneView.as_view
    (template_name='users/password_reset_done.html'),name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),


    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view
    (template_name='users/password_reset_complete.html'),name=('password_reset_complete')),
    
    ]

