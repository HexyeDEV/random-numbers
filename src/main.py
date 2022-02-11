import time

class RandomNumber:
  
  def randn(n1: int, n2: int):
    n = random.randint(0, 9999)
    random.seed(n)
    n = random.randint(0, 999999)
    n = random.randint(0, n)
    random.seed(n)
    n = random.randint(0, n + 999999 + random.randint(0, 199) + time.time()
    random.seed(n)
    return random.randint(n1, n2)
