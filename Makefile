# Requires grpc-tools Python module!

proto: remote/transfer_pb2.py
	python -m grpc_tools.protoc -I./ --python_out=remote --grpc_python_out=remote ./transfer.proto
	sed -i '' 's/import transfer_pb2/import remote.transfer_pb2/' remote/transfer_pb2_grpc.py