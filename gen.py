class max_iter:
    def __init__(self):
        self.mi = 0
        self.change = 0
    
    def algo(self, n):
        self.change += 1
        if n == 1:
            final_num = self.change
            self.change = 0
            return final_num
        if n%2 == 0:
            return self.algo(n/2)
        else:
            return self.algo((n*3)+1)

    def does_all(self, a,b):
        assert a> 0 and b < 1000000
        for i in range(a,b+1):
            c = self.algo(i)
            if c > self.mi:
                self.mi = c
        res = self.mi
        self.mi = 0
        return f"{a} {b} {res}"
        


if __name__ == "__main__":
    a = max_iter()
    d = [(1,10),(100,200),(201,210),(900,1000),]
    for i in d:
        print(a.does_all(*i))