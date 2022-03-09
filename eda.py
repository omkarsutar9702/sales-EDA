import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel("C:/Users/py_st/Downloads/Sales_Data Project 1.xlsx")

### create year, month, day column
df["year"] = df["ORDERDATE"].dt.year
df["month"] = df["ORDERDATE"].dt.month
df["weekday"] = df["ORDERDATE"].dt.weekday

### year vs all variables
def years(y):
  plt.figure()
  plt.bar(df["year"] , y)
  plt.xlabel("Date")
  plt.ylabel("Values")
  plt.show()
  
years(df["SALES"])
years(df["MSRP"])
years(df["DAYS_SINCE_LASTORDER"])
years(df["ORDERLINENUMBER"])
years(df["QUANTITYORDERED"])

### month vs all variables
def monthly(y):
  plt.figure()
  plt.bar(df["month"] , y)
  plt.xlabel("Date")
  plt.ylabel("value")
  plt.show()
  
monthly(df["SALES"])
monthly(df["MSRP"])
monthly(df["DAYS_SINCE_LASTORDER"])
monthly(df["ORDERLINENUMBER"])
monthly(df["QUANTITYORDERED"])

### day vs all variables
def weekly(y):
  plt.figure()
  plt.bar(df["weekday"] , y)
  plt.xlabel("Date")
  plt.ylabel("value")
  plt.show()
  
weekly(df["SALES"])
weekly(df["QUANTITYORDERED"])
weekly(df["ORDERLINENUMBER"])
weekly(df["MSRP"])
weekly(df["DAYS_SINCE_LASTORDER"])

### count of all variables
def count(y):
  plt.figure()
  sns.countplot(y)
  plt.xticks(rotation="vertical")
  plt.show()

count(df["DEALSIZE"])
count(df["STATUS"])
count(df["PRODUCTLINE"])
count(df["CITY"])
count(df["COUNTRY"])

### city ###
city = df.groupby("CITY").sum()
cities=df["CITY"].unique()
cities = [city for city , df in df.groupby("CITY")]

def plot_city(y):
  plt.figure()
  plt.bar(cities,y)
  plt.xticks(cities , rotation="vertical" , size=5)
  plt.show()
  
plot_city(city["MSRP"])
plot_city(city["DAYS_SINCE_LASTORDER"])
plot_city(city["ORDERLINENUMBER"])
plot_city(city["QUANTITYORDERED"])
plot_city(city["SALES"])

### country ###
country = df.groupby("COUNTRY").sum()
countries = df["COUNTRY"].unique()
countries = [country for country , df in df.groupby("COUNTRY")]

def plot_country(y):
  plt.figure()
  plt.bar(countries,y)
  plt.xticks(countries , rotation="vertical" , size=5)
  plt.show()

plot_country(country["QUANTITYORDERED"])
plot_country(country["ORDERLINENUMBER"])
plot_country(country["DAYS_SINCE_LASTORDER"])
plot_country(country["MSRP"])
plot_country(country["SALES"])


#### size ###
size = df.groupby("DEALSIZE").sum()
sizes = df["DEALSIZE"].unique()
sizes = [size for size , df in df.groupby("DEALSIZE")]

def plot_size(y):
  plt.figure()
  plt.bar(sizes,y)
  plt.xticks(sizes , rotation="vertical" , size=5)
  plt.show()

plot_size(size["SALES"])
plot_size(size["MSRP"])
plot_size(size["DAYS_SINCE_LASTORDER"])
plot_size(size["ORDERLINENUMBER"])
plot_size(size["QUANTITYORDERED"])

### product line ###
product= df.groupby("PRODUCTLINE").sum()
products = df["PRODUCTLINE"].unique()
products = [product for product , df in df.groupby("PRODUCTLINE")]

def plot_product(y):
  plt.figure()
  plt.bar(products,y)
  plt.xticks(products , rotation="vertical" , size=8)
  plt.show()

plot_product(product["SALES"])
plot_product(product["MSRP"])
plot_product(product["DAYS_SINCE_LASTORDER"])
plot_product(product["ORDERLINENUMBER"])
plot_product(product["QUANTITYORDERED"])







