import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ml_model.predict_sub import predict_subreddit

@csrf_exempt #not recommended for production
def predict(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('title', None)
        if text:
            prediction = predict_subreddit(text)
            return JsonResponse({'prediction':prediction}, status=200)
        else:
            return JsonResponse({'error': 'No text field provided.'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

