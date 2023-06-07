from nltk import word_tokenize #to tokenize sentences
from nltk.corpus import stopwords #importing stopwords
from nltk.stem import WordNetLemmatizer #importing lemmatizer, alternately import any stemmer of your choice
lemmatizer=WordNetLemmatizer() #creating lemmatizer object
# f=open(r'C:\Users\Rini\Desktop\Ave_v2.0\ave_question.txt', 'r')
question_list=["None","what are the symptoms of corona","what are the symptoms of corona"]
question_file=open(r'ave_question.txt', 'w')
def clean_list(question_list):    
    def process(enter): 
        global lemmatizer, question_file
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
        question_file.write(" ".join(final_list))
        question_file.write("\n")
        #question_file.write("\n")
    length=len(question_list) 
    for i in range(1,length):
        process(question_list[i])   
    #f.close()
    question_file.close()
clean_list(question_list)
        