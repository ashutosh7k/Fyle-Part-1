from django.shortcuts import render
from rest_framework.views import APIView
from part1 import models
import csv
import os
from rest_framework.response import Response
from part1 import serializers


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


def autocomplete(request):

    q = request.GET.get('q')
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')

    objs = models.BankBranches.objects.filter(branch__icontains=q)
    objs = objs[offset:]
    objs = objs[0:limit]

    branches = list(map(serializerData, objs))
    branches = {"branches": branches}

    return Response(branches)


def search(request):
    q = request.GET.get('q')
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')

    objs = models.BankBranches.objects.filter(branch=q)
    objs = objs[offset:]
    objs = objs[0:limit]

    branches = list(map(serializerData, objs))
    branches = {"branches": branches}

    return Response(branches)
