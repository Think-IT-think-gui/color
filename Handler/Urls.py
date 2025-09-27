from django.urls import path
from . views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    
    path('pay_transaction', Pay_Transaction.as_view(), name="pay_transaction"),
    path('main_transaction', Transfere_Account.as_view(), name="main_transaction"),
    path('recure_transaction', New_Recure.as_view(), name="recure_transaction"),
    path('check_ref', Check_Ref.as_view(), name="check_ref"),
    path('delete_transaction', Delete_transaction.as_view(), name="delete_transaction"),
    path('initialize_transaction', initialize_transaction.as_view(), name="initialize_transaction"),
    path('chech_number', Chech_Number.as_view(), name="chech_number"),    
    path('check_prepiad', Check_Prepaid.as_view(), name="check_prepaid"),
    path('check_card', Check_Card.as_view(), name="check_card"),
    path('check_bank', Check_Bank.as_view(), name="check_bank"),
    path('check_meter', Check_Meter.as_view(), name="check_meter"),
    path('send_bank', Send_Bank.as_view(), name="send_bank"),
    path('initialize_ecg', Initialize_Ecg.as_view(), name="initialize_ecg"),

    path('transaction', Transaction.as_view(), name="transaction"),
    path('dirrect_transaction', Dirrect_Transaction.as_view(), name="dirrect_transaction"),
    path('check_pos', Check_Pos.as_view(), name="check_pos"),
    

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
