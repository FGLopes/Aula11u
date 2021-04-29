import random
import json
import datetime

jogador = input("Inserir Nome: ")

numero_secreto = random.randint(1, 10)
tentativas = 0
tentativas_erradas = []

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

new_score_list = sorted(score_list, key=lambda k: k['tentativas'])[:3]

for score_dict in new_score_list:
    score_text = "O jogador {0} teve {1} tentativas no {2}. O numero secreto era {3}. Tentativas erradas: {4}".format(score_dict.get("jogador"),
                                                                                                                     str(score_dict.get("tentativas")),
                                                                                                                     score_dict.get("data"),
                                                                                                                     score_dict.get("numero_secreto"),
                                                                                                                     score_dict.get("tentativas_erradas"))
    print(score_text)

jogo = True
while jogo:
    guess = int(input("Adivinha o numero secreto (entre 1 e 10): "))
    tentativas += 1

    if guess == numero_secreto:
        score_list.append({"tentativas": tentativas, "data": str(datetime.datetime.now()), "jogador": jogador,
                           "numero_secreto": numero_secreto, "tentativas_erradas": tentativas_erradas})

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Parabéns! É o número " + str(numero_secreto))
        print("Tentativas: " + str(tentativas))
        jogo = False

    elif guess > numero_secreto:
        print("Demasiado alto")
    elif guess < numero_secreto:
        print("Demasiado baixo")