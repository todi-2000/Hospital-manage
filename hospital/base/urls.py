from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('patient/home/',views.phome,name='phome'),
    path('doctor/home/',views.dhome,name='dhome'),
    path('reception/home',views.rhome,name='rhome'),
    path('hr/home',views.hhome,name='hhome'),
    path('appointment/',views.appointment,name='app'),
    path('prescription/',views.prescription,name='pre'),
    path('form/new/',views.pre_new,name='pre_new'),
    path('reception/dashboard/',views.dashboard,name='dash'),
    path('app/new/',views.createapp,name='app_new'),
    path('pat/new/',views.createpat,name='pat_new'),
    path('hr/dashboard/',views.ddashboard,name='ddash'),
    path('doc/new/',views.createdoc,name='doc_new'),
    path('profile/<int:pk>/edit/', views.profile_update, name='profile_update'),
    path('profile/<int:pk>/delete/', views.profile_delete, name='profile_delete'),
    path('patient/payments/',views.payments,name='payment'),
    path('hr/accounts/',views.accounting,name='accounts'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)
