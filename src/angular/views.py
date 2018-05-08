from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from .forms import AngularForm
from .models import Angular
import json
from django.http import JsonResponse

from .serializers import AngularSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


def index(request):
    return render(request,'index.html',{})

def update(request,data=""):
    if request.method == 'POST':
        if data == 'data':
            print("######",data,"#########")
            data = request.body
            # print(data)
            convert = data.decode("utf-8")

            ds = json.loads(convert)
            # print("-------------------",ds)
            id = ds["id"]
            id = Angular.objects.filter(id=id)
            obj = get_object_or_404(Angular,pk=id)
            dict = {"id":obj.id,"name":obj.name,"number":obj.number}
            print(dict)
            # json = json.dumps(dict)
            # print(json)
            return JsonResponse(dict)
            # return redirect("/")
        else:
            print("@@@@@@@@@@@2",data,"@@@@@@@@@@@@@@@")
            data = request.body
            convert = data.decode("utf-8")
            ds = json.loads(convert)
            print(ds)
            id = ds["id"]
            name = ds["name"]
            number = ds["number"]
            print(id,name,number)
            obj=Angular.objects.filter(pk=id).update(name=name,number=number)
            return redirect("/")


def ajax(request):
    obj=Angular.objects.all()
    context = {
    "data" : obj,
    }
    return render(request,"ajax.html",context)



def sweet(request):
    return render(request,"sweet.html")


def request(request):
    return render(request,"response.htm")



def test(request):
    return render(request,"angular.html")


def angular(request):
    if request.method == "POST":
        data    = request.POST.get
        data    = request.body
        convert = data.decode("utf-8")
        ds      = json.loads(convert)
        name    = ds["name"]
        number  = ds["number"]
        obj = Angular(name=name,number=number)
        obj.save()
        return redirect("/")

    # form = AngularForm()
    data = Angular.objects.all()
    context = {
    # "form" : form,
    "data" : data
    }
    return render(request,"index.html",context)

def delete(request,table="",id=0):
    if request.is_ajax():
        print('yes')
    else:
        print('no')
        if request.method == 'POST':
            data = request.body
            print(data)
            print("--Table name--",table)
            convert = data.decode("utf-8")
            ds = json.loads(convert)
            print("-------------------",ds)
            id = ds["id"]
            print(id)
            obj = Angular.objects.filter(id=id)
            obj.delete()
            return redirect("/")
    print(table)
    print(id)
    return redirect("/")


class ApiData(APIView):
    def get(self,request):
        emp=Angular.objects.all()
        serialized_obj=AngularSerializer(emp,many=True)
        # print(serialized_obj.data)
        return Response(serialized_obj.data)
