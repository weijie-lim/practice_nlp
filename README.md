# practice_nlp

<h2>Goal of the Project: </h2> 
Attempts to classify sections of legal texts to find out which label should it fall under.

<h2>Categories:</h2>
There are 10 labels in total: ['amendments', 'counterparts', 'governing laws', 'government regulations', 'terminations', 'trade relations', 'trading activities', 'valid issuances', 'waivers', 'warranties']

<h2> Process: </h2>
The model utilises Distilbert trained over google-collab with additional GPU units (roughly 150 compute units) purchased. It has been found that 1 cycle fit produces the best results even whilst the training epochs are fewer.

Instead of using pickle, the model is here has been saved into my google drive and thereafter transferred over git large file transfer into github. 

The web app utilitises a simple one page static text input submit which is then fed via jQuery/Ajax post method into the flask server where the saved model is extracted again to run the predictions. Two results are taken: the probability outcome for each label based on the input text as well as the most likely category the section of text should be classified as. The 2 results are put into json format via python's json.dump() and then returned to jQuery where the responses are then shot into the html element.

<h2> Deployment:</h2>
The deployment phase is a simple connection to heroku cloud via the github connection pipeline. Other possible ways would be creating a free Amazon EC2 instance. However, the downside of the free EC2 instance is that the IP address will be reset and hence the config file would have to been constantly update. Static EC instance address would have to be purchased with additional cost. Heroku cloud, on the other hand, provides a fixed domain name which allows the app to be accessed more easily without future configurations.
