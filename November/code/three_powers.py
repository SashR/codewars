import math
def three_powers(n):
    pow2 = lambda a: math.log(a, 2)%1 == 0
    lst = [x for x in list(range(1,n)) if pow2(x)]
    
    print(n, lst)
    
    if n<3: return False
    for i in range(len(lst)):
        lst2 = [x for x in list(range(1,n-lst[i])) if pow2(x)]
        for j in range(i, len(lst2)):
            try:
                # print("i: {}, j: {}, k: {}".format(lst[i], lst[j], n- lst[i] - lst[j]))
                if n- lst[i] - lst2[j] < 1: break
                # if pow2(n-lst[i]-lst[j]): return True
                if (n-lst[i]-lst2[j]) in lst: return True 
            except Exception:
                print("ERROR i: {}, j: {}, k: {}".format(i, j, n- lst[i] - lst2[j]))
    return False

print(three_powers(1))
print(three_powers(2))
print(three_powers(3))
print(three_powers(5))
print(three_powers(9))
print(three_powers(15))
print(three_powers(276))
print(three_powers(354))
print(three_powers(2**25 - 1))