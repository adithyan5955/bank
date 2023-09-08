from django.urls import  path
from . import views
app_name='bankapp'

urlpatterns = [
   path('',views.HomePage,name='homepage'),
   path('login/',views.LoginPage,name='loginpage'),
   path('registration/',views.register,name='registration'),
   path('logout/',views.logout,name='logout'),
   path('submit_application/', views.submit_application, name='submit_application'),
   path('form_details/<int:form_id>/', views.form_details, name='form_details'),  

]