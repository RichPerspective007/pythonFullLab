import matplotlib.pyplot as plt

candidates = ['ABC','XYZ','MNP']
seats = [180,200,20]
s = seats.copy()
plt.pie(x=seats, labels=candidates,autopct=lambda p: f'{p:.1f}% ({s.pop(0)})',startangle=90)
#plt.pie(seats, labels=candidates, startangle=90, colors=['green','orange','red'],autopct='%1.1f%%', explode=[0.04,0.06,0.04], shadow=True)  

'''plt.bar(candidates,seats,0.3,color=['green','orange','red'],align='center') 
for i in range(3): 
    plt.text(i, seats[i]+10.0, seats[i], ha = 'center') 
plt.xlim(-0.5,6) 
plt.ylim(0,400) 
 
plt.xlabel("Parties",loc='left') 
plt.ylabel("Seats", loc='bottom') 
plt.title('Election results of India for the year 2000')''' 

plt.title('India Elections year 2000, votes share.')
plt.legend(loc="upper right")
plt.show()


