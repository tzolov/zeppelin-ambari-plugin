# Zeppelin Service for Apache Ambari [ ![Download](https://api.bintray.com/packages/big-data/rpm/zeppelin-ambari-plugin/images/download.svg) ](https://bintray.com/big-data/rpm/zeppelin-ambari-plugin/_latestVersion)

<img align="right" src="https://github.com/tzolov/zeppelin-ambari-plugin/blob/master/doc/images/ZeppelinAmbariService.png" alt="zeppelin-service" width="350"></img>
[Apache Zeppelin](https://zeppelin.incubator.apache.org/) service for [Apache Ambari](https://ambari.apache.org/). It allows you to install and manage Zeppelin as an Ambari service. The plugin is compatible with Ambari `1.7`, `2.0.x` and `2.1.x` and Stacks: `PHD3.0`, `HDP2.2x` and `HDP2.3`.
To embed the Zepplein UI pages within Ambari you can use the [Ambari Webpage Embedder](https://github.com/tzolov/ambari-webpage-embedder-view) project.



> This project builds upon the excellent work done in the [ambari-zeppelin-service](https://github.com/hortonworks-gallery/ambari-zeppelin-service). The original code was significantly refactored to remove some unnecessary functionality and keep the focus only on the Zeppelin service. All assumptions on pre-installed other services are removed. Also is removed the build-on-the-fly functionality. Instead it is expected that the installer will use a pre-build Zeppelin tarball (default tarball is provided). The plugin installation is simplified and one can install it through a public YUM repository. 

This [Video](https://www.youtube.com/watch?v=BrFWXLAVOa4) illustrates the capabilities of the plugin.

## How to build
Clone the project and build and use gradle to build it
```
git clone https://github.com/tzolov/zeppelin-ambari-plugin.git
./gradlew clean build dist
```
The `build/distributions/` contains the a generic tar.gz as well as RPM pacakges for each suppoerted stack. 

## How to Use 
Install the plugin to Ambari and then deploy the Zeppeling service.
#### Instal the plugin to Ambari
Add the Big-Data YUM repository to your CentOS/RedHat system, install the latest Zeppelin plugin RPM and restart the Ambari Server: 
```
sudo wget https://bintray.com/big-data/rpm/rpm -O /etc/yum.repos.d/bintray-big-data-rpm.repo
sudo yum -y install zeppelin-ambari-plugin-phd30
sudo /etc/init.d/ambari-server restart
```
This installs the Zeppelin plugin for PHD30 Hadoop distro. For HDP2.2 install `zeppelin-ambari-plugin-hdp22` and for HDP2.3 install `zeppelin-ambari-plugin-hdp23` instead.

#### Deploy the Zeppelin Service
1. Login to Ambari server
2. Open the `Services` view and click on `Actions`/`+Add Services` button.
3. Select the `Zeppelin Notebook` service from the list and press `Next`.
4. Select a host for the Zeppelin server component and press `Next`.
5. Open the `zeppelin-ambari-config` configuration panel. By default the plugin will check if the `zeppelin.temp.file` points to a valid Zeppelin tarball. If the tarball is not available the plugin uses `zeppelin.tarball.url` to download it. By default plugin will use this URL to download the [zeppelin-0.6.0-incubating-SNAPSHOT.tar.gz](https://dl.dropboxusercontent.com/u/79241625/zeppelin-0.6.0-incubating-SNAPSHOT.tar.gz) tarball. You can change the download URL or provide a Zeppelin tarball locally by setting the `zeppelin.temp.file`. Note that the local tarball must be on the Ambari server.
6. Review the `zeppelin-config` and `zeppelin-env` configurations. You may want to change the `zeppelin.server.addr` from `0.0.0.0` to the host name of the server Zeppelin is installed on.
7. Press `Next` to complete the installation. 

#### Configuration Properties
The `Zeppelin Notebook/Configs` windows exposes the standard [Zeppelin configuration properties](https://github.com/apache/incubator-zeppelin/blob/gh-pages/docs/install/install.md#configure). Grouped in the `zeppelin-env` and `zeppelin-config` sections. 
In addition the `zeppelin-ambari-config` section exposes some Zepelin Ambari specific configuration options like the URLof the Zeppelin tarball being installed or the URL of the predefied notebooks arhive. Table below lists those properties:

<table>
	<thead>
		<tr>
			<th><sub>Property</sub></th>
			<th><sub>Description</sub></th>
			<th><sub>Default Value</sub></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><sub>zeppelin.notebooks.url</sub></td>
			<td><sub>URL of pre-build notebooks (tar.gz).</sub></td>
			<td><sub>https://dl.dropboxusercontent.com/u/79241625/notebooks.tar.gz</sub></td>
		</tr>
		<tr>
			<td><sub>zeppelin.tarball.url</sub></td>
			<td><sub>URL location of pre-build Zeppelin tarball (tar.gz)</sub></td>
			<td><sub>https://dl.dropboxusercontent.com/u/79241625/zeppelin-0.6.0-incubating-SNAPSHOT.tar.gz</sub></td>
		</tr>
		<tr>
			<td><sub>zeppelin.temp.file</sub></td>
			<td><sub>Temporary file where pre-built package will be downloaded to. If your env has limited space under /tmp, change this to different location. In this case you must ensure that the zeppelin user must be able to write to this location.</sub></td>
			<td><sub>/tmp/zeppelin.tar.gz</sub></td>
		</tr>
		<tr>
			<td><sub>zeppelin.install.dir</sub></td>
			<td><sub>Local dir where to install component. incubator-zeppelin folder will be created as a subdir of this dir e.g. /opt/incubator-zeppelin</sub></td>
			<td><sub>/opt</sub></td>
		</tr>
		<tr>
			<td><sub>zeppelin.executor.mem</sub></td>
			<td><sub>Executor memory to use (e.g. 512m or 1g)</sub></td>
			<td><sub>512m</sub></td>
		</tr>
	</tbody>	  	
</table>



