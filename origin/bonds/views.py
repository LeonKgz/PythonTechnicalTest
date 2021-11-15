from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from bonds.models import Bond

import json
import requests
import sqlite3

class HelloWorld(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        username = request.user
        filters = request.META["QUERY_STRING"].split("&")

        if filters[0]:

          query = dict([s.split("=") for s in request.META["QUERY_STRING"].split("&")])
          query["username"] = str(username)
          return Response([b.get_json() for b in Bond.objects.filter(**query)])
        
        else:

          return Response([b.get_json() for b in Bond.objects.filter(username=username)])

    def post(self, request):
        username = request.user

        parameters = request.META["QUERY_STRING"].split("&")

        if not parameters[0]:
          return Response("Parameters are not present")

        query = dict([s.split("=") for s in parameters])
        all_fields_present = "isin" in query \
                              and "size" in query \
                              and "currency" in query \
                              and "maturity" in query \
                              and "lei" in query 

        if not all_fields_present:
          return Response("Not all parameters are present")
          
        
        lei = query["lei"]

        url = f"https://api.gleif.org/api/v1/lei-records/{lei}"
        response = requests.get(url)
        legal_name = response.json()["data"]["attributes"]["entity"]["legalName"]["name"]

        query["username"] = username
        query["legal_name"] = legal_name

        b = Bond(**query)
        b.save()

        return Response("Bond saved successfully")

