from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from .models import Counter
from .serializers import CounterModelSerializer, CounterUpdateSerializer


class CounterView(APIView):
    queryset = Counter.objects.all()
    serializer_class = CounterModelSerializer
    serializer_upadte = CounterUpdateSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, id):
        try:
            counter = self.queryset.get(id=id)
        except Counter.DoesNotExist:
            error = {"error": f"Counter with id ({id})doesn't exist"}
            return Response(error=error, status=status.HTTP_404_NOT_FOUND)
        data = self.serializer_class(counter).data
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request, id):
        try:
            counter = self.queryset.get(id=id)
        except Counter.DoesNotExist:
            error = {"error": f"Counter with id ({id})doesn't exist"}
            return Response(error=error, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_upadte(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.data["action"] == 1:
            counter.count = serializer.data["counter"] + 1
            counter.save()
            result = {"counter": counter.count}
            return Response(data=result, status=status.HTTP_200_OK)
        else:
            if serializer.data["counter"] == 0:
                return Response(data={"counter": 0}, status=status.HTTP_200_OK)
            counter.count = serializer.data["counter"] - 1
            counter.save()
            result = {"counter": counter.count}
            return Response(data=result, status=status.HTTP_200_OK)
