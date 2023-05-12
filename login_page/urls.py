
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login_view,name="login_page"),
    path('signup/',views.sign_up_view,name="sign_up"),
    path('logout/',views.log_out_view,name="log_out")
]
