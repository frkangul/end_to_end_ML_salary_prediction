# GITHUB LINK: https://github.com/frkangul/udacity_course3
# Notes on Project Requirements:
## git and dvc
* In "screenshots" folder, there are continuous_integration.png and dvcdag.png. 
## Model building
* Create a machine learning model: On CLI, one can run "python src/train_model.py" and get model, encoder, lb, and performance metrics.
* Write unit tests: On CLI, one can run "pytest src/model_test.py -vv" and get the unit test results for ML modelling
* Write a function that computes model metrics on slices of the data: In "data" folder, there is sliced_output.txt that shows the performance of ML model on sliced data.
* Write a model card: it is model_card.md file.
## API Creation
* Create a REST API: api.py file is used to generate FastAPI. On CLI, one can run "uvicorn api:app --reload" to start API. In "screenshots" folder, there is example.png which shows example for POST method in API.
* Create tests for an API:  api_test.py file is used to test API. On CLI, one can run "pytest api_test.py -vv" to see the result of test. 
## API Deployment
* Deploy an app to Heroku: In "screenshots" folder, there are live_get.png and continuous_deloyment.png files.
* Query live API: In "screenshots" folder, there is live_post.png file.
