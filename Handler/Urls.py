from django.urls import path
from . views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    
    path('pay_transaction', Pay_Transaction.as_view(), name="pay_transaction"),
    path('transaction', Transaction.as_view(), name="transaction"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
