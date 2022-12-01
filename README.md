# practice_nlp

<h2>Goal of the Project: </h2> 
Attempts to classify sections of legal texts to find out which label should it fall under.

<h2>Model Chosen</h2> 
Distilbert -- using 1 cycle policy

<h2> Heroku App Link for Sample of how the App should work (if model size / memory can be handled / does not explode) </h2>
Click on Link: https://limweijie-nlp-legal-classifier.herokuapp.com/ 

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
Original Data Size: 

<img width="304" alt="image" src="https://user-images.githubusercontent.com/47061871/205100265-912989fd-0c0f-4db9-9b6d-97e41499a8ce.png">

Training Data Size: (70% of each category taken into the training)

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
Example of a waiver example shows good testing results.

Refer to: https://legaltemplates.net/form/release-of-liability-waiver/

<img width="1088" alt="Screenshot 2022-12-01 at 8 46 16 PM" src="https://user-images.githubusercontent.com/47061871/205056981-4cecceda-80c0-4839-8eb2-88ff7673c4f7.png">

<img width="1094" alt="Screenshot 2022-12-01 at 8 46 41 PM" src="https://user-images.githubusercontent.com/47061871/205057003-da34bbda-d3b7-4b66-b251-c942db77b377.png">

The waiver example performs well possibly due to the fact that the initial training sample size is large enough such that oversampling does not affect the overfitting of the model by too much. Let us look at the smallest training sample given: "Trading activities"

<h4> Amendments Example </h4>
I attempt to classify a sample amendments clause with the following results. The results seem good as it is able to rightfully pick out with a high degree of accuracy.

Refer to: https://www.lawinsider.com/clause/amendment

<img width="1052" alt="image" src="https://user-images.githubusercontent.com/47061871/205096724-b5bf91b0-3c8b-4bfe-a02d-87ff307b2e62.png">

<img width="973" alt="image" src="https://user-images.githubusercontent.com/47061871/205096983-28f631e0-282e-4732-a9d6-e68a80fc67d2.png">


<h4> Warranties Example </h4>
I attempt to classify a sample warranties clause with the following results. The results seem good as it is able to rightfully pick out with a high degree of accuracy. Do note that the actual real training data (70%-30% train-test split stratified across all categories) was only 425 samples, which I then later oversampled to 8500 samples.

Refer to: https://www.lawinsider.com/clause/general-warranty

<img width="1047" alt="image" src="https://user-images.githubusercontent.com/47061871/205097549-a7f74b6a-85bf-4382-882d-dd8b727eff71.png">

<img width="1044" alt="image" src="https://user-images.githubusercontent.com/47061871/205098086-370d1d3a-bd43-4689-ad38-548bc8094490.png">


<h4> Government Regulations Example </h4>
I attempt to classify a sample government regulations clause with the following results. The original training data set, which is 70% of the total data set, only contained 89 samples of this specific clause. I have then oversampled it to approximately 8722 samples to balance it out. We can see that the lack of data has started to degrade the performance whereby the unseen government regulations clause was misclassified by the model.

Refer to: https://www.lawinsider.com/clause/government-requirements

<img width="1050" alt="image" src="https://user-images.githubusercontent.com/47061871/205099338-ea407b2c-db49-4e26-b496-fad11f4513bd.png">

<img width="975" alt="image" src="https://user-images.githubusercontent.com/47061871/205099465-2f475635-a546-4cc0-a701-91e31711a9f8.png">


<h4> Trading Activities Example </h4>
Example of Trading Activities clause that shows poor results. The original data training size was 27 samples which was then oversampled to 8748 samples. The oversampling probably caused an overfitting that made it too specific to the original 27 samples provided.

Refer to: https://www.lawinsider.com/contracts/9JZAFsYwduH#securities-trading-activities

<img width="1099" alt="image" src="https://user-images.githubusercontent.com/47061871/205058046-4d4fa664-7dae-4326-bfb0-8143f016d42e.png">

<img width="1092" alt="image" src="https://user-images.githubusercontent.com/47061871/205058127-0cf37670-5673-4901-83f3-8cc7ed12a53a.png">

<h2> Possible Improvements to the Model </h2>
The model is able to perform well on the categories with larger sample size but overfits on the smaller categories as apparent in the results above. It is unable to properly classify the unseen data of smaller categories as a result. 


Further Experiments if time and GPU units are available:
- Improvement 1: Easiest way would be to get actual real life data such that the model is able to capture the differences.
- Improvement 2: Take the catgeory with a median amount of samples. Downsample the categories with a higher sample size than it and oversample the categories with a lower sample size. This would evenly spread out the data set to become more balanced.
- Improve 3: Utilise other techniques in upsampling the categories which are smaller in sample sizes i.e. contextual sentence generators, word generators, etc.

