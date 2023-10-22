# Neural Machine Translation

Traditional Language Translation model - Seq2Seq Model
![imge](https://docs.chainer.org/en/stable/_images/seq2seq.png)
![image](https://pytorch.org/tutorials/_images/seq2seq.png)
## Ingredients
- **Encoder** 
- **Decoder** 
    - In order to translate one language to another
    - Ex. Translation using LSTM based system that has both encoder and decoder.

# How algorithm works:
- Encoder takes input tokens of words/text.
- Encoder outputs it's **final hidden state.**
- Decoder receives/uses this hidden state and generate the translated sentence in the target language.

# Encoder
- Consist of embedding layer and LSTM module with one or more layers.
- Embedding layers transforms words tokenized first into a vector for input to the LSTM module(s).
	- At each step in the input sequence, LSTM module receives inputs from the embedding layer as well as hidden states from previous step.
- Encoder returns the hidden states of the final step. 
- **Final Hidden State** has information from whole sentence and it encodes its overall meaning.

# Decoder
- Similar to the encoder, which is constructed with an embedding layer and an LSTM layer. 
- You use the output word of a step as an input step for the next step. 
- You also pass the LSTM hidden state to the next step


# Limitation of Seq2Seq
- The information bottleneck.