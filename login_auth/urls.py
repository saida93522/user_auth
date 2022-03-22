"""login_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from  django.conf.urls.static import static

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    # link when user submits forgot password
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="reset_password.html"),name="password_reset"),
    
    # link Email reset instructions.
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
         name="password_reset_done"),

    # link reset password.
    #  user.id encoded in base64,token to check if password is valid
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),
         name="password_reset_confirm"),

    # link Email sent to let user know password reset complete
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"),
         name="password_reset_complete"),
    path('', include('login_app.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)