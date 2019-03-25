import csv

even_day_slots = 5
odd_day_slots = 3
no_of_lt = 10

even_day_morning = []
even_day_evening = []
odd_day_morning = []
odd_day_evening = []

for slot in range(even_day_slots):
    even_day_morning.append([0] * no_of_lt)
    even_day_evening.append([0] * no_of_lt)

for slot in range(odd_day_slots):
    odd_day_morning.append([0] * no_of_lt)
    odd_day_evening.append([0] * no_of_lt)

with open('data.csv') as data_csv:
    data = csv.reader(data_csv, delimiter=',')
    for index, subject in enumerate(data):
        if index > 0:
            alloted = False
            # For 4 Batch Class
            if int(subject[6]) > 400 and alloted == False:
                if alloted == False:
                    for slot in range(even_day_slots):
                        if even_day_morning[slot][0] == 0 and even_day_morning[slot][1] == 0 and even_day_evening[slot][0] == 0 and even_day_evening[slot][1] == 0:
                            if subject[5] == "I":
                                if slot == 3:
                                    break
                            even_day_morning[slot][0] = subject[1] + " - A1" + " | " + subject[4]
                            even_day_morning[slot][1] = subject[1] + " - A2" + " | " + subject[4]
                            even_day_evening[slot][0] = subject[1] + " - B1" + " | " + subject[4]
                            even_day_evening[slot][1] = subject[1] + " - B2" + " | " + subject[4]
                            alloted = True
                            break
                
                if alloted == False:
                    for slot in range(odd_day_slots):
                        if odd_day_morning[slot][8] == 0 and odd_day_morning[slot][9] == 0 and odd_day_evening[slot][8] == 0 and odd_day_evening[slot][9] == 0:
                            odd_day_morning[slot][8] = subject[1] + " - A1" + " | " + subject[4]
                            odd_day_morning[slot][9] = subject[1] + " - A2" + " | " + subject[4]
                            odd_day_evening[slot][8] = subject[1] + " - B1" + " | " + subject[4]
                            odd_day_evening[slot][9] = subject[1] + " - B2" + " | " + subject[4]
                            alloted = True
                            break
                
                if alloted == False:
                    for slot in range(odd_day_slots):
                        if odd_day_morning[slot][8] == 0 and odd_day_morning[slot][9] == 0 and odd_day_evening[slot][8] == 0 and odd_day_evening[slot][9] == 0:
                            odd_day_morning[slot][8] = subject[1] + " - A1" + " | " + subject[4]
                            odd_day_morning[slot][9] = subject[1] + " - A2" + " | " + subject[4]
                            odd_day_evening[slot][8] = subject[1] + " - B1" + " | " + subject[4]
                            odd_day_evening[slot][9] = subject[1] + " - B2" + " | " + subject[4]
                            alloted = True
                            break

            
            elif int(subject[6]) > 200 and alloted == False:
                if "CSE" in subject[3] and subject[5] == "II":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_morning[slot][0] == 0 and even_day_morning[slot][1] == 0:
                                even_day_morning[slot][0] = subject[1] + " - A1" + " | " + subject[4]
                                even_day_morning[slot][1] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_morning[slot][0] == 0 and odd_day_morning[slot][1] == 0:
                                odd_day_morning[slot][0] = subject[1] + " - A1" + " | " + subject[4]
                                odd_day_morning[slot][1] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break
                
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_morning[slot][8] == 0 and even_day_morning[slot][9] == 0:
                                even_day_morning[slot][8] = subject[1] + " - A1" + " | " + subject[4]
                                even_day_morning[slot][9] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_morning[slot][8] == 0 and odd_day_morning[slot][9] == 0:
                                odd_day_morning[slot][8] = subject[1] + " - A1" + " | " + subject[4]
                                odd_day_morning[slot][9] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break

                elif "ECE" in subject[3] and subject[5] == "II":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_evening[slot][0] == 0 and even_day_evening[slot][1] == 0:
                                even_day_evening[slot][0] = subject[1] + " - A1" + " | " + subject[4]
                                even_day_evening[slot][1] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_evening[slot][0] == 0 and odd_day_evening[slot][1] == 0:
                                odd_day_evening[slot][0] = subject[1] + " - A1" + " | " + subject[4]
                                odd_day_evening[slot][1] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break
                
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_evening[slot][8] == 0 and even_day_evening[slot][9] == 0:
                                even_day_evening[slot][8] = subject[1] + " - A1" + " | " + subject[4]
                                even_day_evening[slot][9] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_evening[slot][8] == 0 and odd_day_evening[slot][9] == 0:
                                odd_day_evening[slot][8] = subject[1] + " - A1" + " | " + subject[4]
                                odd_day_evening[slot][9] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break

                elif "ECE" in subject[3] and subject[5] == "III":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_morning[slot][0] == 0 and even_day_morning[slot][1] == 0:
                                even_day_morning[slot][0] = subject[1] + " - A1" + " | " + subject[4]
                                even_day_morning[slot][1] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_morning[slot][0] == 0 and odd_day_morning[slot][1] == 0:
                                odd_day_morning[slot][0] = subject[1] + " - A1" + " | " + subject[4]
                                odd_day_morning[slot][1] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break
                
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_morning[slot][8] == 0 and even_day_morning[slot][9] == 0:
                                even_day_morning[slot][8] = subject[1] + " - A1" + " | " + subject[4]
                                even_day_morning[slot][9] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_morning[slot][8] == 0 and odd_day_morning[slot][9] == 0:
                                odd_day_morning[slot][8] = subject[1] + " - A1" + " | " + subject[4]
                                odd_day_morning[slot][9] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break

                elif "CSE" in subject[3] and subject[5] == "III":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_evening[slot][0] == 0 and even_day_evening[slot][1] == 0:
                                even_day_evening[slot][0] = subject[1] + " - A1" + " | " + subject[4]
                                even_day_evening[slot][1] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_evening[slot][0] == 0 and odd_day_evening[slot][1] == 0:
                                odd_day_evening[slot][0] = subject[1] + " - A1" + " | " + subject[4]
                                odd_day_evening[slot][1] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break
                
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_evening[slot][8] == 0 and even_day_evening[slot][9] == 0:
                                even_day_evening[slot][8] = subject[1] + " - A1" + " | " + subject[4]
                                even_day_evening[slot][9] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_evening[slot][8] == 0 and odd_day_evening[slot][9] == 0:
                                odd_day_evening[slot][8] = subject[1] + " - A1" + " | " + subject[4]
                                odd_day_evening[slot][9] = subject[1] + " - A2" + " | " + subject[4]
                                alloted = True
                                break

            elif int(subject[6]) > 100 and alloted == False:
                if "CSE" in subject[3] and subject[5] == "II":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_morning[slot][0] == 0:
                                even_day_morning[slot][0] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                            
                            if even_day_morning[slot][1] == 0:
                                even_day_morning[slot][1] = subject[1] + " | " + subject[4]
                                alloted = True
                                break

                            if even_day_morning[slot][8] == 0:
                                even_day_morning[slot][8] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                
                            if even_day_morning[slot][9] == 0:
                                even_day_morning[slot][9] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_morning[slot][0] == 0:
                                odd_day_morning[slot][0] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                            
                            if odd_day_morning[slot][1] == 0:
                                odd_day_morning[slot][1] = subject[1] + " | " + subject[4]
                                alloted = True
                                break

                            if odd_day_morning[slot][8] == 0:
                                odd_day_morning[slot][8] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                
                            if odd_day_morning[slot][9] == 0:
                                odd_day_morning[slot][9] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                                
                elif "ECE" in subject[3] and subject[5] == "II":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_evening[slot][0] == 0:
                                even_day_evening[slot][0] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                            
                            if even_day_evening[slot][1] == 0:
                                even_day_evening[slot][1] = subject[1] + " | " + subject[4]
                                alloted = True
                                break

                            if even_day_evening[slot][8] == 0:
                                even_day_evening[slot][8] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                
                            if even_day_evening[slot][9] == 0:
                                even_day_evening[slot][9] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_evening[slot][0] == 0:
                                odd_day_evening[slot][0] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                            
                            if odd_day_evening[slot][1] == 0:
                                odd_day_evening[slot][1] = subject[1] + " | " + subject[4]
                                alloted = True
                                break

                            if odd_day_evening[slot][8] == 0:
                                odd_day_evening[slot][8] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                
                            if odd_day_evening[slot][9] == 0:
                                odd_day_evening[slot][9] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                                
                elif "ECE" in subject[3] and subject[5] == "III":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_morning[slot][0] == 0:
                                even_day_morning[slot][0] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                            
                            if even_day_morning[slot][1] == 0:
                                even_day_morning[slot][1] = subject[1] + " | " + subject[4]
                                alloted = True
                                break

                            if even_day_morning[slot][8] == 0:
                                even_day_morning[slot][8] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                
                            if even_day_morning[slot][9] == 0:
                                even_day_morning[slot][9] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_morning[slot][0] == 0:
                                odd_day_morning[slot][0] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                            
                            if odd_day_morning[slot][1] == 0:
                                odd_day_morning[slot][1] = subject[1] + " | " + subject[4]
                                alloted = True
                                break

                            if odd_day_morning[slot][8] == 0:
                                odd_day_morning[slot][8] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                
                            if odd_day_morning[slot][9] == 0:
                                odd_day_morning[slot][9] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                                
                elif "CSE" in subject[3] and subject[5] == "III":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_evening[slot][0] == 0:
                                even_day_evening[slot][0] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                            
                            if even_day_evening[slot][1] == 0:
                                even_day_evening[slot][1] = subject[1] + " | " + subject[4]
                                alloted = True
                                break

                            if even_day_evening[slot][8] == 0:
                                even_day_evening[slot][8] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                
                            if even_day_evening[slot][9] == 0:
                                even_day_evening[slot][9] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_evening[slot][0] == 0:
                                odd_day_evening[slot][0] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                            
                            if odd_day_evening[slot][1] == 0:
                                odd_day_evening[slot][1] = subject[1] + " | " + subject[4]
                                alloted = True
                                break

                            if odd_day_evening[slot][8] == 0:
                                odd_day_evening[slot][8] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
                                                
                            if odd_day_evening[slot][9] == 0:
                                odd_day_evening[slot][9] = subject[1] + " | " + subject[4]
                                alloted = True
                                break
            
            else :
                if "CSE" in subject[3] and subject[5] == "II":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            for lt in range(2,8):
                                if even_day_morning[slot][lt] == 0:
                                    even_day_morning[slot][lt] = subject[1] + " | " + subject[4]
                                    alloted = True
                                    break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            for lt in range(2,8):
                                if odd_day_morning[slot][lt] == 0:
                                    odd_day_morning[slot][lt] = subject[1] + " | " + subject[4]
                                    alloted = True
                                    break                
                                                            
                elif "ECE" in subject[3] and subject[5] == "II":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            for lt in range(2,8):
                                if even_day_evening[slot][lt] == 0:
                                    even_day_evening[slot][lt] = subject[1] + " | " + subject[4]
                                    alloted = True
                                    break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            for lt in range(2,8):
                                if odd_day_evening[slot][lt] == 0:
                                    odd_day_evening[slot][lt] = subject[1] + " | " + subject[4]
                                    alloted = True
                                    break                
                                                            
                elif "CSE" in subject[3] and subject[5] == "III":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            for lt in range(2,8):
                                if even_day_evening[slot][lt] == 0:
                                    even_day_evening[slot][lt] = subject[1] + " | " + subject[4]
                                    alloted = True
                                    break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            for lt in range(2,8):
                                if odd_day_evening[slot][lt] == 0:
                                    odd_day_evening[slot][lt] = subject[1] + " | " + subject[4]
                                    alloted = True
                                    break                
                                                            
                elif "ECE" in subject[3] and subject[5] == "III":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            for lt in range(2,8):
                                if even_day_morning[slot][lt] == 0:
                                    even_day_morning[slot][lt] = subject[1] + " | " + subject[4]
                                    alloted = True
                                    break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            for lt in range(2,8):
                                if odd_day_morning[slot][lt] == 0:
                                    odd_day_morning[slot][lt] = subject[1] + " | " + subject[4]
                                    alloted = True
                                    break
                                                            
                elif "CSE" in subject[3] and subject[5] == "IV":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            for lt in range(2,8):
                                if even_day_morning[slot][lt] == 0:
                                    even_day_morning[slot][lt] = subject[1] + " | " + subject[4]
                                    alloted = True
                                    break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            for lt in range(2,8):
                                if odd_day_morning[slot][lt] == 0:
                                    odd_day_morning[slot][lt] = subject[1] + " | " + subject[4]
                                    alloted = True
                                    break
                    
                elif "ECE" in subject[3] and subject[5] == "IV":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            for lt in range(2,8):
                                if even_day_evening[slot][lt] == 0:
                                    even_day_evening[slot][lt] = subject[1] + " | " + subject[4]
                                    alloted = True
                                    break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            for lt in range(2,8):
                                if odd_day_evening[slot][lt] == 0:
                                    odd_day_evening[slot][lt] = subject[1] + " | " + subject[4]
                                    alloted = True
                                    break
                    

for slot_no, slot in enumerate(even_day_morning):
    for index, lt in enumerate(slot):
        print("EDM => Slot "+str(slot_no+1)+" -> L"+str(index+1)+": "+str(lt))
    print(" ")

for slot_no, slot in enumerate(even_day_evening):
    for index, lt in enumerate(slot):
        print("EDE => Slot "+str(slot_no+1)+" -> L"+str(index+1)+": "+str(lt))
    print(" ")

for slot_no, slot in enumerate(odd_day_morning):
    for index, lt in enumerate(slot):
        print("ODM => Slot "+str(slot_no+1)+" -> L"+str(index+1)+": "+str(lt))
    print(" ")

for slot_no, slot in enumerate(odd_day_evening):
    for index, lt in enumerate(slot):
        print("ODE => Slot "+str(slot_no+1)+" -> L"+str(index+1)+": "+str(lt))
    print(" ")
