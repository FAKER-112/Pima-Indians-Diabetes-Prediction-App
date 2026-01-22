# Makefile for Diabetes Prediction App

IMAGE_NAME = diabetes-app
IMAGE_TAG = latest
CLUSTER_NAME = kind

.PHONY: all build create-cluster load-image deploy clean run help

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

all: run ## Build, create cluster, and deploy

build: ## Build the Docker image
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

create-cluster: ## Create a Kind cluster with custom config
	kind create cluster --config kind-config.yaml --name $(CLUSTER_NAME)

load-image: ## Load the Docker image into Kind
	kind load docker-image $(IMAGE_NAME):$(IMAGE_TAG) --name $(CLUSTER_NAME)

deploy: ## Apply Kubernetes manifests
	kubectl apply -f deployment.yaml
	kubectl apply -f service.yaml

clean: ## Delete the Kind cluster and local image
	kind delete cluster --name $(CLUSTER_NAME)
	# docker rmi $(IMAGE_NAME):$(IMAGE_TAG) || true

run: build create-cluster load-image deploy ## Full sequence: Build -> Create -> Load -> Deploy
	@echo "Waiting for pods to be ready..."
	@kubectl wait --for=condition=ready pod -l app=diabetes-app --timeout=120s
	@echo "App should be accessible at http://localhost:5000"
