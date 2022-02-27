import chatgptuse as ct
import randombin as dr
import time  

def myfun(P):
    if P==1:
        return "Yes"
    else:
        return "No"

age=dr.generate_random_binary1()
print(age,end=",")
family_history=dr.generate_random_binary()
print(family_history,end=",")
Physical_excercise=dr.generate_random_binary()
print(Physical_excercise,end=",")
obesity=dr.generate_random_binary()
print(obesity,end=",")
Heart_diseases=dr.generate_random_binary()
print(Heart_diseases,end=",")
somking=dr.generate_random_binary()
print(somking,end=",")
painkiller=dr.generate_random_binary()
print(painkiller,end=",")
alchol=dr.generate_random_binary()
print(alchol,end=",")



c1=myfun(family_history)

c2=myfun(Physical_excercise)

c3=myfun(obesity)

c4=myfun(Heart_diseases)

c5=myfun(somking)

c6=myfun(painkiller)

c7=myfun(alchol)

print("Before Query")
# Construct the query based on your data
query = ( '''i age is {a}, my family has The kidney diesease {c1}, i do excersice {c2},i have obesity {c3}
        i have Heart Diseases {c4},i smoke {c5},i take excessive painkiller {c6},i drink alchol {c7}.Do I Have Danger of Kidney diesese .Just Tell Yes Or No Only One word
        '''.format(a=age,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7)

)
print("After Query")
result="hello"
result=ct.query_chat_gpt(query)
print(result)
print("Execution done ")
# Make the API call and handle rate limits
# result = None
# while result is None:
#     try:
#         result = ct.query_chat_gpt(query)
#     except Exception as e:
#         result=None
#         time.sleep(20)  # Wait for 20 seconds before retrying

# # Process the result as needed
# n = 0 if result == 'No' else 1
# print(n)
