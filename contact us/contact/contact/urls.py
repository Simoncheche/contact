from django.contrib import admin
from django.urls import path, include
from contact_us.views import contact_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact_us/', include('contact_us.urls')),  
    path('', contact_us, name='contact_us')
]
