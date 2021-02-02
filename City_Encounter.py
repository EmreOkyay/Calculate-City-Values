class Input:

    def __init__(self, File_1, File_2):

        self.File_1 = File_1
        self.File_2 = File_2

        self.Data_1, self.Data_2 = self.Dissect_Data(self.File_1, self.File_2)

        self.Dic_Init(self.Data_1, self.Data_2)


    def Dissect_Data(self, File_1, File_2): # Takes the data and makes it more readable and easy to compare

        Data_1, Data_2 = [], []

        self.Dic_1, self.Dic_2 = {}, {}

        self.City_Name_Dic_1, self.City_Name_Dic_2 = {}, {}

        self.City_Days_1, self.City_Days_2 = [], []

        self.City_Encounter_1, self.City_Encounter_2 = [], []

        self.Paris_Stayed_1, self.Lyon_Stayed_1, self.Rome_Stayed_1, self.London_Stayed_1, self.Berlin_Stayed_1, self.Munich_Stayed_1, self.Madrid_Stayed_1 = 0, 0, 0, 0, 0, 0, 0
        self.Paris_Stayed_2, self.Lyon_Stayed_2, self.Rome_Stayed_2, self.London_Stayed_2, self.Berlin_Stayed_2, self.Munich_Stayed_2, self.Madrid_Stayed_2 = 0, 0, 0, 0, 0, 0, 0

        self.Random = []
        self.BigMonths = [1, 3, 5, 7, 8, 10, 12] # Months that have 31 days
        self.SmallMonths = [2, 4, 6, 9, 11] # Months that have 30 days

        self.Overall_Days = 0
        self.Overall_City_Enc = {}

        for i in File_1.readlines():
            Data_1.append(i)

        for i in File_2.readlines():
            Data_2.append(i)

        for i in range(len(Data_1)):
            Data_1[i] = Data_1[i].split(',')
            Data_1[i][2] = Data_1[i][2].rstrip("\n")

        for i in range(len(Data_2)):
            Data_2[i] = Data_2[i].split(',')
            Data_2[i][2] = Data_2[i][2].rstrip("\n")

        for i in range(len(Data_1)):  # Turns string type M, D and Y into integers
            Data_1[i][0] = Data_1[i][0].split(".")
            Data_1[i][0][0] = int(Data_1[i][0][0])
            Data_1[i][0][1] = int(Data_1[i][0][1])
            Data_1[i][0][2] = int(Data_1[i][0][2])

        for i in range(len(Data_2)):  # Turns string type M ,D and Y into integers
            Data_2[i][0] = Data_2[i][0].split(".")
            Data_2[i][0][0] = int(Data_2[i][0][0])
            Data_2[i][0][1] = int(Data_2[i][0][1])
            Data_2[i][0][2] = int(Data_2[i][0][2])

        for i in range(len(Data_1)):  # Turns string type M, D and Y into integers
            Data_1[i][2] = int(Data_1[i][2])

        for i in range(len(Data_2)):  # Turns string type M, D and Y into integers
            Data_2[i][2] = int(Data_2[i][2])

        return Data_1, Data_2

    def Dic_Init(self, Data_1, Data_2): # I used a dictionary to make it easier on my self when comparing

        self.Stayed_1, self.Stayed_2 = {}, {}
        self.a = ""

        for i in range(len(Data_1)):
            self.Days_Stayed = Data_1[i][2]
            self.City_Name = Data_1[i][1]
            self.Day = Data_1[i][0][0]
            self.Month = Data_1[i][0][1]
            self.Year = Data_1[i][0][2]
            self.Day_Copy = self.Day
            self.Month_Copy = self.Month
            self.Year_Copy = self.Year
            self.Stayed_1[self.Day, self.Month, self.Year, self.City_Name] = self.Days_Stayed
            for j in range(self.Days_Stayed): # If we exceed the month limit, we proceed to the next month
                if self.Month_Copy in self.BigMonths and (self.Day_Copy+(j+1)) > 31:
                    self.Month_Copy += 1
                    self.Day_Copy = self.Day_Copy+(j+1) - 31
                    self.City_Days_1.append([self.Day_Copy + j, self.Month_Copy, self.Year, self.City_Name])
                    self.City_Name_Dic_1[self.Day, self.Month, self.Year] = self.City_Name
                elif self.Month_Copy in self.SmallMonths and (self.Day_Copy+(j+1)) > 30:
                    self.Month_Copy += 1
                    self.Day_Copy = self.Day_Copy+(j+1) - 30
                    self.City_Days_1.append([self.Day_Copy + j, self.Month_Copy, self.Year, self.City_Name])
                    self.City_Name_Dic_1[self.Day, self.Month, self.Year] = self.City_Name
                else:
                    self.City_Days_1.append([self.Day_Copy + (j + 1), self.Month_Copy, self.Year, self.City_Name])
                self.Dic_1[self.Day_Copy + (j + 1), self.Month_Copy, self.Year] = self.Day, self.Month, self.Year, self.City_Name
                self.City_Name_Dic_1[self.Day, self.Month, self.Year] = self.City_Name


        for i in range(len(Data_2)):
            self.Days_Stayed = Data_2[i][2]
            self.City_Name = Data_2[i][1]
            self.Day = Data_2[i][0][0]
            self.Month = Data_2[i][0][1]
            self.Year = Data_2[i][0][2]
            self.Stayed_2[self.Day, self.Month, self.Year, self.City_Name] = self.Days_Stayed
            self.Day_Copy = self.Day
            self.Month_Copy = self.Month
            self.Year_Copy = self.Year
            for j in range(self.Days_Stayed):
                if self.Month_Copy in self.BigMonths and (self.Day_Copy+(j+1)) > 31:
                    self.Month_Copy += 1
                    self.Day_Copy = self.Day_Copy+(j+1) - 31
                    self.City_Days_2.append([self.Day_Copy + j, self.Month_Copy, self.Year, self.City_Name])
                    self.City_Name_Dic_2[self.Day, self.Month, self.Year] = self.City_Name
                elif self.Month_Copy in self.SmallMonths and (self.Day_Copy+(j+1)) > 30:
                    self.Month_Copy += 1
                    self.Day_Copy = self.Day_Copy+(j+1) - 30
                    self.City_Days_2.append([self.Day_Copy + j, self.Month_Copy, self.Year, self.City_Name])
                    self.City_Name_Dic_2[self.Day, self.Month, self.Year] = self.City_Name
                else:
                    self.City_Days_2.append([self.Day_Copy + (j + 1), self.Month_Copy, self.Year, self.City_Name])
                self.Dic_2[self.Day_Copy+(j+1), self.Month_Copy, self.Year] = self.Day, self.Month, self.Year, self.City_Name
                self.City_Name_Dic_2[self.Day, self.Month, self.Year] = self.City_Name


class Logic(Input): # Checks if the two different dics have common dates and, what is the original date of those dates

    def __init__(self):
        super().__init__(File_1, File_2)

        self.Cache_City_1, self.Cache_City_2 = [], []
        self.Cache_dic_1, self.Cache_dic_2 = {}, {}


    def Enc_Init(self, City_Days_1, City_Days_2, Overall_Days, City_Encounter_1, City_Encounter_2, City_dic_1, City_dic_2):
        for i in range(len(City_Days_1)):
            for j in range(len(City_Days_2)):
                if City_Days_1[i] == City_Days_2[j]:
                    if self.City_Days_1[i][3] not in self.Overall_City_Enc:
                        self.Overall_City_Enc[self.City_Days_1[i][3]] = 1
                    else:
                        self.Overall_City_Enc[self.City_Days_1[i][3]] += 1
                    self.Day = City_Days_1[i][0]
                    self.Month = City_Days_1[i][1]
                    self.Year = City_Days_1[i][2]
                    City_Encounter_1.append(City_dic_1[self.Day,self.Month,self.Year])
                    City_Encounter_2.append(City_dic_2[self.Day, self.Month, self.Year])
        return City_Encounter_1, City_Encounter_2, City_dic_1, City_dic_2, Overall_Days, self.Overall_City_Enc

class Output(Logic): # Finally, we write and display the necessary values

    def __init__(self):
        super().__init__()

        self.OverallDays = 0

        self.Cache_City_1, self.Cache_City_2, self.Cache_dic_1, self.Cache_dic_2, self.OverallDays, self.Overall_City_Enc = self.Enc_Init(self.City_Days_1, self.City_Days_2, self.Overall_Days, self.City_Encounter_1, self.City_Encounter_2, self.Dic_1, self.Dic_2)
        self.Write(self.Cache_City_1, self.Cache_dic_1, "Output_1.txt", self.Stayed_1)
        self.Write(self.Cache_City_2, self.Cache_dic_2, "Output_2.txt", self.Stayed_2)
        self.Display(self.Overall_City_Enc)


    def Write(self, City_Encounter, City_dic, File_Name, Stayed):

        Out = open(File_Name, "a")

        self.Count = 0
        self.Dic_Copy = {}

        self.Random = list(set(City_Encounter))

        for i in self.Random:
            if i in Stayed:
                self.Dic_Copy[i] = Stayed[i]

        for k in self.Random:
            if k in City_dic.values():
                self.Count = City_Encounter.count(k)
                Out.write(str(k)+ "," + str(self.Dic_Copy[k]) + "," + str(self.Count))
                Out.write("\n")
        Out.close()


    def Display(self, Overall):
        for i in Overall:
            print(i, Overall[i])


File_1 = open("Text_5_1.txt", "r")
File_2 = open("Text_5_2.txt", "r")


Output = Output()
