def aten(n):
  if n==1 :
    return n
  return aten(n-1)+n
