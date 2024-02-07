def correct_sentence(sentence):
    copy_sentence = sentence
    if sentence[-1] != '.':
        sentence += '.'
        copy_sentence = sentence

    if sentence[0].islower():
        copy_sentence = sentence.capitalize()
    return copy_sentence


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
