a=0
totalf=0
somage=0
mage=0
for x in range (0,5):

  nome=input("informe o nome:")
  sexo=input("informe o sexo M ou F:")
  age=int(input("inf. a idade:"))
  alt=float(input("inf. a altura em metros:"))
  if (sexo=="M") and (alt<1.80) and (age>30) :
   a= a+ 1

  if sexo=="F":
    totalf= totalf+1
    somage= somage+age

  if age>mage:
    mage==age

print("o total de pessoas do sexo Masculino que têm menos de 1.80m de altura e mais de 30 anos de idade é:",a)

print("A média de idade das pessoas do sexo feminino:",(somage/totalf))

print("o nome da pessoa de menor idade é:",mage)  