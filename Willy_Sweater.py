print "How much money does it cost to make a Willy Sweater in my size?"

print "size made: M"
skeins_needed_of_main_color= 6
cost_per_skein_of_main_color = 8.00
total_cost_for_main_color = skeins_needed_of_main_color * cost_per_skein_of_main_color
print "This is how much I will spend on the main color: $" , total_cost_for_main_color

total_cost_for_snout_color_brown = 0.00

print "This is how much I will spend on the snout color: $" , total_cost_for_snout_color_brown

skeins_for_ear_color_white = 1
cost_per_skein_of_ear_color = 8.00
total_cost_for_ear_color = skeins_for_ear_color_white * cost_per_skein_of_ear_color
print "This is how much I on the ear color: $", total_cost_for_ear_color

total_cost_for_yarn = total_cost_for_main_color + total_cost_for_snout_color_brown +  total_cost_for_ear_color

print "This is the total cost of the yarn project: $", total_cost_for_yarn