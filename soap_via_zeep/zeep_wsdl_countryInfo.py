from zeep import Client

client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')

print("All services:")
print(client.wsdl.dump())

# print("*****************************************************************")
# print("Service ListOfCountryNamesByName() ")
# result = client.service.ListOfCountryNamesByName()
# print(result)