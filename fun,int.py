def fun():
    a=["a","i","l","s"]
    b=a[0]
    a[0]=a[2]
    a[2]=a[3]
    a[3]=b
    print(a)
fun()
