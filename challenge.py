class max_iter:
    def __init__(self):
        self._max_cycle_length = 0
        self._cycle_length = 0
    
    def _algo(self, n): #Returns max iteration for each value.
        self._cycle_length += 1
        if n == 1:
            final_cycle_length = self._cycle_length
            self._cycle_length = 0
            return final_cycle_length
        if n%2 == 0:
            return self._algo(n/2)
        else:
            return self._algo((n*3)+1)

    def _find_max_cycle_length(self, a,b):
        assert a> 0 and b < 1000000
        for i in range(a,b+1):
            c = self._algo(i)
            if c > self._max_cycle_length:
                self._max_cycle_length = c
        max_cycle_length = self._max_cycle_length
        self._max_cycle_length = 0
        return f"{a} {b} {max_cycle_length}"
    
    def run(self,a,b):
        return self._find_max_cycle_length(a,b)
        


if __name__ == "__main__":
    a = max_iter()
    d = [(1,10),(100,200),(201,210),(900,1000),]
    for i in d:
        print(a.run(*i))