# list is collection of same of differnt data type elements.

# Data structures #
##################
        #
        #

a = [1000,200,True,45.6]

print(type(a))
a.append(5000)

print(a)

clouds = list()

print(type(clouds))
clouds.append('aws')
clouds.append("azure")
clouds.append("gcp")
clouds.append('ibm')
clouds.append('alibaba')
clouds.append("utho")

print(clouds)


print("Length of cloud service, ",len(clouds))
print("World leader of cloud provider is ,",clouds[0])

print("Indian cloud cloud provider is,",clouds[-1])
 

for i in clouds:
    if i =="aws":
      print("World leader hai cloud me.")
    elif i =="azure":
      print("Josh batch me cover hoga!")
