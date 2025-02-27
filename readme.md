# GDPR Obfuscator Project

## Overview

The GDPR Obfuscator Project is a general-purpose tool designed to process data ingested to AWS and intercept personally identifiable information (PII). This project aims to comply with GDPR regulations by anonymizing sensitive data in bulk data analysis scenarios, ensuring that all information stored does not identify individuals.

## Context

This tool is intended for the **Skills Bootcamp: Software Developer/Coding Skills Graduates** in a **Data Engineering** context. The primary goal is to create a library module that obfuscates PII from CSV files stored in AWS S3.

## Assumptions and Prerequisites

- Data is stored in CSV format in S3.
- Fields containing GDPR-sensitive data will be known and provided in advance.
- Data records will include a primary key.

## High-Level Desired Outcome

The tool will be provided with the S3 location of a file containing sensitive information and the names of the affected fields. It will create a new file or byte stream object that contains an exact copy of the input file but with the sensitive data replaced by obfuscated strings. The calling procedure will handle saving the output to its destination.

### Example Input

The tool will be invoked with a JSON string containing:

```json
{"bucket_name": "bucket_name",
"s3_file_path": "data.csv",
"pii_fields": ["Name", "Email Address"]}
```

### Example Input CSV File

```plaintext
User ID,Name,Graduation Date,Email Address
1001,Alice Johnson,2022-05-15,alice.johnson1001@example.com
1002,Bob Smith,2023-06-20,bob.smith1002@example.com
1003,Carol Davis,2022-08-30,carol.davis1003@example.com
```

### Example Output

The output will be a byte stream representation of a file that looks like this:

```plaintext
User ID,Name,Graduation Date,Email Address
1001,***,2022-05-15,***
1002,***,2023-06-20,***
1003,***,2022-08-30,***
```

## Non-Functional Requirements

- The tool should be written in Python, PEP-8 compliant, and tested for security vulnerabilities.
- The code must include documentation.
- No credentials should be recorded in the code.
- The total size of the module should not exceed the memory limits for Python Lambda dependencies.

## Performance Criteria

- The tool should handle files of up to 1MB with a runtime of less than 1 minute.

## Possible Extensions

The MVP could be extended to support other file formats, primarily JSON and Parquet, while maintaining compatibility with the input formats.

## Tech Stack

- **Programming Language**: Python
- **AWS SDK**: Boto3
- **Testing Tools**: Pytest
- **Deployment**: AWS Lambda

# Usage

Although the tool is intended to function as a library, demonstration of its use can be done through command-line invocation.

This project is designed to run on Python 3.11.1

# Opening a Free AWS Account

Amazon Web Services (AWS) offers a free tier that allows you to access various services without incurring costs for a limited period. Follow these steps to create your free AWS account:

## Step 1: Go to the AWS Free Tier Page

1. Open your web browser and navigate to the [AWS Free Tier page](https://aws.amazon.com/free/).

## Step 2: Click on "Create a Free Account"

2. Click on the **Create a Free Account** button located in the center of the page.

# Forking and Cloning the Repository

Before setting up AWS, you need to fork and clone the repository to your local machine. Follow these steps:


## Step 1: Fork the GDPR Repository

1. **Log in to GitHub**
   - Go to [GitHub](https://github.com) and log in to your account.

2. **Navigate to the GDPR Repository**
   - Visit the GDPR repository by going to this URL: [https://github.com/A-Waterhouse/GDPR](https://github.com/A-Waterhouse/GDPR).

3. **Fork the Repository**
   - On the repository page, click the "Fork" button in the top-right corner and the click `Create fork`. This will create a copy of the `GDPR` repository under your GitHub account.

## Step 2: Clone the Forked GDPR Repository

1. **Go to Your Forked GDPR Repository**
   - After forking, navigate to your forked copy of the repository, which will now be under your GitHub account.

2. **Copy the Repository URL**
   - On your forked repository page, click the green "Code" button, and copy the HTTPS or SSH URL.
     - **HTTPS URL**: `https://github.com/your-username/GDPR.git`
     - **SSH URL**: `git@github.com:your-username/GDPR.git`

3. **Open a Terminal (Command Line)**
   - On your local machine, open a terminal or command prompt.

4. **Run the Clone Command**
   - Use the `git clone` command followed by the URL you copied. For example, if you’re using HTTPS:

   ```bash
   git clone https://github.com/your-username/GDPR.git
   ```

   Replace `your-username` with your GitHub username.

5. **Navigate into the Cloned Directory**
   - After cloning, navigate into the repository’s folder using the `cd` command:

   ```bash
   cd GDPR
   ```

# Local machine setup

Run the command 

```bash
make requirements
```
in the terminal.

This will install all the libraries needed to run the project.

# Setting up AWS CLI
### Step 1
Run command 
```bash
aws --version
```
in the terminal

This is to see if you already have AWS CLI installed. you should see something like this `aws-cli/2.15.8 Python/3.11.6 Linux/5.15.153.1-microsoft-standard-WSL2 exe/x86_64.ubuntu.22 prompt/off` in the terminal if you have it installed already.

If not follow the instructions <a href="https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html" target="_blank">here</a> to install the AWS CLI.


### Step 2
### logging in to AWS using the CLI

Run the command 
```bash
aws configure
``` 
in the terminal.

   -  Go to the AWS website 

You will have been prompted in the terminal to enter your `AWS Access Key ID` which can be found in the security credentials 
section of the AWS website under your username in the top right. 

Select `Create Access Key` to create one and follow the instructions which follow.

Click `Download .csv file` open it so you can view the ID and Key and save it locally to your PC, being sure
to follow `Access key best practices` which are displayed on the page.

The keys will be used throughout the project and are essential.

### Step 3
enter the information from the downloaded .csv file (`rootkey.csv`) into the terminal following the prompts.

the next 2 prompts should be -
   - `eu-west-2` for the `Default Region Name` 
   - `json` for the `Default output format`

Now you have the access rights to control your AWS account from the terminal or within python scripts.

## Setting Up AWS Access Keys in GitHub

To enable the project to interact with AWS services, you need to configure AWS access keys in your GitHub repository. Follow these steps to set up the necessary secrets:

1. **Navigate to the GDPR Repository:**
   - Go to the GitHub website and open the repository. 
   - `github.com/your-username/GDPR.git`

2. **Access Repository Settings:**
   - Click on the `Settings` tab located at the top of your repository page.

3. **Select Secrets and Variables:**
   - On the left sidebar, click on `Secrets and variables`.
   - Then click on `Actions` to manage secrets for GitHub Actions.

4. **Add 2 New Repository Secrets:**
   - Click on the `New repository secret` button.

5. **Enter the Secrets:**
  
----------------------------------------------------------------
   - In the `Name` field, enter `AWS_ACCESS_KEY`.
   - In the `Value` field, paste your Access Key ID from the `rootkey.csv` made earlier.
   - Click on `Add secret`.
----------------------------------------------------------------
   - Repeat the process to create another secret:
   - In the `Name` field, enter `AWS_SECRET`.
   - In the `Value` field, paste your Secret Access Key from the `rootkey.csv` made earlier.
   - Click on `Add secret`.

Once these secrets are set up, your GitHub Actions workflows will have the necessary permissions to access AWS resources securely.


### Creating an S3 Bucket for Terraform State Storage

Before running Terraform, you need to create an S3 bucket to store the Terraform state file. You can create the bucket using the terminal by running the following command:

```bash
make bucket
```
You will be asked to input a unique bucket name in the terminal.

If you get error during bucket creation it may be because that bucket name is taken by another user, unique 
bucket names must be used. see <a href=" https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html" target="_blank">here</a> for more information.

**Note**:  
- Ensure you have the correct permissions to create S3 buckets in your AWS account.  
- This bucket will be used exclusively to store the Terraform state.

## Automatic Invocation

### Step 1
Run the command 



```bash 
make data
```
In the terminal.

This will use the tool provided `GDPR/src/data/create_data.py` to create a .csv file named `dummy_data_large.csv` in `GDPR/src/data` which contains over 1MB of fake user data.

### Step 2
It is now essential that you push to github which will trigger actions and create the necessary infrastructure. check your github actions tab (in your forked GDPR repo on the github website) to make sure the pipeline is complete before proceeding further, you should see a green tick next to the workflow run which is named the same as the commit message from the push.

You will now have 4 buckets in total in your AWS account which can be viewed in the AWS console by searching in the top left for `S3`, 
after clicking on `S3` you should be able to see the buckets, 1 with the name which you entered when you ran the `make bucket` command and 3 others which have been made
automatically, the 3 others are prefixed with the titles gdpr-input-, gdpr-invocation- and gdpr-processed- referred to from now on as input bucket, invocation bucket and processed bucket respectively.
The numbers after the titles are time/date stamps to ensure that they are unique names.
The user does not need to worry about naming conventions, this is done automatically.

----------------------------------------------------------------

### Step 3
run the command 
```bash 
make upload
``` 
In the terminal.

This automatically uploads a time/date stamped version of `dummy_data_large.csv` file to the input bucket within the AWS system.
### Step 4
To invoke the function run the command 
```bash 
make invoke
```
In the terminal.
This creates a .json file (containing the bucket name, file to obfuscate and which fields to obfuscate), uploads it to the invocation bucket
 and invokes the lambda function on the AWS system.

The PII fields get obfuscated and a new time/date stamped file is generated and uploaded to the processed bucket on the AWS system.

All other files are removed from the other buckets and you will be left with just the time/date stamped obfuscated file(s) in the processed bucket.

You can now download the obfuscated file from the bucket and view the results.

--------------------------------

the default PII fields to be obfuscated 
are `["Name", "Email Address", "Sex", "DOB"]` 
   -  these can be changed in **line 6** of `create_json_payload.py` in `GDPR/src/utils`, the fields are case sensitive and must match existing fields in the `dummy_data_large.csv` file.


If the PII fields are changed run `make data` (to make another csv file), `make upload` (to put it in the correct bucket) and `make invoke` (to make the json file with updated PII fields and trigger the lambda) in that order
## Manual Invocation

Alternatively you can use your own `.csv` file using the same format as the `Example Input CSV file` (as seen at start of this readme) and upload it manually to the `input` bucket on the aws website or via the AWS CLI.

Once this is done you can invoke the lambda function by uploading a `.json` file to the `invocation` bucket in the format mentioned above in the `Example input` (as seen at start of this readme).

Make sure the file name, bucket name and PII fields are correct as this is case sensitive.

## Viewing results

   -  Go to AWS website

there will now be a file in the `processed` bucket on the AWS website with the same filename as the original file uploaded to the `input` bucket with the selected PII fields data replaced with `***`.

   -  The `***` can be replaced with any characters on 
   -  **line 97** of the file `src/utils/processing2.py`

If the `***` is changed you must again push to github to update the lambda function.

all data in the `input` and `invocation` buckets will be erased once a .json file is uploaded to the invocation bucket.

To run the lambda successfully there must be no data in the `input` and `invocation` buckets before any data is added either manually or automatically with use of the tools.

There are also detailed log messages which can be viewed on the AWS website, at the top of the console use the search tool for the word `cloudwatch`, select it and then click log groups on the left, once here you will see a log group
named `/aws/lambda/my_lambda_function` click on that and then in there you will see a date stamped log file which can be viewed within the browser if you so wish.

----------------------------------------------------------------


## Cleaning up your AWS console automatically

It is important that the following is done in the correct order.

### Step 1:

Go into the git hub actions menu, on the github website, this is where you can see the workflows that have been ran, on the left hand side you should see a work flow called `Destroy Infrastructure GDPR` you should click on this to open a `workflow runs` menu and to the right of `This workflow has a workflow_dispatch event trigger.` there is a drop down box, if you click on that and press the green `Run workflow` button you will destroy all the resources which were required for this project but leaving your existing AWS resources in place.

### Step 2:

The bucket that was created when 
```bash
make bucket
```
which was used to store a terraform state file can now be deleted along with its contents. I suggest that this be done in the AWS console on the website.

----------------------------------------------------------------

Now your AWS account is back to how it was before this project was created.



# Future enhancements

   -  Support for other input file formats such as json and parquet
   -  convert to library format
   -  Make project compatible with EC2 and ECS systems
   