from django.conf.urls import url 
from EmployeeApp import views 

from django.conf.urls.static import static 
from django.conf import settings

urlpatterns =[
    url(r'^department/$',views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi),

     url(r'^employee/$',views.employeeApi),
    url(r'^employee/([0-9]+)$', views.employeeApi),


    url(r'^SaveFiles/$' , views.SaveFile),

    url(r'^getdata/$' , views.GetDept),
    url(r'^getdata/([0-9]+)$', views.GetDept)

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)