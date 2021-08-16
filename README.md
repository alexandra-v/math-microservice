I created a simple microservice using the Flask framework. The client makes requests to the http://35.202.6.100/operations/ endpoint and a celery tasks will be launched to compute the operation. When the operation is done, the client will be notified using a webhook provided by him. The application uses RabbitMQ as a message broker. 

The application is containerized using Docker and for the local environment I used docker-compose. The app is deployed using Kubernetes in Google Cloud. For monitoring I am using Grafana and Prometheus.
 
- **The endpoint`s documentation can be accesed at** http://35.202.6.100/

- **The admins` interface can be accesed at** http://35.202.6.100/admin/

- **The Grafana can be accesed at** http://35.222.243.20/d/4mYv0Nn7k/cluster-monitoring-for-kubernetes?orgId=1&refresh=10s (user: math-serv, pass: math-serv)