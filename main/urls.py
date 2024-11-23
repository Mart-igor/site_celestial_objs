from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.category_list, name='category_list'),
    path('shop/category/<slug:category_slug>/', views.category_list, name='category_list'),
    path('shop/<slug:detail_slug>/', views.detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEdiA_URL,
                          document_root=settings.MEDIA_ROOT)