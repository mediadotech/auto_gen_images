{
  "createdBy": "arn:aws:iam::787337621160:user/kazunori_tsuno",
  "deploymentConfiguration": {
    "maximumPercent": 200,
    "minimumHealthyPercent": 100
  },
  "desiredCount": ${DESIRED_COUNT},
  "enableECSManagedTags": false,
  "healthCheckGracePeriodSeconds": 0,
  "launchType": "FARGATE",
  "loadBalancers": [
    {
      "containerName": "image-generator",
      "containerPort": 3000,
      "targetGroupArn": "arn:aws:elasticloadbalancing:ap-northeast-1:787337621160:targetgroup/grdev-front-api-image-gen/5e0451e306cd5ce0"
    }
  ],
  "networkConfiguration": {
    "awsvpcConfiguration": {
      "assignPublicIp": "ENABLED",
      "securityGroups": [
        "sg-0d1f9e9d40da9967e"
      ],
      "subnets": [
        "subnet-043d469bf49616c60",
        "subnet-0aedebd5407507b49"
      ]
    }
  },
  "placementConstraints": [],
  "placementStrategy": [],
  "platformVersion": "LATEST",
  "schedulingStrategy": "REPLICA",
  "serviceRegistries": []
}
