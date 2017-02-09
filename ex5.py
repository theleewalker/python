# ex5.py

name = 'Lee M. Walker'
age = 32 # not a lie
height = 70.0 # inches
weight = 180.0 # lbs
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %r centimeters tall." % (height * 2.54)
print "He's %d pounds heavy." % weight
print "He's %r kilograms heavy." % (weight * 0.453592)
print "Actually that's not too heavy."
print"He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight) 