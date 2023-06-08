from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ml_model.predict_sub import predict_subreddit
# Create your views here.
@csrf_exempt
def predict(request):
    if request.method == 'POST':
        text = request.POST['text']
        prediction = predict_subreddit(text)
        return JsonResponse({'prediction':prediction})
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)