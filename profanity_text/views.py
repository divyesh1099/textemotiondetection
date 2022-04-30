from re import A
from django.shortcuts import render
import text2emotion as te
import nltk
nltk.download('omw-1.4')

happy_words = ["joyful", "lucky", "jolly"]
sad_words = ["miserable", "depressed", "unhappy"]
angry_words = ["annoyed", "irritated", "aggrieved"]


# Create your views here.
def index(request):
    result=""
    user_input_string = ''
    if request.method=="POST":
        user_input_string = request.POST['content']
        result = te.get_emotion(user_input_string)
    context ={
           "result":result,
           "original": user_input_string
    }

    return render(request, 'profanity_text/Home.html', context)
