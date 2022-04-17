# AWS-SAM-Application

# [YouTube Video](https://www.youtube.com/watch?v=MipjLaTp5nA&ab_channel=BeABetterDev)

## Preparation
```
docker pull ubuntu:21.10
docker run -it ubuntu:21.10
```

```
apt-get update -y
apt-get install awscli -y
aws --version
```

```
apt-get install wget -y
wget https://github.com/aws/aws-sam-cli/releases/download/v1.46.0/aws-sam-cli-linux-x86_64.zip
apt-get install unzip -y
unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
./sam-installation/install
sam --version
```

## Deploying the stack on AWS

1
```aws confiure``` ...

2
 ```s3://[BUCKETNAME] --region us-east-1```

3
Update ```samconfig.toml``` with the new bucket name provided in step 2

4
```sam build```

5
```sam deploy```


Extras
==========
1 Local Lamnbda API testing
```sam local start-api```

2 Invoke Function: 
```sam local invoke```
