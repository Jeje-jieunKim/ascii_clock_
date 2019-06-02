#digital Clock
import time
import os

line1={1:"        []", 2:"[][][][][]", 3:"[][][][][]", 4:"[]      []", 5:"[][][][][]", 6:"[][][][][]", 7:"[][][][][]", 8:"[][][][][]", 9:"[][][][][]", 0:"[][][][][]"}
line2={1:"        []", 2:"        []", 3:"        []", 4:"[]      []", 5:"[]        ", 6:"[]        ", 7:"        []", 8:"[]      []", 9:"[]      []", 0:"[]      []"}
line3={1:"        []", 2:"        []", 3:"        []", 4:"[]      []", 5:"[]        ", 6:"[]        ", 7:"        []", 8:"[]      []", 9:"[]      []", 0:"[]      []"}
line4={1:"        []", 2:"        []", 3:"        []", 4:"[]      []", 5:"[]        ", 6:"[]        ", 7:"        []", 8:"[]      []", 9:"[]      []", 0:"[]      []"}
line5={1:"        []", 2:"[][][][][]", 3:"[][][][][]", 4:"[][][][][]", 5:"[][][][][]", 6:"[][][][][]", 7:"        []", 8:"[][][][][]", 9:"[][][][][]", 0:"[]      []"}
line6={1:"        []", 2:"[]        ", 3:"        []", 4:"        []", 5:"        []", 6:"[]      []", 7:"        []", 8:"[]      []", 9:"        []", 0:"[]      []"}
line7={1:"        []", 2:"[]        ", 3:"        []", 4:"        []", 5:"        []", 6:"[]      []", 7:"        []", 8:"[]      []", 9:"        []", 0:"[]      []"}
line8={1:"        []", 2:"[]        ", 3:"        []", 4:"        []", 5:"        []", 6:"[]      []", 7:"        []", 8:"[]      []", 9:"        []", 0:"[]      []"}
line9={1:"        []", 2:"[][][][][]", 3:"[][][][][]", 4:"        []", 5:"[][][][][]", 6:"[][][][][]", 7:"        []", 8:"[][][][][]", 9:"[][][][][]", 0:"[][][][][]"}


before = 0
for i in range(0, 100000000):
  t=time.localtime()
  os.system("cls")

  hour=t.tm_hour
  minute=t.tm_min
  second=t.tm_sec
  print()
  print(line1[hour//10]+"\t"+line1[hour%10]+"\t  \t"+line1[minute//10]+"\t"+line1[minute%10]+"\t  \t"+line1[second//10]+"\t"+line1[second%10])
  print(line2[hour//10]+"\t"+line2[hour%10]+"\t  \t"+line2[minute//10]+"\t"+line2[minute%10]+"\t  \t"+line2[second//10]+"\t"+line2[second%10])
  print(line3[hour//10]+"\t"+line3[hour%10]+"\t  \t"+line3[minute//10]+"\t"+line3[minute%10]+"\t  \t"+line3[second//10]+"\t"+line3[second%10])
  print(line4[hour//10]+"\t"+line4[hour%10]+"\t 0\t"+line4[minute//10]+"\t"+line4[minute%10]+"\t 0\t"+line4[second//10]+"\t"+line4[second%10])
  print(line5[hour//10]+"\t"+line5[hour%10]+"\t  \t"+line5[minute//10]+"\t"+line5[minute%10]+"\t  \t"+line5[second//10]+"\t"+line5[second%10])
  print(line6[hour//10]+"\t"+line6[hour%10]+"\t 0\t"+line6[minute//10]+"\t"+line6[minute%10]+"\t 0\t"+line6[second//10]+"\t"+line6[second%10])
  print(line7[hour//10]+"\t"+line7[hour%10]+"\t  \t"+line7[minute//10]+"\t"+line7[minute%10]+"\t  \t"+line7[second//10]+"\t"+line7[second%10])
  print(line8[hour//10]+"\t"+line8[hour%10]+"\t  \t"+line8[minute//10]+"\t"+line8[minute%10]+"\t  \t"+line8[second//10]+"\t"+line8[second%10])
  print(line9[hour//10]+"\t"+line9[hour%10]+"\t  \t"+line9[minute//10]+"\t"+line9[minute%10]+"\t  \t"+line9[second//10]+"\t"+line9[second%10])


  time.sleep(1)
