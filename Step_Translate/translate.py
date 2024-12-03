import os
import json
import re

JSON_LEXICON_FILE = "lexicon.json"


def is_georgian_word(word):
    georgian_regex = re.compile(r'^[\u10A0-\u10FF]+$')
    return bool(georgian_regex.match(word))


def is_english_word(word):
    english_regex = re.compile(r'^[a-zA-Z]+$')
    return bool(english_regex.match(word))


def is_french_word(word):
    french_regex = re.compile(r'^[a-zA-Zéèàùâêîôûç]+$')
    return bool(french_regex.match(word))


def load_json_lexicon():
    if not os.path.exists(JSON_LEXICON_FILE):
        return {}
    with open(JSON_LEXICON_FILE, "r", encoding="utf-8") as f:
        try:
            lexicon = json.load(f)
            return {
                src_lang.lower(): {
                    tgt_lang.lower(): {
                        word.lower(): translation.lower()
                        for word, translation in translations.items()
                    }
                    for tgt_lang, translations in target_langs.items()
                }
                for src_lang, target_langs in lexicon.items()
            }
        except json.JSONDecodeError as e:
            print(f"Error reading {JSON_LEXICON_FILE}: {e}.\n")
            return {}


def save_json_lexicon(lexicon):
    with open(JSON_LEXICON_FILE, "w", encoding="utf-8") as f:
        json.dump(lexicon, f, indent=4)


def translate_word_json(lexicon, source_lang, target_lang, word):
    return lexicon.get(source_lang.lower(), {}).get(target_lang.lower(), {}).get(word.lower(), None)


def translate_sentence_json(lexicon, source_lang, target_lang, sentence):
    words = sentence.split()
    translated_words = []

    for word in words:
        translation = translate_word_json(lexicon, source_lang, target_lang, word)
        if translation:
            translated_words.append(translation)
        else:
            translated_words.append(word)

    return " ".join(translated_words)


def add_translation_json(lexicon, source_lang, target_lang, source_word, target_word):
    source_lang = source_lang.lower()
    target_lang = target_lang.lower()
    source_word = source_word.lower()
    target_word = target_word.lower()

    if source_word in lexicon.setdefault(source_lang, {}).setdefault(target_lang, {}):
        print(f"Translation for '{source_word}' already exists!\n")
        return

    if source_lang == "georgian" and not is_georgian_word(source_word):
        print(f"Error: The source word '{source_word}' is not a valid Georgian word.\n")
        return
    elif source_lang == "english" and not is_english_word(source_word):
        print(f"Error: The source word '{source_word}' is not a valid English word.\n")
        return
    elif source_lang == "french" and not is_french_word(source_word):
        print(f"Error: The source word '{source_word}' is not a valid French word.\n")
        return

    if target_lang == "georgian" and not is_georgian_word(target_word):
        print(f"Error: The target word '{target_word}' is not a valid Georgian word.\n")
        return
    elif target_lang == "english" and not is_english_word(target_word):
        print(f"Error: The target word '{target_word}' is not a valid English word.\n")
        return
    elif target_lang == "french" and not is_french_word(target_word):
        print(f"Error: The target word '{target_word}' is not a valid French word.\n")
        return

    lexicon[source_lang][target_lang][source_word] = target_word
    print(f"Translation for '{source_word}' added successfully!\n")


def select_language():
    while True:
        print("Choose a language pair:")
        print("1. Georgian -> English")
        print("2. Georgian -> French")
        print("3. English -> Georgian")
        print("4. French -> Georgian")
        choice = input("Enter your choice (1-4): ").strip()
        languages = {
            "1": ("Georgian", "English"),
            "2": ("Georgian", "French"),
            "3": ("English", "Georgian"),
            "4": ("French", "Georgian"),
        }
        if choice in languages:
            return languages[choice]
        print("Invalid choice! Please enter a number between 1 and 4.\n")
