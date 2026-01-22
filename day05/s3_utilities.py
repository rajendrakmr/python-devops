import boto3
 
client = boto3.client('s3') 
def show_bucket(client):
    s3_client = client.list_buckets() 
    # pdb.set_trace()
    for key, value in s3_client.items():
        print("=" * 80)
        print(f"Key: {key}")
        if isinstance(value, dict):
            for k, v in value.items():
                print('----')
                print(f"{k:<20} : {v}") 
        elif isinstance(value, list):
            for bucket in value: 
                print(f"{"Bucket Name":<20} : Created Date")  
                print(f"{bucket["Name"]:<20} : {bucket["CreationDate"]}") 
                print('-' * 30)
        # if value.items():
        #     



def create_bucket(client,bucket_name):
    response = client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-1',
        },
    ) 
    print(response)

create_bucket(client,"rk03126540")
show_bucket(client)