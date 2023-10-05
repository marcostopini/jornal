from django.urls import path
from principal.views import PublicacaoApiView

urlpatterns = [
    path('api',PublicacaoApiView.as_view())
]