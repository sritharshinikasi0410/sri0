def is_prime(5):
  if n<=1:
    return False
    for i in range(2,int(n**0.5)+1):
      if n % i==0:
        return False
        return True
        num=int(input("Enter a number:"))
        if is_prime(num):
          print("Prime")
        else:
          print("Not prime")
