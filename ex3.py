# This line just prints out exactly what is between the ".
print "I will now count my chickens:"
# This line prints the word "Hens" and adds 25 + the result of 30 divided by (/) 6 which yield 30.  Order of operations!
print "Hens", 25 + 30 / 6.
# This line prints the word "Roosters" % is the Modulus operator and divides left hand operand by right hand operand
# and returns remainder.  Because PEMDAS order of operations, we first multiply 25*3 to get 75.  That result is then divided by
#4 to give 18 r 3.  Remainder 3 is the output.  Then we subtract 3 from 100 to get 97.
print "Roosters", 100 - 25 * 3 % 4.
# Just printing out a string.
print "Now I will count the eggs:"
# PEMDAS order of operations again...4 modulus 2 is the first operation which gives 0. 3 + 2 + 1 -5 + 0-1/4+6. .. 1-1/4 + 6 gives 6.75.  
print 3 + 2 + 1 - 5 + 4 % 2 - 1/4 + 6.
# This just prints a string.
print "Is it true that 3 + 2 < 5 - 7?"
# This prints the false, because 5 is not less than - 2.
print 3 + 2 < 5 -7.0
# This first prints a string and prints 5 as the result.  The use of the comma is interesting to me.
print "What is 3 + 2?", 3 + 2.
# This first prints a string and prints -2 as the result.  Again, the use of the comma is interesting to me.
print "What is 5 - 7?", 5 - 7.
# This first prints a string.
print "Oh, that's why it's False."
# This first prints a string.
print "How about some more."
# This first prints a string and then prints True, because 5 is greater than -2.
print "Is it greater?", 5 > -2
# This first prints a string and then prints True, because 5 is greater than or equal to -2.
print "Is it greater or equal?", 5 >= -2
# This first prints a string and then prints False, because 5 is NOT less than or equal to -2.
print "Is it less or equal?", 5 <= -2



