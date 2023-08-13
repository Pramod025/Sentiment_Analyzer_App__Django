import os
from django.shortcuts import render
import joblib

def home(request):
    sentiment_result = None
     # Construct the full path to the model file
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(BASE_DIR, 'folder1', 'Sentiment_model')

    # Load the pre-trained model using joblib from the specified path
    sentiment_model = joblib.load(model_path)
    
    # Rest of your code...
    if request.method == 'POST':
        review_text = request.POST.get('review_text', '')
        
        # Use the loaded sentiment model to predict sentiment
        prediction = sentiment_model.predict([review_text])
        if prediction[0] == 1:
            sentiment_result = 'Great Work there! Majority of people liked your product 😃'
        elif prediction[0] == -1:
            sentiment_result = "Try improving your product! Majority of people didn't find your product upto the mark 😔"
        else:
             sentiment_result = "Good Work there, but there's room for improvement! Majority of people have neutral reactions to your product 😶"
        
        return render(request, 'index.html', {'sentiment_result': sentiment_result})
    
    return render(request, 'index.html')

