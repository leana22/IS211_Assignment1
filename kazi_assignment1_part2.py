# -*- coding: utf-8 -*-
"""assignment1_part2.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fhsKMbrpuSAiEOJVsxdkcWk6XaClXO-P
"""

class Book:   
# creating a class with attributes author and title
    author = "" 
    title = ""

    def __init__(self, Author, Title):  
    # An __init__ function that takes in an author and a title, and sets them to the object variables
        self.author = Author
        self.title = Title

    def display(self):
    # display function which when called, simply prints out a string representing the book. 
        print("\""+self.title+", written by "+self.author+"\"")

object1 = Book("John Steinbeck", "Of Mice and Men")
# creating the first object that represents the book ‘Of Mice and Men’, written by John Steinbeck
object1.display()
# display function call


object2 = Book("Harper Lee", "To Kill a Mockingbird")
# creating the second object that represents the book ‘To Kill a Mockingbird’ by Harper Lee.
object2.display()
# display function call