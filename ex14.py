from sys import argv

script, user_name, color = argv
prompt = '* '

print "Hi, %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)
print "What is your favorite %s?" % color
favorite_color = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "What is the %s of your home?" % color
house_color = raw_input(prompt)

print "What kind of computer do you have?" 
computer = raw_input(prompt)
print "What %s is it?" % color
computer_color = raw_input(prompt)

print """
Alright, so you said %r about liking me.
And your favorite color is %r.
You live in a %r.  Not sure where that is.
That home is %r in color.
And you have a %r computer.  
A lovely color %r surely is! Nice!
""" % (likes, favorite_color, lives, house_color, computer, computer_color)

print """
oououwoeru 
powueorpuper
"""
	