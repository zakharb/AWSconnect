<p align="center">
  <a href="https://www.linkedin.com/in/zakharb/microapi">
  <img src="img/logo.png" alt="logo" />
</p>

<p align="center">

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&pause=1000&color=ED7308&center=true&width=435&lines=Get+all+information+from+AWS;EC2+S3+SQS" alt="description" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.2-orange" height="20"/>
  <img src="https://img.shields.io/badge/python-3.11-orange" height="20"/>
  <img src="https://img.shields.io/badge/boto3-1.26-orange" height="20"/>
</p>


<p align="center">
  <img src="img/usage.gif" alt="usage" />
</p>


## :orange_square: Getting Started

[AWS Client](https://github.com/zakharb/awsconnect) is python utility that use boto3 library    
to get information about EC2 instances  
to put, get files from S3 buckets  
to send, receive messages from SQS  

### Installing

Clone the project
```
git clone git@github.com:zakharb/awsconnect.git
cd awsconnect
```

Install and activate virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

Install and run the package
```
python3 -m pip install -e .
python3 -m awsconnect
```

<p align="center">
  <img src="img/install.gif" alt="animated" />
</p>

## :orange_square: Run  

<p align="center">
  <img src="img/run.png" />
</p>

### Examples EC2   
Get information about instances in EC2  
```
python3 -m awsconnect ec2 
```  

### Examples S3   
Put files to S3 buckets  
```
python3 -m awsconnect s3 put --filename test.json --bucket test  
```  

Get files from S3 buckets  
```
python3 -m awsconnect s3 get --filename test.json --bucket test  
```  

### Examples SQS   
Send messages from SQS  
```
python3 -m awsconnect sqs send --queue test --filename example_sqs_messages.json
```  

Receive messages from SQS  
```
python3 -m awsconnect sqs receive --queue test
```  

## :orange_square: Versioning

Using [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/zakharb/awsconnect/tags). 

## :orange_square: Authors

* **Zakhar Bengart** - *Initial work* - [Ze](https://github.com/zakharb)

See also the list of [contributors](https://github.com/zakharb/awsconnect/contributors) who participated in this project.

## :orange_square: License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation - see the [LICENSE](LICENSE) file for details  