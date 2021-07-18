def getDataFromuser():
	D={}
	while True:
		studentId=input("Enter student ID:")
		marksList=input("Enter the marks by comma seperated values:")
		morestudents=input("Enter \"no\" to quit insertion:")
		if studentId in D:
			print(studentId,"is alredy inserted")
		else:
			D[studentId]=marksList.split(",")
		if morestudents.lower()=="no":
			return D
studentData=getDataFromuser()
print(studentData)