import numpy
import psycopg2
import win32com.client

# score = 51
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')

def someMath(v1, v2, v3):
    # v1 = 1
    # v2 = 5
    add = v1 * v2 - v3
    subtract = v2 - v1
    print (v1)
    print(str(v1) + " + " + str(v2) + " = " + str(add))
    print(subtract)
    return add
prod = someMath(5, 5, 1)
print('proizvod je: '+ str(prod))

# f_in = open('D:/KURSEVI/Udemy Python for Geospatial/python/addresses.txt','r')
# f_out = open('D:/KURSEVI/Udemy Python for Geospatial/python/addresses.csv','w')
#
# for line in f_in:
#     print(line)
#     f_out.write(line + '\n')
# f_in.close()
# f_out.close()

conn = psycopg2.connect(dbname='richland', host='localhost', port='5432', user='postgres', password='start#01')

excel = win32com.client.Dispatch("Excel.Application")

cur = conn.cursor()
# getschools = 'SELECT DISTINCT schools."NAME" ' \
#              'FROM schools, tri92 ' \
#              'WHERE st_distance (schools.geometry, tri92.geometry) < 5000'

getschools = " SELECT DISTINCT schools.\"NAME\", min(st_distance(schools.geometry, tri92.geometry)) AS dist " \
             " FROM schools, tri92 " \
             " WHERE st_dWithin(schools.geometry, tri92.geometry,5000) " \
             " GROUP BY schools.\"NAME\" ORDER BY dist "

# getschools = ' SELECT DISTINCT schools."NAME", st_distance (schools.geometry, tri92.geometry) as dist ' \
#              ' FROM schools, tri92 ' \
#              ' WHERE st_dWithin(schools.geometry, tri92.geometry, 5000) ' \
#              ' AND tri92."NAME" = \'+ "LINDAU CHEMICAL" +' \
#              ' ORDER BY dist ASC '

cur.execute(getschools)
thevals = cur.fetchall()

mydists = []
for dists in thevals:
    mydists.append(dists[1])
    print(dists)
print(mydists)
print(thevals)

print(numpy.average(mydists))

stdev = excel.WorksheetFunction.StDev(mydists)
print(stdev)

conf = excel.WorksheetFunction.Confidence(0.1, stdev, len(mydists))
print(conf)

avg = numpy.average(mydists)
print(avg)
