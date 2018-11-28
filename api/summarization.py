from gensim.summarization.summarizer import summarize

def text_rank(text):
	summ  = summarize(text)

	if len(summ):
		return summ
	else:
		return "Error"