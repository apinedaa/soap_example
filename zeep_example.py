import zeep
  
dne_client = zeep.Client(wsdl='http://dneonline.com/calculator.asmx?WSDL')

print (dne_client.service.Divide(8,4))
print (dne_client.service.Add(8,4))