# **Cut-up text generator**  
*A vocabulary-constrained text generator mimicking William S. Burroughs' style*

## **Overview**  
This project generates original passages in the style of *Naked Lunch*, using **only a user-provided vocabulary list** (`hoard.txt`). It combines:  
1. **Markov Chains** (for structured, vocabulary-safe drafts)  
2. **GPT-2 Fine-Tuning** (for stylistic expansion)  

Ideal for constrained creativity exercises or experimental writing.  

---

## **Workflow**  
### **1. Inputs**  
- **`hoard.txt`**: Your vocabulary list (one word per line).  
- **`naked_lunch.txt`**: Raw text of *Naked Lunch* for style learning.  

### **2. Key Steps**  
#### **A. Markov Chain Setup**  
- Extracts word transitions from *Naked Lunch* using only `hoard.txt` words.  
- Generates coherent but simple "seed" phrases (e.g., `"junk whispers through syringe streets"`).  

#### **B. GPT-2 Fine-Tuning** *(Optional)*  
- Trains a GPT-2 model on *Naked Lunch* to learn Burroughs’ style.  
- Saved to `./results` for reuse.  

#### **C. Hybrid Generation**  
1. **Markov Chain** creates a seed phrase.  
2. **GPT-2** expands it into a richer passage, constrained by `hoard.txt`.  

---

## **Usage**  
### **1. Pure Markov Mode**  
```python
python markov.py --seed "clinic" --length 20
```  
**Output**:  
> *"clinic smells of rust and ether... the syringe priest laughs in dank rooms"*  

### **2. Hybrid (Markov + GPT-2) Mode**  
```python
python hybrid_generator.py --seed "junk" --max_length 50 --temperature 0.7
```  
**Output**:  
> *"junk whispers through the syringe streets where typewriters vomit ectoplasmic laughter—a virus of peeling wallpaper and insect screams."*  

### **3. Override Vocabulary**  
Replace `hoard.txt` with your own word list to change constraints.  

---

## **Requirements**  
```text
Python >= 3.8  
numpy  
torch  
transformers  
datasets  
```  
Install:  
```bash
pip install numpy torch transformers datasets
```

---

## **Customization**  
- **Style**: Adjust `temperature` (0.3–1.0) for more/less randomness.  
- **Vocabulary**: Edit `hoard.txt` to permit/disallow specific words.  
- **Output Length**: Set `--length` in Markov or `--max_length` in GPT-2.  

---

## **Why This Works**  
- **Markov Chains** ensure vocabulary compliance and baseline coherence.  
- **GPT-2** adds stylistic flourishes while respecting constraints via `bad_words_ids`.  
- **Lightweight**: Hybrid approach reduces GPU dependency (MacBook-friendly).  

---

## **Example Outputs**  
| Seed          | Generated Passage |  
|---------------|-------------------|  
| `"needle"`    | *"needle streets hum with static... a boy’s spine dissolves into typewriter glue."* |  
| `"mugwump"`   | *"mugwump chemistry in a bathtub—rectal spasms echo through the hotel lobbies of hell."* |  

---

## **Limitations**  
- **Repetition**: Markov chains may loop; mitigated by `repetition_penalty` in GPT-2.  
- **Hardware**: GPT-2 fine-tuning requires a modern CPU/GPU (slow on base MacBook Air).  

---

**License**: MIT  
**Author**: [Your Name]  

--- 

Let me know if you’d like to emphasize specific features or add setup instructions!

