# Homework 2.2

# Given Probabilities
P = {'A': 0.5, '~A': 0.5,
     'X1|A': 0.2, 'X1|~A': 0.6,
     'X2|A': 0.2, 'X2|~A': 0.6,
     'X3|A': 0.2, 'X3|~A': 0.6}

# Complementary Probability
P['~X3|A'] = 1.0 - P['X3|A']
P['~X3|~A'] = 1.0 - P['X3|~A']

# Total Probability
P['~X3'] = P['~X3|A']*P['A'] + P['~X3|~A']*P['~A']

# Baye's Theorm
P['A|~X3'] = (P['~X3|A'] * P['A']) / P['~X3']

# Conditional Independance
P['X2|A,~X3'] = P['X2|A']

# Total Probability
P['X2'] = P['X2|A']*P['A'] + P['X2|~A']*P['~A']

# Complementary Probability
P['X2|~A,~X3'] = 1.0 - P['X2|A,~X3']
P['~A|~X3'] = 1.0 - P['A|~X3']

# Conditional Dependence
P['X2|~X3'] = P['X2|A,~X3']*P['A|~X3'] + P['X2|~A,~X3']*P['~A|~X3']

# Baye's Theorm
P['A|X2,~X3'] = (P['X2|A,~X3'] * P['A|~X3']) / P['X2|~X3']

# Conditional Independance
P['X1|A,X2,~X3'] = P['X1|A']

# Total Probability
P['X1'] = P['X1|A']*P['A'] + P['X1|~A']*P['~A']

# Independance Variable not Given A
P['X1|X2,~X3'] = P['X1']

# Baye's Theorm
P['A|X1,X2,~X3'] = (P['X1|A,X2,~X3'] * P['A|X2,~X3']) / P['X1|X2,~X3']

print "P['A|X1,X2,~X3'] =", P['A|X1,X2,~X3']

# Homework 2.3

# Complementary Probability
P['X3'] = 1.0 - P['~X3']

# Conditional Independance
P['X3|A,X1'] = P['X3|A']
P['X3|~A,X1'] = P['X3|~A']

# Independent Variable not Given A
P['X3|X1'] = P['X3|A,X1']*P['A'] + P['X3|~A,X1']*P['~A']

print "P['X3|X1'] =", P['X3|X1']


