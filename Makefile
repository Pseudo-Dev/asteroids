# Requires grpc-tools Python module!

proto: remote/transfer_pb2.py
	python3 -m grpc_tools.protoc -I./ --python_out=remote --grpc_python_out=remote ./asteroids.proto
	sed -i '' 's/import asteroids_pb2/import remote.asteroids_pb2/' remote/asteroids_pb2_grpc.py