const express = require("express")
const path = require("path");  
const bp = require("body-parser");
const { dirname } = require("path");
const { log } = require("console");
const app = express();
const port =3000
app.use(express.static("public"))
app.get('/',(req,res)=>
{
res.render('index')
})

app.post('/add',(req,res)  =>
{
    const task = req.body.task;
    if (!task) {
        return res.status(400).send('Task is required!');  // Error handling if task is empty
    }

    res.render('thanku', { task: task });
})


app.listen(port, () => {
    console.log(`🚀 Server running at http://localhost:${port}`);
});