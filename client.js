const grpc = require('grpc')
const protoLoader = require('@grpc/proto-loader');
const PROTO_PATH = './stream.proto'

let packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });
let stream_proto = grpc.loadPackageDefinition(packageDefinition);

// const Stream = grpc.load(PROTO_PATH).Stream

// const client = new Stream('localhost:50051',
//     grpc.credentials.createInsecure())

// client.detection(5, (error, notes) => {
//     console.log("Done");
    
// })

function main() {
    let client = new stream_proto.Stream('0.0.0.0:50051',
                                         grpc.credentials.createInsecure());
                                         
    let call = client.Detection({request: 9});
  
    call.on('data',function(response){
      console.log(response.frame);
    });
  
    call.on('end',function(){
      console.log('All Salaries have been paid');
    });
  
  }
  
  main();