# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 09:14:09 2019

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 7 - DESIGNING RELATIONAL DATABASES
#----------------------------------------------------------------------------------------------------------------------

#a relational database is a database that contains more than one table
#the relational aspect refers to relationships between different tables in a database

#NULL values are usde when a particular value is unknown or undefined


#first step is to identify entities and the relationships between them
#a relationship database schema involves the name of the relationship, attribute (column) of the relationship (i.e. primary key, foreign key) and the type of relationship
#instances are the actual contents of the table at a given point in time
#a 1:1 relationship occurs when there is a 1:1 relationship between an entity in one table and an entity in another table (i.e. relationship between user and an account number/email address)
#a 1:many relationship refers to a relationship between an entity and multiple other objects (i.e. one user can access many different playlists)
#a many:many relationship - e.g. customer and items in an ecommerce database - a customer can order many items, and one item can be ordered by mnay customers
#most relationships fall in one of these three categories


#primary and foreign keys
#a primary key is an attribute of a relationship where every value for that attribute is unique (i.e. ID number)
#a primary key in one table is a foreign key in another table
#a primary key is column like every other column in the database, but the values in that column are unique
#you can not enter a record that doesn't have a primary key
#foreign keys can be duplicated, but they must be mapped to a unique primary key on a different table


#modelling a database
#then need to put relationships in an entity relationship diagram (ERD)
#this visualises entities, relationships and attributes (of entities, columns)
#use software to map this
#the type of relationship, directionality of relationship are important

#structured vs unstructured data
#structured data has pre-defined data models and is easy to searhc
#unstructured data has no pre-defined data model
#use SQL to query structured data
#if dealing with unstructured data, can use NoSQL
#structured data is stored in relational databases and data warehouses
#unstructured data is stored in applications, NoSQL databases, data warehouses and data lakes






