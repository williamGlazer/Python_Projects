
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from scipy import stats




# Heights ~ N(70,4)
mean = 70
std  =4
heights = stats.norm(mean,std)

# p(X < 70)
print(heights.cdf(70))

# p(66 < X < 74) (~68% empirical rule)
print(heights.cdf(mean+std) - heights.cdf(mean-std))

# p(62 < X < 78) (~95% empirical rule)
print(heights.cdf(mean+std*2) - heights.cdf(mean-std*2))

# p(58 < X < 82) (~99.7% empirical rule)
print(heights.cdf(mean+std*3) - heights.cdf(mean-std*3))





# TCL large enough >= 30 ou 40
# Parle pas ditrib. pop mais distrib. moyenne echant.
# Base hyp. test.



# Hypothesis testing -> always 2
#   Null H0 : Assume true
#   Altr H1 : Claim to answer
# 
# Preuve par Absurde
# Thus 2 outcomes   -> Reject null and accept true
#                   -> Cannot reject null
# 
# Std Error (SE) std/sqrt(n)
# z = ( x-mu ) / SE  Voit quel pt loin mu
# Avec z on trouve quelle probab. SE soit ca
# Cette proba. est p-value
# Donc seuil alpha (.05) doit etre plus 
#   petit que p-value pour test passe
#
# 1/2 Tails est soit mu >/</!= qu<on suppose


#Nouvelle methode enseignement a moyenne 72
#On sait test ~ N(70,4)
#Methode est-elle + sharp? 

STANDARD_NORM = stats.norm(0,1)

# Hypothesis
# H_0: mu = 70
# H_1: mu > 70
alpha = 0.05

mean = 70
std  =  4
n    = 40
x    = 72

z = (x - mean) / (std / math.sqrt(n))
p_value = STANDARD_NORM.sf(z)

if p_value < alpha:
    print('Methode plus efficace')
else:
    print('On ne peut conclure')
    
    
# H_0: mu  = 70
# H_1: mu != 70
p_value = 2 * STANDARD_NORM.sf(z)
if p_value < alpha:
    print('Methode pas 70 moyenne')
else:
    print('On ne peut conclure')
    
    
    
    
    
    
    
# Tests sur 2 echant. (ex. placebo & medic)
# on fait mu1 - mu2 =? 0 (medic inutile)
# H_0: mu1 - mu2 =  0
# H_1: mu1 - mu2 != 0
#
# Trouver z et p-value associe
# Accept ou reject H selon alpha
#
# Conditions:
#   Echant. Indep.
#   Pop. Normales et connait std
#   Echant. < 10% Pop. Tot.


# Hypothesis
# H_0: mu_1 - mu_2 =  0
# H_1: mu_1 - mu_2 != 0
alpha = 0.05

n_control = 1000
x_control = 185
s_control = 39

n_exp = 900
x_exp = 180
s_exp = 50

z = (x_control - x_exp) / math.sqrt( s_control** 2 / n_control + s_exp** 2 / n_exp )
p_value = 2 * STANDARD_NORM.sf(abs(z))

if p_value < alpha:
    print('Med plus efficace')
else:
    print('On ne peut conclure')



# T-Test used when dunno std
# Sharp qd petit echant. sinon N Idem
# Parametrise par degre lib (n-1)
#   donc courbe change selon qte echant.
# Variance = dl/(dl-2)
# Au lieu z puis comp. alpha
#   on a t vs t.alpha