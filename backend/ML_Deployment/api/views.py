import imp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_500_INTERNAL_SERVER_ERROR

from .serialzers import PhishingSerializer, TransactionSerializer

from ML.models.creditcard import CreditCard
from ML.models.phishing_site import PhishingSite
from ML.models.phishing_url import PhishingURL
from ML.models.document import Document

class TransactionDetection(APIView):
    def post(self,request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
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

class PhishingSiteDetection(APIView):
   
    def post(self,request):
        serializer = PhishingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        p = PhishingSite()
        try:
            result = p.predict(request.data.get('url'))
            return Response(
                {
                    "phishing":result[0] == 1
                },
                status = HTTP_200_OK
            )
        except:
             return Response(
                    {
                        "error":"could not process request"
                    },
                    status=HTTP_500_INTERNAL_SERVER_ERROR,
             )

class PhishingUrlDetection(APIView):
    permission_classes=[]
    def post(self,request):
        serializer = PhishingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        p = PhishingURL()
        try:
            result = p.predict(request.data.get('url'))
            return Response(
                {
                    "phishing":result[0] == 1
                },
                status = HTTP_200_OK
            )
        except:
             return Response(
                    {
                        "error":"could not process request"
                    },
                    status=HTTP_500_INTERNAL_SERVER_ERROR,
             )

class DocumentDetection(APIView):
    def post(self,request):
        serializer = PhishingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        d = Document()

        try:
            result = d.verify(request.data.get('url'))
            return Response(
                {
                    "document":result,
                },
                status=HTTP_200_OK
            )
        except:
            return Response(
                {
                    "document":False,
                },
                status=HTTP_200_OK
            )
