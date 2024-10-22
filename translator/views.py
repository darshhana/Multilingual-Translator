from django.shortcuts import render

# # Create your views here.
# from .translation import translate_to_hindi

# def translate_view(request):
#     if request.method == 'POST':
#         # Get the input text from the form
#         input_text = request.POST.get('english_text')
        
#         # Perform translation
#         translated_text = translate_to_hindi(input_text)
        
#         # Pass the translated text back to the template
#         return render(request, 'translator/result.html', {'translated_text': translated_text})
#     return render(request, 'translator/translate.html')
from .translation import translate_text

def translate_view(request):
    if request.method == 'POST':
        input_text = request.POST.get('english_text')
        target_language = request.POST.get('target_language')  # Get selected target language
        translated_text = translate_text(input_text, target_language)
        return render(request, 'translator/result.html', {'translated_text': translated_text})
    return render(request, 'translator/translate.html')
