# Session 1 Cheatsheet: Vibe Check

> Check the Vibes on Your LLM Application

---

## Quick Reference

| Concept | Definition | Key Pattern |
|---------|------------|-------------|
| LLM Application | Language model + context + interface | Input → LLM → Output |
| Chat Completions API | Message-based interface to GPT models | `system`, `user`, `assistant` roles |
| Prompt Engineering | Crafting inputs for desired outputs | Clear, specific, structured |
| Few-Shot Learning | Learning from examples in the prompt | Demonstrate, then ask |
| Chain-of-Thought | Step-by-step reasoning in responses | "Think step by step" |
| Context Engineering | Adding information to prompts | Context + Question format |
| Vibe Check | Qualitative evaluation of outputs | Manual review for patterns |

---

## Setup Requirements

### Dependencies
```bash
pip install openai fastapi uvicorn python-dotenv
```

### Environment Variables
```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"

# Or use .env file with python-dotenv
from dotenv import load_dotenv
load_dotenv()
```

### Verify Installation
```python
from openai import OpenAI
client = OpenAI()
print("Setup complete!")
```

---

## 1. LLM Application Architecture

### The Simplest LLM App
```
User Query → Add Context → LLM → Response
```

### Core Components
| Component | Role | Example |
|-----------|------|---------|
| Input | User's question or task | "What is photosynthesis?" |
| Context | Relevant background info | System prompt, examples, documents |
| Model | Language model processing | GPT-4o, GPT-4o-mini |
| Output | Generated response | Explanation of photosynthesis |

### Why Context Matters
> **"The quality of your LLM output depends heavily on the quality of the context you provide."**

Without context, models rely on training data alone. With good context, they can answer questions about:
- Your specific domain
- Recent information
- Private data

**Official Docs**: [OpenAI API Overview](https://platform.openai.com/docs) [[1]](https://platform.openai.com/docs)

---

## 2. The Chat Completions API

### Message Roles
| Role | Purpose | When to Use |
|------|---------|-------------|
| `system` | Sets model behavior | First message, defines personality |
| `user` | Human input | Questions, tasks, data |
| `assistant` | Model responses | Previous answers, few-shot examples |

### Basic API Call
```python
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(completion.choices[0].message.content)
# Output: The capital of France is Paris.
```

### Response Structure
```python
# Access the response
response_text = completion.choices[0].message.content
finish_reason = completion.choices[0].finish_reason
total_tokens = completion.usage.total_tokens
```

**Official Docs**: [Chat Completions Guide](https://platform.openai.com/docs/guides/chat-completions) [[2]](https://platform.openai.com/docs/guides/chat-completions)

---

## 3. Prompt Engineering Fundamentals

### The Three Pillars
1. **Clarity**: Be specific about what you want
2. **Context**: Provide relevant background
3. **Constraints**: Define boundaries and format

### System Prompt Best Practices
```python
# Bad - Too vague
system_prompt = "Be helpful."

# Good - Clear role and behavior
system_prompt = """You are a technical support assistant for a software product.
Your responses should be:
- Concise and actionable
- Technical but accessible
- Include code examples when relevant
Always ask clarifying questions if the user's issue is unclear."""
```

### Instruction Clarity
| Vague | Specific |
|-------|----------|
| "Summarize this" | "Summarize in 3 bullet points under 20 words each" |
| "Write about AI" | "Write a 200-word introduction to machine learning for high school students" |
| "Help me code" | "Write a Python function that validates email addresses" |

**Official Docs**: [Prompt Engineering Overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) [[3]](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)

---

## 4. Few-Shot Learning

### From the GPT-3 Paper
> **"Scaling language models dramatically improves few-shot performance... tasks and few-shot demonstrations specified purely via text interaction with the model."**
> — Brown et al., 2020 [[4]](https://arxiv.org/abs/2005.14165)

### Why It Works
- Models learn patterns from examples
- No retraining required
- Works for many tasks: classification, formatting, style

### Few-Shot Template
```python
messages = [
    {"role": "system", "content": "You classify customer feedback sentiment."},
    # Example 1
    {"role": "user", "content": "This product exceeded my expectations!"},
    {"role": "assistant", "content": "Positive"},
    # Example 2
    {"role": "user", "content": "Worst purchase I've ever made."},
    {"role": "assistant", "content": "Negative"},
    # Example 3
    {"role": "user", "content": "It does what it's supposed to do."},
    {"role": "assistant", "content": "Neutral"},
    # Actual query
    {"role": "user", "content": "I love how easy it is to use!"}
]
```

### Zero-Shot vs Few-Shot
| Approach | Examples | Best For |
|----------|----------|----------|
| Zero-shot | 0 | Simple, well-defined tasks |
| One-shot | 1 | Format demonstration |
| Few-shot | 2-5 | Complex patterns, edge cases |

**Paper**: [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) [[4]](https://arxiv.org/abs/2005.14165)

---

## 5. Chain-of-Thought Prompting

### From the Original Paper
> **"Generating a chain of thought — a series of intermediate reasoning steps — significantly improves the ability of large language models to perform complex reasoning."**
> — Wei et al., 2022 [[5]](https://arxiv.org/abs/2201.11903)

### When to Use CoT
- Math problems
- Multi-step reasoning
- Logic puzzles
- Complex analysis

### Simple CoT Trigger
```python
# Add to the end of your prompt:
"Think step by step before giving your final answer."
```

### CoT in Practice
```python
# Without CoT
messages = [
    {"role": "user", "content": "A store sells apples for $2 each. "
     "If I buy 3 apples and pay with a $10 bill, how much change do I get?"}
]
# Model might make errors

# With CoT
messages = [
    {"role": "user", "content": "A store sells apples for $2 each. "
     "If I buy 3 apples and pay with a $10 bill, how much change do I get? "
     "Think step by step."}
]
# Response: "Let me work through this:
# 1. Cost per apple: $2
# 2. Number of apples: 3
# 3. Total cost: $2 × 3 = $6
# 4. Payment: $10
# 5. Change: $10 - $6 = $4
# The answer is $4."
```

### Few-Shot CoT
```python
messages = [
    {"role": "user", "content": "Q: Roger has 5 tennis balls. He buys 2 more cans "
     "of 3 tennis balls each. How many does he have now?"},
    {"role": "assistant", "content": "Let's think step by step.\n"
     "Roger starts with 5 balls.\n"
     "He buys 2 cans × 3 balls = 6 balls.\n"
     "Total: 5 + 6 = 11 balls.\n"
     "Answer: 11"},
    {"role": "user", "content": "Q: [Your actual question here]"}
]
```

**Paper**: [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) [[5]](https://arxiv.org/abs/2201.11903)

---

## 6. Context Engineering (Naive RAG)

### The Core Pattern
```python
context = """[Relevant information about your domain]"""

question = "User's question here"

messages = [
    {"role": "system", "content": "Answer questions based only on the provided context."},
    {"role": "user", "content": f"""Context:
{context}

Question: {question}

Answer:"""}
]
```

### Why Add Context?
| Without Context | With Context |
|-----------------|--------------|
| Uses only training data | Uses your specific data |
| May hallucinate | Grounded in provided info |
| Generic answers | Domain-specific answers |
| Static knowledge | Current information |

### Context Placement
```python
# Option 1: In system prompt (for persistent context)
messages = [
    {"role": "system", "content": f"You are an assistant. Use this info:\n{context}"},
    {"role": "user", "content": question}
]

# Option 2: In user message (for query-specific context)
messages = [
    {"role": "system", "content": "Answer based on the provided context."},
    {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
]
```

**Paper**: [RAG - Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) [[6]](https://arxiv.org/abs/2005.11401)

---

## 7. Vibe Check Evaluation

### What is a Vibe Check?
> **"LLM outputs are non-deterministic, which makes response quality hard to assess. Evaluations (evals) are a way to break down what 'good' looks like and measure it."**
> — LangSmith Documentation [[7]](https://docs.langchain.com/langsmith/evaluation-concepts)

### Vibe Check Questions
| Dimension | Questions to Ask |
|-----------|------------------|
| Accuracy | Is the information correct? |
| Helpfulness | Does it answer the question? |
| Tone | Is the style appropriate? |
| Format | Is it well-structured? |
| Safety | Is it free of harmful content? |

### Running a Vibe Check
1. **Collect outputs**: Run your app on 10+ diverse queries
2. **Review manually**: Read each response carefully
3. **Document patterns**: What works? What doesn't?
4. **Identify vibes**: Note tone, style, formatting patterns
5. **Prioritize issues**: What matters most to fix?

### VibeCheck Research (ICLR 2025)
> "Users have found Llama3 outputs tend to be more friendly compared to outputs from GPT-4 and Claude which tend to be more formal."
> — Dunlap et al., 2024 [[8]](https://arxiv.org/abs/2410.12851)

The VibeCheck paper shows that "vibes" can be:
- Discovered automatically
- Quantified and compared
- Used to predict user preferences

**Paper**: [VibeCheck: Discover and Quantify Qualitative Differences](https://arxiv.org/abs/2410.12851) [[8]](https://arxiv.org/abs/2410.12851)

---

## 8. From Vibes to Metrics

### Building a Simple Rubric
```python
rubric = {
    "accuracy": {
        "description": "Information is factually correct",
        "scale": [1, 2, 3, 4, 5]
    },
    "helpfulness": {
        "description": "Response addresses the user's need",
        "scale": [1, 2, 3, 4, 5]
    },
    "clarity": {
        "description": "Response is easy to understand",
        "scale": [1, 2, 3, 4, 5]
    }
}
```

### Evaluation Workflow
```
┌────────────────────────────────────────────────────┐
│                EVALUATION WORKFLOW                  │
│                                                     │
│   Test Cases → Run App → Collect Outputs → Score   │
│       ↑                                      │     │
│       └──────── Improve Prompts ←───────────┘     │
└────────────────────────────────────────────────────┘
```

### Success Criteria Framework
From Anthropic:
> Good success criteria are **Specific**, **Measurable**, **Achievable**, **Relevant**, and **Time-bound**.

| Bad Criteria | Good Criteria |
|--------------|---------------|
| "Safe outputs" | "Less than 1% responses flagged by content filter" |
| "Accurate" | "90%+ factual accuracy on test set" |
| "Fast enough" | "P95 latency under 3 seconds" |

**Official Docs**: [Define Success Criteria](https://platform.claude.com/docs/en/test-and-evaluate/define-success) [[9]](https://platform.claude.com/docs/en/test-and-evaluate/define-success)

---

## 9. FastAPI Basics

### Minimal API
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

### LLM Endpoint Pattern
```python
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
client = OpenAI()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": request.message}
        ]
    )
    return ChatResponse(response=completion.choices[0].message.content)
```

### Run the Server
```bash
uvicorn main:app --reload
```

**Official Docs**: [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/first-steps/) [[10]](https://fastapi.tiangolo.com/tutorial/first-steps/)

---

## 10. OpenAI API Parameters

### Key Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | string | Model ID (e.g., "gpt-4o", "gpt-4o-mini") |
| `messages` | array | Conversation history |
| `temperature` | float | Randomness (0-2, default 1) |
| `max_tokens` | int | Maximum response length |
| `top_p` | float | Nucleus sampling (0-1) |

### Temperature Guide
| Value | Behavior | Use Case |
|-------|----------|----------|
| 0 | Deterministic | Factual Q&A, code |
| 0.3-0.5 | Focused | Writing, summaries |
| 0.7-1.0 | Balanced | General conversation |
| 1.2-2.0 | Creative | Brainstorming, fiction |

### Example with Parameters
```python
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0.7,  # Balanced creativity
    max_tokens=500,   # Limit response length
)
```

**Official Docs**: [API Reference](https://platform.openai.com/docs/api-reference/chat) [[11]](https://platform.openai.com/docs/api-reference/chat)

---

## 11. Model Selection Guide

### Available Models (2026)
| Model | Strength | Cost | Use Case |
|-------|----------|------|----------|
| gpt-4o | Highest quality | $$$ | Complex reasoning, production |
| gpt-4o-mini | Good quality, fast | $ | General tasks, prototyping |
| gpt-4-turbo | High quality | $$ | Long context, vision |

### Choosing a Model
```
Start with gpt-4o-mini for development
    ↓
If quality insufficient → Try gpt-4o
    ↓
If cost too high → Optimize prompts first
    ↓
Consider gpt-4o-mini with better prompts
```

### Token Economics
| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|-------|----------------------|------------------------|
| gpt-4o-mini | $0.15 | $0.60 |
| gpt-4o | $2.50 | $10.00 |

**Official Docs**: [Models Overview](https://platform.openai.com/docs/models) [[12]](https://platform.openai.com/docs/models)

---

## 12. Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| "I don't know" responses | Missing context | Add relevant information |
| Hallucinations | No grounding | Provide source material |
| Wrong format | Unclear instructions | Be explicit about format |
| Too long/short | No length guidance | Specify word/sentence count |
| Wrong tone | No style guidance | Add tone in system prompt |
| Inconsistent outputs | High temperature | Lower temperature for stability |

---

## Code Patterns Reference

### Pattern 1: Simple Q&A
```python
def ask(question: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}]
    )
    return completion.choices[0].message.content
```

### Pattern 2: Few-Shot Classification
```python
def classify_sentiment(text: str) -> str:
    messages = [
        {"role": "system", "content": "Classify sentiment as Positive, Negative, or Neutral."},
        {"role": "user", "content": "Love it!"},
        {"role": "assistant", "content": "Positive"},
        {"role": "user", "content": "Hate it!"},
        {"role": "assistant", "content": "Negative"},
        {"role": "user", "content": text}
    ]
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0  # Deterministic
    )
    return completion.choices[0].message.content
```

### Pattern 3: Context-Augmented Q&A
```python
def answer_with_context(context: str, question: str) -> str:
    messages = [
        {"role": "system", "content": "Answer based only on the provided context."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
    ]
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    return completion.choices[0].message.content
```

### Pattern 4: Chain-of-Thought
```python
def solve_with_reasoning(problem: str) -> str:
    messages = [
        {"role": "system", "content": "Solve problems step by step, showing your reasoning."},
        {"role": "user", "content": f"{problem}\n\nThink step by step."}
    ]
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    return completion.choices[0].message.content
```

---

## Official Documentation Links

### OpenAI
- [OpenAI Platform](https://platform.openai.com/docs) [[1]](https://platform.openai.com/docs)
- [Chat Completions](https://platform.openai.com/docs/guides/chat-completions) [[2]](https://platform.openai.com/docs/guides/chat-completions)
- [API Reference](https://platform.openai.com/docs/api-reference/chat) [[11]](https://platform.openai.com/docs/api-reference/chat)
- [Models](https://platform.openai.com/docs/models) [[12]](https://platform.openai.com/docs/models)
- [OpenAI Python SDK](https://github.com/openai/openai-python) [[13]](https://github.com/openai/openai-python)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) [[14]](https://github.com/openai/openai-cookbook)

### Anthropic
- [Prompt Engineering Overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) [[3]](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [Chain of Thought](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-of-thought) [[15]](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-of-thought)
- [Define Success Criteria](https://platform.claude.com/docs/en/test-and-evaluate/define-success) [[9]](https://platform.claude.com/docs/en/test-and-evaluate/define-success)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) [[16]](https://github.com/anthropics/anthropic-cookbook)

### Evaluation
- [LangSmith Evaluation Concepts](https://docs.langchain.com/langsmith/evaluation-concepts) [[7]](https://docs.langchain.com/langsmith/evaluation-concepts)
- [LLM-as-a-Judge](https://docs.langchain.com/langsmith/llm-as-judge) [[17]](https://docs.langchain.com/langsmith/llm-as-judge)

### Tools
- [FastAPI](https://fastapi.tiangolo.com/) [[10]](https://fastapi.tiangolo.com/)
- [Vercel](https://vercel.com/docs) [[18]](https://vercel.com/docs)

---

## References

1. OpenAI. "API Documentation." https://platform.openai.com/docs

2. OpenAI. "Chat Completions Guide." https://platform.openai.com/docs/guides/chat-completions

3. Anthropic. "Prompt Engineering Overview." https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

4. Brown, Tom B., et al. "Language Models are Few-Shot Learners." arXiv:2005.14165, May 2020. https://arxiv.org/abs/2005.14165

5. Wei, Jason, et al. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." arXiv:2201.11903, January 2022. https://arxiv.org/abs/2201.11903

6. Lewis, Patrick, et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." arXiv:2005.11401, May 2020. https://arxiv.org/abs/2005.11401

7. LangSmith Documentation. "Evaluation Concepts." https://docs.langchain.com/langsmith/evaluation-concepts

8. Dunlap, Lisa, et al. "VibeCheck: Discover and Quantify Qualitative Differences in Large Language Models." arXiv:2410.12851, ICLR 2025. https://arxiv.org/abs/2410.12851

9. Anthropic. "Define Your Success Criteria." https://platform.claude.com/docs/en/test-and-evaluate/define-success

10. FastAPI. "First Steps Tutorial." https://fastapi.tiangolo.com/tutorial/first-steps/

11. OpenAI. "Chat API Reference." https://platform.openai.com/docs/api-reference/chat

12. OpenAI. "Models Overview." https://platform.openai.com/docs/models

13. OpenAI. "OpenAI Python SDK." https://github.com/openai/openai-python

14. OpenAI. "OpenAI Cookbook." https://github.com/openai/openai-cookbook

15. Anthropic. "Let Claude Think (Chain of Thought Prompting)." https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-of-thought

16. Anthropic. "Anthropic Cookbook." https://github.com/anthropics/anthropic-cookbook

17. LangSmith. "LLM-as-a-Judge Evaluator." https://docs.langchain.com/langsmith/llm-as-judge

18. Vercel. "Documentation." https://vercel.com/docs

---

*Cheatsheet created for AIE9 Session 1: Vibe Check*
*Last updated: January 2026*
