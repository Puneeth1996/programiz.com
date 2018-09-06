h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)



h_letters = [ letter for letter in 'human' ]
print( h_letters)


h_letters = list(map(lambda x: x, 'human'))



number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)



obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)










matrix = [[1, 2],[3,4],[5,6],[7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)
