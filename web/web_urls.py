from django.urls import path, include, re_path

from web import views
urlpatterns = [
    path('test/', views.test),

    path('uploadInvoicePic/', views.uploadInvoicePic),
    path('modifyInvoiceCode/', views.modifyInvoiceCode),
    path('modifyInvoiceType/', views.modifyInvoiceType),
    path('modifyInvoiceNum/', views.modifyInvoiceNum),
    path('modifyInvoiceDate/', views.modifyInvoiceDate),
    path('retrieveInvoicePic/', views.retrieveInvoicePic),
    path('deleteInvoice/', views.deleteInvoice),

    path('register/', views.register),
    path('loginid/', views.loginid),
    path('loginphone/', views.loginphone),
    path('iflogged/', views.iflogged),
    path('logout/', views.logout),
    path('avatar/', views.upload_avatar),
    path('statistics/', views.getSta),

]
