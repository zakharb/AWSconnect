
![logo](https://github.com/bengart-ze/ziem/blob/8dad879ec60f847391e0cbcdc3caede0983e3701/logo.png)

## AWS Client  
### Utility for EC2 and S3 operations  


![](https://img.shields.io/badge/version-1.0-blue)
![](https://img.shields.io/badge/python-3.9-blue)

## Содержание  
[Important info](#important_info)  
[Install](#install)  
[Run](#install)  
[Usage](#usage)  


<a name="important_info"/>

## Important info  
</a>  

> AWS Client is python utility that use boto3 library    
> Put privacy key to `conf` dir and set credentials  

<a name="install"/>  

- Download installation package and install via `pip`  
```
python3 -m pip install awsclient-XX-py3-none-any.whl  
```

- Or clone repo and install  
```
python3 -m pip install -e .
```

<a name="run"/>  

- Start with some help  
```
└─$ python -m awsclient -h                 
   __    _    _  ___   ___  __    ____  ____  _  _  ____ 
  /__\  ( \/\/ )/ __) / __)(  )  (_  _)( ___)( \( )(_  _)
 /(__)\  )    ( \__ \( (__  )(__  _)(_  )__)  )  (   )(  
(__)(__)(__/\__)(___/ \___)(____)(____)(____)(_)\_) (__) 

usage: __main__.py [-h] {getinfo,config} ...

positional arguments:
  {getinfo,config}
    getinfo         Get info from EC2
    config          Set AWS connection config

optional arguments:
  -h, --help        show this help message and exit
```

<a name="usage"/>  

- Set configuration to connect ASW instances  
```
python3 -m awsclient config
```
- Get info from EC2 (you can save info to S3 or local file)  
```
python3 -m awsclient getinfo -h
```
