from django.shortcuts import render
from rest_framework.views import APIView
from part1 import models
import csv
import os
from rest_framework.response import Response
from part1 import serializers
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import JsonResponse


# Create your views here.

def populateDatabase():
    print(os.getcwd())
    with open('bank_branches.csv') as file_:
        reader = csv.reader(file_)
        for row in reader:
            _, created = models.BankBranches.objects.get_or_create(
                ifsc=row[0],
                bank_id=row[1],
                branch=row[2],
                address=row[3],
                city=row[4],
                district=row[5],
                state=row[6],
                bank_name=row[7],
            )
            print(created)
            if not created:
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def serializerData(obj):
    return serializers.BankBranchesSerializer(obj).data


# @api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))

class Autocomplete(APIView):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        limit = request.GET.get('limit')
        offset = request.GET.get('offset')

        objs = models.BankBranches.objects.filter(branch__icontains=q)
        objs = objs[int(offset):]
        objs = objs[0:int(limit)]

        branches = list(map(serializerData, objs))
        branches = {"branches": branches}

        return JsonResponse(branches, safe=False)


class Search(APIView):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        limit = request.GET.get('limit')
        offset = request.GET.get('offset')

        objs = models.BankBranches.objects.filter(branch__iexact=q)
        objs = objs[int(offset):]
        objs = objs[0:int(limit)]

        branches = list(map(serializerData, objs))
        branches = {"branches": branches}

        return JsonResponse(branches)
