# Module imports

# Wikipedia module
import wikipedia


def search_wiki(text):

    wikipedia.set_lang('en')           
    result = wikipedia.summary(text, sentences = 2)
    
    return result
