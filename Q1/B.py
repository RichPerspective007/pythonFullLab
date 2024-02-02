'''
B) Display the marks of two students for 5 subjects using suitable graphical tools.
'''

import matplotlib.pyplot as plt
import numpy as np

print('There are two students: Manav and Pranav. Enter their marks in the following subjects.')
subjects = ['English','Mathematics 1','Digital Electronics','COA','DSA']

marksStudent1 = []
marksStudent2 = []


for i in range(len(subjects)):
    print(f'\n{subjects[i]}:\n -\tManav: ',end='')
    marksStudent1.append(int(input()))
    print(' -\tPranav: ',end='')
    marksStudent2.append(int(input()))

#attempted radar or spider chart, ignore for now.
'''angles = np.linspace(0, 2*np.pi, len(subjects), endpoint=False)

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, marksStudent1, alpha=0.25, label='Student 1')
ax.fill(angles, marksStudent2, alpha=0.25, label='Student 2')

ax.set_thetagrids(angles * 180/np.pi, labels=subjects)'''

#we will plot a side-by-side bar chart

#custom bar_width
bar_width = 0.35

#setting the bar positions
bar_positions_student1 = [i for i in range(len(subjects))] #bars for Student at positions 0,1,2,3,4
bar_positions_student2 = [pos+bar_width for pos in bar_positions_student1] #bars for Student at positions 0.35,1.35,2.35,3.35,4.35


plt.bar(bar_positions_student1,marksStudent1,color='springgreen',width=bar_width)
for i in range(len(subjects)):
    plt.text(bar_positions_student1[i],marksStudent1[i],marksStudent1[i],ha='center') #adding marks value text on top of each bar for student1
plt.bar(bar_positions_student2,marksStudent2,color='blue',width=bar_width)
for i in range(len(subjects)):
    plt.text(bar_positions_student2[i],marksStudent2[i],marksStudent2[i],ha='center') #adding marks value text on top of each bar for student2

plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Comparison of Marks in Different Subjects')

plt.xticks([pos + bar_width / 2 for pos in bar_positions_student1], subjects) #setting the position of Subject labels at the middle of the two bars per subject

plt.legend(['Manav','Pranav'], title='Responses', loc='center left', bbox_to_anchor=(1, 0.5)) #adding legend for the colors used to denote each entity

plt.show()
