from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RandomUserSerializer
import requests

# def fetch_random_user(request):
#     response = requests.get("https://randomuser.me/api/")
#     data = response.json()
#     # print(data)
#     return JsonResponse(data)


@api_view(["GET"])
def fetch_random_user(request):
    response = requests.get("https://randomuser.me/api/")
    data = response.json()["results"][0]
    # Transform the data to fit the serializer
    transformed_data = {
        "gender": data["gender"],
        "title": data["name"]["title"],
        "first_name": data["name"]["first"],
        "last_name": data["name"]["last"],
        "street_number": data["location"]["street"]["number"],
        "street_name": data["location"]["street"]["name"],
        "city": data["location"]["city"],
        "state": data["location"]["state"],
        "country": data["location"]["country"],
        "postcode": data["location"]["postcode"],
        "latitude": data["location"]["coordinates"]["latitude"],
        "longitude": data["location"]["coordinates"]["longitude"],
        "timezone_offset": data["location"]["timezone"]["offset"],
        "timezone_description": data["location"]["timezone"]["description"],
        "email": data["email"],
        "username": data["login"]["username"],
        "password": data["login"]["password"],
        "dob": data["dob"]["date"][:10],  # Only date part
        "age": data["dob"]["age"],
        "phone": data["phone"],
        "cell": data["cell"],
        "picture_large": data["picture"]["large"],
        "picture_medium": data["picture"]["medium"],
        "picture_thumbnail": data["picture"]["thumbnail"],
        "nat": data["nat"],
    }
    serializer = RandomUserSerializer(data=transformed_data)
    if serializer.is_valid():
        # print(serializer.data)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)


def user_info(request):
    return render(request, "api/user_info.html")


def home(request):
    return render(request, "api/home.html")
