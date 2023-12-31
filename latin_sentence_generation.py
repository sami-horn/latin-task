# -*- coding: utf-8 -*-
"""Latin Sentence Generation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1USFsMq2esT4g_Wt-1ePy5sKxjmZumbDV
"""

import random
import pandas as pd

nouns = {
    'puella': {
        'gender': 'feminine',
        'nominative': 'puella',
        'accusative': 'puellam',
        'nominative_plural': 'puellae',
        'accusative_plural': 'puellas',
        'translation': 'girl',
        'translation_plural': 'girls'
    },
    'columba': {
        'gender': 'feminine',
        'nominative': 'columba',
        'accusative': 'columbam',
        'nominative_plural': 'columbae',
        'accusative_plural': 'columbas',
        'translation': 'dove',
        'translation_plural': 'doves'
    },
    'advena': {
        'gender': 'feminine',
        'nominative': 'advena',
        'accusative': 'advenam',
        'nominative_plural': 'advenae',
        'accusative_plural': 'advenas',
        'translation': 'stranger',
        'translation_plural': 'strangers'
    },
    'ancilla': {
        'gender': 'feminine',
        'nominative': 'ancilla',
        'accusative': 'ancillam',
        'nominative_plural': 'ancillae',
        'accusative_plural': 'ancillas',
        'translation': 'maid',
        'translation_plural': 'maids'
    },
    'nauta': {
        'gender': 'feminine',
        'nominative': 'nauta',
        'accusative': 'nautam',
        'nominative_plural': 'nautae',
        'accusative_plural': 'nautas',
        'translation': 'sailor',
        'translation_plural': 'sailors'
    },
    'gallina': {
        'gender': 'feminine',
        'nominative': 'gallina',
        'accusative': 'gallinam',
        'nominative_plural': 'gallinae',
        'accusative_plural': 'gallinas',
        'translation': 'hen',
        'translation_plural': 'hens'
    }
}

verbs = {
    'pello': {
        'present': {
            'singular': {
                'first': {'conjugation': 'pello', 'translation': 'I hit'},
                'second': {'conjugation': 'pelles', 'translation': 'you hit'},
                'third': {'conjugation': 'pellet', 'translation': 'hits'}
            },
            'plural': {
                'first': {'conjugation': 'pellemus', 'translation': 'we hit'},
                'second': {'conjugation': 'pelletis', 'translation': 'you all hit'},
                'third': {'conjugation': 'pellent', 'translation': 'hit'}
            }
        },
        'translation': 'loves'
    },
    'video': {
        'present': {
            'singular': {
                'first': {'conjugation': 'video', 'translation': 'I see'},
                'second': {'conjugation': 'vides', 'translation': 'you see'},
                'third': {'conjugation': 'videt', 'translation': 'sees'}
            },
            'plural': {
                'first': {'conjugation': 'videmus', 'translation': 'we see'},
                'second': {'conjugation': 'videtis', 'translation': 'you all see'},
                'third': {'conjugation': 'vident', 'translation': 'see'}
            }
        },
        'translation': 'reads'
    },
    'moneo': {
        'present': {
            'singular': {
                'first': {'conjugation': 'moneo', 'translation': 'I warn'},
                'second': {'conjugation': 'mones', 'translation': 'you warn'},
                'third': {'conjugation': 'monet', 'translation': 'warns'}
            },
            'plural': {
                'first': {'conjugation': 'monemus', 'translation': 'we warn'},
                'second': {'conjugation': 'monetis', 'translation': 'you all warn'},
                'third': {'conjugation': 'monent', 'translation': 'warn'}
            }
        },
        'translation': 'runs'
    },
    'debeo': {
        'present': {
            'singular': {
                'first': {'conjugation': 'debeo', 'translation': 'I owe'},
                'second': {'conjugation': 'debes', 'translation': 'you owe'},
                'third': {'conjugation': 'debet', 'translation': 'owes'}
            },
            'plural': {
                'first': {'conjugation': 'debemus', 'translation': 'we owe'},
                'second': {'conjugation': 'debetis', 'translation': 'you all owe'},
                'third': {'conjugation': 'debent', 'translation': 'owe'}
            }
        },
        'translation': 'bites'
    },
    'timeo': {
        'present': {
            'singular': {
                'first': {'conjugation': 'timeo', 'translation': 'I fear'},
                'second': {'conjugation': 'times', 'translation': 'you fear'},
                'third': {'conjugation': 'timet', 'translation': 'fears'}
            },
            'plural': {
                'first': {'conjugation': 'timemus', 'translation': 'we fear'},
                'second': {'conjugation': 'timetis', 'translation': 'you all fear'},
                'third': {'conjugation': 'timent', 'translation': 'fear'}
            }
        },
        'translation': 'fears'
    },
    'doceo': {
        'present': {
            'singular': {
                'first': {'conjugation': 'doceo', 'translation': 'I teach'},
                'second': {'conjugation': 'doces', 'translation': 'you teach'},
                'third': {'conjugation': 'docet', 'translation': 'teaches'}
            },
            'plural': {
                'first': {'conjugation': 'docemus', 'translation': 'we teach'},
                'second': {'conjugation': 'docetis', 'translation': 'you all teach'},
                'third': {'conjugation': 'docent', 'translation': 'teach'}
            }
        },
        'translation': 'teaches'
    }
}

def choose_word(word_type):
    """ Takes the string 'nouns' or 'verbs' as an argument and returns a random selection from the dictionary"""
    return random.choice(list(word_type.keys()))


def choose_number():
    """ Randomly selects singular or plural number"""
    return random.choice(['singular', 'plural'])


def choose_person():
    """ Randomly selects first, second, or third person"""
    return random.choice(['first', 'second', 'third'])


def generate_sentence_components():
    """ From the word keys and the associated conjugations, create the sentence as a string"""
    subject = choose_word(nouns)
    object = choose_word(nouns)
    verb = choose_word(verbs)

    conjugation = choose_number()
    obj_conjugation = choose_number()
    person = choose_person()

    return [subject, object, verb, conjugation, obj_conjugation, person]

# Function to generate a Latin sentence
def construct_sentence(components):

    subject, object, verb, conjugation, obj_conjugation, person = components

    subject_word = nouns[subject]['nominative' if conjugation == 'singular' else 'nominative_plural']
    subject_dec = 'nominative' if conjugation == 'singular' else 'nominative_plural'

    object_word = nouns[object]['accusative' if obj_conjugation == 'singular' else 'accusative_plural']
    object_dec = 'accusative' if obj_conjugation == 'singular' else 'accusative_plural'

    verb_word = verbs[verb]['present'][conjugation][person]['conjugation']
    verb_conj = [conjugation, person]

    if person == 'third':
      sentence = f"{subject_word} {verb_word} {object_word}"
      sentence_keys = [subject, verb, object]
      sentence_conj = [conjugation, verb_conj, obj_conjugation]
    else:
      sentence = f"{verb_word} {object_word}"
      sentence_keys = [verb, object]
      sentence_conj = [verb_conj, obj_conjugation]

    return sentence, sentence_keys, sentence_conj

# Function to translate a Latin sentence to English
def translate_sentence(data):
    sentence = data[0]
    sentence_keys = data[1]
    sentence_conj = data[2]

    translated_words = []
    counter = 0

    for word in sentence_keys:
        if word in nouns:
            if sentence_conj[counter] == 'singular':
              translated_words.append('the ' + nouns[word]['translation'])
            else:
              translated_words.append('the ' + nouns[word]['translation_plural'])
        elif word in verbs:
            translated_words.append(verbs[word]['present'][sentence_conj[counter][0]][sentence_conj[counter][1]]['translation'])

        counter += 1

    translated_sentence = ' '.join(translated_words)
    return translated_sentence

def mistranslate_sub_pl(data):
    sentence = data[0]
    sentence_keys = data[1]
    sentence_conj = data[2]

    if len(sentence_conj) == 3:
      if sentence_conj[0]=='plural':
        new_conj = ['singular', ['singular', sentence_conj[1][1]], sentence_conj[2]]
      if sentence_conj[0]=='singular':
        new_conj = ['plural', ['plural', sentence_conj[1][1]], sentence_conj[2]]

    if len(sentence_conj) == 2:

      if sentence_conj[0][0]=='plural':
        new_conj = [['singular', sentence_conj[0][1]], sentence_conj[1]]
      if sentence_conj[0][0]=='singular':
        new_conj = [['plural', sentence_conj[0][1]], sentence_conj[1]]

    return translate_sentence([sentence, sentence_keys, new_conj])


def mistranslate_obj_pl(data):
    sentence = data[0]
    sentence_keys = data[1]
    sentence_conj = data[2]

    if len(sentence_conj) == 3:
      if sentence_conj[2]=='plural':
        new_conj = [sentence_conj[0], sentence_conj[1], 'singular']
      if sentence_conj[2]=='singular':
        new_conj = [sentence_conj[0], sentence_conj[1], 'plural']

    if len(sentence_conj) == 2:
      if sentence_conj[1]=='plural':
        new_conj = [sentence_conj[0], 'singular']
      if sentence_conj[1]=='singular':
        new_conj = [sentence_conj[0], 'plural']

    return translate_sentence([sentence, sentence_keys, new_conj])


def mistranslate_wrong_subj(data):
  sentence = data[0]
  sentence_keys = data[1]
  sentence_conj = data[2]

  if len(sentence_keys) == 3:
    new_subj_key = choose_word(nouns)

    while new_subj_key == sentence_keys[0]:
      new_subj_key = choose_word(nouns)

    sentence_keys[0] = new_subj_key

  if len(sentence_keys) == 2:

    if sentence_conj[0][1] == 'first':
      verb_conj = [sentence_conj[0][0], 'second']
    else:
      verb_conj = [sentence_conj[0][0], 'first']

    sentence_conj[0] = verb_conj

  return translate_sentence([sentence, sentence_keys, sentence_conj])


def mistranslate_wrong_verb(data):
  sentence = data[0]
  sentence_keys = data[1]
  sentence_conj = data[2]

  if len(sentence_keys) == 3:
    new_verb_key = choose_word(verbs)
    while new_verb_key == sentence_keys[1]:
      new_verb_key = choose_word(verbs)
    sentence_keys[1] = new_verb_key

  if len(sentence_keys) == 2:
    new_verb_key = choose_word(verbs)
    while new_verb_key == sentence_keys[0]:
      new_verb_key = choose_word(verbs)
    sentence_keys[0] = new_verb_key

  return translate_sentence([sentence, sentence_keys, sentence_conj])


def mistranslate_wrong_obj(data):
  sentence = data[0]
  sentence_keys = data[1]
  sentence_conj = data[2]

  if len(sentence_keys) == 3:
    new_obj_key = choose_word(nouns)
    while new_obj_key == sentence_keys[2]:
      new_obj_key = choose_word(nouns)
    sentence_keys[2] = new_obj_key

  if len(sentence_keys) == 2:
    new_obj_key = choose_word(nouns)
    while new_obj_key == sentence_keys[1]:
      new_obj_key = choose_word(nouns)
    sentence_keys[1] = new_obj_key

  return translate_sentence([sentence, sentence_keys, sentence_conj])


def mistranslate_switcheroo(data):
  sentence = data[0]
  sentence_keys = data[1]
  sentence_conj = data[2]

  if len(sentence_keys) == 3:
    sentence_keys[0], sentence_keys[2] = sentence_keys[2], sentence_keys[0]

  if len(sentence_keys) == 2:
    new_obj_key = choose_word(nouns)
    while new_obj_key == sentence_keys[1]:
      new_obj_key = choose_word(nouns)
    sentence_keys[1] = new_obj_key

  return translate_sentence([sentence, sentence_keys, sentence_conj])


def shuffle_sentence(sentence):
    words = sentence.split()
    random.shuffle(words)
    shuffled_sentence = ' '.join(words)
    return shuffled_sentence


# Generate sentences and translations
num_sentences = 100
sentences = []
translations = []
mistranslations = []
mistranslation_templates_3word = [mistranslate_sub_pl, mistranslate_obj_pl, mistranslate_wrong_subj, mistranslate_wrong_verb, mistranslate_wrong_obj, mistranslate_switcheroo]
mistranslation_templates_2word = [mistranslate_sub_pl, mistranslate_obj_pl, mistranslate_wrong_subj, mistranslate_wrong_verb, mistranslate_wrong_obj]

for _ in range(num_sentences):
    sentence_components = generate_sentence_components()
    sentence_data = construct_sentence(sentence_components)
    translation = translate_sentence(sentence_data)
    sentences.append(shuffle_sentence(sentence_data[0]))
    translations.append(translation)

    if len(sentence_data[1]) == 3:
      templates = mistranslation_templates_3word
    else:
      templates = mistranslation_templates_3word

    chosen_templates = random.sample(templates, 3)
    mistranslations.append([func(sentence_data) for func in chosen_templates])

df_mis = pd.DataFrame(mistranslations, columns=['Mistranslation A', 'Mistranslation B', 'Mistranslation C'])

# Create pandas dataframe
df = pd.DataFrame({'Latin Sentence': sentences, 'English Translation': translations})
df = df.join(df_mis)

df.to_csv('sentences.csv')