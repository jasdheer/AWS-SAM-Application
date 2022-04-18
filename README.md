# [YouTube Video](https://www.youtube.com/watch?v=MipjLaTp5nA&ab_channel=BeABetterDev)

# [YouTube Video](https://www.youtube.com/watch?v=MipjLaTp5nA&ab_channel=BeABetterDev)

## Preparation
```
docker pull amazon/aws-sam-cli-build-image-python3.9
docker run -it amazon/aws-sam-cli-build-image-python3.9
```

```
yum install -y
yum install nano -y

aws --version
```

```
sam --version
```

## Deploying the stack on AWS

0
```
git clone https://<githubtoken>@github.com/mandheer-maan/AWS-SAM-Application.git
```

1
```
aws configure
AWS Access Key ID [None]: [Get Access Key ID from AWS]
AWS Secret Access Key [None]: [Get from AWS]
Default region name [None]: us-east-1
Default output format [None]: json

aws configure import --csv file://Downloads/test2_accessKeys.csv

```

2
 ```aws s3 mb s3://bucketname --region us-east-1```

3
Update ```samconfig.toml``` [change the required fields]
```
s3_bucket = "bucketname"   [get this from step 2]
```
3.1
```
cd AWS-SAM-Application/sam-app/
```

4
```apt-get -y install python3-pip```
```sam build```

5
```sam deploy```


Extras
==========
1 Local Lamnbda API testing
```sam local start-api```

2 Invoke Function: 
```sam local invoke```
