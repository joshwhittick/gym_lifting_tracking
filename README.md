# gym_lifting_tracking

developing a python program for tracking lifts in the gym and also some analysis of the resulting lifting data

currently teaching myself python so apologies for the uncode-like code

note on python programs included:

input_log.py

	when run asks for a list of exercises done on a specific date as an input then loops over those exercises to gather the sets, reps and load before writing that into lifting_log.txt
	note: use the EXACT same name for the exercise each time inputing into log e.g. bench press is always "BENCH"

interrogate.py 

	asks for a specific exercise and can then print all the days on which that exercise was carried out and the associated data

output_totals.py

	outputs the total amount of weight lifted for each exercise

write_log_to_xlsx.py
	
	write the lifting log to excel in a much more accessible and useful format than a text file obviously
	overwrites the same document each time it is ran as it starts from the (0, 0) of excel 


Dependencies:
	xlsxwriter (for write_log_to_xlsx.py)