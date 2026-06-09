import pickle
import json
# avoid requiring pandas at module import time; construct prediction input as plain lists

from django.shortcuts import render

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model.json", "r") as f:
    data_columns = json.load(f)["data_columns"]


def home(request):

    prediction = None

    if request.method == "POST":

        location = request.POST["location"].lower()
        sqft = float(request.POST["total_sqft"])
        bath = float(request.POST["bath"])
        bhk = int(request.POST["bhk"])

        input_data = {col: 0 for col in data_columns}

        input_data["total_sqft"] = sqft
        input_data["bath"] = bath
        input_data["bhk"] = bhk

        if location in input_data:
            input_data[location] = 1

        # build feature vector in the same order as data_columns
        feature_vector = [input_data.get(col, 0) for col in data_columns]
        prediction = model.predict([feature_vector])[0]

    return render(
        request,
        "home.html",
        {"prediction": prediction}
    )

