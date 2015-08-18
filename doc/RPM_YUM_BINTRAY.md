## Public YUM Repository
The `zeppelin-ambari-plugin` RPMs are distributed through the [Big-Data](https://bintray.com/big-data/rpm/zeppelin-ambari-plugin/view) public YUM repository.  

#### Install the plugin via the YUM repository
Add the Big-Data to your YUM repositories, use `yum` to install `zeppelin-ambari-plugin-xxx` and restart Ambari.
```
sudo wget https://bintray.com/big-data/rpm/rpm -O /etc/yum.repos.d/bintray-big-data-rpm.repo
sudo yum -y install zeppelin-ambari-plugin-phd30
sudo /etc/init.d/ambari-server restart
```
For `HDP2.2` install `zeppelin-ambari-plugin-hdp22` and for `HDP2.3` install `zeppelin-ambari-plugin-hdp23` instead.

#### Upload new build RPMs to the Big-Data YUM repository
```
./gradlew clean dist bintrayUpload
```
Make sure that the `BINTRAY_BIGDATA_USER` and `BINTRAY_BIGDATA_KEY` variables are set.
Finally go to the Bintray [zeppelin-ambari-plugin](https://bintray.com/big-data/rpm/zeppelin-ambari-plugin/view) project and publish the newly uploaded RPMs.
