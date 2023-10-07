from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from principal.models import Publicacao
from principal.serializers import PublicacaoSerializer


# Create your views here.

class PublicacaoApiView(APIView):

    def post(self,request, *args, **kwargs):
        obj = {
            'titulo': request.data.get('titulo'),
            'texto': request.data.get('texto'),
            'dataPublicacao': request.data.get('dataPublicacao')
        }

        serializer = PublicacaoSerializer(data=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,*args, **kwargs):
        publicacoes = Publicacao.objects.all()
        serializer = PublicacaoSerializer(publicacoes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PublicacaoDetalheApiview(APIView):

    def buscar(self, id):
        try:
            return Publicacao.objects.get(id=id)
        except:
            return None

    def retornarErro(self):
        return Response(
            {"resposta": "A publicação não foi encontrada."},
            status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id, *args, **kwargs):
        publicacao = self.buscar(id)

        if publicacao is not None:
            serializer = PublicacaoSerializer(publicacao)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return self.retornarErro()

    def put(self, request, id, *args, **kwargs):
        publicacao = self.buscar(id)

        if publicacao is not None:
            obj = {
                "titulo": request.data.get("titulo"),
                "texto": request.data.get("texto"),
                "dataPublicacao": request.data.get("dataPublicacao")
            }
            serializer = PublicacaoSerializer(instance=publicacao, data=obj)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return self.retornarErro()

    def delete(self,request,id, *args, **kwargs):
        publicacao = self.buscar(id)

        if publicacao is not None:
            publicacao.delete()
            return Response( {"resposta:": "A publicação foi excluída com sucesso."},
                             status=status.HTTP_404_NOT_FOUND
                             )