from sys import argv

script, first, second, third = argv


print "The script is called:", script
print "Your first variable is:", first
print "Your second varible is:", second
print "Your third variable is:", third

mookles = raw_input ("Fang color? ")
punkles = raw_input ("Number of dew claws? ")
print "These animals have %r fangs and %r dew claws." % (
	mookles, punkles)