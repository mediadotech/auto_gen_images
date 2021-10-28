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
      "targetGroupArn": "arn:aws:elasticloadbalancing:ap-northeast-1:787337621160:targetgroup/grdev-front-api-new-igen/f636ac0c7dd7f21e"
    },
    {
      "containerName": "image-generator",
      "containerPort": 3000,
      "targetGroupArn": "arn:aws:elasticloadbalancing:ap-northeast-1:787337621160:targetgroup/grdev-front-api-new-igen-nlb/58b93ab5cd7ec762"
    }
  ],
  "networkConfiguration": {
    "awsvpcConfiguration": {
      "assignPublicIp": "ENABLED",
      "securityGroups": [
        "sg-0bafd4a724c64a17a"
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
