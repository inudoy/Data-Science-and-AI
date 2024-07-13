file=open('youtube.txt','w')
try:
    file.write('imran nazir udoy')
finally:
    file.close()
with open('youtube.txt','w') as file:
    file.write('imran nazir udoy')