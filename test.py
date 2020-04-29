import pandas as pd
submit = pd.read_csv('input/sample_submission.csv')
submit['label'] = 1.0
submit.to_csv('submission1.csv')
submit['label'] = 0.0
submit.to_csv('submission2.csv')