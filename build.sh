# Build the file descriptor set
protoc -I=./proto/ -I=/opt/googleapi/googleapis-master --descriptor_set_out=test.pb ./proto/*.proto

# Compile the annotations proto
python3 -m grpc_tools.protoc -I=./proto -I=/opt/googleapi/googleapis-master --python_out=./ ./proto/descriptor.proto

