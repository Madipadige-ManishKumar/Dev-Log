const express = require('express');
const app = express();
const port = 2006;

const path = require('path');

const fs = require('fs');

app.use(express.static(path.join(__dirname, 'public')));



app.get('/', (req, res) => {
    const my_file = path.join(__dirname, 'templates/index.html');
    res.sendFile(my_file, (err) => {
        if (err) {
            throw err;
        }
        console.log('File sent successfully');
    });
});  // <-- Closing parenthesis here


app.get('/index.html', (req, res) => {
    const my_file = path.join(__dirname, 'templates/index.html');
    res.sendFile(my_file, (err) => {
        if (err) {
            throw err;
        }
        console.log('File sent successfully');
    });
});  // <-- Closing parenthesis here


app.get('/login.html',(req,res)=>{
    res.sendFile(path.join(__dirname, 'templates/login.html'), (err) => {
        if (err) {
            throw err;
        }
        console.log('File sent successfully');
    });
})


app.get('/loginauth',(req,res) =>{
const {email,pass}=req.query;
const userData=("("+email+","+pass+")");
fs.readFile('database.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return res.status(500).send('Server Error');
    }
    
    // Split the data by ':' and store in a list
    const emailList = data.split(':').map(entry => entry.trim());

    // Check if userData exists in the emailList
    if (emailList.includes(userData)) {
        console.log('User data found in the list.');
        res.sendFile(path.join(__dirname, 'templates/home.html'), (err) => {
            if (err) {
                throw err;
            }
            console.log('File sent successfully');
        });
    } else {
        console.log('User data not found.');
        res.send({ exists: false });
    }
});

});


app.get('/home',(req,res)=>{
res.sendFile(path.join(__dirname,'templates/home.html'),(err)=>{
    if (err) {
        throw err;
    }
    console.log('File sent successfully');
});
});

app.get('/signauth',(req,res) =>{
    const {email1,pass1}=req.query;
    const userData=("("+email1+","+pass1+"):");
    fs.appendFile('database.txt', userData, (err) => {
        if (err) {
            console.error('Error saving data:', err);
            return res.status(500).send('Server Error');
        }
        console.log('Data saved successfully');
    });
    res.sendFile(path.join(__dirname, 'templates/login.html'), (err) => {
        if (err) {
            throw err;
        }
        console.log('File sent successfully');
    });
    
    
});


app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});
