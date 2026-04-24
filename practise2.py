def self_root(n):
    
        for i in range(1, n+1):
            if i*i==n:
                print("The number is square root")
            else:
                res = n/i
                return res
                
self_root(4)