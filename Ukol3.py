test_list = [1, 4, 6, 7, 2]

print ("Original list : " + str(test_list))

test_list = test_list[3:] + test_list[:3]


print ("List after left rotate : " + str(test_list))

test_list = test_list[-3:] + test_list[:-3]

print ("List after right rotate (back to original) : "
										+ str(test_list))
#bylo by dobre, kdybych mohl zadat o kolik 
#chci provest rotaci