import math

class DistanceFormula:
    def __init__(self, outfile, infile):
        self.outfile = open(outfile, "a")
        self.infile = open(infile, "rt")

    def main(self):
        self.outfile.write("\n")
        self.outfile.write(('{:-^30}').format("DISTANCE FORMULA"))
        self.outfile.write("\n\n")
        nums = []
        for line in self.infile: 
            numbers = line.rstrip()
            nums.append(numbers) # appends the nums to list

        x1 = nums[0]    ##############################
        x2 = nums[1]    #                            #
        y1 = nums[2]    #   SETS NUMS TO VARIABLES   #
        y2 = nums[3]    #   x1, x2, y1, y2, z1, z2   #
        z1 = nums[4]    #                            #
        z2 = nums[5]    ##############################

        global result
        result = math.sqrt(((int(x2)) - (int(x1))**2) + (((int(y2)) - (int(y1)))**2)+(((int(z2)) - (int((z1)))))**2)
        
        self.outfile.write(str(nums)) 
        print(nums)
        print(result)

    def show(self):
        self.outfile.write(str("\n"))
        self.outfile.write(str(result))
        self.outfile.write("\n")
        

             

    def closeFiles(self):
        self.outfile.close()
        self.infile.close()

d1 = DistanceFormula("output.txt", "infile.txt") 
d1.main()
d1.show() 
d1.closeFiles()
    




    