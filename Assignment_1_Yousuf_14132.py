# List variable initiation
salaries = ['20k', '40k', '50k', '60k', '35k', '89k','40k']

# 1. What is the length of the salaries list.
print (len(salaries))

# 2. Retrieve the third salary in the list by using index.
print (salaries[2])

# 3. Extract the last salary from the list by using a negative index.
print (salaries[-1])

# 4. Slice the salaries list to get only the middle three salaries.
print (salaries[2:5])

# 5. Add a new salary to the list, ‘100k’ by using append() method.
salaries.append('100k')
print (salaries)

# 6. Add a new salary to the list, ‘120k’ without method.
salaries = salaries + ['120k']
print (salaries)

# 7. Replace the third salary in the list with '55k' and print the updated list.
salaries = salaries[0:2] + ['55k'] + salaries[3:]
print (salaries)

# Another way to replace value
salaries[2] = '55K'
print (salaries)


# 8. Count how many times '40k' appears in the list.
print (salaries.count('40k'))

# 9. Insert a new salary at the second position.
salaries = salaries[0:1] + ['25k'] + salaries[1:]
print (salaries)

# Another way to insert value at the second position.	
salaries.insert(1, '25K')
print (salaries)

# 10. Reverse the order of the salaries list with method.
salaries.reverse()
print (salaries)

# 11. Reverse the order of the salaries list without method.
print (salaries[::-1])