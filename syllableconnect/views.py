from django.shortcuts import render, redirect
from django.urls import reverse
from syllableconnect.models import *
import random
import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play


def load_app_syllableconnect(request):

    words = request.session.get("word_bank", None)
    if not words:
        words = [x.word for x in WordBank.objects.filter(connect_app=True)]
        random.shuffle(words)
        jp_words = [WordBank.objects.get(word=entries).jp_word for entries in words]
        images = [WordBank.objects.get(word=entries).image_filename for entries in words]
        request.session['word_bank'] = words
        request.session['jp_words'] = jp_words
        request.session['images'] = images
    else:
        jp_words = request.session.get('jp_words', [])
        images = request.session.get('images', [])

    index = request.session.get("index", 0)
    request.session["index"] = index
    print(f"the word bank is {len(words)}")

    if index == len(words):
        return redirect(reverse('menu'))
    print(f"the index is {index}")
    request.session['answer'] = words[index]

    syllables = SyllableBank.objects.get(word=words[index]).syllables
    reshuffle(syllables, words[index])

    audio = SyllableBank.objects.get(word=words[index]).audio_json

    syllable_audio_paths = ["/static/audio/syllables/syllable - " + audio[syllable] + ".mp3" for syllable in syllables]
    word_audio_path = "/static/audio/words/" + WordBank.objects.get(word=words[index]).audio_filename

    progress_percentage = ((index + 1) / len(words)) * 100
    request.session['progress_percentage'] = progress_percentage

    current_image = "/images/" + images[index]
    print(current_image)
    print(os.path.isfile("static/" + current_image))
    context = {
        "index": index+1,
        "total": len(words),
        "answer_length": len(words[index]),
        "syllables": syllables,
        "progress_percentage": progress_percentage,
        "jp_word": jp_words[index],
        "image_exists": os.path.isfile("static/" + current_image),
        "current_image": current_image,
        "syllable_audio_paths": syllable_audio_paths,
        "syllable_data": zip(syllables, syllable_audio_paths),
        "word_audio_path": word_audio_path
        }

    return render(request, 'syllableconnect.html', context)


def load_previous_question(request):
    current_index = request.session.get("index", 0)

    if current_index > 0:
        request.session["index"] = current_index - 1

    return redirect('/syllableconnect/')


def load_next_question(request):
    current_index = request.session.get("index", 0)
    question_total = request.session.get("total", 20)
    if current_index < question_total:
        request.session["index"] = current_index + 1

    return redirect('/syllableconnect/')



@csrf_exempt
def check_answer(request):
    data = json.loads(request.body)
    user_answer = data.get('answer', '')
    correct_answer = request.session['answer']
    if user_answer == correct_answer:
        is_correct = True
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

