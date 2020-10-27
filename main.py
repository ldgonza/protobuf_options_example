from google.protobuf.descriptor_pb2 import FileDescriptorSet

# Required to get "http" option
import google.api.annotations_pb2

# Required to get our custom "unsecurded" option
import descriptor_pb2

with open('test.pb', mode='rb') as f:
    data = f.read()

fd = FileDescriptorSet.FromString(data)

for proto_file in fd.file:
    for service in proto_file.service:
        for method in service.method:
            # print(method.options) # Will show all options

            # Print only the one we want
            unsecured = method.options.Extensions[descriptor_pb2.unsecured]
            print(service.name, method.name,
                  "unsecured" if unsecured else "secured")
