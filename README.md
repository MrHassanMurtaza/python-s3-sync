# python-s3-sync

Boto3 doesn't support AWS S3 Sync commands therefore we can use this script to make use of AWS CLI to do s3 sync.

### Dependencies
- Make sure the AWS CLI is installed on the system.
- Use constants.py to supply AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_DEFAULT_REGION.

### Running the script

- Get help
`python main.py -h`

- Sync the two directories:
`python main.py <source_directory> <destination_directory>

### Motivation
- The script can be used to create API using Flask etc.