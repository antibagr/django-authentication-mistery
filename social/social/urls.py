from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from account import views as account_views

tmp: dict = {
    'login': 'LoginView',
    'password_reset': 'PasswordResetView',
    'password_reset_done': 'PasswordResetDoneView',
    'password_reset_complete': 'PasswordResetCompleteView',
}

urlpatterns = [
    path('', include('account.urls')),
    path('admin/', admin.site.urls),
    path('signup/', account_views.sign_up, name='sign_up'),
    path('logout/', account_views.custom_logout, name='logout'),

    *[path(k + '/', getattr(auth_views, v).as_view(template_name=f'account/{k}.html'), name=k) for k,v in tmp.items()],

    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
