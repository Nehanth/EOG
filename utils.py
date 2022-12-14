import pandas as pd
import numpy as np
import math





class drillBit:
    def __init__ (self, name, cPerRun, cPerFoot, cPerHour):
        self.name = name
        self.cPerRun = cPerRun
        self.cPerFoot = cPerFoot
        self.cPerHour = cPerHour

  #1st graph - hour - x axsis , per foot - y axis
  #3nd graoh = cost per run - x axus ,c. ost per foot
  #3rd graph =

Buzz = drillBit('Buzz Drilldrin', 5000, 1.5, 0)
Astro = drillBit('AstroBit', 3000, 1, 1500)
Apollo = drillBit('Apollo', 1000, 4, 2500)
Chall = drillBit('ChallengDriller', 10000, 0, 0)

bitData = {
    'Name': ['Buzz Drilldrin', 'AstroBit', 'Apollo', 'ChallengeDriller'],
    'Cost Per Run': ['5000', '3000', '1000', '10000'],
    'Cost Per Foot': ['1.5', '1', '4','0'],
    'Cost Per Hour': ['0', '1500','2500', '0']
}

# DEFINE PD INFORMATION OF ALL DRILL BITS
bitDataframe = pd.DataFrame(bitData)





def getCPR(testName):
    
    global PR
    
 
    if (testName == Buzz.name):
        PR = Buzz.cPerRun
       
    elif (testName == Astro.name):
        PR = Astro.cPerRun
        
    elif (testName == Apollo.name):
        PR = Apollo.cPerRun
       
    elif (testName == Chall.name):
        PR = Chall.cPerRun
      

    return PR

def getCPF(testName):
    global PF

    if (testName == Buzz.name):
       
        PF = Buzz.cPerFoot
 
        
    elif (testName == Astro.name):
        
        PF = Astro.cPerFoot
      
    elif (testName == Apollo.name):
        
        PF = Apollo.cPerFoot
      
    elif (testName == Chall.name):
       
        PF = Chall.cPerFoot
       
    return(PF)

def getCPH(testName):
    global PH
    if (testName == Buzz.name):
      
        PH = Buzz.cPerHour
    elif (testName == Astro.name):
   
        PH = Astro.cPerHour
    elif (testName == Apollo.name):
     
        PH = Apollo.cPerHour
    elif (testName == Chall.name):
  
        PH = Chall.cPerHour

    return(PH)


listHours = ["","","","",""]
listNames = ["","","","",""]


'''
RETURN A TABLE LIKE SO

[DRILL BIT, 'OCCURRENCES']

[.., ..]

"""
BIT_DEPTH,
RATE_OF_PENETRATION,
HOOK_LOAD,
DIFFERENTIAL_PRESSURE,
WEIGHT_ON_BIT,
DRILL_BIT_ID,
DRILL_BIT_NAME
"""
'''
def getBitRecurrences(df):
    return df["DRILL_BIT_NAME"].nunique()

def getBitOccurrences(df):
    return df["DRILL_BIT_NAME"].value_counts()

def TC (df):
    # DEFINE OUTPUT DF
    column_names = ['Depth','Cost']
    outputDF = pd.DataFrame(columns=column_names)
    # SET VARIABLES TO ZERO
    sumHours = 0.0
    sumFeet = 0.0
    row = 0
    overAllCost = 0.0
    upCost = 0

    # DEFINE THE NUMBER OF ROWS
    rowsCount = len(df.index) - 1

    # DEFINE THE DRILL COUNTER
    drillCounter = 1

    # DEFINE FLAGS
    flagBuzz = False
    flagAstro = False
    flagApollo = False
    flagChall = False

    #feet per instantance
    # ITERATE THROUGH THE ROWS
    for row in range(rowsCount):

        # DEFINE THE VARIABLES PER ROW
        # DEFINE THE BIT DEPTH OF THE ROW AFTER CURRENT ROW
        rowPlus1 = df.loc[row+1,"BIT_DEPTH"].item()

        # DEFINE THE BIT DEPTH OF THE CURRENT ROW
        thisRow = df.loc[row, "BIT_DEPTH"].item()

        # DEFINE THE CURRENT PEN RATE
        ratePen = df.loc[row, "RATE_OF_PENETRATION"].item()

        # DEFINE THE CHANGE IN DISTANCE
        #deltaFt = change per instance
        deltaFt = rowPlus1 - thisRow

        #
        if (deltaFt < 0):
            print(f'{row} has erronous bit depth')
        
        if (ratePen > 0) :
    
            hours = deltaFt / ratePen

            if (hours < 0):
                print(str(row) + ' wrong ')
                print(df.loc[[row]])
                print(deltaFt)
        
        sumHours = sumHours + hours
        sumFeet = sumFeet + deltaFt
    
        testName = df.loc[row, 'DRILL_BIT_NAME']
        if(flagBuzz == False):
            if (testName == Buzz.name):
                flagBuzz = True
                upCost = upCost + getCPR(Buzz.name)

        if(flagAstro == False):
            if(testName == Astro.name):
                flagAstro = True
                upCost = upCost + getCPR(Astro.name)

        if(flagApollo == False):
            if (testName == Apollo.name):
                flagApollo == True
                upCost = upCost + getCPR(Apollo.name)

        if(flagChall == False):
            if (testName == Chall.name):
                flagChall = True
                upCost = upCost + getCPR(Chall.name)
        
        dID = df.loc[row, 'DRILL_BIT_ID'].item()

        if (drillCounter != dID or row == rowsCount):
            #calcualte cost 
            #print (drillCounter)
            listHours[drillCounter-1] = sumHours
            listNames[drillCounter-1] = df.loc[row-1, 'DRILL_BIT_NAME']
               
            
            #costPR = getCPR(testName)
            costPF = getCPF(testName)
            costPH = getCPH(testName)
            

            
            costOfDrill =  (sumFeet * costPF) + (sumHours * costPH)
            costOfChange = ((sumFeet / 100 * 30)/3600) * costPH
            #print (costOfDrill, costOfChange)
            overAllCost = overAllCost + costOfDrill + costOfChange


            # APPEND TO DATAFRAME
            outputDF.loc[len(outputDF.index)] = [str(sumFeet), str(int(overAllCost))]


            sumFeet = 0
            sumHours = 0
            drillCounter += 1




    

        #sum = sum + deltaFt
    print(outputDF)
    overAllCost = overAllCost + upCost
    return outputDF

    # return(overAllCost)


def getHours():
    print("t")
# GET AN AVERAGE OF ANY COLUMN
def getAverage(df, columnName, roundOff):

    # DEFINE THE DF AFTER ROUNDOFF
    return round((df[columnName]).mean(), roundOff)
def getMin(df, columnName, roundOff):
    return round(df[columnName].min(), roundOff)

def getMax(df, columnName, roundOff):
    return round(df[columnName].max(), roundOff)

def getListHours():
    return(listHours)

def getListNames():
    return(listNames)
