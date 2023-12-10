from django.urls import path
from first_app.views import signup, signin, signout, home, profile, pass_change, pass_change2

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('pass_change/', pass_change, name='pass_change'),
    path('pass_change2/', pass_change2, name='pass_change2'),
    path('profile/', profile, name='profile'),
]
