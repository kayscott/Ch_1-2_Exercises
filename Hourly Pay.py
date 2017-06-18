hours = raw_input('Enter Hours') 
rate = raw_input('Enter Rate') 
hours1 = int(hours)
type(hours)
rate1 = float(rate)
type(rate1) 
wpay = rate1 * hours1
print wpay 


#solving to find yearly salary 
ypay = wpay * 35
print ypay - (wpay * 2) 