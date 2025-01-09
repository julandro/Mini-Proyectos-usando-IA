from transformers import pipeline
# Use a pipeline as a high-level helper

pipe = pipeline("text-classification",
                model="nlptown/bert-base-multilingual-uncased-sentiment")

print('')
print('-'*25)
print('Clasificacion de Texto')
print('')
result = pipe(input('Escriba la frase a Analizar: '))

stars = int(result[0]['label'].replace(' stars', '').replace(' star', ''))

match stars:
    case 1:
        print("La frase es Bastante Negativa😡")
    case 2:
        print('La frase es Negativa😠')
    case 3:
        print('La frase es Neutra😐')
    case 4:
        print('La frase ess Positiva😊')
    case 5:
        print('La frase es Bastante Positiva😁')
    case _:
        print('...')
