# VisionKernel CLI
### BETA Version
### VisionKernel Corp.
### https://nicksimpkins.github.io/visionkernel_cli/

### REQUIRED: Python 3.9.0 or later

<div align="center">
![GitHub Repo stars](https://img.shields.io/github/stars/nicksimpkins/visionkernel_cli)
![GitHub forks](https://img.shields.io/github/forks/nicksimpkins/visionkernel_cli)
![GitHub watchers](https://img.shields.io/github/watchers/nicksimpkins/visionkernel_cli)
![GitHub License](https://img.shields.io/github/license/nicksimpkins/visionkernel_cli)
![GitHub issues](https://img.shields.io/github/issues/nicksimpkins/visionkernel_cli)
</div>

## About

VisionKernel is a data management and analysis tool that allows easy access to cloud databases. Say goodbye to using excel for data management. This open-source CLI tool allows for the rapid processing and analysis of all your data, and makes it easy to upload your excel files into your cloud databases.

### Getting Started

The VisionKernel CLI allows you to connect to a cloud database from your preferred provider. Adding a database is as easy as running the `visionkernel add cloud-database` command and following the prompts. Once a database is added, you are able to access the previously setup tables and export data to them.


### Exporting data

To export data, simply connect to the database and select which Excel files you want to upload. If files are in CSV format, use our conversion tool to convert to Excel before upload. Our program also allows for the creation of tables in your cloud database from the command line.

### Converting data -- DONE

Converting data is simple with our `convert` option. Easily convert a file such as .txt, .xml, .json, .csv or .xls into a different supported file type. The convert feature allows for the quick conversion of data into a more readable or preferred type. Synatax is `python main.py convert example.csv name_of_new_file.xlxs`.

### Connecting Cloud Database -- DONE (AWS Support)

To connect to your cloud database you will need certain information that is unique for every database and every cloud provider. We currently offer AWS support; to connect to a cloud database run `python main.py aws` and follow the prompts.
AWS RDS: Instance Identifier, Database Name, Username, Password, Port


### API implementation

To add an API, check the "Supported APIs" section in the documentation (check link above). If the API you want to access is supported, all you have to do is run the `visionkernel install datafeed API_goes_here`. This will prompt the user for the API key and then import the libraries and save the API to your system.

### Adding services

To add a service for charting, graphing, data analysis or any other reason check out the "Supported Services" section of our documentation (check link above). If the service you are looking for is supported, run `visionkernel install service service_goes_here`. To launch the service from the command line, run `visionkernel run service service_goes_here < example.txt`. This will feed the file into the service and display the desired results.  

### Thank you!

Thank you for downloading the VisionKernel CLI! If you have comments or suggestions feel free to reach out at visionkernel@gmail.com as we would love to hear from you. Please reach out if you have an API or service you would like added to VisionKernel, we will do our best to add support for it in a timely manner.

