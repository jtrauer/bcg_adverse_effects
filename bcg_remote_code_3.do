edit
# Paste in data from spreadsheet including variable names this time

lab def cat 	///
	1 "All neonatal and young children"	///
	2 "Paediatric, short follow-up"	///
	3 "Paediatric, high-burden, longer follow-up"	///
	4 "Paediatric/adolescent, declining burden, longer follow-up"	///
	5 "Adult, short follow-up"	///
	6 "Adult, declining burden, longer follow-up"	///
	7 "Adult, high-burden, longer follow-up"
	
lab val category cat

metan mypointestimate mylowerci myupperci,	///
	nooverall label(namevar=myname) random	///
	xlab(0, 0.5, 1.0, 1.5, 2.0) nulloff force	///
	favours(Favours BCG#Favours control) nowarning	///
	by(category)
