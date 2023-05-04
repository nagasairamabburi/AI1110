p_E=0.25 #Probability of event E
p_notE=1-p_E #Probability of not E
total_p= p_E + p_notE # Total probability
print(total_p)

p_impossible=0 #Probability iof an impossible event
print(p_impossible) 

p_certain = 1 #Probability of a certain event
print(p_certain) 
 
 #let there be three elementary events of an experiment 
p_event1=0.5
p_event2=0.34
p_event3=0.16
p_total=p_event1+p_event2+p_event3
print(p_total)
 
p_event=0.7 #Probability of an event
if p_event >=0 and p_event <=1:
	print("Valid Probability")
else:
	print("Invalid probability")
