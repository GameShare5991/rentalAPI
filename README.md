# rentalAPI
#### to add user renting the game: http://localhost:3005/addRental/?gameId=GAMEIDHERE&rentalUser=USERNAMEHERE

#### for retriving all games the user rented, go to http://localhost:3005/rentals?rentalUser=USERNAMEHERE


# build image: 
docker build . -t jackjackzhou/rental-api

# run image though docker: 
docker run --publish 3005:3005 rental-api

# push image:
docker push jackjackzhou/rental-api

# kubectl create&run
minikube start
kubectl create -f rental-app-deployment.yaml
minikube tunnel
minikube dashboard

# secret
kubectl create secret generic rental-app-key --from-file=serviceAccountKey.json

kubectl describe secrets/rental-app-key

# clean up
kubectl delete -f rental-app-deployment.yaml