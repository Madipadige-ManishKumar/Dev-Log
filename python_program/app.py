from flask import Flask,render_template,request,send_file
import pyttsx3
import openai
import wikipedia
import webbrowser
import mysql.connector
import datetime
from apikey import apikey
import os
f="C:\\flaskfiles\\static\\history.txt"
f1="C:\\flaskfiles\\static\\history1.txt"
app = Flask(__name__)   
uname=""
pword=""
Jname=""
Topic_Name=""
currentDate=datetime.datetime.now()
currentDate=""
dbdata=""+currentDate+'''


'''
engine=pyttsx3.init()
openai.api_key = apikey
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# engine.setProperty('rate',500)
r=""
connection =mysql.connector.connect(
    host="localhost",
    user="root",
    password="cme123",
    database="db1"
    )
cursor=connection.cursor()
@app.route('/',methods=['GET','POST'])
def welcome():
        return render_template("index.html")
@app.route("/createaccont")
def createaccount():
    return render_template("createacc.html")
@app.route("/accver",methods=['GET','POST'])
def account_verfication():
    try:
        uname1=request.form['Uname']
        pword1=request.form['Pword']
        Jname=request.form['Jname']
        if Jname=='':
            Jname="Jarvis"
        query1="insert into Account_Table values('"+uname1+"','"+pword1+"','"+Jname+"','')"
        cursor.execute(query1)
        connection.commit()
        # connection.close()
        return render_template("index.html")
    except Exception as e:
            return "The Account Already Exists"
@app.route('/htmlfile.html',methods=['GET','POST'])
def AudioFile():
    global uname, pword
    uname=request.form['text1']
    pword=request.form['text2']
    topic=request.form['Topic']
    Topic_Name=str(topic)
    with open(f,'w') as file:
            file.write("")
    query="Select  Name_Of_Jarvis from  Account_Table  where user_name='"+uname+"' and  Password='"+pword+"'"
    cursor.execute(query)
    Jar_name=cursor.fetchone()
    i=0
    if Jar_name:
        i=1
    Jar_name=str(Jar_name)
    r="Hello  Sir I Am"+Jar_name+"I am Your Personal Assisstant .How Can I Assisst You"
    r=str(r)
    # query="Select   Topic_Description from  Account_Table  where user_name='"+uname+"' and  Password='"+pword+"'"
    # cursor.execute(query)
    # global  dbdata 
    # dbdata+=str(cursor.fetchone())+"\n"
    # dbdata=dbdata.replace("\n","\n")
    # engine.save_to_file(r,"C:\\flaskfiles\\static\\play.mp3")
    # r+=str(currentDate)+"Today's Topic is "+Topic_Name
    # dbdata+=r
    
    
    with open(f,'a') as file:
        file.write( r+"\n")
    # with open(f1,'a') as file:
    #     file.write( dbdata+"\n")
    if i==1:
        engine.save_to_file(r,"C:\\flaskfiles\\static\\play.mp3")
        r+=str(currentDate)+"Today's Topic is "+Topic_Name
        engine.runAndWait()
        return render_template("htmlfile.html",text12=uname)
    else:
        return "You Don't Have The Account Please Check Your Details And Or Try To Create It Again"

@app.route('/talk.html')
def talk():
    
    return render_template("talk.html")
@app.route('/home.html')
def home():
    return render_template("htmlfile.html",text12=uname)
@app.route("/result.html" ,methods=['GET','POST'])
def result():
    global dbdata
    if request.method=='POST':
        text=request.form['text']
        query=text.lower()
        dbdata +="User Query:"+query+"\n"
        with open(f,'a') as file:
            file.write("User said:  "+query+"\n")
        
        if 'open' in query:
            if 'open youtube' in query:
                engine.save_to_file("Opening youtube... ","C:\\flaskfiles\\static\\play.mp3")
                r="Opening youtube..."
                engine.runAndWait()
                webbrowser.open("youtube.com")
            elif 'open stackoverflow' in query:
                engine.save_to_file("Opening statckoverflow ","C:\\flaskfiles\\static\\play.mp3")
                r="Opening statckoverflow "
                engine.runAndWait()
                webbrowser.open('stackoverflow.com')
            elif 'open google' in query:
                engine.save_to_file("Opening Google","C:\\flaskfiles\\static\\play.mp3")
                r="Opening Google"
                engine.runAndWait()
                webbrowser.open('google.com')
            elif 'open amazon' in query:
                engine.save_to_file("Opening Amazon ","C:\\flaskfiles\\static\\play.mp3")
                r="Opening Amazon"
                webbrowser.open('amazon.in')
                engine.runAndWait()
            elif 'open flipkart' in query:
                engine.save_to_file("Opening filpkart","C:\\flaskfiles\\static\\play.mp3")
                r="Opening filpkart"
                webbrowser.open('flipkart.com')
                engine.runAndWait()
            # return ('result.html','text=text')
        else:
            if 'play game' in query:
                engine.save_to_file("I Also Like To Play Games But Try To Play For A Limit Thank You  ","C:\\flaskfiles\\static\\play.mp3")
                r="Have Fun"
                engine.runAndWait()
                webbrowser.open('poki.com')
            else:
                user_query = query
                response = query_chat_gpt(user_query)
                r=response
            
                engine.save_to_file(r,"C:\\flaskfiles\\static\\play.mp3")
                engine.runAndWait()
        text1=r
        # dbdata+="Responese:"+ r+"\n"
        # # with open(f1,'w') as file:
        # #     file.write(dbdata)
        with open(f,'a') as file:
            file.write("Response:"+r+"\n")
        return render_template('htmlfile.html',text=text1,text12=uname)

@app.route('/openfile')
def openfile():
    filepath="C:\\flaskfiles\\static\\history.txt"
    return send_file(filepath,as_attachment=True)
@app.route("/totalhistory")
def tot():
    return send_file(f1,as_attachment=True)

@app.route("/save")
def save():
    # global dbdata
    # global uname
    # global pword
    # uname=uname.replace(" ","")
    # pword=pword.replace(" ","")
    # query="update Account_table set  Topic_Description= %s where user_name='"+uname+"' and  Password='"+pword+"'"
    # cursor.execute(query,(dbdata,))
    # connection.commit()
    return  "hi"
    
def query_chat_gpt(query):
    # Define the parameters for the chat completion
    parameters = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': query}]
    }

    # Send the request to ChatGPT
    response = openai.ChatCompletion.create(**parameters)

    # Retrieve and return the response
    chat_reply = response.choices[0].message.content
    return chat_reply

  