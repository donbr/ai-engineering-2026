# Session 1: Vibe Check

> Check the Vibes on Your LLM Application

---

## Goal

Understand LLM prototyping best practices, learn how to add context naively, and get introduced to evaluations through vibe checks.

---

## Learning Outcomes

By the end of this session, you will be able to:

1. **Understand** course structure, certification requirements, and how to succeed on Demo Day
2. **Connect** with your peer supporter and journey group for collaborative learning
3. **Explain** LLM prototyping best practices including prompt engineering fundamentals
4. **Apply** few-shot learning and chain-of-thought prompting to improve LLM outputs
5. **Implement** context engineering by adding relevant information to prompts
6. **Evaluate** LLM outputs using vibe checks as an introduction to systematic evaluation

---

## Tools Introduced

| Tool | Purpose |
|------|---------|
| OpenAI GPT Models | Foundation language models for text generation |
| OpenAI Python SDK | Programmatic access to GPT models via chat completions API |
| FastAPI | Modern Python web framework for building API backends |
| Vercel | Deployment platform for frontend applications |
| Vibe Check Evaluation | Qualitative assessment method for LLM outputs |

---

## Key Concepts

### 1. What is an LLM Application?

An LLM application combines a large language model with additional context, tools, or systems to solve specific tasks. At its simplest, this means:

- **Input**: User query + context
- **Processing**: LLM generates a response
- **Output**: Formatted answer to the user

The key to building good LLM applications is **context engineering** — providing the right information to the model.

**Reference**: [OpenAI API Documentation](https://platform.openai.com/docs)

---

### 2. The Chat Completions API

The OpenAI Chat Completions API uses a message-based format with three key roles:

| Role | Purpose |
|------|---------|
| `system` | Sets the model's behavior and personality |
| `user` | Contains the human's input |
| `assistant` | Contains the model's previous responses |

Understanding this message structure is foundational to all LLM application development.

**Reference**: [OpenAI Chat Completions](https://platform.openai.com/docs/guides/chat-completions)

---

### 3. Prompt Engineering

Prompt engineering is the practice of crafting effective inputs to get desired outputs from language models.

> **"Prompt engineering is the core skill of AI engineering."**

**Key principles:**
- Be specific and clear in your instructions
- Provide relevant context
- Use structured formats when helpful
- Iterate based on results

**Reference**: [Anthropic Prompt Engineering Guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)

---

### 4. Few-Shot Learning

> **"Scaling language models dramatically improves few-shot performance... tasks and few-shot demonstrations specified purely via text interaction with the model."**
> — Brown et al., 2020 (GPT-3 Paper)

Few-shot learning means providing examples in the prompt to guide the model's behavior. Instead of fine-tuning, you demonstrate the desired pattern:

**Structure:**
```
Here are some examples:

Input: [example 1 input]
Output: [example 1 output]

Input: [example 2 input]
Output: [example 2 output]

Input: [your actual input]
Output:
```

The model learns the pattern from the examples and applies it to new inputs.

**Reference**: [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)

---

### 5. Chain-of-Thought Prompting

> **"Generating a chain of thought — a series of intermediate reasoning steps — significantly improves the ability of large language models to perform complex reasoning."**
> — Wei et al., 2022

Chain-of-thought (CoT) prompting asks the model to show its reasoning, not just the answer:

**Without CoT**: "What is 23 * 17?" → "391"

**With CoT**: "What is 23 * 17? Think step by step."
→ "Let me work through this:
   23 * 17 = 23 * (10 + 7)
   = 230 + 161
   = 391"

CoT dramatically improves performance on math, logic, and multi-step reasoning tasks.

**Reference**: [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)

---

### 6. Context Engineering (Naive RAG)

Context engineering is adding relevant information to prompts so the LLM can answer questions it wasn't trained on.

**Naive approach:**
1. Take the user's question
2. Add relevant context directly to the prompt
3. Ask the LLM to answer based on the context

```
Context: [relevant information here]

Based on the context above, answer the following question:
Question: [user's question]
```

This is the foundation of Retrieval-Augmented Generation (RAG), which we'll formalize in Session 2.

**Reference**: [RAG Paper](https://arxiv.org/abs/2005.11401)

---

### 7. What is a Vibe Check?

A **vibe check** is an informal, qualitative evaluation of an LLM's output. Before building formal evaluation frameworks, AI engineers often start by manually reviewing outputs to develop intuition.

> **"LLM outputs are non-deterministic, which makes response quality hard to assess. Evaluations (evals) are a way to break down what 'good' looks like and measure it."**
> — LangSmith Documentation

**Vibe check questions:**
- Does the output feel right?
- Is it helpful, accurate, and appropriate?
- What patterns do you notice across multiple outputs?

This human judgment is the starting point for more systematic evaluation.

**Reference**: [VibeCheck: Discover and Quantify Qualitative Differences in LLMs](https://arxiv.org/abs/2410.12851)

---

### 8. From Vibes to Metrics

The VibeCheck research (ICLR 2025) shows that subtle model characteristics ("vibes") like tone, formatting, and style influence user preferences. Systematic evaluation requires:

1. **Define success criteria** — What does "good" look like?
2. **Create examples** — Build golden test cases
3. **Measure consistently** — Apply the same standards
4. **Iterate** — Improve based on results

**Key insight**: Start with vibes, then formalize into measurable metrics.

**Reference**: [Define Success Criteria](https://platform.claude.com/docs/en/test-and-evaluate/define-success)

---

### 9. FastAPI for LLM Backends

FastAPI is a modern Python web framework ideal for LLM application backends:

- **Fast**: High performance, built on Starlette
- **Easy**: Python type hints for automatic validation
- **Documented**: Auto-generated OpenAPI/Swagger docs
- **Async**: Native support for async/await

FastAPI lets you expose your LLM application as an API endpoint that frontends can call.

**Reference**: [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

### 10. Vercel for Frontend Deployment

Vercel provides instant deployment for web applications:

- **Serverless**: No infrastructure management
- **Preview deployments**: Test before going live
- **Edge functions**: Low-latency globally
- **Integration**: Works with any frontend framework

Deploy your "vibe coded" frontend to share your LLM application with the world.

**Reference**: [Vercel Documentation](https://vercel.com/docs)

---

## Recommended Reading

### Essential Papers
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) (May 2020) — The GPT-3 paper introducing few-shot learning
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) (Jan 2022) — How reasoning traces improve performance

### Prompt Engineering
- [Anthropic Prompt Engineering Overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) — Comprehensive guide
- [Let Claude Think (Chain of Thought)](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-of-thought) — CoT best practices
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) — Practical examples

### Evaluation
- [VibeCheck Paper](https://arxiv.org/abs/2410.12851) — ICLR 2025 paper on qualitative LLM evaluation
- [Define Your Success Criteria](https://platform.claude.com/docs/en/test-and-evaluate/define-success) — Anthropic's evaluation guide
- [LangSmith Evaluation Concepts](https://docs.langchain.com/langsmith/evaluation-concepts) — Evaluation framework overview

### Tools & Deployment
- [OpenAI Python SDK](https://github.com/openai/openai-python) — Official Python library
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/first-steps/) — Getting started guide
- [Vercel Documentation](https://vercel.com/docs) — Deployment guide

---

## Assignment

### Part 1: The AI Engineer Challenge
Complete the AI Engineering Bootcamp Challenge to verify your environment and understanding:
1. Clone the challenge repository
2. Set up your OpenAI API key
3. Run the baseline application
4. Submit via the provided form

### Part 2: Vibe Check Your Application
Evaluate your LLM application from the challenge:
1. Test with 5-10 different queries
2. Document what works well and what doesn't
3. Identify patterns in the model's responses
4. Note specific "vibes" (tone, formatting, helpfulness)

### Part 3: Improve the Vibes
Apply the concepts from this session to improve your application:
1. Add a better system prompt
2. Try few-shot examples for a specific task
3. Implement chain-of-thought for complex questions
4. Add relevant context to improve answers

### Deliverable
Record a Loom video (5-10 minutes) demonstrating:
- Your baseline application and its current "vibes"
- The improvements you made
- Before/after comparisons showing the impact
- What you learned about prompt engineering

---

## Advanced Build

### Quantify Your Vibes
Go beyond qualitative assessment:
1. Create a rubric with 3-5 criteria (accuracy, helpfulness, tone, etc.)
2. Score 10+ outputs on each criterion
3. Track scores before and after your improvements
4. Calculate improvement percentages

### Build an Evaluation Pipeline
Automate your vibe checks:
1. Create a test dataset with expected outputs
2. Build a simple scorer function
3. Run automated evaluations on prompt changes
4. Log results for comparison

### Explore Model Differences
Use the VibeCheck methodology:
1. Test the same prompts on different models (GPT-4o, GPT-4o-mini, etc.)
2. Document qualitative differences
3. Identify which "vibes" matter for your use case
4. Choose the best model based on your criteria

---

## Quick Reference

### Environment Setup
```bash
pip install openai fastapi uvicorn python-dotenv
```

### Environment Variables
```
OPENAI_API_KEY=your-api-key
```

### Basic Chat Completion Pattern
```python
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

print(completion.choices[0].message.content)
```

### Few-Shot Prompt Template
```python
messages = [
    {"role": "system", "content": "You classify sentiment."},
    {"role": "user", "content": "Great product!"},
    {"role": "assistant", "content": "Positive"},
    {"role": "user", "content": "Terrible experience."},
    {"role": "assistant", "content": "Negative"},
    {"role": "user", "content": "It was okay I guess."},
]
```

### Chain-of-Thought Trigger
```python
# Add to your prompt:
"Think step by step before giving your final answer."
```

---

*Session Sheet for AIE9 Session 1: Vibe Check*
*Last updated: January 2026*
