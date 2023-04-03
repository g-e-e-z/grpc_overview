gogen:
	protoc -I=proto --go_out=. proto/*.proto

pygen:
	python3 -m grpc_tools.protoc -I=./proto --python_out=./pb/serialization/ --grpc_python_out=./pb --pyi_out=./pb proto/*.proto

gen: gogen pygen

clean:
	rm -f pb/*.go
	rm -f pb/*.py
	rm -f pb/*.pyi
	rm -f pb/serialization/*.py

run:
	go run main.go

