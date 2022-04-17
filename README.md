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

0
```
apt install git -y
git clone https://github.com/mandheer-maan/AWS-SAM-Application.git
```

1
```
aws configure
AWS Access Key ID [None]: [Get Access Key ID from AWS]
AWS Secret Access Key [None]: [Get from AWS]
Default region name [None]: us-east-1
Default output format [None]: json
```

2
 ```aws s3 mb s3://bucketname --region us-east-1```

3
Update ```samconfig.toml``` [change the required fields]
```
apt install nano -y
s3_bucket = "bucketname"   [get this from step 2]
```
3.1
```
cd AWS-SAM-Application/
```

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
