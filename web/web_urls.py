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
    path('deleteInvoicePic/', views.deleteInvoicePic),
    path('deleteInvoice/', views.deleteInvoice),
]
