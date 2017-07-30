'''
Created on Jul 29, 2017

@author: manan
'''
import csv, time


def condition_change(string_value, acc_time):
    if string_value == "Dusk/Dawn" or string_value == "Dark Street lights on" or string_value == "Dark Street lights unknown":
        return 0.5
    elif string_value == "Day":
        return 1
    elif string_value == "Dark Street lights off" or "Dark No street lights":
        return 0
    elif string_value == "Unk.": 
        accident_time = float(acc_time)
        if accident_time > 19.0: 
            return 0
        elif accident_time > 0 and accident_time < 7.00:
            return 0
        else: 
            return 1

start = time.time()

#Read the tweet dump and then output a new file 
r = open('file.csv',encoding='utf-8')  #encode as utf-8 since pyhton doesn't recognize emoji
w = open('output.csv','w',encoding='utf-8')

#Read the dump file and write the headers in the new file
fieldnames = ['Latitude', 'Longitude', 'Accident_Date', 'Accident_Time', 'Light_Condition', 'Speed_Zone', 'Crash_OR_NOT']
reader = csv.reader(r)
writer = csv.DictWriter(w, fieldnames=fieldnames)
writer.writeheader()

#Create a table for all the data to be copied
table = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
#find the number of columns
col_num = len(table)

#Read every row in the file
for row in reader: 
    #print(row)
    for i,j in zip(row,range(col_num)):
        #for every row item add it to a different column
        table[j].append(i)
    #print(table)
    
#close the files    
r.close()

count = 1
till = len(table[4])
#for every text in the tweet column
try:
    for i in range(till):
        #print(sentence)
        accident_speed = [int(s) for s in table[17][count].split() if s.isdigit()]
        accident_time = float(table[7][count][:5])
#         print(accident_time)
        if accident_speed:
    #         print(accident_speed[0])
            writer.writerow({'Latitude': table[21][count], 'Longitude': table[20][count], 'Accident_Date': table[6][count], 'Accident_Time': round((accident_time*60)/(24*60),4), 'Light_Condition': condition_change(table[13][count], table[12][count]), 'Speed_Zone': round(int(accident_speed[0])/120, 4), 'Crash_OR_NOT': 1})
        count += 1
except ValueError:
    print(table[7][count][:5])
except IndexError:
    print(accident_speed)
    
finish = time.time() - start
print(finish)