from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.

def infractionsMin(request, min):
    with open('./infractions.json') as f:
        infractions_dict = json.load(f)
    
    json_data = open('./infractions.json')   
    data1 = json.load(json_data) # deserialises it
    data2 = json.dumps(data1, indent=4, sort_keys=True) # json formatted string
    output = "<body>"

    infractions_dict.sort(key=extract_time)
    for infraction in infractions_dict:
        if infraction['infractions_speed'] >= int(min):
            output += "<p>" + str(infraction) + "</p><br>"
    output += "</body>"
    return HttpResponse(output)
    json_data.close()

def infractions(request):
    with open('./infractions.json') as f:
        infractions_dict = json.load(f)
    
    json_data = open('./infractions.json')   
    data1 = json.load(json_data) # deserialises it
    data2 = json.dumps(data1, indent=4, sort_keys=True) # json formatted string
    output = "<body>"

    infractions_dict.sort(key=extract_time)
    for infraction in infractions_dict:
        output += "<p>" + str(infraction) + "</p><br>"
    output += "</body>"
    return HttpResponse(output)
    json_data.close()

def extract_time(json):
    try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
        return int(json['infractions_speed'])
    except KeyError:
        return 0