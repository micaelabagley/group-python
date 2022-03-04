"""Some stuff for playing with astropy.table.Table

The two tables in question are called table1.dat and table2.dat. The data
in the tables are completely made up, but let's pretend each row 
corresponds to an object in the CANDELS catalog.

In this imaginary reality, the columns are:
field - the name of the CANDELS field 
pointing - an ID of the HST pointing in which the object was observed
objid - an object ID number, unique to the field and pointing
xx - the x pixel position in the HST image
yy - the y pixel position in the HST image
z - the source redshift

Both tables contain the same objects, but the objects do not appear in the 
same order in both tables.
"""
from astropy.table import Table


### reading in the tables:
t1 = Table.read('table1.dat', format='ascii')
t2 = Table.read('table2.dat', format='ascii')
# if they were in the FITS format:
t1 = Table.read('table1.fits', format='fits')
# actually, Table can understand some basic filetypes, so if the file
# ends in FITS, you don't have to specify. 
t1 = Table.read('table1.fits')


### basic exploration of the data
# print table in a "formatted"
t1.pprint() 
# print the names of the columns
print(t1.columns)
# print all info from the 1st row (remember python is 0-indexed)
print(t1[0])
# print everything from the column called 'field'
print(t1['field'])

# you can save each of these things to a variable if you want to work with it:
columns = t1.columns 
row1 = t1[0]
fields = t1['field']
# the variable types are Table variable types. so you may notice that 
# columns is a TableColumns rather than a regular list. row1 is a Row, 
# fields is a Column. Howver, you can essentially treat them as regular 
# lists and arrays

### adding a column
# let's say you have a value calculated for each object, called grism_redshift
# first we import the Column object from astropy.table
from astropy.table import Column
# then we can add the info as a Column to t1
t1.add_column(Column(data=grism_redshift, name='grism_redshift'))
# let's remove the xx and yy because we want to
t1.remove_column('xx')
t1.remove_column('yy')
# Or remove a list of columns all at once:
t1.remove_columns(['xx', 'yy'])

### calculate some new stuff and add a new object to the catalog
# use add_row() and pass a list of values, one for each column in t1
t1.add_row([objfield, objpointing, objgrism_redshift])


### writing the catalog
# write to fits format
t1.write('newtable.fits')
# again, it will recognize the FITS format
# add overwrite=True if the file already exists and you want to overwrite it
t1.write('newtable.fits', overwrite=True)
# for a different format
t1.write('newtable.dat', format='ascii')
# there are TONS of formats available for both reading in and writing out, 
# including latex tables, sextractor catalogs, machine readable tables 
# that astronomy journals require, etc.
# see here:
#   https://docs.astropy.org/en/stable/io/unified.html#table-io


### stacking tables
# let's say you have two tables and you already know they line up exactly
# i.e., 0th row corresponds to 0th row, etc. (NOTE that this is not the case 
# with t1 and t2)
# you can stack the tables horizontally:
from astropy.table import hstack
new = hstack([t1, t2])
# new has the same number of rows as t1 and t2, but now includes all columns 
# from both tables together.
# you'll notice that columns with the same names have been renamed 
# so field is now field_1 and field_2 because it appears in both tables

# if you have two tables with at least a few column names in common, you can 
# vertically stack them:
from astropy.table import vstack
new2 = vstack([t1,t2])
# new2 has one copy of all unique columns from the two tables, and has 
# the number of rows in t1 + rows in t2
# you'll see that where one of the tables didn't have a column in the other,
# the value is --. for example, t1 did not have a 'z' column, so in new2 there 
# are a bunch of --'s associated with 'z' for the objects in t1.
# These represent data that is masked out or missing. Astropy Table is 
# very good at dealing with missing data. It's one of it's strengths. 

### joining tables
# the big guns! 
# our assumption is that t1 and t2 include the same 30 objects, or at least 
# some objects in common. (actually it'll work if no objects are in common, 
# it'll just return an empty table depending on how you run it). let's join 
# the two tables together so all info is in the same place. let's also use 
# something more sophisticated than hstack, so astropy.table actually matches 
# the data for us before combining
# we have an objid column, but we know this is not unique. For example, there 
# are multiple objects with objid=1. Don't worry, astropy join() let's us 
# match on multiple columns
from astropy.table import join
new = join(t1, t2, keys=['field', 'pointing', 'objid'])
# with 'keys', you provide a list of column names to match
# in this case, it first checks for a match on 'field', then moves to 
# 'pointing', etc. 
# the default join type is 'inner', which means only rows that are present 
# in BOTH tables make it to the final, joined version. options for 
# join type are:
#   'inner' (only include matches), 
#   'outer' (include all sources in both catalogs
#   'left' (include all sources from left table (t1 in this case)
#   'right' (include all sources from right table (t2 in this case)
new = join(t1, t2, keys=['field', 'pointing', 'objid'], join_type='left')


### here ends the whirlwind tutorial

