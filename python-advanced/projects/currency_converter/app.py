from flask import Flask,render_template,request
import math 
app=Flask(__name__)

#function section 

def aplha_numeric(num):
    alpha="ABCDEFGHOJKLMNOPQRSTUVWXYZabcdefghijklmonpqrstuvwxyz"
    n=alpha.find(num)
    if n>25:
        n-=26
    n+=10
    return n
def any_to_decimal(num,base):
    n=str(num)
    sum=0
    for i in range(len(n)):
        if str(n[len(n)-i-1]).isalpha():
            val=aplha_numeric(n[len(n)-i-1])
            sum+=int(int(val)*int(math.pow(base,i)))

        elif int(n[len(n)-i-1])<base :
            sum+=int(int(n[len(n)-i-1])*int(math.pow(base,i)))
        else:
            raise Exception("out of the range")
    return sum
def decimal_to_any(num,base):
    s=""
    while num:
        n=int(num%base)
        if n>=10:
            aplha="ABCDEFGHIJKLMNOPQRSTUVWYXZ"  
            n-=10
            n=aplha[n]
        s+=str(n)
        num=int(num/base)
    return s[::-1]
    pass

@app.route("/")
def index():
    currency=[10,2,8,16]
    return render_template  ("index.html",currency=currency)
# @app.route("/convert",methods="POST")
# def convert():
#     amount=int(request.form['amount'])
#     f=request.form['form']
#     to= request.form['to']
#     if f =="decimal":
#         pass

if __name__=="__main__":
    # app.run(debug=True,port=2006)
    n=decimal_to_any(10,16)
    print(n)