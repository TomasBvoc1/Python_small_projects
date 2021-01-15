# Exercise 2 :  There are two keyboards, one is secret Keyboard, and the other is your regular keyboard, the mapping is as following
#               Your program should be able to decipher the following sentence and print out the right sentence

secret_keyboard = [" ","'",",",".","p","y","f","g","c","r","l","a","o","e","u","i","d","t","n","s","-",";","q","j","k","x","b","m","w","v","z"]
regular_keyboard = [' ','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m',',','.','/']

print(len(secret_keyboard))
print(len(regular_keyboard))

cryptic_sentence = ",. jab dak. a ,rbe.pugs ycm. cb jrmlgy.p ojc.bj.v"
print("Cryptic sentence --->   ", cryptic_sentence)
cryptic_sentence_list = list(cryptic_sentence)

my_list = []
for c in cryptic_sentence_list:
    x_index = secret_keyboard.index(c)
    my_list.append(x_index)
print (my_list)

deciphered_sentence_list = []
for d in my_list:
    letters = deciphered_sentence_list.append(regular_keyboard[d])
#print(deciphered_sentence_list)

DSL = ''.join(deciphered_sentence_list)
print("Deciphered sentence --->   ",DSL)

# one-line solution
print("\n")
print("oooooooooooooooooooooooooooooooooo")
my_message = ""
for x in cryptic_sentence:
    my_message += regular_keyboard[secret_keyboard.index(x)]
print(my_message)