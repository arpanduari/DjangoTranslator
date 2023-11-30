from django.shortcuts import render
from googletrans import Translator
from .languages import langs

translator = Translator()


def home(request):
    translated_word = None
    input_word = request.session.get("inputWord", "")
    output_language = request.session.get("outputLanguage", "")
    translator_result = request.session.get("translator_result", "")
    translation_history = request.session.get("translation_history", [])

    if request.method == "POST":
        input_word = request.POST.get("inputWord")
        output_word_code = request.POST.get("outputLanguage")
        translated_word = translator.translate(input_word, dest=output_word_code).text

        output_language = langs[output_word_code]

        translation_history = request.session.get("translation_history", [])
        translation_history.append(
            {
                "input_word": input_word,
                "output_language": output_language,
                "translated_word": translated_word,
            }
        )
        request.session["inputWord"] = input_word
        request.session["outputLanguage"] = output_language
        request.session["translator_result"] = translated_word
        request.session["translation_history"] = translation_history

    return render(
        request,
        "app/home.html",
        {
            "input_word": input_word,
            "output_language": output_language,
            "translator_result": translator_result,
            "translation_history": translation_history,
            "langs": langs,
        },
    )
