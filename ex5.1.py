name = 'Marja N. Mullings'
age = 29.25# not a lie
height = 68.00 # inches
weight = 145.00 # lbs
eyes = 'brown'
teeth = 'white'
hair = 'black with a warm red henna glow'
hair_structure = 'tightly coiled'
favorite_craft = 'knitting' # because knitting is super cool
# %r means to print everything after the variable assignment of '='
height_in_centimeters  =(height*2.54) # There are 10 centimeters in 4 inches.  I know this from knitting gauge
	#swatches.
height_in_meters = height_in_centimeters/100
weight_in_kg = weight * (1/2.2000) # There are 2.2 lbs in 1 kg
body_mass_index = weight_in_kg/(height_in_meters)**2
water_weight =  weight + 10 # a weight gain of 10 lbs
new_body_mass_index = 703*water_weight/(height)**2 # this is the BMI formula that uses imperial values


print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "This %d  height in inches converts to %d in centimeters and %g in meters." % (height,height_in_centimeters, height_in_meters) 
print "She's %d pounds heavy." % weight
print "For most of the world, her weight would be recorded as %g kg." %(weight_in_kg)
print "Actually that's not too heavy."
print "In fact, this corresponds to a BMI of %g, which falls within the healthy range of 18.5-25." % body_mass_index
print "Marja really despises the BMI, because if she gained %g pounds of water weight during PMS, the BMI would change to %g." % (water_weight, new_body_mass_index)
print "She's got %s eyes and hair that is %s." % (eyes, hair)
print "Her teeth are usually %s, because she brushes after tea consumption." % teeth
print "Here favorite craft is %s." %favorite_craft
print  "Her teeth are usually %r, because she brushes after tea consumption." % teeth
print "She's got %s eyes and %r hair that is %s." % (eyes, hair_structure, hair)
#this line is trick, try to get it exactly right
print "If I add %g, %g, and % g, I get %g." % (
	age, height, weight, age + height + weight) 
	