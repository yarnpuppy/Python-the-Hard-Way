# An attempt to write a pattern for a 2x2 ribbed scarf. 

cast_on_stitches =raw_input("> ")

# This code block seeks to determine if the  number of cast on stitches is even.  They need to be for 2x2 ribbing.

if int(cast_on_stitches)%2 == 0:
	print "Cast on %s stitches." % cast_on_stitches
else:
	#add 1 stitch to cast_on_stitches to make the stitch count even
	 cast_on_stitches = int(cast_on_stitches) + 1
	 print "Cast on %s stitches." % cast_on_stitches