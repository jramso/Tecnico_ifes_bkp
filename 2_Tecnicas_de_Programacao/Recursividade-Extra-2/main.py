def contalg(num):
  if num<10:
    return 1
  else:
    return contalg(num/10) +1
    
  