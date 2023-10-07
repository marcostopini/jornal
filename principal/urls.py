from django.urls import path
from principal.views import PublicacaoApiView, PublicacaoDetalheApiview

urlpatterns = [
    path('api/publicacao',PublicacaoApiView.as_view()),
    path('api/publicacao/<int:id>', PublicacaoDetalheApiview.as_view())
    #path('api/autor', .....)
]
