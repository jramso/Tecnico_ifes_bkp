
(input("escreva a matrícula: "))
nota1 = int(input("escreva a primeira nota: "))
nota2 = int(input("escreva a segunda nota: "))
nota3= int(input("escreva a terceira nota: "))
ME = int(input("escreva a média dos exercícios:"))
MA = ((nota1)+(nota2*2)+(nota3*3)+(ME*7))/13


print("Média de aproveitamento: ",MA)
print("Média dos exercícios: ",ME)
print("notas: ",nota1,",",nota2,",",nota3)
if  MA >= 90: 
    print ("conceito: A")
    print("Situação;Aprovado")

elif 75<= MA<90:
    print("conceito:B")
    print("Situação;Aprovado")
elif 60<= MA <75:
    print("conceito:C")
    print("Situação:Recuperação")
  
elif 50 <= MA <60:
    print("conceito:D")
  
    print("Recuperação")
elif MA < 50:
    print("conceito:E")
    print ("Reprovado")




