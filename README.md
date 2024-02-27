# stack overflow ngram analysis

This project fetches StackOverflow API get questions and make ngram analysis

# install

pip install sosq

pip install emek

pip install ngramso

# for use

1- Get your key and token from stackexchange (https://stackapps.com/users/login?returnurl=/apps/oauth/register)

2- sample code below.


```
import sosq
import emek
import ngramso
df = sosq.get_result("your_search_query", "your_key", "your_access_token")
emek.process_data(df)
ngramso.process_and_generate_ngrams(df)
```

sosq for dataframe
emek for tag analysis
ngramso for ngram analysis to compare tags with ngrams