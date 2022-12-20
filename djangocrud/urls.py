from django.urls.conf import include
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.urls.conf import include
from Users.views import SignUp, Logout
from .views import (Home, 
CreateTaskUser, 
DetailTask, 
UpdateTask,
DeleteTask,
FinishedTask,
ImportantTask,
CreateCategory,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', Home.as_view(), name='home'),
    path('important/',ImportantTask, name='important'),
    path('finished/', FinishedTask, name='finished'),
    

    path('accounts/', include('allauth.urls')),

    path('registers/', SignUp, name='sign-up'),
    path('logout/', Logout, name='logout'),

    #Task
    path('create/', CreateTaskUser.as_view(), name='create' ),
    path('task/<id>/detail', DetailTask.as_view(), name='detail'),
    path('task/<pk>/update', UpdateTask.as_view(), name='update'),
    path('task/<id>/delete', DeleteTask, name='delete'),

    #Categories
    path('create-categories/', CreateCategory, name='create-category' ),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)