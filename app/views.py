
from django.shortcuts import render,HttpResponse
from app.models import info
from app.serializers import infoserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET','POST','DELETE','UPDATE'])
def list(request):
    bloods=info.objects.all()
    convert=infoserializer(bloods,many=True)
    return Response(convert.data)


@api_view(['GET'])
def listitem(request,pk):
    bloods=info.objects.get(id=pk)
    convert=infoserializer(bloods,many=False)
    return Response(convert.data)


@api_view(['POST'])
def addlist(request):
    add=infoserializer(data=request.data)
    if add.is_valid():
        add.save()
    return Response(add.data)    

# @api_view(['UPDATE'])
# def update(request,pk):
#     task=info.objects.get(id=pk)
#     add=infoserializer(instance=task,task=request.data)
#     if add.is_valid():
#         add.save()
#     return Response(add.data)    

@api_view(['POST'])
def update_items(request, pk):
	item = info.objects.get(pk=pk)
	group = infoserializer(instance=item, data=request.data)
	if group.is_valid():
		group.save()
		return Response(group.data)
        

@api_view(['DELETE'])
def delete(request, pk):
	item = info.objects.get( pk=pk)
	item.delete()
	return Response("item deleted succesfully")

	


        


