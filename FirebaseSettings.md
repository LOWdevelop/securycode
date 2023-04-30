Documentation .

Welcome to Secury Code , this lib is for secury your code using Tokens.
This lib Will Authenticate token/key for give acess you application to you client.


1. Creating you clients data-base . 
to start you need one data-base , this lib use FireBase
  1.1 For your create one database using firebase follow this link ->  https://console.firebase.google.com/u/0/
  after login using you google account  , create you first project
  ![image](https://user-images.githubusercontent.com/132000523/235349739-393fe037-72eb-474c-b31a-bbb6d86ca9fa.png)
  
  1.2 Create you project name. and finish
  
  ![image](https://user-images.githubusercontent.com/132000523/235349863-71175648-e6f5-4a31-8068-50452cbfdea3.png)
  
  1.3 Selected Realtime Databse ->
  
  ![image](https://user-images.githubusercontent.com/132000523/235349995-5e3b8997-d996-4274-8986-b77109f1860a.png)
  
  1.4 Create.
  
  ![image](https://user-images.githubusercontent.com/132000523/235350031-ea679903-3915-49fc-9fce-bbc22f2036c8.png)
  
  1.5 Finish You database Creation.
  
  ![image](https://user-images.githubusercontent.com/132000523/235350066-5468778c-a976-4399-8c4a-1bf4c0459f9c.png)

  1.6 Change Rules to .
	
  
	{ 
	  "rules": {
	 
     "auth-keys": {
		 
       ".read": true,
			 
       "$user_id": {
			 
         "registered": {
				 
           ".write": true,
					 
           ".validate": "newData.isString() && newData.val().length > 5"
					 
        }
     	 }
     }
	 }
	}
	


      
  EXAMPLE  --->
  
  ![image](https://user-images.githubusercontent.com/132000523/235368402-60f8982b-89ed-483d-b2e4-9b9bfc3c20f7.png)
  ![image](https://user-images.githubusercontent.com/132000523/235368470-6d716187-9911-4c8e-97c0-55c53ce228a7.png)

1.7 and use this template for create new user

	
		"auth-keys": {
			"username": {
				"key": "create-one-key-using-this-format",
				"name": "username",
				"registered": ""
			  }
		  }
	
	
EXAMPLE --->

![image](https://user-images.githubusercontent.com/132000523/235369125-1c83079e-ace1-435f-b0fd-e5038ed084e7.png)
