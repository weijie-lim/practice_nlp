# practice_nlp

<h2>Goal of the Project: </h2> 
Attempts to classify sections of legal texts to find out which label should it fall under.

<h2>Model Chosen</h2> 
Distilbert -- using 1 cycle policy

<h2>Categories:</h2>
There are 10 labels in total: ['amendments', 'counterparts', 'governing laws', 'government regulations', 'terminations', 'trade relations', 'trading activities', 'valid issuances', 'waivers', 'warranties']

<h2> Process: </h2>
The model utilises Distilbert trained over google-collab with additional GPU units (roughly 150 compute units) purchased. It has been found that 1 cycle fit produces the best results even whilst the training epochs are fewer.

Instead of using pickle, the model is here has been saved into my google drive and thereafter transferred over git large file transfer into github.

The web app utilitises a simple one page static text input submit which is then fed via jQuery/Ajax post method into the flask server where the saved model is extracted again to run the predictions. Two results are taken: the probability outcome for each label based on the input text as well as the most likely category the section of text should be classified as. The 2 results are put into json format via python's json.dump() and then returned to jQuery where the responses are then shot into the html element.

<h2> Deployment:</h2>
The deployment phase is a simple connection to heroku cloud via the github connection pipeline. Other possible ways would be creating a free Amazon EC2 instance. However, the downside of the free EC2 instance is that the IP address will be reset and hence the config file would have to been constantly update. Static EC instance address would have to be purchased with additional cost. Heroku cloud, on the other hand, provides a fixed domain name which allows the app to be accessed more easily without future configurations.

<h3> For Deployment disclaimer </h3>
As the heroku cloud deployment is unable to take the 240mb worth of pretrained model weights and details, I have only deployed a mockup of how the app should look like. For proper testing, do clone my github repo and run the Flask app on your local development server. Pictures will be added below to show how it should look like.


<h2> Data Shape </h2>
<img width="405" alt="image" src="https://user-images.githubusercontent.com/47061871/205058312-ba70d9b0-f52a-4d1c-b14c-6f8e118f8bcc.png">

We can see that the following have very little actual data as compared to the rest. Thus, I have chosen to use oversampling with replacement whilst applying substitution to words in each sample using synonyms. These substitutions are carried out at a fixed rate per number of 1N tokens in a sample.

- valid issuances             90
- government regulations      89
- trade relations             37
- trading activities          27


<h2> Examples of results run on local server </h2>
<h4> Empty Webpage </h4>
<img width="1094" alt="Screenshot 2022-12-01 at 8 46 52 PM" src="https://user-images.githubusercontent.com/47061871/205056929-5e800768-d0b3-442a-929e-02ef2e2fc1db.png">

<h4> Waiver Example </h4>
Example of a waiver example shows good testing results: Taken from https://legaltemplates.net/form/release-of-liability-waiver/
<img width="1088" alt="Screenshot 2022-12-01 at 8 46 16 PM" src="https://user-images.githubusercontent.com/47061871/205056981-4cecceda-80c0-4839-8eb2-88ff7673c4f7.png">

<img width="1094" alt="Screenshot 2022-12-01 at 8 46 41 PM" src="https://user-images.githubusercontent.com/47061871/205057003-da34bbda-d3b7-4b66-b251-c942db77b377.png">

The waiver example performs well possibly due to the fact that the initial training sample size is large enough such that oversampling does not affect the overfitting of the model by too much. Let us look at the smallest training sample given: "Trading activities"

<h4> Trading Activities Example </h4>
Example of Trading Activities clause that shows poor results: Taken from https://www.lawinsider.com/contracts/9JZAFsYwduH#securities-trading-activities

<img width="1099" alt="image" src="https://user-images.githubusercontent.com/47061871/205058046-4d4fa664-7dae-4326-bfb0-8143f016d42e.png">

<img width="1092" alt="image" src="https://user-images.githubusercontent.com/47061871/205058127-0cf37670-5673-4901-83f3-8cc7ed12a53a.png">


<h2> Possible Improvements to the Model </h2>
The model is able to perform well on the categories with larger sample size but overfits on the smaller categories as apparent in the results above. It is unable to properly classify the unseen data of smaller categories as a result. 


Further Experiments if time and GPU units are available:
- Improvement 1: Easiest way would be to get actual real life data such that the model is able to capture the differences.
- Improvement 2: Take the catgeory with a median amount of samples. Downsample the categories with a higher sample size than it and oversample the categories with a lower sample size. This would evenly spread out the data set to become more balanced.
- Improve 3: Utilise other techniques in upsampling the categories which are smaller in sample sizes i.e. contextual sentence generators, word generators, etc.

