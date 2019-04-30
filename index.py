import csv

even_day_slots = 5
odd_day_slots = 3
no_of_lt = 10

even_day_morning = []
even_day_evening = []
odd_day_morning = []
odd_day_evening = []

alloted_count = 0

for slot in range(even_day_slots):
    even_day_morning.append([0] * no_of_lt)
    even_day_evening.append([0] * no_of_lt)

for slot in range(odd_day_slots):
    odd_day_morning.append([0] * no_of_lt)
    odd_day_evening.append([0] * no_of_lt)

def check_clash(slot, teacher, subject, audience = "Specific", year = "I"):
    for lt in slot:
        if teacher in str(lt) and subject not in str(lt):
            print("clash")
            return False
        if "All" in audience and year in str(lt):
            if "CSE" in str(lt) or "ECE" in str(lt):
                print("clash")
                return False
    return True

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
                            even_day_morning[slot][0] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                            even_day_morning[slot][1] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                            even_day_evening[slot][0] = subject[1] + " - B1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                            even_day_evening[slot][1] = subject[1] + " - B2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                            alloted = True
                            print("Alloted "+ subject[1])
                            alloted_count += 1 
                            break
                
                if alloted == False:
                    for slot in range(odd_day_slots):
                        if odd_day_morning[slot][8] == 0 and odd_day_morning[slot][9] == 0 and odd_day_evening[slot][8] == 0 and odd_day_evening[slot][9] == 0:
                            odd_day_morning[slot][8] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                            odd_day_morning[slot][9] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                            odd_day_evening[slot][8] = subject[1] + " - B1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                            odd_day_evening[slot][9] = subject[1] + " - B2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                            alloted = True
                            print("Alloted "+ subject[1])
                            alloted_count += 1 
                            break
                
                if alloted == False:
                    for slot in range(odd_day_slots):
                        if odd_day_morning[slot][8] == 0 and odd_day_morning[slot][9] == 0 and odd_day_evening[slot][8] == 0 and odd_day_evening[slot][9] == 0:
                            odd_day_morning[slot][8] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                            odd_day_morning[slot][9] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                            odd_day_evening[slot][8] = subject[1] + " - B1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                            odd_day_evening[slot][9] = subject[1] + " - B2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                            alloted = True
                            print("Alloted "+ subject[1])
                            alloted_count += 1 
                            break

            
            elif int(subject[6]) > 200 and alloted == False:
                if "CSE" in subject[3] and subject[5] == "II":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_morning[slot][0] == 0 and even_day_morning[slot][1] == 0:
                                if(check_clash(even_day_morning[slot],subject[4],subject[1])):
                                    even_day_morning[slot][0] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    even_day_morning[slot][1] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_morning[slot][0] == 0 and odd_day_morning[slot][1] == 0:
                                if(check_clash(odd_day_morning[slot],subject[4],subject[1])):
                                    odd_day_morning[slot][0] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    odd_day_morning[slot][1] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_morning[slot][8] == 0 and even_day_morning[slot][9] == 0:
                                if(check_clash(even_day_morning[slot],subject[4],subject[1])):
                                    even_day_morning[slot][8] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    even_day_morning[slot][9] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_morning[slot][8] == 0 and odd_day_morning[slot][9] == 0:
                                if(check_clash(odd_day_morning[slot],subject[4],subject[1])):
                                    odd_day_morning[slot][8] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    odd_day_morning[slot][9] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break

                elif "ECE" in subject[3] and subject[5] == "II":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_evening[slot][0] == 0 and even_day_evening[slot][1] == 0:
                                if(check_clash(even_day_evening[slot],subject[4],subject[1])):
                                    even_day_evening[slot][0] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    even_day_evening[slot][1] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_evening[slot][0] == 0 and odd_day_evening[slot][1] == 0:
                                if(check_clash(odd_day_evening[slot],subject[4],subject[1])):
                                    odd_day_evening[slot][0] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    odd_day_evening[slot][1] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_evening[slot][8] == 0 and even_day_evening[slot][9] == 0:
                                if(check_clash(even_day_evening[slot],subject[4],subject[1])):
                                    even_day_evening[slot][8] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    even_day_evening[slot][9] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_evening[slot][8] == 0 and odd_day_evening[slot][9] == 0:
                                if(check_clash(odd_day_evening[slot],subject[4],subject[1])):
                                    odd_day_evening[slot][8] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    odd_day_evening[slot][9] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break

                elif "ECE" in subject[3] and subject[5] == "III":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_morning[slot][0] == 0 and even_day_morning[slot][1] == 0:
                                if(check_clash(even_day_morning[slot],subject[4],subject[1])):
                                    even_day_morning[slot][0] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    even_day_morning[slot][1] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_morning[slot][0] == 0 and odd_day_morning[slot][1] == 0:
                                if(check_clash(odd_day_morning[slot],subject[4],subject[1])):
                                    odd_day_morning[slot][0] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    odd_day_morning[slot][1] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_morning[slot][8] == 0 and even_day_morning[slot][9] == 0:
                                if(check_clash(even_day_morning[slot],subject[4],subject[1])):
                                    even_day_morning[slot][8] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    even_day_morning[slot][9] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_morning[slot][8] == 0 and odd_day_morning[slot][9] == 0:
                                if(check_clash(odd_day_morning[slot],subject[4],subject[1])):
                                    odd_day_morning[slot][8] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    odd_day_morning[slot][9] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break

                elif "CSE" in subject[3] and subject[5] == "III":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_evening[slot][0] == 0 and even_day_evening[slot][1] == 0:
                                if(check_clash(even_day_evening[slot],subject[4],subject[1])):
                                    even_day_evening[slot][0] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    even_day_evening[slot][1] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_evening[slot][0] == 0 and odd_day_evening[slot][1] == 0:
                                if(check_clash(odd_day_evening[slot],subject[4],subject[1])):
                                    odd_day_evening[slot][0] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    odd_day_evening[slot][1] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if even_day_evening[slot][8] == 0 and even_day_evening[slot][9] == 0:
                                if(check_clash(even_day_evening[slot],subject[4],subject[1])):
                                    even_day_evening[slot][8] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    even_day_evening[slot][9] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if odd_day_evening[slot][8] == 0 and odd_day_evening[slot][9] == 0:
                                if(check_clash(odd_day_evening[slot],subject[4],subject[1])):
                                    odd_day_evening[slot][8] = subject[1] + " - A1" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    odd_day_evening[slot][9] = subject[1] + " - A2" + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break

            elif int(subject[6]) > 100 and alloted == False:
                if "CSE" in subject[3] and subject[5] == "II":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if(check_clash(even_day_morning[slot],subject[4],subject[1])):
                                if even_day_morning[slot][0] == 0:
                                    even_day_morning[slot][0] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                
                                if even_day_morning[slot][1] == 0:
                                    even_day_morning[slot][1] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break

                                if even_day_morning[slot][8] == 0:
                                    even_day_morning[slot][8] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                    
                                if even_day_morning[slot][9] == 0:
                                    even_day_morning[slot][9] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if(check_clash(odd_day_morning[slot],subject[4],subject[1])):
                                if odd_day_morning[slot][0] == 0:
                                    odd_day_morning[slot][0] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                
                                if odd_day_morning[slot][1] == 0:
                                    odd_day_morning[slot][1] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break

                                if odd_day_morning[slot][8] == 0:
                                    odd_day_morning[slot][8] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                    
                                if odd_day_morning[slot][9] == 0:
                                    odd_day_morning[slot][9] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                                
                elif "ECE" in subject[3] and subject[5] == "II":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if(check_clash(even_day_evening[slot],subject[4],subject[1])):
                                if even_day_evening[slot][0] == 0:
                                    even_day_evening[slot][0] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                
                                if even_day_evening[slot][1] == 0:
                                    even_day_evening[slot][1] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break

                                if even_day_evening[slot][8] == 0:
                                    even_day_evening[slot][8] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                    
                                if even_day_evening[slot][9] == 0:
                                    even_day_evening[slot][9] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if(check_clash(odd_day_evening[slot],subject[4],subject[1])):
                                if odd_day_evening[slot][0] == 0:
                                    odd_day_evening[slot][0] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                
                                if odd_day_evening[slot][1] == 0:
                                    odd_day_evening[slot][1] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break

                                if odd_day_evening[slot][8] == 0:
                                    odd_day_evening[slot][8] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                    
                                if odd_day_evening[slot][9] == 0:
                                    odd_day_evening[slot][9] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                                
                elif "ECE" in subject[3] and subject[5] == "III":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if(check_clash(even_day_morning[slot],subject[4],subject[1])):
                                if even_day_morning[slot][0] == 0:
                                    even_day_morning[slot][0] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                
                                if even_day_morning[slot][1] == 0:
                                    even_day_morning[slot][1] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break

                                if even_day_morning[slot][8] == 0:
                                    even_day_morning[slot][8] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                    
                                if even_day_morning[slot][9] == 0:
                                    even_day_morning[slot][9] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if(check_clash(odd_day_morning[slot],subject[4],subject[1])):
                                if odd_day_morning[slot][0] == 0:
                                    odd_day_morning[slot][0] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                
                                if odd_day_morning[slot][1] == 0:
                                    odd_day_morning[slot][1] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break

                                if odd_day_morning[slot][8] == 0:
                                    odd_day_morning[slot][8] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                    
                                if odd_day_morning[slot][9] == 0:
                                    odd_day_morning[slot][9] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                                
                elif "CSE" in subject[3] and subject[5] == "III":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if(check_clash(even_day_evening[slot],subject[4],subject[1])):
                                if even_day_evening[slot][0] == 0:
                                    even_day_evening[slot][0] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                
                                if even_day_evening[slot][1] == 0:
                                    even_day_evening[slot][1] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break

                                if even_day_evening[slot][8] == 0:
                                    even_day_evening[slot][8] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                    
                                if even_day_evening[slot][9] == 0:
                                    even_day_evening[slot][9] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if(check_clash(odd_day_evening[slot],subject[4],subject[1])):
                                if odd_day_evening[slot][0] == 0:
                                    odd_day_evening[slot][0] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                
                                if odd_day_evening[slot][1] == 0:
                                    odd_day_evening[slot][1] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break

                                if odd_day_evening[slot][8] == 0:
                                    odd_day_evening[slot][8] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
                                                    
                                if odd_day_evening[slot][9] == 0:
                                    odd_day_evening[slot][9] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                    alloted = True
                                    print("Alloted "+ subject[1])
                                    alloted_count += 1 
                                    break
            
            else :
                if "CSE" in subject[3] and subject[5] == "II":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if alloted == True:
                                break
                            if(check_clash(even_day_morning[slot],subject[4],subject[1])):
                                for lt in range(2,8):
                                    if even_day_morning[slot][lt] == 0:
                                        even_day_morning[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if alloted == True:
                                break
                            if(check_clash(odd_day_morning[slot],subject[4],subject[1])):
                                for lt in range(2,8):
                                    if odd_day_morning[slot][lt] == 0:
                                        odd_day_morning[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break                
                                                            
                elif "ECE" in subject[3] and subject[5] == "II":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if alloted == True:
                                break
                            if(check_clash(even_day_evening[slot],subject[4],subject[1])):
                                for lt in range(2,8):
                                    if even_day_evening[slot][lt] == 0:
                                        even_day_evening[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if alloted == True:
                                break
                            if(check_clash(odd_day_evening[slot],subject[4],subject[1])):
                                for lt in range(2,8):
                                    if odd_day_evening[slot][lt] == 0:
                                        odd_day_evening[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break                
                                                            
                elif "CSE" in subject[3] and subject[5] == "III":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if alloted == True:
                                break
                            if(check_clash(even_day_evening[slot],subject[4],subject[1])):                                
                                for lt in range(2,8):
                                    if even_day_evening[slot][lt] == 0:
                                        even_day_evening[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if alloted == True:
                                break
                            if(check_clash(odd_day_evening[slot],subject[4],subject[1])):
                                for lt in range(2,8):
                                    if odd_day_evening[slot][lt] == 0:
                                        odd_day_evening[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break                
                                                            
                elif "ECE" in subject[3] and subject[5] == "III":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if alloted == True:
                                break
                            if(check_clash(even_day_morning[slot],subject[4],subject[1])):
                                for lt in range(2,8):
                                    if even_day_morning[slot][lt] == 0:
                                        even_day_morning[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if alloted == True:
                                break
                            if(check_clash(odd_day_morning[slot],subject[4],subject[1])):
                                for lt in range(2,8):
                                    if odd_day_morning[slot][lt] == 0:
                                        odd_day_morning[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break
                                                            
                elif "CSE" in subject[3] and subject[5] == "IV":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if alloted == True:
                                break
                            if(check_clash(even_day_morning[slot],subject[4],subject[1])):
                                for lt in range(2,8):
                                    if even_day_morning[slot][lt] == 0:
                                        even_day_morning[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if alloted == True:
                                break
                            if(check_clash(odd_day_morning[slot],subject[4],subject[1])):
                                for lt in range(2,8):
                                    if odd_day_morning[slot][lt] == 0:
                                        odd_day_morning[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break
                    
                elif "ECE" in subject[3] and subject[5] == "IV":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if alloted == True:
                                break
                            if(check_clash(even_day_evening[slot],subject[4],subject[1])):
                                for lt in range(2,8):
                                    if even_day_evening[slot][lt] == 0:
                                        even_day_evening[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            if alloted == True:
                                break
                            if(check_clash(odd_day_evening[slot],subject[4],subject[1])):
                                for lt in range(2,8):
                                    if odd_day_evening[slot][lt] == 0:
                                        odd_day_evening[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break
                    
                elif "All" in subject[3] and subject[5] == "IV":
                    if alloted == False:
                        for slot in range(even_day_slots):
                            if alloted == True:
                                break
                            print("Tried Alloting " + subject[1])
                            if(check_clash(even_day_morning[slot],subject[4],subject[1],subject[3],subject[5])):
                                for lt in range(2,8):
                                    if even_day_morning[slot][lt] == 0:
                                        even_day_morning[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            print("Tried Alloting " + subject[1])
                            if alloted == True:
                                break
                            if(check_clash(odd_day_morning[slot],subject[4],subject[1],subject[3],subject[5])):
                                for lt in range(2,8):
                                    if odd_day_morning[slot][lt] == 0:
                                        odd_day_morning[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break

                    if alloted == False:
                        for slot in range(even_day_slots):
                            if alloted == True:
                                break
                            print("Tried Alloting " + subject[1])
                            if(check_clash(even_day_evening[slot],subject[4],subject[1],subject[3],subject[5])):
                                for lt in range(2,8):
                                    if even_day_evening[slot][lt] == 0:
                                        even_day_evening[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break
                
                    if alloted == False:
                        for slot in range(odd_day_slots):
                            print("Tried Alloting " + subject[1])
                            if alloted == True:
                                break
                            if(check_clash(odd_day_evening[slot],subject[4],subject[1],subject[3],subject[5])):
                                for lt in range(2,8):
                                    if odd_day_evening[slot][lt] == 0:
                                        odd_day_evening[slot][lt] = subject[1] + " | " + subject[4] + " | " + subject[3] + " | " + subject[5]
                                        alloted = True
                                        print("Alloted "+ subject[1])
                                        alloted_count += 1 
                                        break

initial_html = '''<!DOCTYPE HTML>
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            <title>Time Table</title>
            <style>
                * { font-size: 12px }
                table { table-layout: fixed ; width: 100% ; }
                td { width: 10%; vertical-align: top; }
                table { border-collapse: collapse; }
                table, th, td { border: 1px solid black; }
            </style>
        </head>
        <body>
            <table>
                <tr>
                    <td colspan="10" style="text-align: center">Monday</td>
                </tr>'''

html1 = initial_html
html1+= '''
                <tr>
                    <td colspan="2" style="text-align: center">8:00 - 9:00</td>
                    <td colspan="2" style="text-align: center">9:00 - 10:00</td>
                    <td colspan="2" style="text-align: center">10:00 - 11:00</td>
                    <td colspan="2" style="text-align: center">11:00 - 12:00</td>
                    <td colspan="2" style="text-align: center">12:00 - 1:00</td>
                </tr>
                <tr>\n'''
for slot_no, slot in enumerate(even_day_morning):
    html1 += '<td colspan="2">\n'
    for index, lt in enumerate(slot):
        html1 += '\tL'+str(index+1)+': '+str(lt)+'<br>\n'
        print("EDM => Slot "+str(slot_no+1)+" -> L"+str(index+1)+": "+str(lt))
    print(" ")
    html1 += '</td>\n'

html1 += '</tr></table><br><br>'

html2 = initial_html
html2+= '''
                <tr>
                    <td colspan="2" style="text-align: center">1:00 - 2:00</td>
                    <td colspan="2" style="text-align: center">2:00 - 3:00</td>
                    <td colspan="2" style="text-align: center">3:00 - 4:00</td>
                    <td colspan="2" style="text-align: center">4:00 - 5:00</td>
                    <td colspan="2" style="text-align: center">5:00 - 6:00</td>
                </tr>
                <tr>\n'''

for slot_no, slot in enumerate(even_day_evening):
    html2 += '<td colspan="2">\n'
    for index, lt in enumerate(slot):
        html2 += '\tL'+str(index+1)+': '+str(lt)+'<br>\n'
        print("EDE => Slot "+str(slot_no+1)+" -> L"+str(index+1)+": "+str(lt))
    print(" ")
    html2 += '</td>\n'

html1 += '<table><tr><td colspan="10" style="text-align: center">Tuesday</td></tr>'
html1+= '''
                <tr>
                    <td colspan="3" style="text-align: center">8:00 - 9:30</td>
                    <td colspan="3" style="text-align: center">9:30 - 11:00</td>
                    <td colspan="3" style="text-align: center">11:00 - 12:30</td>
                    <td style="text-align: center">12:30 - 1:00</td>
                </tr>
                <tr>'''
for slot_no, slot in enumerate(odd_day_morning):
    html1 += '<td colspan="3">\n'
    for index, lt in enumerate(slot):
        html1 += '\tL'+str(index+1)+': '+str(lt)+'<br>\n'
        print("ODM => Slot "+str(slot_no+1)+" -> L"+str(index+1)+": "+str(lt))
    print(" ")
    html1 += '</td>\n'

html1 += '''
                <td>&nbsp;</td>
            </tr>
        </table>
    </body>
</html>'''
html1_file= open("1.html","w+")
html1_file.write(html1)
html1_file.close()

html2 += '<table><tr><td colspan="10" style="text-align: center">Tuesday</td></tr>'
html2+= '''
                <tr>
                    <td colspan="3" style="text-align: center">8:00 - 9:30</td>
                    <td colspan="3" style="text-align: center">9:30 - 11:00</td>
                    <td colspan="3" style="text-align: center">11:00 - 12:30</td>
                    <td style="text-align: center">12:30 - 1:00</td>
                </tr>
                <tr>'''
for slot_no, slot in enumerate(odd_day_evening):
    html2 += '<td colspan="3">\n'
    for index, lt in enumerate(slot):
        html2 += '\tL'+str(index+1)+': '+str(lt)+'<br>\n'
        print("ODE => Slot "+str(slot_no+1)+" -> L"+str(index+1)+": "+str(lt))
    print(" ")
    html2 += '</td>\n'

html2 += '''
                <td>&nbsp;</td>
            </tr>
        </table>
    </body>
</html>'''
html2_file= open("2.html","w+")
html2_file.write(html2)
html2_file.close()        

print(alloted_count)
