from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('lob', views.lob, name='lob'),
    path('rform', views.rform, name='rform'),
    path('saveform', views.saveform, name='rform1'),
    path('edit/<int:isbn>', views.edit, name='edit'),
    path('editdetails', views.editdetails, name='edit1'),
    path('search', views.search, name='edit2'),
    path('price', views.price, name='edit3'),
    path('ascen_order', views.ascen_order, name='edit4'),
    path('decen_order', views.decen_order, name='edit5'),

    #path('postlist', views.postlist, name='edit6'),
]
