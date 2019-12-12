class Tyres:
    # class level variables:
    objectCount = 0

    def __init__(self):
        pass

    def setTyreCount(self, tyreCount=4):
        self.TyreCount = tyreCount
        print("method : setTyreCount")
        print("id(self.TyreCount) : ", id(self.TyreCount))
        print("value(self.TyreCount) : ", self.TyreCount)

    def getTyreCount(self):
        print("method : getTyreCount")
        print("id(self.TyreCount) : ", id(self.TyreCount))
        print("value(self.TyreCount) : ",self.TyreCount)
        return self.TyreCount

    def increaseTyreCount(self):
        self.TyreCount += 1
        print("method : increaseTyreCount")
        print("id(self.TyreCount) : ", id(self.TyreCount))
        print("value(self.TyreCount) : ",self.TyreCount)

    def setBrandNames(self, brandNames=[]):
        self.brandNames = brandNames
        print("method : setBrandNames")
        print("id(self.brandNames) : ", id(self.brandNames))
        print("value(self.brandNames) : ",self.brandNames)

    def getBrandNames(self):
        print("method : getBrandNames")
        print("id(self.brandNames) : ", id(self.brandNames))
        print("value(self.brandNames) : ",self.brandNames)
        return self.brandNames

    def increaseBrandNames(self, newBrandName):
        self.brandNames.append(newBrandName)
        print("method : increaseBrandNames")
        print("id(self.brandNames) : ", id(self.brandNames))
        print("value(self.brandNames) : ",self.brandNames)


brandNames = ["ford", "chev"]
print("brandNames : ", brandNames)
print("id(brandNames) : ", id(brandNames))

s2 = Tyres()
s2.setBrandNames(brandNames)

s2.increaseBrandNames("maruti")

print("brandNames : ", brandNames)
print("id(brandNames) : ", id(brandNames))

# tyreCount = 3
# print("Value : ", tyreCount)
# print("id(tyreCount) : ", id(tyreCount))
#
# s1 = Tyres()
# s1.setTyreCount(tyreCount)
# s1.increaseTyreCount()
#
# print("Value : ", tyreCount)
# print("id(tyreCount) : ", id(tyreCount))
#
# t1 = s1.getTyreCount()
# print("Value : ", t1)
# print("id(t1) : ", id(t1))
