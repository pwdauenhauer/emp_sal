#Name: Peter Dauenhauer
#Assignment #5
#Date: 10/25/19
#Section: MW 9:30-11
#This is a program to read and report the salaries earned by different
#employees from a file

MONTHS = 3              # only constant

salSum = 0
avg = 0
janSal = 0
febSal = 0
marSal = 0              # initializing quantitative variables
avgSal = 0
minSal = 0

def average(listName, months):      #defining average function
    count = 1
    for count in range(4):          # creating for loop
        salSum = sum(listName[1:4])
        avg = salSum/MONTHS
        count = count + 4
    return avg                  # returning avg variable to main()


def main():                 #defining main()
    try:
        employeeRecords = open('EmployeeRecords.txt','r') #open records file
        empName = employeeRecords.readline().rstrip('\n')
        averageFile = open('EmployeeAverageSalaries.txt','w')   #open outfile
        salaryList = []         #empty list
    
        while empName != '':        #start while loop

            salaryList.insert(0,empName)
            janSal = float(employeeRecords.readline()) #reading from records file
            salaryList.insert(1,janSal)
            febSal = float(employeeRecords.readline())
            salaryList.insert(2,febSal)                # inserting to list
            marSal = float(employeeRecords.readline())
            salaryList.insert(3,marSal)
            minSal = min(salaryList[1:4])           #calculating minimums
            avgSal = average(salaryList, MONTHS)
            avgString = str(format(avgSal,'.2f'))         #convert avg variable to string
            averageFile.write(empName + '  $' + avgString)  #write names and averages to outfile
            averageFile.write('\n')
            print('Employee Name:', empName)
            print('January: $', format(janSal, '.2f'), sep = '')    #printing out read values
            print('February: $', format(febSal, '.2f'), sep = '')
            print('March: $', format(marSal, '.2f'), sep = '')
            print('The lowest monthly salary is $', format(minSal, '.2f'), sep = '') # printing minimums
            print('Average monthly salary for ', empName, ' is $', format(avgSal, '.2f'), sep = '') 
            print()
            empName = employeeRecords.readline().rstrip('\n')
        averageFile.close()    #close outfile
    except Exception as err:        #exception handling
        print('System Message:', err)  #system error message
    
main()  #call main
