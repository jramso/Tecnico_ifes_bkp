ano= int(input("informe o ano:"))
N= ano+76
M= ano-76

print ('ano atual:',ano)
if ano % 76 == 10 :
  print ('o cometa já passou esse ano mas, \n a próxima passagem do cometa é:',N)
  print('e a ultima vez que ele passou antes do ano atual foi',M)
else:
  for i in range (ano,N):
    if i % 76 == 10:
      print ("a próxima passagem do cometa é:",i)
  for j in range (M,ano):
    if j% 76 ==10:
      print (" a ultima vez que o cometa passou foi:",j) 

