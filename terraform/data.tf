data "aws_caller_identity" "current" {}

data "aws_region" "current" {}


data "terraform_remote_state" "gdpr_state" {
  backend = "s3"

  config = {
    bucket = var.bucket  
    key    = "terraform.tfstate"                  
    region = "eu-west-2"                 
  }
}


resource "null_resource" "combine_zips" {
  provisioner "local-exec" {
command = <<EOT
      mkdir -p ${path.module}/../temp_zip/src/utils
      cp ${path.module}/../src/utils/processing2.py ${path.module}/../temp_zip/
      cp ${path.module}/../src/utils/shared_variables.json ${path.module}/../temp_zip/src/utils/
      cd ${path.module}/../temp_zip && zip -r ${path.module}/../upload.zip *
      rm -rf ${path.module}/../temp_zip
    EOT
  }
}

resource "aws_s3_object" "lambda_code" {
  bucket = data.terraform_remote_state.gdpr_state.outputs.gdpr_input_bucket  
  key    = "upload.zip"
  source = "${path.module}/../upload.zip"
}

