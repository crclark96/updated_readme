# updated_readme

This project is inspired by the caliber of pull requests I made during Hacktoberfest 2017. It will (should) parse and spellcheck readmes of public repositories, then open pull requests with the edits.

## usage

Follow [this link](https://github.com/settings/tokens) to generate access tokens for your Github account.

`sed "s/API_KEY/<YOUR_API_KEY_HERE>/" sample_credentials.json > credentials.json`

(replace the API_KEY field with your personal API key in sample_credentials.json and rename as credentials.json)

`pip install -r requirements.txt`

(install dependencies using pip)

`python ghub.py`

(run)