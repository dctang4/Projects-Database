# from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .models import Projects
from django.core.serializers import serialize
from json import loads

# Create your views here.
class ProjectsView(View):
  def get(self, req):
    # Serialize the data into JSON then turn the JSON into a dict
    all = loads(serialize('json', Projects.objects.all()))
    # Send the JSON response
    return JsonResponse(all, safe=False)

  def post(self, req):
    # Turn the body into a dict
    body = loads (req.body.decode("utf-8"))
    #create the new item
    newproject = Projects.objects.create(
      project=body['project'],
      livelurl=body['livelurl'],
      giturl=body['giturl'],
      image=body['image'],
      description=body['description'],
    )
    # Turn the object to json to dict, put in array to avoid non-iterable error
    data = loads(serialize('json', [newproject]))
    # send json response with new object
    return JsonResponse(data, safe=False)

class OneProjectView(View):
  def get(slef, req, param):
    # Filter and find a single item then serialize the data into JSON then turn the JSON into a dict
    one = loads(serialize('json', Projects.objects.filter(name=param)))
    # Send the JSON response
    return JsonResponse(one, safe=False)

  def put(self, req, param):
    # Turn the body into a dict
    body = loads(req.body.decode("utf-8"))
    # update the item
    Projects.objects.filter(name=param).update(
      project=body['project'],
      livelurl=body['livelurl'],
      giturl=body['giturl'],
      image=body['image'],
      description=body['description'],
    )
    newrecord = Projects.object.filter(name=param)
    # Turn the object to json to dict, put in array to avoid non-iterable error
    data = loads(serialize('json', [newrecord]))
    # send json response with updated object
    return JsonResponse(data, safe=False)

  def delete(self, req, param):
    # delete the item, get all remaining records for response
    Projects.objects.filter(name=param).delete()
    newrecord = Projects.objects.all()
    # Turn the results to json to dict, put in array to avoid non-iterable error
    data = loads(serialize('json', [newrecord]))
    # send json response with updated object
    return JsonResponse(data, safe=False)