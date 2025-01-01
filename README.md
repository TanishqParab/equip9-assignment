Hello Team,
My name is Tanishq Parab 
I’m assigned a task  as per your requirement for Cloud Engineer position at Equip9 Pvt. Ltd. ************************************************************************************************************************************************************

Task Details :-
Part 1: HTTP Service
Develop an HTTP service in any programming language of your choice. The service should expose the following endpoint: Endpoint: GET http://IP:PORT/list-bucket-content/
● Functionality:
○ This endpoint returns the content of an S3 bucket for the specified path.
○ If no path is specified, the top-level content of the bucket is returned.
○ The response should be in JSON format.
Part 2: Terraform Deployment
Write a Terraform layout to provision AWS infrastructure and deploy the HTTP service created in Part 1.
● The Terraform code should:
1.	Create and configure the necessary AWS resources.
2.	Deploy the service to AWS (e.g., using EC2, ECS, Lambda, or any other appropriate AWS service).
________________________________________
Here the steps I used to accomplish this Task
steps :
1.	First create AWS account.
2.	Create IAM User and permission or group policies which required for EC2 and S3 Bucket.
3.	After that generate Access key and Secret Access key of this IAM user.
4.	After that download AWS CLI and Terraform extension.
5.	Setup AWS CLI and Terraform.
6.	After that provide AWS Authentication on your local Machine by using CMD.
7.	After environment completly setup moving toward assignment 1st task.
8.	So, open code editor like VScode.
9.	Create one folder for assignment first Part.
10.	In this folder add DATA-FOLDERS which you want to upload in S3 Bucket.
11.	Now create an s3 bucket from the aws console
12.	Now upload the directories and files (objects) to the s3 bucket from the console

  
S3 Bucket:

![image](https://github.com/user-attachments/assets/f53aef9d-3f67-4d01-a7c3-7e3fb37444aa)


13.	Now to call and retrieve data form s3 bucket used following steps :
14.	create python file app.py.
15.	befor that install python related packages like (Boto3, flask, jsionify, dotenv)
16.	for this use command ( pip install package-name ).
17.	after that write python code. In this file app.py import all packages like (Boto3, flask, jsionify, dotenv).
18.	after that define and configure S3 bucket details like Bucket-name, Access-key, Secrete-Access-key, region.).
19.	After that write a python function to call GET method which display or return S3 bucket data in jsion format.
20.	After that, At the end of this file define the PORT in which you wan to run your application app.py .

 ![image](https://github.com/user-attachments/assets/7854949a-427a-4a26-a89c-e79fc2640028)

21.	after that run app.py file it provides you api to retrieve data using port .
 	 
![image](https://github.com/user-attachments/assets/f924f414-8fb7-4355-aed8-aee3b08b76ed)

22.	After that used curl command to get data on terminal. ( curl http://127..0.0.1:5000/list-bucket-content )


23.	After running this API on browser it will provide you output in json format.
![image](https://github.com/user-attachments/assets/db12d004-ea09-4aa0-ba00-d768401562cd)

24.	if you want to explore bucket content again edit this api and run on browser.
![image](https://github.com/user-attachments/assets/d31ce75e-3e78-4719-babc-5b608553de57)

S3 Bucket Objects:

![image](https://github.com/user-attachments/assets/6255ca4e-e4a0-4dfa-a75f-299428dddef3)


________________________________________






25.	Now its time to complete 2nd task.
26.	for this task create folder 
27.	In this folder add your terraform files main.tf 
28.	now first open git bash and generate ssh public key (developer-key) cy using ssh-keygen command.
29.	after that copy developer-key and developer-key.pub and in 2nd-Task folder.
30.	after that for aws configuration use aws configure command in the  
31.	after that create files like ec2_userdata.sh, main.tf, output.tf and variable.tf.
32.	So, in variables.tf file define all variables.
33.	after that in main.tf file create security group in this open 5000 port on both inbound and outbound rule.
34.	after that write a terraform code to create ec2 instance in this provide path of file ec2_userdata.sh for user_data keyword which you was declare in aws_instance.
35.	after that in ec2_userdata.sh file write all linux command and shell script for installing packages in ec2-instance like python3, boto3, flask, etc.
36.	after successfully written terraform and python code . run the terraform commands to deploy virtual machine.
37.	terraform command already mentioned in first task copy it.
38.	when successfully deploying VM it gives you public ip address.
terraform-code 

main.tf

 ![image](https://github.com/user-attachments/assets/415f5454-3f3a-4f5a-a282-bd83e9c202d5)


Variables.tf

 ![image](https://github.com/user-attachments/assets/356b84c2-5e57-4b32-82b9-3d82ad0cbc33)

HTTP-server instance

![image](https://github.com/user-attachments/assets/8a40be98-4e04-43b8-acfe-9b9c7cd5aded)

 
39.	After that copy this ip address and paste it with application port number on browser.( 13.233.78.36:5000).
40.	After that it will return similar output of first task in jsion format.

Ec2-ip-output
 
![image](https://github.com/user-attachments/assets/cba6f8da-971c-4b05-9707-6d9c8e4796fa)
 
________________________________________

Video demonstration of the Task
https://drive.google.com/file/d/1i-zfrrP8dunL7P4CrI-zbY_8RiwXpdMq/view?usp=sharing
The task is completed successfully.
Thanks…..
________________________________________
