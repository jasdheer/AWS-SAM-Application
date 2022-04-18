# [YouTube Video](https://www.youtube.com/watch?v=MipjLaTp5nA&ab_channel=BeABetterDev)

## Preparation of Docker file
```
FROM amazon/aws-sam-cli-build-image-python3.9
RUN yum -y update && \
    yum -y install nano && \
    yum clean all

RUN aws --version && \
    sam --version

RUN git clone https://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@github.com/mandheer-maan/AWS-SAM-Application.git


RUN aws configure set aws_access_key_id "AKIAX2ZZMHSLAQ2CSAJ2" --profile jasdheer && \
    aws configure set aws_secret_access_key "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" --profile jasdheer && \
    aws configure set region "us-east-1" --profile jasdheer && \
    aws configure set output "json" --profile jasdheer

RUN aws configure list


RUN aws s3 mb s3://mynews4bucket-new3 --region us-east-1

RUN cd AWS-SAM-Application/sam-app/

RUN sam build 
RUN sam deploy

ENV HOME /root

WORKDIR /root

```

## Deploying the stack on AWS

**1.**
```
 git clone https://github.com/mandheer-maan/AWS-SAM-Application.git
```

**2.**
```
aws configure
AWS Access Key ID [None]: [Get Access Key ID from AWS]
AWS Secret Access Key [None]: [Get from AWS]
Default region name [None]: us-east-1
Default output format [None]: json

aws configure import --csv file://Downloads/test2_accessKeys.csv

```

**3.**

 ```aws s3 mb s3://bucketname --region us-east-1```

**4.**

Update ```samconfig.toml``` [change the required fields]
```
s3_bucket = "bucketname"   [get this from step 2]
```

**5.**

```
cd AWS-SAM-Application/sam-app/
```

**6.**

```sam build```

**7.**

```sam deploy```


Extras
=======
1. Local Lamnbda API testing
```sam local start-api```

2. Invoke Function: 
```sam local invoke```
