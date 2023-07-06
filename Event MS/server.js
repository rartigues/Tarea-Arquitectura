const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const packageDefinition = protoLoader.loadSync('proto/villain.proto');
const villainProto = grpc.loadPackageDefinition(packageDefinition).VillainService;
const MongoClient = require('mongodb').MongoClient;

const server = new grpc.Server();

server.addService(villainProto.service, {
  AddVillain: async (call, callback) => {
    const villain = call.request;
    // console.debug(`Server - Recieved following request: ${JSON.stringify(villain)}`)
    const { nombreVillano, fechaIngreso } = villain;
    if (!nombreVillano || !fechaIngreso) {
      return callback({
        code: grpc.status.INVALID_ARGUMENT,
        message: `Missing required fields. Required fields are nombre_villano and fecha_ingreso`,
      });
    }
    const villainObj = { nombreVillano, fechaIngreso };
    console.debug(`Server - Adding villain: ${JSON.stringify(villainObj)}`)


    // Connect to MongoDB
    // const client = new MongoClient('mongodb://localhost:27017', { useUnifiedTopology: true });
    // mongodb+srv://root:<password>@cluster0.iwrd3cq.mongodb.net/?retryWrites=true&w=majority
    // const client = new MongoClient('mongodb://root:1234@localhost:27017');
    const client = new MongoClient('mongodb://root:1234@mongo:27017');
    await client.connect();

    // Get the database and collection
    const db = client.db('test');
    const collection = db.collection('villains');

    // Insert the villain
    await collection.insertOne(villain);

    // Close the connection
    await client.close();

    callback(null, { message: `Villain ${nombreVillano} added successfully` });
  },
});

server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
console.log(`Server - Running on port 50051`)
server.start();
