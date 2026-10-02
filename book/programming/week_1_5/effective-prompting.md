(llms-effective-prompting)=
# Effective prompting
When interacting with an LLM about your code, the way you prompt the model can significantly impact the quality of its responses. We recommend using the integrated AI chat panel if present in your editor instead of external chatbot like ChatGPT. This allows the LLM to directly reference your project files and the broader code context.

```{tip}
If you are using a coding assistant embedded into your editor, such as GitHub Copilot or Cursor AI, you can open the chatbot panel to interact with the LLM. This is typically found in the sidebar of your coding editor, allowing you to ask questions and get code suggestions directly related to your current project.
```

## Best Practices for Prompting LLMs
When prompting an LLM, it is essential to be clear and specific about what you want. Here are some strategies to improve your prompts:

1. Be Specific: Instead of asking a vague question, provide clear details about what you need. The more specific your question, the more related and useful the response will be.

2. Specify Context: If you are working with a specific language, library, or framework, mention it in your prompt. This helps the LLM tailor its response to your needs.

    ```{admonition} Example
    :class: example
    Say you want to create a numpy array with random values. Instead of asking "How do I create a random array?", you can ask "How do I create a numpy array with random integers between 1 and 10 in Python?".
    ```

3. Desired Output Format: If you want the response in a specific format, such as code with comments or a brief explanation, include that in your prompt.

    ```{admonition} Example
    :class: example
    Instead of asking "How do I use Matplotlib in Python?", you can ask "Outline the steps to create a simple line plot using Matplotlib in Python, and provide a code example with comments explaining each step."
    ```

4. Task Definition: Telling the LLM what you want it to do in clear steps is far more important than telling it what not to do. 

    ```{admonition} Example
    :class: example
    Instead of saying "Don't give me a long explanation," you can say "Provide a brief example."
    ```

5. Structure: Using a structure format in your question can lead to drastically better results. Rather than asking a general multipart question, break it down into smaller, more manageable parts with clear instructions. 

6. Role Definition: If you want the LLM to act as a specific type of expert, such as a patient mentor or an expert in a particular field, specify that in your prompt. This helps the LLM understand the tone and depth of response you expect. 


```{admonition} Tip
:class: tip    
These skills apply to any LLM interaction, not just coding assistants. Next time you are using a personal assistant like ChatGPT, remember that specific prompts with context will yield better results! 
``` 
