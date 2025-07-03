# yourapp/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer
from .services.embedding import get_embedding

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.validated_data['title']
        content = serializer.validated_data['content']

        try:
            vector = get_embedding(content)
        except Exception as e:
            return Response({"error": "Embedding failed", "detail": str(e)}, status=500)

        doc = Document.objects.create(
            title=title,
            content=content,
            embedding=vector
        )

        return Response({"id": doc.id}, status=status.HTTP_201_CREATED)
