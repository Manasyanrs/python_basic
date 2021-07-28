
# TODO чтобы не использовать символ \
# TODO заключите весь текст в """ """
text = "vujgvmCfb tj ufscfu ouib z/vhm " \
       "jdjuFyqm jt fscfuu uibo jdju/jnqm " \
       "fTjnqm tj scfuuf ibou fy/dpnqm " \
       "yDpnqmf jt cfuufs boui dbufe/dpnqmj " \
       "uGmb tj fuufsc ouib oftufe/ " \
       "bstfTq jt uufscf uibo otf/ef " \
       "uzSfbebcjmj vout/dp " \
       "djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf " \
       "ipvhiBmu zqsbdujdbmju fbutc uz/qvsj " \
       "Fsspst tipvme wfsof qbtt foumz/tjm " \
       "omfttV mjdjumzfyq odfe/tjmf " \
       "Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv " \
       "Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ " \
       "Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( " \
       "i/Evud " \
       "xOp tj scfuuf ibou /ofwfs " \
       "uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op " \
       "gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb " \
       "Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ " \
       "bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf'uip".lower().split()

lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&*()_-+=,.:/'"
results = ""
sentence = ""
my_step = -3
for words in text:
    step = my_step
    count_letters_in_word = 0
    step = -(abs(step) % len(words))
    for _ in words:
        letter = words[step]
        step += 1
        count_letters_in_word += 1
        if letter in symbols:
            sentence += letter

        else:
            index = lower_alphabet.index(letter)
            sentence += lower_alphabet[index - 1]

        if count_letters_in_word == len(words):
            sentence += " "
            if "/" in words:
                my_step -= 1
                results += "\n" + sentence.capitalize()
                sentence = ""

print(results)

# TODO результат должен быть таким, есть нераскодированные символы

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

