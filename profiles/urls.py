from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import profiles_list, register_profile, user_profile

urlpatterns = [
    path('', profiles_list, name='profiles_list'),
    path('register_profile/', register_profile, name='register_profile'),
    re_path(r'^user_profile/(?P<nickname>[\w\d]+)/$', user_profile, name='user_profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
