from django.shortcuts import render
from .models import People
# Create your views here.
from django.http import JsonResponse
import json


def validate(request):
    if request.method == 'POST':
        body = request.body
        data = json.loads(body)
        code = data.get('code')
        response = {
            "message": "",
            "status": ""
        }
        people = People.objects.filter(code=code).first()
        if not people:
            response["message"] = "No esta registrado"
            response["status"] = "Error"
            return JsonResponse(response)

        gender = 'a' if people.gender == "Mujer" else 'o'
        full_name = people.full_name
        is_valid = people.is_valid
        if not is_valid:
            response["message"] = "Hola {} No fuiste seleccionad{} para estar en este evento presencial".format(
                full_name, gender
            )
            response["status"] = "Error"
            response["user_data"] = {
                "full_name": people.full_name,
                "gender": people.gender,
            }
            return JsonResponse(response)

        response["message"] = "Bienvenid{} {} al mejor evento de marketing digital 2022".format(
            gender, full_name
        )
        response["status"] = "Success"
        response["user_data"] = {
            "full_name": people.full_name,
            "gender": people.gender,
        }
        return JsonResponse(response)

