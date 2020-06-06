from parse import *
import csv

print 'opening eui.in'
f = open("eui-in.txt", "r")
s = f.read()
f.close()
#print s

print 'opening out file'
g = open("eui.out.txt", "w")

f = open("eui-in.txt", "r")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
f.close()
print  'closing eui.in'

print "\n",'scanning lines'
print >>g, '"lora.device-eui": "{',
print '"lora.device-eui": "{',
l1=""
for x in range(0,15,2):
  l1 = l1+"0x"+line1[x:x+2]+", "
l1 =l1[0:46]+' }",'
print >>g, l1
print  l1

print >>g, '            "lora.application-eui": "{',
print '            "lora.application-eui": "{',
l2=""
for x in range(0,15,2):
  l2 = l2+"0x"+line2[x:x+2]+", "
l2 =l2[0:46]+' }",'
print >>g, l2
print  l2

print >>g, '            "lora.application-key": "{',
print '            "lora.application-key": "{',
l3=""
for x in range(0,31,2):
  l3 = l3+"0x"+line3[x:x+2]+", "
l3 =l3[0:94]+' }"'
print >>g, l3
print l3

print  'closing output file'
g.close()




