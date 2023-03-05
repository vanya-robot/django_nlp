from django.shortcuts import render
from django.http import JsonResponse
from .models import PredResults
from catboost import CatBoostClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        review_text = str(request.POST.get('review_text'))

        # Unpickle model
        vectorizer = pickle.load(open('predict/vectorizer.pickle', 'rb'))
        model = pickle.load(open('predict/django_ml.pickle', 'rb'))
        bi_model = pickle.load(open('predict/bi_classifier.pickle', 'rb'))
        # Make prediction
        result = model.predict(vectorizer.transform([review_text, ]))
        bi_result = bi_model.predict(vectorizer.transform([review_text, ]))
        classification = int(result[0][0])
        bi_class = 'Positive' if int(bi_result[0]) == 1 else 'Negative'

        PredResults.objects.create(review_text=review_text, classification=classification, bi_class=bi_class)

        return JsonResponse({'result': classification, 'review_text': review_text, 'bi_class': bi_class})


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)
