# -*- coding: utf-8 -*-
"""selimgul_q7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TSWbL7Yiop12Ve3v5MdFnYDVDRFlZFyY
"""

courseEnroll = {"IF100A":262, "IF100B":212, "IF100C":248, 
                "SPS102A":263, "NS102A":64, "NS102B":52, 
                "MATH101A":236, "SPS101A":360, "HIST191A":304, 
                "MATH101B":209, "MATH101C":213, "HIST191B":264, 
                "NS102C":68, "SPS101B":385, "NS102D":69, "HIST191Y":83}

def numberOfStudents(courseEnroll):
  keyList = list(courseEnroll.keys())
  nameList = []
  newDict = {}
  for i in range(len(keyList)):
    names = keyList[i]
    names = names[:-1]
    nameList.append(names)
  valueList = list(courseEnroll.values())
  countList = []
  for j in range(len(valueList)):
    values = valueList[j]
    countList.append(values)
  for k in range(len(nameList)):
    key = nameList[k]
    value = countList[k]
    if key not in newDict:
      newDict[key] = value
    else:
      newDict[key] += value
  return newDict

