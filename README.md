# Novabot: A Burroughs-Inspired Cut-Up Language Model  

![GitHub](https://img.shields.io/badge/license-MIT-blue)  
![Python](https://img.shields.io/badge/Python-3.8%2B-green)  
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red)  
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow)  

Novabot is a fine-tuned language model that emulates the **"cut-up" technique** pioneered by experimental writer **William S. Burroughs**. By algorithmically rearranging a curated "word hoard" extracted from Burroughs' novels, Novabot generates surreal, fragmented prose in the spirit of *Naked Lunch* and *Nova Express*.  

## 🔮 Inspiration  

The project is based on the apocryphal **"Word Hoard"**—a lost manuscript Burroughs allegedly compiled between 1954 and 1958. This 1000-page collection of words and phrases was physically cut up and reassembled into his *Nova Trilogy* (*The Soft Machine*, *The Ticket That Exploded*, *Nova Express*) and *Naked Lunch*.  

Novabot revives this method computationally, using **GPT-2 fine-tuning** and **constrained vocabulary generation** to produce Burroughs-esque cut-ups.  

## ⚙️ Technical Approach  

1. **Data Extraction & Word Hoard Creation**  
   - Processed Burroughs' novels (*Naked Lunch*, *The Soft Machine*, *The Ticket That Exploded*, *Nova Express*) as text files.  
   - Used **NumPy** to compute the **intersection of words** across all texts, forming a constrained vocabulary.  
   - Filtered out digits, symbols, and noise to refine the word set.  

2. **Model Fine-Tuning**  
   - Loaded **GPT-2** (via HuggingFace `transformers`) and fine-tuned on *Naked Lunch* to capture Burroughs' style.  
   - Implemented **prompt engineering** to enforce vocabulary constraints from the word hoard.  
   - Used **PyTorch** for training (limited by GPU resources).  

3. **Generation Method**  
   - Outputs are produced via **constrained decoding**, ensuring words are drawn from the curated hoard.  
   - Future improvements could involve **beam search** or **top-k sampling** for more coherent cut-ups.  

## 🚀 Future Work  

- Experiment with **Llama 3 or GPT-4** for richer outputs (requires GPU scaling).  
- Develop a **web interface** (Flask/Streamlit) for interactive cut-up generation.  
- Expand the word hoard with additional Burroughs texts (*The Wild Boys*, *Cities of the Red Night*).  
- Implement **image cut-ups** (ala Burroughs/Brion Gysin) using diffusion models.  

## 📂 Repository Structure  

```
novabot/  
├── data/  
│   ├── naked_lunch.txt  
│   ├── soft_machine.txt  
│   ├── ticket_exploded.txt  
│   └── nova_express.txt  
├── notebooks/  
│   └── word_hoard_analysis.ipynb  
├── scripts/  
│   ├── preprocess.py  
│   └── train.py  
├── outputs/  
│   └── examples/  
├── models/  
│   └── fine_tuned_gpt2/  
└── README.md  
```  

## 🛠️ Installation  

1. Clone the repo:  
   ```sh  
   git clone https://github.com/[yourusername]/novabot.git  
   cd novabot  
   ```  

2. Install dependencies:  
   ```sh  
   pip install -r requirements.txt  # (PyTorch, transformers, numpy, etc.)  
   ```  

3. Run preprocessing & training:  
   ```sh  
   python scripts/preprocess.py  
   python scripts/train.py  
   ```  

## 💡 Example Output  

**Prompt:** `"the virus is"`  

**Novabot:**  
> *the virus is a green sunset in the terminal sewer—  
> flesh machines whisper in the hotel rooms of the irradiated  
> and the word itself crawls like a centipede made of typewriter keys*  

## 🔗 References  

- William S. Burroughs, *The Cut-Up Method of Brion Gysin* (1963)  
- HuggingFace [Transformers](https://huggingface.co/docs/transformers/index)  
- *Naked Lunch* @ [OpenAIRE](https://explore.openaire.eu/) (public domain)  

