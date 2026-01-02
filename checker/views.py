from django.shortcuts import render
from django.http import JsonResponse
import json
from Levenshtein import distance
import re

import os

# Load dictionary from file
# We assume words.txt is in the same directory as views.py or adjust path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DICTIONARY_PATH = os.path.join(BASE_DIR, 'words.txt')
BENGALI_DICTIONARY = set()

try:
    with open(DICTIONARY_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip()
            if word:
                BENGALI_DICTIONARY.add(word)
except FileNotFoundError:
    print(f"Warning: Dictionary file not found at {DICTIONARY_PATH}. Using empty dictionary.")


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
