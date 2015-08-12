from sys import argv

script, filename = argv
prompt= '> '

txt = open(filename)

print "Here's your file %r:" % filename
print raw_input(prompt)