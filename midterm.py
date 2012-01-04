# Generic Stuff

def ls(count, N, cats, k):
    """
    Laplace Smoothing
    count is the occurence of the variable
    N is the total number of elements
    cats is the number of categories
    k is the smoothing term
    """
    return (float(count)+float(k))/(float(N)+(float(k)*float(cats)))

# midterm-5
# 
# P = {}
# 
# P['P1'] = 0.5
# P['H|P1'] = 0.5
# P['T|P1'] = 0.5
# 
# P['P2'] = 0.5
# P['H|P2'] = 1.0
# P['T|P2'] = 0.0
# 
# P['H'] = P['H|P1']*P['P1'] + P['H|P2']*P['P2']
# 
# P['P2|H'] = P['H|P2'] * P['P2'] / P['H']
# 
# print "P['P2|H'] =", P['P2|H']
# 
# P['H|H'] = P['H']
# P['H|P2,H'] = P['H|P2']
# 
# P['P2|H,H'] = P['H|P2,H'] * P['P2|H'] / P['H|H']
# 
# print "P['P2|H,H'] =", P['P2|H,H']


# midterm-7

# P = {}
# 
# P['A'] = 0.5
# P['~A'] = 1.0 - P['A']
# P['B|A'] = 0.2
# P['B|~A'] = 0.2
# P['C|A'] = 0.8
# P['C|~A'] = 0.4
# 
# P['B|C,A'] = P['B|A']
# 
# P['C'] = P['C|A']*P['A'] + P['C|~A']*P['~A']
# 
# P['A|C'] = P['C|A']*P['A']/P['C']
# 
# P['B|C,~A'] = P['B|~A']
# 
# P['~A|C'] = P['C|~A']*P['~A']/P['C']
# 
# P['B|C'] = P['B|C,A']*P['A|C'] + P['B|C,~A']*P['~A|C']
# 
# print "P['B|C'] =", P['B|C']
# 
# P['C|B,A'] = P['C|A']
# 
# P['B'] = P['B|A']*P['A'] + P['B|~A']*P['~A']
# 
# P['A|B'] = P['B|A']*P['A']/P['B']
# 
# P['C|B,~A'] = P['C|~A']
# 
# P['~A|B'] = P['B|~A']*P['~A']/P['B']
# 
# P['C|B'] = P['C|B,A']*P['A|B'] + P['C|B,~A']*P['~A|B']
# 
# print "P['C|B'] =", P['C|B']



# mineterm-8

# P = {}
# k = 1.0
# 
# 
# P['OLD'] = ls(3,5,2,k)
# P['NEW'] = ls(2,5,2,k)
# 
# print "P['OLD'] =", P['OLD']
# print "P['NEW'] =", P['NEW']
# print "P['NEW'] + P['OLD'] =", P['NEW'] + P['OLD']
# 
# num_words = 6
# 
# P['"TOP"|OLD'] = ls(2,6,num_words,k)
# 
# print "P['\"TOP\"|OLD'] =", P['"TOP"|OLD']
# 
# P['"TOP"|NEW'] = ls(1,4,num_words,k)
# 
# P['"TOP"'] = P['"TOP"|OLD']*P['OLD'] + P['"TOP"|NEW']*P['NEW']
# 
# P['OLD|"TOP"'] = P['"TOP"|OLD']*P['OLD']/P['"TOP"']
# 
# print "P['OLD|\"TOP\"'] =", P['OLD|"TOP"']


# midterm-10

# def w_0(xs,ys,M,w1):
#     """docstring for w_0"""
#     ans = sum(ys)/float(M)
#     ans -= (w1/float(M))*sum(xs)
#     return ans
# 
# def w_1(xs,ys,M):
#     """docstring for w_1"""
#     num = float(M)*sum([x*y for x,y in zip(xs,ys)])
#     num -= sum(xs)*sum(ys)
#     den = float(M)*sum([x**2 for x in xs])
#     den -= sum(xs)**2
#     return float(num)/float(den)
# 
# # Test
# # X = [0,1,2,3,4]
# # Y = [3,6,7,8,11]
# # M = len(X)
# 
# X = [1,3,4,5,9]
# Y = [2,5.2,6.8,8.4,14.8]
# M = len(X)
# 
# w1 = w_1(X,Y,M)
# w0 = w_0(X,Y,M,w1)
# 
# print "w0 =", w0, "w1 =", w1


# midterm-15

# k = 1.0
# P = {}
# 
# P['A_0'] = ls(1,1,2,k)
# 
# print "P['A_0'] =", P['A_0']
# 
# P['A|A'] = ls(3,4,2,k)
# 
# print "P['A|A'] =", P['A|A']
# 
# P['A|B'] = ls(0,0,2,k)
# 
# print "P['A|B'] =", P['A|B']










