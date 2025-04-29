with open('Codingal.txt','w') as file:
  file.write("Hi!, I am a girl")
file.close()

with open('Codingal.txt','r')as file:
  data = file.readlines()
  print("Words in file are .....")
  for line in data:
    word = line.split()
    print(word)
    file.close()