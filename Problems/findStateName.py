def findStateName(ipCityName):
    op=[]
    for i in obj:
        for j in obj[i]:
            if (ipCityName in obj[i][j]):
                op.append(j)

                
    return op

obj = {
"India" : {
"Karnataka" : ["Bangalore", "Mysore"],
"Maharashtra" : ["Mumbai", "Pune"]
},
"USA" : {
"Texas" : ["Dallas", "Houston"],
"IL" : ["Chicago", "Aurora", "Pune"]
}
}

ipCityName=input()
print(findStateName(ipCityName))
