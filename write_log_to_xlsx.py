import xlsxwriter
workbook = xlsxwriter.Workbook('log.xlsx')
worksheet = workbook.add_worksheet('sheet1')

row = 0
col = 0

worksheet.write(row, col, "Date")
worksheet.write(row, col+1, "Exercise")
worksheet.write(row, col+2, "Sets")
worksheet.write(row, col+3, "Reps")
worksheet.write(row, col+4, "Load")
worksheet.write(row, col+5, "Total Reps")
worksheet.write(row, col+6, "Total Load")

with open("lifting_log.txt") as f:
        for line in f:
            parts = line.split()
            exercise = parts[0]
            sets = int(parts[7])
            reps = int(parts[9])
            load = float(parts[4])
            date = parts[2]
            total_reps = int(parts[12])
            total_load = float(parts[15])
            
            worksheet.write(row+1, col, date)
            worksheet.write(row+1, col +1, exercise)
            worksheet.write(row+1, col +2, sets)
            worksheet.write(row+1, col +3, reps)
            worksheet.write(row+1, col +4, load)
            worksheet.write(row+1, col +5, total_reps)
            worksheet.write(row+1, col +6, total_load)
            
            row = row + 1
            
workbook.close()
