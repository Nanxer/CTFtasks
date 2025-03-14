## MoeCTF_2024_small_and_big

### description:

这个e看起来小小的，好可爱啊(❁´◡`❁)

### analysis:
e很小，n很大，说明很可能pow(m,e)==pow(m,e,n)，或者之间差的n可以爆破出来。

### exp:

```python
from gmpy2 import iroot
m=iroot(c,e)[0]
print(long_to_bytes(m))
```

### attach:

进一步可以进行coppersmith攻击
