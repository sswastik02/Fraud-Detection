from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_500_INTERNAL_SERVER_ERROR

from .serialzers import TransactionSerialzier

from ML.models.creditcard import CreditCard

class TransactionDetection(APIView):
    def post(self,request):
        transaction_serializer = TransactionSerialzier(data=request.data)
        if transaction_serializer.is_valid(raise_exception=True):
            c = CreditCard()
            try:
                result = c.predict(request.data)
                return Response(
                    {
                        "fraud": result[0] == 1
                    },
                    status= HTTP_200_OK,
                )
            except:
                return Response(
                    {
                        "error":"could not process request"
                    },
                    status=HTTP_500_INTERNAL_SERVER_ERROR,
                )