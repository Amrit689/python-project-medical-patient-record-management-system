from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient line from a plaintext file.

    fileName: The name of the file to read patient line from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temp (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temp (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temp (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    read1=open(fileName,"r")            # Open the file for reading        
    patients = {}
    for line in read1:
        patientinfo=[]                        
        patientinfo=line.split(",")
        if len(patientinfo)!= 8:         # Check if there are 8 fields in the line            
            print("invalid no of fields",len(patientinfo),"in line",line)
            continue
        try:
            # Unpack patient information from the line
            patientID,date,temp,hr,rr,sbp,dbp,spo2=patientinfo
            #Typecasting the data into desired format      
            patientID=int(patientID)                                
            date=str(date)
            temp=float(temp)
            hr=int(hr)
            rr=int(rr)
            sbp=int(sbp)
            dbp=int(dbp)
            spo2=int(spo2)
             # Validate patient vitals within specified ranges
            if not (35 <= temp <= 42):
                print(f"Invalid temp value ({temp}) in line: {line}")
                continue
            if not (30 <= hr <= 180):
                print(f"Invalid heart rate value ({hr}) in line: {line}")
                continue
            if not (5 <= rr <= 40):
                print(f"Invalid respiratory rate value ({rr}) in line: {line}")
                continue
            if not (70 <= sbp <= 200):
                print(f"Invalid systolic blood pressure value ({sbp}) in line: {line}")
                continue
            if not (40 <= dbp <= 120):
                print(f"Invalid diastolic blood pressure value ({dbp}) in line: {line}")
                continue
            if not (70 <= spo2 <= 100):
                print(f"Invalid oxygen saturation value ({spo2}) in line: {line}")
                continue
            # Append patient data to the dictionary
            if patientID not in patients:             
                patients[patientID]=[]
            patients[patientID].append([date,temp,hr,rr,sbp,dbp,spo2])

        except ValueError:    
                print("invalid data type in line:",line)
        except FileNotFoundError:              
            print("the file",fileName,"could not be found")
        except Exception as e:  
            print("unexpected error occured while reading the file",e)
    return patients
 

def displayPatientData(patients, patientId=0):
    """
    Displays patient line for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display line for. If 0, line for all patients will be displayed.
    """
    if patientId==0:                    #Display patient data for all the patients
        for key,value in patients.items():
            print("Patient ID:",key)
            for visit in value:
                print(" Visit Date:",visit[0])
                print("  Temperature:", "%.2f" % visit[1],"C")
                print("  Heart Rate:",visit[2],"bpm")
                print("  Respiratory Rate:",visit[3],"bpm")
                print("  Systolic Blood Pressure:",visit[4],"mmHg")
                print("  Diastolic Blood Pressure:",visit[5],"mmHg")
                print("  Oxygen Saturation:",visit[6],"%")
                print()
    else:
        try:                                            #Display patient data for a specific patient
            print("Patient ID:",patientId)    
            for visit in patients[patientId]:            
                print(" Visit Date:",visit[0])
                print("  Temperature:", "%.2f" % visit[1],"C")
                print("  Heart Rate:",visit[2],"bpm")
                print("  Respiratory Rate:",visit[3],"bpm")
                print("  Systolic Blood Pressure:",visit[4],"mmHg")
                print("  Diastolic Blood Pressure:",visit[5],"mmHg")
                print("  Oxygen Saturation:",visit[6],"%")
                print()
        except KeyError:
            print("Patient with Id",patientId,"not found")



def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    try:
        patientId=int(patientId)        # Convert patientId to integer
        # Initialize variables to store total vital sign values and visit count
        total_temp=0
        total_hr=0
        total_rr=0
        total_sbp=0
        total_dbp=0
        total_spo2=0
        num_visits=0
        # Loop through all patients and their visits
        if patientId==0:
            print("Vitals Signs For All Patients:")
            for value in patients.values():
                for visit in value:
                    total_temp += visit[1]
                    total_hr+=visit[2]
                    total_rr+=visit[3]
                    total_sbp+=visit[4]
                    total_dbp+=visit[5]
                    total_spo2+=visit[6]
                    num_visits=num_visits+1
            
            # Print average vital sign values for all patients
            print("  Average Temperature:", "%.2f" % (total_temp / num_visits), "C")
            print("  Average Heart Rate:", "%.2f" % (total_hr / num_visits), "bpm")
            print("  Average Respiratory Rate:", "%.2f" % (total_rr / num_visits), "bpm")
            print("  Average Systolic Blood Pressure:", "%.2f" % (total_sbp / num_visits), "mmHg")
            print("  Average Diastolic Blood Pressure:", "%.2f" % (total_dbp / num_visits), "mmHg")
            print("  Average Oxygen Saturation:", "%.2f" % (total_spo2 / num_visits), "%")
        else:
            try:
                # Loop through the visits of the specified patient
                print("Vital signs for patient",patientId,":")
                for visit in patients[patientId]:
                    total_temp += visit[1]
                    total_hr+=visit[2]
                    total_rr+=visit[3]
                    total_sbp+=visit[4]
                    total_dbp+=visit[5]
                    total_spo2+=visit[6]
                    num_visits=num_visits+1
                
                # Print average vital sign values for all patients                
                print("  Average Temperature:", "%.2f" % (total_temp / num_visits), "C")
                print("  Average Heart Rate:", "%.2f" % (total_hr / num_visits), "bpm")
                print("  Average Respiratory Rate:", "%.2f" % (total_rr / num_visits), "bpm")
                print("  Average Systolic Blood Pressure:", "%.2f" % (total_sbp / num_visits), "mmHg")
                print("  Average Diastolic Blood Pressure:", "%.2f" % (total_dbp / num_visits), "mmHg")
                print("  Average Oxygen Saturation:", "%.2f" % (total_spo2 / num_visits), "%")

            except KeyError:
                print("No data found for the patient with ID",patientId)
    except ValueError:
        print("error:",patientId,"should be an integer")




def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient line to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add line to.
    patientId: The ID of the patient to add line for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temp.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new line to.
    """
     # Split the date into its components
    visit_date=date.split('-')
    # Validate the date format and values
    if not(len(visit_date)==3):
        print("Invalid date format.Please enter date in the format'yyyy-mm-dd'")
    elif not (1 <= int(visit_date[1]) <=12 and 1 <=int(visit_date[2])<= 31 and 1900<=int(visit_date[0])<2100):
        print('Invalid date. Please enter a valid date.')
    elif not (35 <= temp <= 42):
        print(f"Invalid temperature value.Please enter the temperature between 35 and 42C")        
    elif not (30 <= hr <= 180):
        print(f"Invalid heart rate value.Please enter the heart rate between 30 and 180bpm")        
    elif not (5 <= rr <= 40):
        print(f"Invalid respiratory rate value.Please enter the respiratory rate value 5 and 40bpm")        
    elif not (70 <= sbp <= 200):
        print(f"Invalid systolic blood pressure value.Please enter the systolic blood pressure  between 70 and 200mmHg")       
    elif not (40 <= dbp <= 120):
        print(f"Invalid diastolic blood pressure value.Please enter the diastolic blood pressure between 40 and 120mmHg")        
    elif not (70 <= spo2 <= 100):
        print(f"Invalid oxygen saturation value.Please enter the oxygen saturation between 70 and 100%")
    else:
        # Check if patientId is already in patients dictionary, and append data accordingly
        if patientId in patients:            
            patients[patientId].append([date, temp, hr, rr, sbp, dbp, spo2])
        else:
            patients[patientId]=[]
            patients[patientId].append([date, temp, hr, rr, sbp, dbp, spo2])
        
        # Append the patient data to the file on a new line
        append1=open(fileName,"a")
        append1.write("\n")
        append1.write(f"{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}")
        append1.close()      # Close the file after writing
        print("Visit saved for patient #",patientId)


def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []     # List to store matching visits
    # If no year and month are specified, return all visits for all patients
    if year is None and month is None:
        for key,value in patients.items():       
            for visit in value:
                visits.append((key,visit))
    # If only a year is specified, filter visits by year
    elif year is not None and month is None:
        for key,value in patients.items():
            for visit in value:
                visit_date=[]
                visit_date=visit[0].split("-")
                visit_year=int(visit_date[0])
                if year==visit_year:
                    visits.append((key,visit))
    #If both year and month are specified, filter visits by both year and month
    elif year is not None and month is not None:
        for key,value in patients.items():
            for visit in value:
                visit_date=[]
                visit_date=visit[0].split("-")          #splitting the visit date
                visit_year=int(visit_date[0])
                visit_month=int(visit_date[1])
                if year==visit_year and month==visit_month:     
                    visits.append((key,visit))
    else:                  #if only month is provided,filter visit by months
        for key,value in patients.items():
            for visit in value:
                visit_date=[]
                visit_date=visit[0].split("-")
                visit_month=int(visit_date[1])
                if month==visit_month:
                    visits.append((key,visit)) 

    return visits     # Return the list of tuples containing matching patient IDs and visits

def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []
    # Loop through each patient and their visits
    for key,value in patients.items():
        for visit in value:
            hr=visit[2]
            sbp=visit[4]
            dbp=visit[5]
            spo2=visit[6]
            # Check for abnormal vital signs
            if((60>hr or hr>100) or (140<sbp or dbp>90) or spo2<90):
                 # Add patient to follow-up list if not already there
                if key not in followup_patients:
                    followup_patients.append(key)
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, fileName):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete line from.
    patientId: The ID of the patient to delete line for.
    fileName: The name of the file to save the updated patient line.
    return: None
    """
    if patientId in patients:
        patients.pop(patientId)     # Remove the patient's records from the dictionary
        # Open the file in write mode
        open1=open(fileName,"w")

        for key,value in patients.items():         #loop through patient dictionary
            for visit in value:
                # Write the patient's data to the file with a newline character
                open1.write(f"{key},{visit[0]},{visit[1]},{visit[2]},{visit[3]},{visit[4]},{visit[5]},{visit[6]}\n")
        print("Data for patient",patientId,"has been deleted")
        open1.close()
    else:
        print("patient with ID",patientId,"not found")

###########################################################################
###########################################################################
#                                                                         #
#   The following code is being provided to you. Please don't modify it.  #
#                                                                         #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient line")
        print("2. Display patient line by ID")
        print("3. Add patient line")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temp (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid line.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()
