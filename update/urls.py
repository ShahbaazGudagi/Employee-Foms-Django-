from django.urls import path
from .import views
urlpatterns = [
  path('view/',views.AddEmployeeView,name='Addmployee'),
  path('',views.Uploadform,name='Uploadform'),
  path('view/<id>/',views.RetriveForm,name='RetriveForm'), 
]