import os
import json
import io

archivo=open("train.csv","r",encoding="utf-8")
data=[]
i=0
for linea in archivo:
    if i>0: 
        datos=linea.split(",")
        objeto={"id":datos[0],
                "name":datos[1],
                "host_id":datos[2],
                "host_name":datos[3],
                "neighbourhood_group":datos[4],
                "neighbourhood":datos[5],
                "latitude":datos[6],
                "longitude":datos[7],
                "room_type":datos[8],
                "price":datos[9],
                "minimum_nights":datos[10],
                "number_of_reviews":datos[11],
                "last_review":datos[12],
                "reviews_per_month":datos[13],
                "calculated_host_listings_count":datos[14],
                "availability_365":datos[15]
                }
        data.append(objeto)
    i+=1

jsonConversion=json.dumps(data)
json_Archivo=open("data.json","w")
json_Archivo.write(jsonConversion)
json_Archivo.close()



