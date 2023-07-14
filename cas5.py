# import csv
#
# # with open('hehe.csv', 'r') as file:
# #     csv_reader = csv.reader(file)
# #     listdicts = []
# #     for row in csv_reader:
# #         if 'Name' not in row:
# #             listdicts.append({"Name":row[0],"Age":row[1],"City":row[2]})
# #     print(listdicts)
# # data=[
# #     ['1','2','3'],
# #     ['1','2','3'],
# # ['1','2','3']
# # ]
# with open('hehe.csv','w', newline="") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(data)
# data=[
#     {'11':'1','22':'2','33':'3'},
#     {'11':'1','22':'2','33':'3'},
# {'11':'1','22':'2','33':'3'}
# ]
# with open('hehe.csv','w', newline="") as file:
#     fields=data[0].keys()
#     csv_writer = csv.DictWriter(file,fieldnames=fields)
#     csv_writer.writeheader()
#     csv_writer.writerows(data)
# import csv
# try:
#     inp = int(input())
# except ValueError:
#     pass
# else:
#     with open('hehe.csv','r') as f:
#         reader=csv.DictReader(f)
#         with open('hehe_new.csv', 'w', newline='') as f:
#             writer=csv.DictWriter(f,fieldnames=reader.fieldnames)
#             writer.writeheader()
#             for row in reader:
#                 row['Age']=str(int(row['Age'])+inp)
#                 writer.writerow(row)





