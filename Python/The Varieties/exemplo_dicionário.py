dic = {
        "integrantes":  {
            "beatles": ['ringo',
                        'john',
                        'paul',
                        'george',
                        'pete'],
            "the_fellowship": ['gandolfo',
                               'aragorn',
                               'gimli',
                               'legolas',
                               'boromir',
                               'frodo',
                               'sam',
                               'hobbit 3',
                               'hobbit 4'],
            "The_Vindicators": ('Vance Maximus',
                                'Alan Rails',
                                'Crocubot',
                                'Million Ants',
                                'Morty Smith',
                                'Rick Sanchez',
                                'Lady Katana',
                                'Calypso',
                                'Diabo Verde'),
            "Alunos_distraidos_nesse_momento": [],
            },
        "jogos": [
            {"nome": "CS go", "empresa": "valve", "estilo": "FPS"},
            {"nome": "PLANESCAPE:torment", "empresa": "Bioware", "estilo": "Jogo mais bem escrito da historia"},
            {"nome": "The Witcher", "empresa": "CD Project Red", "estilo": "Open World RPG"},
            ],
        }
        
# Para cada um dos print's abaixo, teremos (True, False or Error).
1;  print(dic["jogos"][2]["nome"] == "The Witcher")                 # True
2;  print("CS go" == dic["jogos"][0])                               # False
3;  print("FPS" in dic["jogos"]["CS go"])                           # Error
4;  print("Rick Sanchez" in dic.integrantes.The_vindicators)        # Error
5;  print(dic["integrantes"]["beatles"][3] == "paul")               # False
6;  print("valve" in dic["jogos"]["CS go"])                         # Error
7;  print("empresa" in dic["jogos"]["CS go"])                       # Error
8;  print("legolas" in dic["integrantes"]["the_fellowship"])        # True
9;  print("merlin" in dic["integrantes"]["The_Vindicators"])        # False
10; print("Thor" in dic["filmes"]["Avengers"])                      # Error
11; print("Open World RPG" == dic["jogos"][1]["empresa"])           # False
12; print(dic["jogos"][0]["estilo"] == "FPS")                       # True
13; print(dic["jogos"]["Bioware"] == "PLANESCAPE:torment")          # Error
14; print("pete" in dic["integrantes"]["beatles"])                  # True
15; print(dic["integrantes"]["the_fellowship"][2] == "gimli")       # True
16; print("CD Project Red" in dic["jogos"][2])                      # False
17; print("empresa" in dic["jogos"][2])                             # True
18; print(dic[dic] + dic[dic[dic]])                                 # Error
