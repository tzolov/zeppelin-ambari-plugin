# Uninstall Zeppelin Service

#### Stop the Zeppelin Notebook Service
Use the Ambari UI or REST API:
``` json
curl -u admin:admin -i -H 'X-Requested-By: ambari' -X PUT -d '{ "RequestInfo": {"context" :"Stop ZEPPELIN via REST"}, "Body": {"ServiceInfo": {"state": "INSTALLED"}}}' http://ambari.localdomain:8080/api/v1/clusters/PHD30C1/services/ZEPPELIN
```
#### Remove the Service
```
curl --user admin:admin  -H 'X-Requested-By:mycompany' -X DELETE http://ambari.localdomain:8080/api/v1/clusters/PHD30C1/services/ZEPPELIN
```
#### Stop Ambari Server
```
sudo /etc/init.d/ambari-server stop
```
#### Remove the Zeppelin user and related local and HDFS directories
```
sudo userdel zeppelin
sudo rm -Rf /home/zeppelin/ /opt/zeppelin/ /tmp/zeppelin.tar.gz 
sudo -u hdfs hdfs dfs -rm -R /user/zeppelin
```
#### Uninstall the zeppelin RPM
```
sudo yum -y remove zeppelin-ambari-plugin-phd30
```
#### Start Ambari Server
```
sudo /etc/init.d/ambari-server stop
```
