import fractions

# Example 3

print(0.1 + 0.2 == 0.3)   
print(fractions.Fraction(1, 10) + fractions.Fraction(2, 10) == fractions.Fraction(3, 10))   

f = fractions.Fraction(3, 4)
print(f.numerator)        
print(f.denominator)      
print(float(f))           
print(fractions.Fraction("0.25"))   