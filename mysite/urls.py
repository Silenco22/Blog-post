"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
#my views
from personal.views import (
    
    home_screen_view,
)
    
from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    must_authenticate_view,
)
 
    



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('blog/', include('blog.urls', 'blog')),
    path('register/', registration_view, name="register"),  
    path('logout/', logout_view, name="logout"),  
    path('login/', login_view, name="login"),  
    path('must_authenticate/', must_authenticate_view, name="must_authenticate"),  
    path('account/', account_view, name="account"),


   	# REST-framework
    path('api/blog/', include('blog.api.urls', 'blog_api')),
    path('api/account/', include('account.api.urls', 'account_api')),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    # to su django source code views for  password reset  (ne trebamo svoje) i svi urlovi za password reset po django dokumentaciji
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),  
]
#postava url i roota za static i media  
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)