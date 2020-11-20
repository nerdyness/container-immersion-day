from flask import Flask
import os
import boto3

def get_param(param_name):
  client_ssm = boto3.client("ssm")
  try:
      param_details = client_ssm.get_parameters(
          Names=[
              param_name,
          ],
          WithDecryption=True
      )
      return param_details["Parameters"][0]["Value"]
  except Exception as e:
      print("Encountered an error fetching {} from SSM.".format(param_name))
      print("Error: {}".format(e, exc_info=True))

app = Flask(__name__)

@app.route('/')
def greeting():
    return get_param(os.environ['GREETING'])
