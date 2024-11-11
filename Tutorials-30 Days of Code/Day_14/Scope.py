class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

	# Add your code here
    def computeDifference(self):
        list_max = []
        for i in range(0, len(self.__elements)-1):
            for j in range(i+1, len(self.__elements)):
                list_max.append(abs(self.__elements[i]-self.__elements[j]))

        self.maximumDifference = max(list_max)
        
    
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)