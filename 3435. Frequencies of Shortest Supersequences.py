class lazy_segtree():
    def update(self,k):self.d[k]=self.op(self.d[2*k],self.d[2*k+1])
    
    def all_apply(self,k,f):
        self.d[k]=self.mapping(f,self.d[k])
        if (k<self.size):self.lz[k]=self.composition(f,self.lz[k])
        
    def push(self,k):
        self.all_apply(2*k,self.lz[k])
        self.all_apply(2*k+1,self.lz[k])
        self.lz[k]=self.identity
        
    def __init__(self,V,OP,E,MAPPING,COMPOSITION,ID):
        self.n=len(V)
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for i in range(2*self.size)]
        self.lz=[ID for i in range(self.size)]
        self.e=E
        self.op=OP
        self.mapping=MAPPING
        self.composition=COMPOSITION
        self.identity=ID
        for i in range(self.n):self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):self.update(i)
        
    def set(self,p,x):
        p+=self.size
        for i in range(self.log,0,-1):self.push(p>>i)
        self.d[p]=x
        for i in range(1,self.log+1):self.update(p>>i)
        
    def get(self,p):
        p+=self.size
        for i in range(self.log,0,-1):self.push(p>>i)
        return self.d[p]
        
    def prod(self,l,r):
        if l==r:return self.e
        l+=self.size
        r+=self.size
        for i in range(self.log,0,-1):
            if (((l>>i)<<i)!=l):self.push(l>>i)
            if (((r>>i)<<i)!=r):self.push(r>>i)
        sml,smr=self.e,self.e
        while(l<r):
            if l&1:
                sml=self.op(sml,self.d[l])
                l+=1
            if r&1:
                r-=1
                smr=self.op(self.d[r],smr)
            l>>=1
            r>>=1
        return self.op(sml,smr)
        
    def all_prod(self):return self.d[1]
    
    def apply_point(self,p,f):
        assert 0<=p and p<self.n
        p+=self.size
        for i in range(self.log,0,-1):self.push(p>>i)
        self.d[p]=self.mapping(f,self.d[p])
        for i in range(1,self.log+1):self.update(p>>i)
        
    def apply(self,l,r,f):
        if l==r:return
        l+=self.size
        r+=self.size
        for i in range(self.log,0,-1):
            if (((l>>i)<<i)!=l):self.push(l>>i)
            if (((r>>i)<<i)!=r):self.push((r-1)>>i)
        l2,r2=l,r
        while(l<r):
            if (l&1):
                self.all_apply(l,f)
                l+=1
            if (r&1):
                r-=1
                self.all_apply(r,f)
            l>>=1
            r>>=1
        l,r=l2,r2
        for i in range(1,self.log+1):
            if (((l>>i)<<i)!=l):self.update(l>>i)
            if (((r>>i)<<i)!=r):self.update((r-1)>>i)
            
    def max_right(self,l,g):
        if l==self.n:return self.n
        l+=self.size
        for i in range(self.log,0,-1):self.push(l>>i)
        sm=self.e
        while(1):
            while(l%2==0):l>>=1
            if not(g(self.op(sm,self.d[l]))):
                while(l<self.size):
                    self.push(l)
                    l=(2*l)
                    if (g(self.op(sm,self.d[l]))):
                        sm=self.op(sm,self.d[l])
                        l+=1
                return l-self.size
            sm=self.op(sm,self.d[l])
            l+=1
            if (l&-l)==l:break
        return self.n
        
    def min_left(self,r,g):
        if r==0:return 0
        r+=self.size
        for i in range(self.log,0,-1):self.push((r-1)>>i)
        sm=self.e
        while(1):
            r-=1
            while(r>1 and (r%2)):r>>=1
            if not(g(self.op(self.d[r],sm))):
                while(r<self.size):
                    self.push(r)
                    r=(2*r+1)
                    if g(self.op(self.d[r],sm)):
                        sm=self.op(self.d[r],sm)
                        r-=1
                return r+1-self.size
            sm=self.op(self.d[r],sm)
            if (r&-r)==r:break
        return 0

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 7 or n == 61:
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    while d % 2 == 0:
        d //= 2
    bases = [2, 7, 61]
    for a in bases:
        t = d
        y = pow_mod(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = y * y % n
            t <<= 1
        if y != n - 1 and t % 2 == 0:
            return False
    return True

def primitive_root(m):
    if m == 2:
        return 1
    if m in (167772161, 469762049, 754974721, 998244353):
        return 3
    divs = [2]
    x = (m - 1) // 2
    while x % 2 == 0:
        x //= 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            divs.append(i)
            while x % i == 0:
                x //= i
        i += 2
    if x > 1:
        divs.append(x)

    g = 2
    while True:
        ok = True
        for d in divs:
            if pow_mod(g, (m - 1) // d, m) == 1:
                ok = False
                break
        if ok:
            return g
        g += 1
        
def zs(s):
    n = len(s)
    ret = [0] * n
    l = 1
    ll = 0
    r = 0
    while l < len(s):
        if l < r:
            ret[l] = min(ret[l-ll],r-l)
        
        i = ret[l]
        while l+i < len(s) and s[i] == s[l+i]:
            ret[l] +=1
            
            i +=1
        if ret[l] >0:
            if l+i-1 > r:
                ll = l
                r = max(r,l+i-1)        
        l+=1
    return ret

class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        lset = set()
        for w in words:
            if len(w) >= 1:
                lset.add(w[0])
            if len(w) >= 2:
                lset.add(w[1])
        letters = sorted(lset)
        k = len(letters)
        ind1 = {letter: i for i, letter in enumerate(letters)}
        adj = [[] for i in range(k)]
        ls1 = [False] * k
        for w in words:
            if len(w) < 2:
                continue
            a = ind1[w[0]]
            b = ind1[w[1]]
            if a == b:
                ls1[a] = True
            else:
                adj[a].append(b)
        disc = [-1] * k
        low = [0] * k
        sid = [-1] * k
        stks = [False] * k
        st = []
        dfst = 0
        scnt = 0

        def solve(u):
            nonlocal dfst, scnt
            disc[u] = low[u] = dfst
            dfst += 1
            st.append(u)
            stks[u] = True
            for v in adj[u]:
                if disc[v] == -1:
                    solve(v)
                    low[u] = min(low[u], low[v])
                elif stks[v]:
                    low[u] = min(low[u], disc[v])
            if low[u] == disc[u]:
                while True:
                    topv = st.pop()
                    stks[topv] = False
                    sid[topv] = scnt
                    if topv == u:
                        break
                scnt += 1

        for i in range(k):
            if disc[i] == -1:
                solve(i)

        mem1 = [[] for i in range(scnt)]
        for i in range(k):
            mem1[sid[i]].append(i)

        freq1 = [[] for i in range(scnt)]

        def solve2(cmpx, rept):
            act = set(x for x in cmpx if not rept[x])
            if not act:
                return True
            adjs = defaultdict(list)
            for x in cmpx:
                if not rept[x]:
                    for v in adj[x]:
                        if v in act:
                            adjs[x].append(v)
            vis = {x: 0 for x in act}

            def dfs(u):
                vis[u] = 1
                for v in adjs[u]:
                    if vis[v] == 0:
                        if dfs(v):
                            return True
                    elif vis[v] == 1:
                        return True
                vis[u] = 2
                return False

            for x in act:
                if vis[x] == 0:
                    if dfs(x):
                        return False
            return True

        for s in range(scnt):
            cmpx = mem1[s]
            sz = len(cmpx)
            if sz == 1:
                x = cmpx[0]
                if ls1[x]:
                    freq1[s].append([2])
                else:
                    freq1[s].append([1])
                continue
            fnx = [x for x in cmpx if ls1[x]]
            lcn = {x: i for i, x in enumerate(cmpx)}
            mskf = 0
            for x in fnx:
                mskf |= (1 << lcn[x])
            bcar = float('inf')
            gsubs = []
            for mask in range(1 << sz):
                if (mask & mskf) != mskf:
                    continue
                c = bin(mask).count('1')
                if c > bcar:
                    continue
                rept = [False] * k
                for i in range(sz):
                    if (mask & (1 << i)):
                        ltx = cmpx[i]
                        rept[ltx] = True
                if solve2(cmpx, rept):
                    if c < bcar:
                        bcar = c
                        gsubs = [rept.copy()]
                    elif c == bcar:
                        gsubs.append(rept.copy())
            for zx in gsubs:
                freqp = [1] * sz
                for i in range(sz):
                    if zx[cmpx[i]]:
                        freqp[i] = 2
                freq1[s].append(freqp)

        pres = []
        sfreqs = [0] * k

        def dfs2(s, curr):
            if s == scnt:
                pres.append(curr.copy())
                return
            for freqv in freq1[s]:
                ncurr = curr.copy()
                for i, ltx in enumerate(mem1[s]):
                    ncurr[ltx] = freqv[i]
                dfs2(s + 1, ncurr)

        dfs2(0, sfreqs)

        msums = float('inf')
        for fv in pres:
            s = sum(fv)
            if s < msums:
                msums = s
        minfreq = [fv for fv in pres if sum(fv) == msums]

        fst = set()
        for fv in minfreq:
            fre26 = [0] * 26
            for i, freq in enumerate(fv):
                letter = letters[i]
                fre26[ord(letter) - ord('a')] = freq
            fst.add(tuple(fre26))

        return [list(t) for t in fst]
