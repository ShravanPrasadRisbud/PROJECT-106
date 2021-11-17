import plotly.express as px
import csv
import numpy as np 

def plotFigure(data_path):
  with open(data_path,encoding="utf-8") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Roll No", y="Marks In Percentage")
    fig.show()

def getDataSource(data_path):
  marksPercent = []
  Rollno = []
  
  with open(data_path,encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      marksPercent.append(float(row["Marks In Percentage"]))
      Rollno.append(float(row["Roll No"]))
      
  return {"x" : Rollno, "y" :marksPercent}

def findCorrelation(datasource):
  correlation = np.corrcoef(datasource["x"], datasource["y"])
  print("Correlation between Marks and Roll no is :-  \n--->".correlation[0,1])
  
def setup():
  data_path = "student_marks_and_days.csv"
  
  datasource = getDataSource(data_path)
  findCorrelation(datasource)
  plotFigure(data_path)
  
setup()
