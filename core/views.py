from django.shortcuts import render
from googletrans import Translator, LANGUAGES

def home(request):
    translated_text = ''
    input_text = ''
    target_lang = 'en'

    # Convert language names to Title Case
    formatted_languages = {key: value.title() for key, value in LANGUAGES.items()}

    if request.method == 'POST':
        input_text = request.POST.get('text')
        target_lang = request.POST.get('language')
        translator = Translator()
        translated = translator.translate(input_text, dest=target_lang)
        translated_text = translated.text

    return render(request, 'home.html', {
        'languages': formatted_languages,
        'translated_text': translated_text,
        'input_text': input_text,
        'selected_language': target_lang
    })
