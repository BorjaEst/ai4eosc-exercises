"""Package to create dataset, build training and prediction pipelines.

This file should define or import all the functions needed to operate the
methods defined at ai4eosc_exercises/api.py. Complete the TODOs
with your own code or replace them importing your own functions.
For example:
```py
from your_module import your_function as predict
from your_module import your_function as training
```
"""
# TODO: add your imports here
import logging
from pathlib import Path
from ai4eosc_exercises import config

logger = logging.getLogger(__name__)
logger.setLevel(config.LOG_LEVEL)


def warm(**kwargs):
    """Main/public method to start up the model
    """
    pass


def predict(model_name, input_file, **options):
    """Main/public method to perform prediction
    """
    predict_result = [x for x in range(100)]
    return predict_result

def train(model_name, input_file, **options):
    """Main/public method to perform training
    """
    train_result = {'result': 'not implemented'}
    return train_result
