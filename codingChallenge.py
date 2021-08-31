from monkeylearn import MonkeyLearn
import re

# importing the text file
file = open("input.txt" , "r")

input_text = file.read()
new_input = input_text.replace('\n', ' ')
 
 # setting up monkey learn api 
ml = MonkeyLearn('35647f9e498c7d977c6dcfceb0873a075f27b389') #entering my api key
data = [new_input] # assigning a data variable with the input text
model_id = 'cl_pi3C7JiL' # since each classifier has a unique ID, the "classify" function takes in the ID of the classifier you are using in order to use the correct classifier
result = ml.classifiers.classify(model_id, data) #function that runs the classifier

print("Overall text sentiment: " , result.body[0]["classifications"][0]["tag_name"]) # printing out the specific classification from the JSON string
print("Confidence: " , result.body[0]["classifications"][0]["confidence"] ) # doing the same for confidence

sentences = new_input.split(".")
setenceResult = ml.classifiers.classify(model_id, sentences) #the classifier can do multiple independent classifications in one call

possibleSents = [0,0,0]

for i in range(len(setenceResult.body)-1):

	sentiment = setenceResult.body[i]["classifications"][0]["tag_name"] #recorded each type of sentiment
	if (sentiment == "Positive"):
		possibleSents[0] += 1
	elif (sentiment == "Neutral"):
		possibleSents[1] +=1
	else:
		possibleSents[2] +=1

	print("Sentence: ", setenceResult.body[i]["text"])
	print ("Sentiment: ", sentiment)
	print("Confidence: ", setenceResult.body[i]["classifications"][0]["confidence"] , "\n")

print("Total Positive Sentences: ", possibleSents[0])
print("Total Neutral Sentences: ", possibleSents[1])
print("Total Negative Sentences: ", possibleSents[2])

# for classification in setenceResult.body:
# 	if (classification["classifications"][0]["tag_name"] is None) :
# 		break

# 	print( classification["text"])
# 	print (classification["classifications"][0]["tag_name"])
	




response = ml.classifiers.list()

print("Different Types of Classifiers: ")
for i in range(len(response.body)-1):
	print(response.body[i]["name"])

