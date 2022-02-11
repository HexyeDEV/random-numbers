import time
import random
from hashlib import sha256

class RandomNumber:
  
  def randn(n1: int, n2: int):
    n = random.randint(0, 9999)
    random.seed(n)
    n = random.randint(0, 999999)
    n = random.randint(0, n)
    random.seed(n)
    n = random.randint(0, n + 999999 + random.randint(0, 199 + int(time.time()) + 104))
    random.seed(a=n+time.time()+sha256(time.time + 104208 - n), version=2)
    return random.randint(n1, n2)
