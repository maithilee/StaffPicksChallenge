# StaffPicksChallenge
1.  Clone this repository.
2.  To train the model, run command, 
      ```
      python buildModel.py
      ```
    To test the model, run command, 
      ```
      python test2.py <clip_id>
      ```
3. To run the Django web server, from your current working directory where this repo has been cloned, run the following command,
      ```
      python webserver/manage.py runserver
      ```
   You will be prompted to enter the clip_id. Enter it and press "View Results" to see the results
   
  PRE-REQUISITES for the project
  1.  Python3.x
  2.  gensim 3.5.0
  3.  nltk 3.3
      -     Under python prompt run the following commands
      ``` 
      import nltk 
      nltk.download('stopwords')
      ```
  4. Django 2.1
  
  
