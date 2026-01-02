from django.shortcuts import render
from django.http import JsonResponse
import json
from Levenshtein import distance
import re

# Load dictionary (Mock for now, can be replaced with a file load)
# Ideally, we load this once when the server starts.
# I will use a small set of common words for demonstration.
BENGALI_DICTIONARY = {
    "আমি", "ভাত", "খাই", "বই", "পড়ি", "স্কুলে", "যাই", "গান", "গাই", "বাংলা", "ভাষা",
    "আমার", "নাম", "ঢাকা", "বাংলাদেশ", "সুন্দর", "পাখি", "আকাশ", "নীল", "সূর্য", 
    "সকাল", "বিকাল", "রাত", "দিন", "মানুষ", "জীবন", "ভালোবাসা", "বন্ধু", "মা", "বাবা",
    "ভাই", "বোন", "কাজ", "খেলা", "আনন্দ", "দুঃখ", "হাসি", "কান্না", "ফুল", "ফল", "গাছ",
    "নদী", "সাগর", "পাহাড়", "গ্রাম", "শহর", "রাস্তা", "গাড়ি", "বাড়ি", "ঘর", "দরজা",
    "জানালা", "টেবিল", "চেয়ার", "কাগজ", "কলম", "খাতা", "শিক্ষক", "ছাত্র", "বিশ্ববিদ্যালয়"
}

def index(request):
    return render(request, 'checker/index.html')

def check_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '')
            
            # Simple tokenization by splitting on whitespace and punctuation
            # We want to keep track of tokens to reconstruct or just return list
            tokens = re.split(r'(\s+|[।?!,;])', text)
            
            result_tokens = []
            
            for token in tokens:
                # Skip whitespace/punctuation for spell checking, but keep in result
                clean_token = token.strip()
                if not clean_token:
                    result_tokens.append({'text': token, 'is_error': False})
                    continue
                
                # Check if it's a Bengali word (basic check)
                if not re.search(r'[\u0980-\u09FF]', clean_token):
                     # English or other text - skip spell check for now or mark as ok
                     result_tokens.append({'text': token, 'is_error': False})
                     continue

                if clean_token in BENGALI_DICTIONARY:
                    result_tokens.append({'text': token, 'is_error': False})
                else:
                    # Error found, find suggestions
                    suggestions = get_suggestions(clean_token)
                    result_tokens.append({
                        'text': token, 
                        'is_error': True,
                        'suggestions': suggestions
                    })

            return JsonResponse({'tokens': result_tokens})
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid method'}, status=405)

def get_suggestions(word, max_suggestions=3):
    # Sort dictionary words by Levenshtein distance
    candidates = []
    for dict_word in BENGALI_DICTIONARY:
        dist = distance(word, dict_word)
        # Threshold: if distance is too big, don't suggest
        if dist <= 3:  
            candidates.append((dict_word, dist))
    
    candidates.sort(key=lambda x: x[1])
    return [word for word, dist in candidates[:max_suggestions]]
