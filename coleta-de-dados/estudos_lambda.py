import pandas as pd

#funcao para calcular o cubo de um num, ** é usado para elevar um número
def eleva_cubo(x):
    return x ** 3

#usando lambda, não tem sentido usar dessa forma, apenas para estudos(academico)
eleva_cubo_lambda = lambda x: x ** 3

print(eleva_cubo(2))
print(eleva_cubo_lambda(2))

df = pd.DataFrame({'numeros': [1,2,3,4,5,10]})

df['cubo_funcao'] = df['numeros'].apply(eleva_cubo)
df['cubo_fun_lambda'] = df['numeros'].apply(lambda x: x**3) #apply serve para aplicar uma função, um map, lambda, etc
print(df)