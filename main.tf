provider "aws" {
  region                   = "us-east-1"
  shared_credentials_files = ["~/.aws/credentials"]
  profile                  = "default"
}

resource "aws_lambda_function" "sensor_reader" {
  filename         = "lambda_function.zip"
  function_name    = "SensorReader"
  role             = "arn:aws:iam::481311808619:role/LabRole" 
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.12"
  source_code_hash = filebase64sha256("lambda_function.zip")
}