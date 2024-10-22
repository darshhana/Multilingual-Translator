from transformers import MarianMTModel, MarianTokenizer

# Mapping target languages to model names
language_model_map = {
    'hi': 'Helsinki-NLP/opus-mt-en-hi',   # English to Hindi
    'fr': 'Helsinki-NLP/opus-mt-en-fr',   # English to French
    'es': 'Helsinki-NLP/opus-mt-en-es',   # English to Spanish
    'de': 'Helsinki-NLP/opus-mt-en-de',   # English to German
    'ja': 'Helsinki-NLP/opus-mt-en-jap',   # English to Japanese
    'zh': 'Helsinki-NLP/opus-mt-en-zh'    # English to Chinese
}

def translate_text(text, target_language):
    model_name = language_model_map.get(target_language, 'Helsinki-NLP/opus-mt-en-hi')  # Default to Hindi
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    tokenized_text = tokenizer(text, return_tensors='pt', padding=True, truncation=True )
    translation = model.generate(**tokenized_text)

    translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
    # translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translation]
    return translated_text
