secret_word1 = "klíč"
secret_word2 = "zubař"
secret_word3 = "m"
guess = ""
guess_count = 0
guesses_wrong = 0
guesses_wrong2 = 0
guess_count1 = 0
guess_count2 = 0
guess_limit = 3
out_of_guesses = False
hádanka1 = "Leze leze po železe, nedá pokoj než tam vleze, co je to?"
hádanka2 = "Víte, kdo se živí cizími zuby? "
hádanka3 = "Co je v každé minutě jednou a v momentě dvakrát?"

while guess != secret_word1 and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(hádanka1 + " Odpověď: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses is True:
        print("Zadal/a jsi 3x špatnou odpověď, další otázka.")
        guesses_wrong += 1
out_of_guesses = False

guess_count = 0
while guess != secret_word2 and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(hádanka2 + " Odpověď: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses is True:
    print("Zadal/a jsi 3x špatnou odpověď, další otázka.")
    guesses_wrong += 1
out_of_guesses = False

guess_count = 0
while guess != secret_word3 and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(hádanka3 + " Odpověď: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses is True:
    print("Zadal/a jsi 3x špatnou odpověď, konec kvízu.")
    guesses_wrong += 1
out_of_guesses = False
guess_count = 0

print("Vyhodnocení:")
print("Měl jsi")
print(guesses_wrong)
if guesses_wrong is 0:
    print("Chyb. Gratuluji!")
if guesses_wrong is 1:
    print("Chybu.")
if guesses_wrong is 2:
    print("Chyby.")
if guesses_wrong is 3:
    print("Chyby. Vedl/a jsi si špatně. Zkus to znovu.")
    while guess != secret_word1 and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input(hádanka1 + " Odpověď: ")
            guess_count += 1
        else:
            out_of_guesses = True
    if out_of_guesses is True:
        print("Zadal/a jsi 3x špatnou odpověď, další otázka.")
        guesses_wrong2 += 1
    out_of_guesses = False

    guess_count = 0
    while guess != secret_word2 and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input(hádanka2 + " Odpověď: ")
            guess_count += 1
        else:
            out_of_guesses = True
    if out_of_guesses is True:
        print("Zadal/a jsi 3x špatnou odpověď, další otázka.")
        guesses_wrong2 += 1
    out_of_guesses = False

    guess_count = 0
    while guess != secret_word3 and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input(hádanka3 + " Odpověď: ")
            guess_count += 1
        else:
            out_of_guesses = True
    if out_of_guesses is True:
        print("Zadal/a jsi 3x špatnou odpověď, konec kvízu.")
        guesses_wrong2 += 1
    out_of_guesses = False
    print("Vyhodnocení:")
    print("Měl jsi")
    print(guesses_wrong)
    if guesses_wrong is 0:
        print("Chyb. Gratuluji!")
    if guesses_wrong is 1:
        print("Chybu.")
    if guesses_wrong is 2:
        print("Chyby.")
    if guesses_wrong is 3:
        print("Chyby. Zase. Jseš marnej")

input("")