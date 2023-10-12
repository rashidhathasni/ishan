from django.urls import path
from.import views
urlpatterns=[
    path("",views.index,name="index"),
    path("departments",views.department,name="department"),
    path("booking",views.booking,name="booking"),
    path("doctors",views.doctors,name="doctors"),

]