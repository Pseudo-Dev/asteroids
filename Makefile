# Requires grpc-tools Python module!

proto: remote/transfer_pb2.py
	python -m grpc_tools.protoc -I./ --python_out=remote --grpc_python_out=remote ./transfer.proto
