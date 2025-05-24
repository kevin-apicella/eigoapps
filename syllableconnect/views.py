from django.shortcuts import render, redirect
from django.urls import reverse

from syllableconnect.models import *
import random
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


def load_app_syllableconnect(request):
    # establish word bank
    words = request.session.get("word_bank", None)
    if not words:
        words = [x.word for x in WordBank.objects.filter(connect_app=True)]
        random.shuffle(words)
        request.session['word_bank'] = words

    # establish index
    index = request.session.get("index", 0)
    request.session["index"] = index
    print(f"the word bank is {len(words)}")

    if index == len(words):
        return redirect(reverse('menu'))
    print(f"the index is {index}")
    request.session['answer'] = words[index]

    # establish syllables and order for blocks
    syllables = SyllableBank.objects.get(word=words[index]).syllables
    reshuffle(syllables, words[index])

    # create percentage for progress bar
    progress_percentage = ((index + 1) / len(words)) * 100
    request.session['progress_percentage'] = progress_percentage
    context = {
        "index": index+1,
        "total": len(words),
        "answer_length": len(words[index]),
        "syllables": syllables,
        "progress_percentage": progress_percentage
        }

    return render(request, 'syllableconnect2.html', context)


@csrf_exempt
def check_answer(request):
    data = json.loads(request.body)
    user_answer = data.get('answer', '')
    correct_answer = request.session['answer']
    if user_answer == correct_answer:
        is_correct = True
        request.session["index"] = request.session.get("index") + 1
    else:
        is_correct = False
    print(f"is_correct is set to {is_correct}")
    return JsonResponse({
        'is_correct': is_correct
    })


def reshuffle(arr, answer):
    random.shuffle(arr)
    order_check = ""
    for x in arr:
        order_check += x
    if order_check == answer:
        print("DING DING DING RESHUFFLE DING DING DING")
        reshuffle(arr, answer)
