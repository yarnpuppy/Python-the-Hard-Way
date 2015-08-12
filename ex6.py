# d is some sort of variable. % allows you define the value
x = "There are %d types of people." % 10
# defines binary as a string binary
binary = "binary"
# defines do_not as the string "don't"
do_not = "don't"
# Compound variable description for s and s.  %(s,s), allows for consecutive variable substitution.
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
# r is defined as x, which should print I said: 'There are 10 types of people.'.
print "I said: %r." % x
# s is defined as y, which should print I also said: 'Those who know binary and those who don't.'.
print "I also said: '%s'. " % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
#prints This is the left side of...a string with a right side.
print w + e

m= "Marja is very "
a = "very cool"

print m + a