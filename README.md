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

## Results:
The overall sentiment score of the text in this file was positive. This means that the language used in the imput text contained more conventionally positive words than negative words. This was different from what I had expected because as I was skimming through the text, I seemed to notice more negative words pop out at me than positive ones. As a psychology major, I do understand that negative emotions tend to be a lot more noticeable to humans than positive emotions so I thought this was an interesting way to maybe get rid of that innate human bias and logistically see whether a wall of text is positive or negative. 
## Explanation: 
Since I don't have much experience with code, I started by understanding exactly what sentimental analysis is and how it works. I found this to be very interesting as a psychology major that there is a way I could use code in order to determine the overall sentiments or vibes from a certain wall of text. 
This led me to the official nltk.org website where I used the instructions to download nltk and python to my computer. I used this video, https://www.youtube.com/watch?v=1heFM9iWF78, in order to properly install both python and nltk onto my computer and have them both be working properly. Next, I used the code presented in https://realpython.com/python-nltk-sentiment-analysis/ to download the different tools from nltk that I thought would be useful. After that, I learned how to add the text into python using this website https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk and began the process of cleaning the text. 
I used the YouTube playlist https://www.youtube.com/playlist?list=PLhTjy8cBISEoOtB5_nwykvB9wfEDscuEo in order to help me with actually conducting the sentiment analysis. First, I lowercased all of the words within the text. Then I took out all of the punctuation so only the words are remaining. Next, I used the stop words function in order to remove neutral and common words that will not be useful to the analysis. Then I imported vader from nltk which is a sentiment analyzer and used that to determine whether the text was positive or negative overall. Finally, using the same YouTube playlist from earlier, I ran the test one more time, but this time, I had the results be a strict positive or negative instead of the previous result which contained both the positive (score of 0.189) and negative (score of 0.076) scores. The code I used mostly came from https://github.com/attreyabhatt/Sentiment-Analysis/blob/master/main_nltk.py. My result was a Positive Sentiment.