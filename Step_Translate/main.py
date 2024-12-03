from translate import *


def main():
    print("Translator Application\n")

    json_lexicon = load_json_lexicon()

    language_pair = select_language()
    source_lang, target_lang = language_pair
    print(f"Selected languages: {source_lang} -> {target_lang}\n")

    while True:
        sentence = input("Enter a sentence to translate or 'exit' to quit: ").strip()
        if not sentence:
            print("Sentence cannot be empty. Please try again.\n")
            continue
        if sentence.lower() == "exit":
            print("Thank you for using the Translator Application!\n")
            break

        words = sentence.split()
        invalid_word_found = False

        for word in words:
            if source_lang.lower() == "georgian" and not is_georgian_word(word):
                print(f"Invalid Georgian word: '{word}'. Please enter a valid Georgian word.\n")
                invalid_word_found = True
                break
            elif source_lang.lower() == "english" and not is_english_word(word):
                print(f"Invalid English word: '{word}'. Please enter a valid English word.\n")
                invalid_word_found = True
                break
            elif source_lang.lower() == "french" and not is_french_word(word):
                print(f"Invalid French word: '{word}'. Please enter a valid French word.\n")
                invalid_word_found = True
                break

        if invalid_word_found:
            continue

        translated_sentence = translate_sentence_json(json_lexicon, source_lang, target_lang, sentence)
        print(f"Translated sentence: {translated_sentence}\n")

        for word in words:
            if translate_word_json(json_lexicon, source_lang, target_lang, word) is None:
                print(f"Word '{word}' not found in the dictionary.\n")
                add_translation = input(
                    f"Would you like to add the translation for '{word}'? (yes/no): ").strip().lower()
                if add_translation == "yes":
                    while True:
                        translation = input(f"Enter the translation for '{word}': ").strip()
                        if translation:
                            break
                        print("Translation cannot be empty. Please try again.\n")

                    add_translation_json(json_lexicon, source_lang, target_lang, word, translation)
                    save_json_lexicon(json_lexicon)


main()
