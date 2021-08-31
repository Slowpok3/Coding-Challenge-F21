(note: I dont really know how to document these things at a professional level, so I kept it informal)

Getting to My Solution:

I started off by researching about sentiment analysis and how to implement it, and I immediately came across a roadblock. Most programs that employ sentiment analysis have been created by a team of individuals throughout a long time using either "hard coded" rules, or Artificial Intelligence models. However, I found a VERY helpful API called Monkey Learn, which would simply return the "sentiment" of a text that I could input, all in less than 10 lines of code. 

The API can classify many types of text as being either "positive" , "neutral", or "negative" , and has different models for different types of texts (a list of the classifiers can be found at the bottom of my output). 

From the given test input, the program outputted that the sentiment of this text was "Positive", with a confidence of "0.626". I would generally agree with this result, as the text seemed to compliment the subject. Since the model I used in the API is generally trained for the purpose of product reviews, this was a very predictable output. I also removed all of the instances of \n in the text, and it returned the same result with the same confidence

Then, I wanted to see the sentiments of each sentence in the input text, so I parsed through the input, separated out the sentences, and I ran it all through the classifier. I counted up the totals for each of the three classifications in hopes that it would provide me with insight into how the classifier handled the multiple sentences during the first call. 

SOURCES:
Api used: https://monkeylearn.com/api/v3/?python#classifier-api




# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

