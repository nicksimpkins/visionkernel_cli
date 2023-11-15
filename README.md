# VisionKernel CLI
### V 1.0.0 LTS
### VisionKernel Corp.
### www.visionkernel.com/visionkernel-cli/v1/documentation

##
### REQUIRED: Python 3.9.0 or later
### Must have following libraries installed: pandas, openpyxl, argparse
##

## About

VisionKernel is a data management tool tailored for the financial industry. That being said, the VisionKernel CLI can make it easier than ever to work with your data.


### Getting Started

The VisionKernel CLI allows you to connect to a cloud database from your preferred provider. Adding a database is as easy as running the `visionkernel add cloud-database` command and following the prompts. Once a database is added, you are able to access the previously setup tables and export data to them.


### Exporting data

Exporting data is made easy with our two export options. `nitroexport` allows for the immediate upload of data. If you have reviewed your data, or otherwise want to send it straight to the cloud, you are able to run our nitroexport command to export it immediately. If you are dealing with data that hasn't been reviewed you can run our `smartexport` command which will run a quick scan of the data to look for things such as "N/A" values, blank values and wrong character type values. Smartexport will also look for values that seem to be out of place, and flag them for review. 

### Converting data -- DONE

Converting data is simple with our `convert` option. Easily convert a file such as .txt, .xml, .json, .csv or .xls into a different supported file type. The convert feature allows for the quick conversion of data into a more readable or preferred type. Synatax is `python main.py convert example.csv name_of_new_file.xlxs`.

### Connecting Cloud Database -- DONE

To connect to your cloud database you will need certain information that is unique for every database and every cloud provider. 
AWS RDS: Instance Identifier, Database Name, Username
Azure SQL: Server Name, Database Name, Username
Google Cloud SQL: Instance Connection Name, Database Name, Username
Google Cloud Storage: Bucket Name

### API implementation

To add an API, check the "Supported APIs" section in the documentation (check link above). If the API you want to access is supported, all you have to do is run the `visionkernel install datafeed API_goes_here`. This will prompt the user for the API key and then import the libraries and save the API to your system.

### Adding services

To add a service for charting, graphing, data analysis or any other reason check out the "Supported Services" section of our documentation (check link above). If the service you are looking for is supported, run `visionkernel install service service_goes_here`. To launch the service from the command line, run `visionkernel run service service_goes_here < example.txt`. This will feed the file into the service and display the desired results.  

### Thank you!

Thank you for downloading the VisionKernel CLI! If you have comments or suggestions feel free to reach out at visionkernel@gmail.com as we would love to hear from you. Please reach out if you have an API or service you would like added to VisionKernel, we will do our best to add support for it in a timely manner.

