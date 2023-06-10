a = 10

def fun2():
    #a= 30
    global a
    print(a)

def fun():
    # global a  전역변수를 사용하겠다는 의미
    a = 20
    print(a)
    fun2()

fun()

print(a)

