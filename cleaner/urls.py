from django.conf.urls import url
from .views import FileFieldView,editable,columnn
from . import views
urlpatterns = [
    url(r'^form/$', FileFieldView.as_view(),name='home'),
    url(r'^edit/$', editable.as_view(),name='edit'),
    url(r'^view/$', views.viewing2,name='view'),
    url(r'^column/$', columnn.as_view(),name='column'),
    #url(r'^column/$', views.viewing,name='column'),
    #url(r'^moreorless', views.modelx,name='moreorless'),
    #url(r'runmodel',views.runmodel,name='runmodel')
    # url(r'^upload/$', views.Upload,name='uploadhome'),
    #url(r'^moreorless',views.option,name='option')
]