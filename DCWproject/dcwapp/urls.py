from django.urls import path
from .views import *
urlpatterns = [
    path('',home_view),
    path('login/',login_view),
    path('logout/',logout_view),
    path('signup/',signup_view),
    path('mobileverification/',mobile_verification),
    path('dashboard/',dashboard_view),
    path('addaddress/<int:id>/',add_address),
    path('updateaddress/<int:id>/',update_address),
    path('addvehicle/<int:id>/',add_vehicle),
    path('forgot-password/',forgot_password),
    path('validatepasswordotp/',password_validate_otp),
    path('reset-password/',reset_password),
    path('reset-password3/',reset_password3),
    path('reset-password2/',reset_password2),
    path('validate-otp-mobile/',validate_otp_mobile),
    path('reset-password-mobile/',reset_password_via_mobile),

]
