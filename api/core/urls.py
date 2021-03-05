from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

app_name = 'core'

urlpatterns = [
        path('', CompanyList.as_view(), name='companies'),
        path('company/<symbol>', CompanyDetail.as_view(), name='company'),
        path('comp/add', CompanyAdd.as_view(), name='new-company'),
        path('company/amend/<symbol>', CompanyAdmin.as_view(), name='ckk'),
        path('markets/', MarketList.as_view(), name='markets'),
        path('market/<mic>', MarketDetail.as_view(), name='mark-you'),
        path('mark/add', MarketAdd.as_view(), name='market-post'),
        path('market/amend/<mic>', MarketAdmin.as_view(), name='market'),
]


urlpatterns = format_suffix_patterns(urlpatterns)