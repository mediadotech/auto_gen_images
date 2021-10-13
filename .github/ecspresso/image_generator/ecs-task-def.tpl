{
  "containerDefinitions": [
    {
      "command": [],
      "cpu": 256,
      "environment": [
        {
          "name": "PYTHON_ENV",
          "value": "production"
        }
      ],
      "essential": true,
      "image": "${ECR_REPOSITORY_URI}:${GITHUB_SHA}",
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/grdev02-front_api-image_gen",
          "awslogs-region": "ap-northeast-1",
          "awslogs-stream-prefix": "image-generator"
        }
      },
      "memory": 512,
      "mountPoints": [],
      "name": "image-generator",
      "portMappings": [
        {
          "containerPort": 3000,
          "hostPort": 3000,
          "protocol": "tcp"
        }
      ],
      "volumesFrom": []
    }
  ],
  "cpu": "1024",
  "executionRoleArn": "arn:aws:iam::787337621160:role/grdev_front_api_ecs_execute_role",
  "family": "grdev02-front_api-image_gen",
  "memory": "2048",
  "networkMode": "awsvpc",
  "placementConstraints": [],
  "requiresCompatibilities": [
    "FARGATE"
  ],
  "taskRoleArn": "arn:aws:iam::787337621160:role/grdev_front_api_ecs_execute_role",
  "volumes": []
}
