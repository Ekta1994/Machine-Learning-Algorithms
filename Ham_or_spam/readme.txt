**Pre-processing of emails-:**
  - This involves normalizing the values such as urls, email-ids and numbers such that all urls are treated the same. This allows the machine learning algorithm to make decisions on the basis of fact for eg whether a URL is present or not instead of which url is present.
  - The entire email is converted into lower case such that capitalization is ignored.
  - Normalizing URLs : All urls are replaced with httpaddr.
  - Normalizing Email-addresses : All email addresses are replaced with emailaddr.
  -Removal of non-words : All non-words and punctuations like space, tab etc are removed.
  - words with length more than three are taken.
  - All numbers are replaced with their english name.
  - '$' sign is replaced with "dollar".
  
  - For above, the initial version of the mail is shown in the image initialmailpng.
  
**Making of vocabulary list-:**
 - All the words of the above email are now maintained in the list with their counts.
 - Some 'k' frequent words are chosen as the feature set for classifying whether the mail is spam or ham.

**Feature Vector-:**
 - For every training example, a vector of length k is maintained.
 - the entry vec[i][j] = 1 denotes wether the j'th feature word ( from the vocab list ) is present in i'th mail or not.
 - a result vector y of length (training_Examples) is maintained.
 - y[i] = 1 denotes that the i'th training mail belongs to the ham category and spam otherwise.
 
**Predicting-:**
 - The mails bifurcated for prediction are now tested and you can see the result in console.
 - Accuracy can be easily calculated.