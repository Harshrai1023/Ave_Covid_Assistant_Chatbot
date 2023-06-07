from nltk import word_tokenize #to tokenize sentences
from nltk.corpus import stopwords #importing stopwords
from nltk.corpus import wordnet #importing wordnet
from nltk.tokenize import punkt
from nltk.stem import WordNetLemmatizer #importing lemmatizer, alternately import any stemmer of your choice
lemmatizer=WordNetLemmatizer() #creating lemmatizer object
f=open(r'question.txt', 'r')
question_list=[]
for question in f.readlines():
    question_list+=[question.rstrip()] #list of cleaned questions

f1=open(r'ave_answers.txt', 'r')
answers=f1.readlines()
answer_list=[]
for answer in answers:
    answer_list+=[answer.rstrip()] #list of answers
f2=open(r'ave_question.txt', 'r')
all_questions=[]
for question in f2.readlines():
    all_questions+=[question.rstrip()] #list of complete questions
best_matches=[] #list containing best matches based on user query


def process(query):
    print("reached alpha") #if query is a string
    global all_questions, answer_list, question_list, best_matches
    def clean_sentence(enter): #function to clean user's query
        global lemmatizer
        raw_words=word_tokenize(enter) #cleaning of sentence begins here
        words=[]
        for word in raw_words:
            words.append(word.lower())
        words_no_punc=[]
        for word in words:
            if word.isalpha():
                words_no_punc.append(word)
        clean_words=[]
        stopword=stopwords.words("english")
        for word in words_no_punc:
            if word not in stopword:
                clean_words.append(word) #cleaning of sentence concludes
        final_list=[] 
        for word in clean_words: #storing only the stem words rather than the actual words
            final_list.append(lemmatizer.lemmatize(word, pos="n"))
            
        return final_list #the list of cleaned, stemmed words of the sentence passed to function
    def compare(l1, l2): #comparing similarity between user's query and cleaned questions
        ratio=0
        n=1
        for i in l1:
            for j in l2:
                word1=wordnet.synsets(i) #list of all available definitions of a word available
                word2=wordnet.synsets(j)
                for element0 in word1:
                    for element1 in word2:
                        if element0.wup_similarity(element1)!=None:
                            ratio+=element0.wup_similarity(element1) #comparing each definition, to ensure maximum accuracy.
                        n+=1
        return (ratio/n) #obtaining final ratio as a measure of the similarity of sentences
    processed_list={} #key value pair of database_questions and similarity ratio
    query=clean_sentence(query) #cleaning query
    for ques in question_list:
        if len(ques)>=len(query):
            similarity=compare(ques.rstrip(),query) #comparing
            processed_list[ques.rstrip()]=similarity #adding data as key value pair
            
                        
        else:
            similarity=compare(ques.rstrip(),query)
            processed_list[ques.rstrip()]=similarity
    
    sorted_values=list(processed_list.values()) #sorting similarity in descending order
    sorted_values.sort(reverse=True)
    final_list=[] #list containing question based on similarity order 
    for i in sorted_values: #loop sorting questions based on similarity
        for question,value in processed_list.items():
            if i==value:
                if question not in final_list:
                    final_list+=[question] 
                    break
                else:
                    continue
    a=""
    for i in range(10):
        a+=str((i+1))
        a+=(". ")
        j=question_list.index(final_list[i])
        a+=all_questions[j]
        best_matches+=[all_questions[j]] #creating a list containing the best 10 matches
        a+=("\n") #creating a string  containing the 10 matches for user display
        
    return a

def produce_answer(choice): #if query is an integer
    print ("reached num")
    choice=int(choice)
    question_choice=best_matches[choice-1] #accessing the question considered as best by user from among the best matches
    i=all_questions.index(question_choice) #accesing the index of the best match from the complete  list of questions
    return answer_list[i] #accesing the answer matching the index and returning it back to user
    


        
        
        
