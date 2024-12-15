# novabot

Concept:
My project is premised on a lost manuscript known as the "Word Hoard" by experimental writer William S. Burroughs. The manuscript consisted of around 1000 typewriter pages written over the course of 4 years in the 1950s. The manuscript was physically cut up and arranged to develop a series of novels: Interzone, Naked Lunch, The Soft Machine, The Ticket That Exploded and Nova Express. The Word Hoard was primarily used in Naked Lunch with remaining text recycled into the succeeding works. The cut-up method had also been employed to varying degrees. 

My project is comprised of two phases:
1. With the novels as text files, find the intersection between them all in order to constitute a de facto Word Hoard. 
2. Train a transformer-based language model on Naked Lunch in order to extract a distinct style with which to enforce the vocabulary of the Word Hoard onto. 

The purpose of my project is to emulate the cut-up method using the vocabulary canonical to Burroughs' work throughout this series of iconic novels. 

What I achieved:
1. I successfully extracted the list of words that may act as a de facto word hoard and saved them as a Python list. 
2. I fine-tuned the transformer model GPT2 on both Naked Lunch and the Word Hoard. I did two different training methods in order to vary my results. 
3. I generated text using Naked Lunch as the model, for style, and the Word Hoard as the tokenizer, for vocabulary. 

My results:
While the generated text resembled the source material superficially, the model employed its learned prose too literally and the results bore no special qualities I could relate to the cut-up method. 

Next steps:
Using a LogitsProcessor to enforce the Word Hoard vocabulary more rigorously. Gauge responses and tinker accordingly. 