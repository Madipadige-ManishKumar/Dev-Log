const { MongoClient, ObjectId } = require('mongodb');
const { log } = require('node:console');

// MongoDB Atlas connection string (replace <password> and <db_name> as needed)
const uri = "";

async function run() {
  const client = new MongoClient(uri);

  try {
    // Connect to the MongoDB cluster
    await client.connect();
    
    console.log("Connected to MongoDB Atlas!");
    mydb=client.db("blog")
    mycollection = mydb.collection("post")
    stu=[
        {
            name:'Manish Kumar M',
            age:'19'
        },
        {
            name:'Chaithanya',
            age:'19'
        },
        {
            name:'SalWomen',
            age:'19'
        }
    ]
    // await mycollection.insertMany(stu)
    // console.log("Data inserted successfully")


    const myname =  await mycollection.find({name:'Manish Kumar M'}).toArray()
    if (myname) {
        const updateResult = await mycollection.updateMany(
            { age: myname[0].age },
            { $set: { age: 18 } }
        );
        console.log("Update done. Matched:", updateResult.matchedCount, "Modified:", updateResult.modifiedCount);

        console.log(myname[0].age);
        
    } else {
        console.log("No user found with name 'Manish Kumar M'");
    }
  } catch (e) {
    console.error(e);
  } finally {
    await client.close();
  }
}

run()
