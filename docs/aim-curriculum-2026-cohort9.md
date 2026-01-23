---
title: The AI Engineering Bootcamp Course Schedule & Curriculum v0.9
source: https://absorbing-toaster-713.notion.site/The-AI-Engineering-Bootcamp-Course-Schedule-Curriculum-v0-9-2b1cd547af3d8075a0a4f67621f18898
author:
  - "[[absorbing-toaster-713 on Notion]]"
published: 2025-12-31
created: 2025-12-31
description: A tool that connects everyday work into one space. It gives you and your teams AI tools—search, writing, note-taking—inside an all-in-one, flexible workspace.
tags:
  - clippings
  - ai-makerspace
  - bootcamp
  - cohort9
  - curriculum
---
![](https://absorbing-toaster-713.notion.site/image/attachment%3A995413a3-01b9-4d6c-9d68-720d7b9df4a9%3A2025-11-19_streamyard.png?table=block&id=2b1cd547-af3d-8075-a0a4-f67621f18898&spaceId=d7a211dd-f900-47ac-8e0e-f6b027cb71b3&width=2000&userId=&cache=v2) ![🧰 Page icon](https://notion-emojis.s3-us-west-2.amazonaws.com/prod/svg-twitter/1f9f0.svg)

This course will teach you production agent engineering, and we’ll rely heavily on the [LangChain platform](https://blog.langchain.com/series-b/), which we believe is the best among [all of them](https://www.youtube.com/playlist?list=PLrSHiQgy4VjFiw_PPVp18afekcArQse2F).

As they say, “ Building reliable agents requires a new approach, one that combines product, engineering, and data science thinking.”

We strive to achieve this ideal within a single course through our unique approach to [building , shipping , and sharing](https://aimakerspace.io/about-us/) .

You’ll love this course if:

1) You love building and going deep on foundational concepts and code,

2) You learn best with accountability, and

3) You’re ready to go on an adventure with a [journey group](https://curiouslionlearning.com/why-group-learning/#Two_Types_of_Groups_Journey_and_Destination) for the next 10 weeks with people just like you, led by one of our expert certified AI Engineers

### TL;DR Curriculum

| Agentic RAG (2 weeks) | 1\. Vibe Check 2. Dense Vector Retrieval 3. The Agent Loop 4. Agentic RAG |
| --- | --- |
| Complex Agents (2 weeks) | 1\. Multi-Agent Applications 2. Agent Memory 3. Deep Agents 4. Deep Research |
| Evals/Systematic Improvement (1.5 weeks) | 1\. Synthetic Data for Evals 2. Agentic RAG Evals 3. Advanced Retrievers |
| AIE Certification Challenge (1.5 weeks) | 1\. Industry Use Cases 2. Full Stack Agent Apps 3. MCP Connectors |
| Production Deployments (2 weeks) | 1\. Agent Servers 2. LLM Servers 3. MCP Servers & A2A 4. Guardrails & Caching |
| Demo Day (1 week) | 1\. Semi-Finals/Rehearsals 2. Demo Day |

#### What is AI Engineering?

AI Engineering refers to

the industry-relevant skills that data science and engineering teams need to successfully

build, deploy, operate, and improve Large Language Model (LLM) applications in production environments

.

#### Evals for Success

In practice, Agent Engineering requires understanding how to prototype and productionize.

During the prototyping phase, we want to have the skills to:

Deploy End-to-End LLM Applications to Users

Build Agentic RAG Applications

Build Deep Agents

Build Multi-Agent Applications

Monitor Agentic RAG Applications

Build and Implement Evals for Agentic RAG Applications

Improve Retrieval Pipelines

When productionizing, we want to make sure we have the skills to:

Build Agents with Production-Grade Components

Deploy Production Agent Servers

Deploy Production LLM Servers

Deploy MCP Servers

#### Ideal Student

This course is designed for e ngineers, developers, builders: people coding  every  day or who want to code every day

This course is not designed for: product managers, executives & leaders, anyone who does not want to write code

#### Prerequisites

The minimum prerequisite for this course is that you can follow the GitHub tutorial and submit [The AI Engineering Bootcamp Challenge](https://aimakerspace.io/the-ai-engineering-bootcamp/aie-challenge/) successfully.

If you struggle to complete the challenge but are committed to becoming an AI Engineer, check out [The AI Engineer Onramp](https://maven.com/aimakerspace/ai-eng-onramp?promoCode=FAST25)

#### Certification

To become a Certified AI Engineer, follow these steps: [The AI Engineering Bootcamp Certification](https://absorbing-toaster-713.notion.site/The-AI-Engineering-Bootcamp-Certification-256cd547af3d808a9c95e8f6efb8fb5a?pvs=24)

TL;DR

≥ 85% on all assignments, cumulative

Certification Challenge (see below)

Demo Day (see below)

## Full Curriculum with All Details Not Shown on Maven

Agentic RAG (2 weeks)

| Learning Outcomes | New Tools | Recommended Reading | Assignment |
| --- | --- | --- | --- |
| Session 1: Vibe Check Check the vibbety vibes on your peers, the LLM app you built during your application process, and how even naive updating of context can have a big impact!\- Understand course structure, how to become a certified AI Engineer, and how to succeed on Demo Day! - Meet your peer supporter and journey group! - Learn LLM prototyping best practices and how to add context naively - Introduction to evals with vibe checks | LLM: [OpenAI GPT models](https://platform.openai.com/docs/models) Frontend: Vibe Coded Backend: [FastAPI](https://fastapi.tiangolo.com/) Deployment: [Vercel](https://github.com/vercel/vercel?tab=readme-ov-file) \*Recommend to add $50 in OpenAI API credits now | [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) (May 2020) [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) (Jan 2022) | Vibe Check The AI Engineer Challenge Advanced Build: Improve the vibes, re-evaluate |
| Session 2: Dense Vector Retrieval Understand RAG from first principles, in concepts and in code \- Introduction to Context Engineering, RAG, and the LLM application stack - Overview of embeddings and similarity search - Learn to add context using a vector databases - Build a RAG (dense vector retrieval) application from scratch in Python | Embedding Model: [OpenAI embeddings](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings#:~:text=*%2D-,ada,-%2D*%2D001) Orchestration: [OpenAI Python SDK](https://github.com/openai/openai-python) Vector Database: Custom | [RAG](https://arxiv.org/abs/2005.11401) (May 2020) [The LLM Application Stack](https://a16z.com/emerging-architectures-for-llm-applications/) (June 2023) [12-Factor Agents](https://github.com/humanlayer/12-factor-agents/tree/main) (June 2025) [Retrieval](https://docs.langchain.com/oss/python/langchain/retrieval), by LangChain | Build a Pythonic RAG application Advanced Build: Add one or more optional ”extras” to the RAG pipeline |
| Session 3: The Agent Loop Understand what an “agent” is and how to use the latest abstractions for building production-grade agents fast \- Understand agents and the foundational agent loop - Learn the core constructs of LangChain - Learn the key components of building agents in LangChain, including create\_agent and middleware | Orchestration: [LangChain](https://docs.langchain.com/oss/python/langchain/overview) Vector Database: [QDrant](https://github.com/qdrant) | [ReAct](https://arxiv.org/abs/2210.03629) (Oct 2022) [LangChain 1.0](https://blog.langchain.com/langchain-langgraph-1dot0/) (Oct 2025) [Philosophy](https://docs.langchain.com/oss/python/langchain/philosophy), by LangChain [Component Architecture](https://docs.langchain.com/oss/python/langchain/component-architecture), by LangChain [Context Overview](https://docs.langchain.com/oss/python/concepts/context), by LangChain [Context engineering in agents](https://docs.langchain.com/oss/python/langchain/context-engineering), by LangChain | Build your first agent (e.g., agentic RAG) application using LangChain Advanced Build: TBD |
| Session 4: Agentic RAG Look under the hood of agentic RAG and the create\_agent abstraction - Learn the core constructs of low-level orchestration using LangGraph - Understand how to set up tracing, view traces, and monitor performance | Orchestration: [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) Monitoring: [LangSmith Observability](https://docs.langchain.com/langsmith/observability) | [LangGraph 1.0](https://blog.langchain.com/langchain-langgraph-1dot0/) (Oct 2025) [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph), by LangGraph | Build an agent using LangGraph and monitor with LangSmith Observability Advanced Build: TBD |

Complex Agents (2 weeks)

| Learning Outcomes | New Tools | Recommended Reading | Assignment |
| --- | --- | --- | --- |
| Session 5: Multi-Agent Applications Understand when to add additional agents to optimize context and how to construct agent teams using typical patterns.\- Understand multi-agent systems, and typical multi-agent patterns - Learn when to add more agents to optimize context - Visualize, debug, and interact with your agent applications | Visualization, Interaction, and Debugging:[LangSmith Studio](https://docs.langchain.com/langsmith/studio) | [Don’t Build Multi-Agents](https://cognition.ai/blog/dont-build-multi-agents) (June 2025) [Context Rot](https://research.trychroma.com/context-rot) (July 2025) [Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents), by LangGraph | Build a multi-agent application that generates reports using multiple teams Advanced Build: Add a [custom SQL agent](https://docs.langchain.com/oss/python/concepts/memory) to the team |
| Session 6: Agent Memory Understand how to build agents capable of managing both short and long-term memory stores - Understand short vs. long term memory in agentic systems and how to manage them - Learn the two primary methods for agents to write memories: in the hot path (e.g., during runtime) and in the background | n/a | [Memory Overview](https://docs.langchain.com/oss/python/concepts/memory), by LangGraph | Build an agent that leverages both short-term and long-term memory systems Advanced Build: TBD |
| Session 7: Deep Agents Understand how to build complex agents that operate over longer time horizons.\- Learn the four key elements of Deep Agents and how to implement them, including planning and task decomposition, context management, subagent spawning, and long-term memory - Learn to use skills with DeepAgents | Orchestration: [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview), [deepagents-cli](https://github.com/langchain-ai/deepagents/tree/master/libs/deepagents-cli) | [Deep Agents](https://blog.langchain.com/deep-agents/) (July 2025) [The Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) (September 2025) [Doubling down on DeepAgents](https://blog.langchain.com/doubling-down-on-deepagents/) (Oct 2025) [Using skills with DeepAgents](https://blog.langchain.com/using-skills-with-deep-agents/) (Nov 2025) | Build an agent that can plan, manage context, delegate, and remember Advanced Build: Create [skill.md](http://skill.md/) file that the agent can discover and load dynamically |
| Session 8: Deep Research Understand how to deep research systems work under the hood and how to build them.\- Learn the lessons that the LangGraph team has learned building open deep research - Understand the three step process for conducting research: scope, research, write | [Open Deep Research](https://github.com/langchain-ai/ope) [Deep Research from Scratch](https://github.com/langchain-ai/deep_research_from_scratch) | [Learning the Bitter Lesson](https://rlancemartin.github.io/2025/07/30/bitter_lesson/) (July 2025) [Deep Research Bench](https://deepresearch-bench.github.io/) | Build an unrolled open source deep research clone Advanced Build: TBD |

Evals/Systematic Improvement (1.5 weeks)

| Learning Outcomes | New Tools | Recommended Reading | Assignment |
| --- | --- | --- | --- |
| Session 9: Synthetic Data Generation for Evals Understand how to generate test data automatically to test agentic RAG applications when you don’t have any eval datasets.\- Learn to generate high-quality synthetic test data for AI applications using LLMs - Understand the knowledge graph approach used to generate data - Understand the process of metrics-driven development - Learn to load datasets into LangSmith when generated elsewhere | Testset Generation:[RAGAS](https://docs.ragas.io/en/stable/getstarted/rag_testset_generation/) Evaluation: [RAG ASessment](https://docs.ragas.io/en/stable)[, LangSmith Evaluations](https://docs.langchain.com/langsmith/evaluation) | [All about synthetic data generation](https://blog.ragas.io/all-about-synthetic-data-generation) (Nov 2024) [Mastering LLM Techniques: Evaluation](https://developer.nvidia.com/blog/mastering-llm-techniques-evaluation/) (Jan 2025) | Create test data and evaluate agentic RAG application Advanced Build: Reproduce the RAGAS Synthetic Data Generation Steps - but utilize a LangGraph Agent Graph, instead of the Knowledge Graph approach. |
| Session 10: Agentic RAG Evaluation Learn to set up and implement effective evals for agents and RAG applications.\- Build an Agentic RAG application with LangGraph - Learn to evaluate RAG and Agent applications quantitatively with the RAG ASsessment (RAGAS) framework - Use metrics-driven development to improve agentic applications, measurably, with RAGAS | Reranking: [Cohere Rerank](https://cohere.com/rerank) | [Self-Refine](https://arxiv.org/abs/2303.17651) (Mar 2023) [RAGAS](https://arxiv.org/abs/2309.15217) (Sep 2023) [Lessons from Improving AI Applications](https://blog.ragas.io/hard-earned-lessons-from-2-years-of-improving-ai-applications) (May 2025) [In Defense of Evals](https://www.sh-reya.com/blog/in-defense-ai-evals/) (Sep 2025) | Evaluate an agentic RAG application using RAG and Agent metrics Advanced Build: TBD |
|  |  |  |  |
| Session 11: Advanced Retrievers Learn best practices for retrieval and a systematic approach for deciding on the best retriever for your AI applications.\- Understand how retrieval, chunking, and ranking can enhance context given to agentic RAG applications - Understand today’s best practices for retrieval - Learn to systematically compare the performance of retrieval algorithms | Retrievers: [L](https://docs.langchain.com/langsmith/deployments) [angChain Retrievers](https://docs.langchain.com/oss/python/integrations/retrievers) | [BM25](https://www.nowpublishers.com/article/Details/INR-019) (2009) [Reciprocal Rank Fusion](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf) (2009) [Semantic Chunking](https://x.com/GregKamradt/status/1737921395974430953?s=20) (2023) | Build a RAG application and evaluate different retrieval strategies Advanced Build: Implement [RAG-Fusion](https://arxiv.org/pdf/2402.03367) using the LangChain ecosystem. |

AIE Certification Challenge (1.5 weeks)

| Learning Outcomes | New Tools | Recommended Reading | Assignment |
| --- | --- | --- | --- |
| Session 12: Industry Use Cases Understand the state of production LLM applications and leading use cases and hear from expert practitioners around the AI Makerspace community \- Understand typical use cases for production LLM application throughout industry in general - Hear from industry practitioners around the AI Makerspace community about what they’ve been building for clients and customers! - Overview of the Certification Challenge | n/a | [Session 3: End-to-End AI Applications & 2025 Industry Use Cases](https://absorbing-toaster-713.notion.site/26acd547af3d80b4b646e2fd6f1fd31c?pvs=25) (AIE8, Sept 2025) [How People Use ChatGPT](https://openai.com/index/how-people-are-using-chatgpt/) (Sept 2025) [Anthropic Economic Index report](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report) (Sept 2025) | The Certification Challenge 1. Define Problem & Audience 2. Propose Solution 3. Deal with Data 4. Build E2E Agentic RAG Prototype 5. Create Golden Test Data Set 7. Assess Performance |
| Session 13: Full Stack Agent Apps Learn to build and deploy local end-to-end agentic RAG applications with open-source models - Understand how to use and locally host the newest open-source LLM and embedding models - Build an end-to-end agentic RAG application based on a specific use case using everything we’ve learned so far | LLM: TBD Embeddings: TBD Frontend: Vibe Coded Backend: [FastAPI](https://fastapi.tiangolo.com/) Inference & Serving: [ollama](https://ollama.com/) | [The AI Engineer Challenge](https://aimakerspace.io/aie-challenge) | Continue Certification Challenge |
| Session 14: MCP Connectors Learn how to leverage collections of tools to enhance retrieval by sitting on the client side of MCP servers.\- Understand how to use MCP to enhance retrieval - Learn about the pros and cons of leveraging MCP on the client side | MCP: [Model Context Protocol](https://github.com/modelcontextprotocol), [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters) | [MCP Announcement](https://www.anthropic.com/news/model-context-protocol) (Nov 2025) [About MCP](https://modelcontextprotocol.io/about) (from the spec) [MCP](https://docs.langchain.com/oss/python/langchain/mcp), by LangChain | Build an agentic RAG application that can retrieve resources via MCP |

Production Deployments (2 weeks)

| Learning Outcomes | New Tools | Recommended Reading | Assignment |
| --- | --- | --- | --- |
| Live Session 15: Agent Servers Learn to deploy complex agent applications to production endpoints that you can use elsewhere.\- Learn to package, build, and deploy agents with tool and data access directly to a production API endpoint - Understand how to use the API in full-stack end-to-end applications | Deployment: [LangSmith Deployment](https://docs.langchain.com/langsmith/deployments) \* \*Requires $30-40/month | [LangSmith Deployment components](https://docs.langchain.com/langsmith/components) [Agent Server](https://docs.langchain.com/langsmith/agent-server), by LangSmith | Deploy a production-ready agent to an API endpoint Advanced Build: Provide tool and data resources through an MCP server |
| Session 16: LLM Servers Learn to deploy remotely-hosted open LLMs and embedding models to use in your agent applications.\- Understand how to deploy open-source LLMs and embeddings to scalable, remote, production-ready endpoints - Learn how to use leaderboards to pick the best OSS models - Learn AI Makerspace’s picks for the best OSS models today | LLM: TBD Embeddings: TBD LLM Serving & Inference: [Together AI](https://www.together.ai/) \* \*Requires $50 for credits | [LLM Leaderboard](https://artificialanalysis.ai/) (current) [Embedding Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) (current) [MTEB](https://arxiv.org/abs/2210.07316) (Oct 2022) | Deploy open LLM and embedding model endpoints to remote APIs Advanced Build: TBD |
| Session 17: MCP Servers & A2A Learn to set up MCP servers and enable public communication between agents.\- Understand how to set up your own MCP servers - Understand Agent2Agent Protocol (A2A) and how to enable A2A communications between remote and client agents through agent cards and MCP | Agent2Agent: [A2A](https://github.com/a2aproject/A2A) | [What is MCP?](https://modelcontextprotocol.io/docs/getting-started/intro) (from the spec) [A2A Announcement](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) (April 2025) | Build an agent, then mimic usage of the app with another agent Advanced Build: TBD |
| Live Session 18: Guardrails & Caching Learn a few upgrades: for performance and security/trustworthiness.\- Understand guardrails, including the key categories of guardrails - Understand the importance of semantic caching - How to use Prompt and Embedding caches | Guardrails: LangGraph custom implementation Caching: [CacheBackedEmbeddings](https://docs.langchain.com/oss/python/integrations/text_embedding#caching) and [Prompt Caching](https://docs.langchain.com/oss/python/langchain/models#prompt-caching) | [The AI Guardrails Index](https://www.guardrailsai.com/blog/introducing-the-ai-guardrails-index) (Feb 2025) [Caching](https://planetscale.com/blog/caching) (July 2025) [Semantic Caching for Low-Cost LLM Serving](https://arxiv.org/html/2508.07675v1) (Aug 2025) [Guardrails](https://docs.langchain.com/oss/python/langchain/guardrails), by LangChain | Build guardrails and set up semantic caching for an agent Advanced Build: TBD |

Demo Day (1 week)

| Learning Outcomes | New Tools | Recommended Reading | Assignment |
| --- | --- | --- | --- |
| Session 19: Semi-Finals Compete with your fellow cohort members for the top 18 spots that will present live on Demo Day during this full dress rehearsal | n/a | [Demo Day Selection Process v0.2](https://absorbing-toaster-713.notion.site/2a9cd547af3d809a9f42cca35c86fc2c?pvs=25) [AIE8 Demo Day Rehearsal Run of Show](https://absorbing-toaster-713.notion.site/2a3cd547af3d80d9aa05fe012b51644f?pvs=25) | Prepare for 1) rehearsal of 10-min Demo Day presentation and 2) 90s pitch |
| Live Session 20: Demo Day Present live in 1 of 18 final spots or support your fellow cohort members! | n/a | [AIE8 Demo Day Invite on LinkedIn](https://www.linkedin.com/events/7389781271427735552/) [AIE8 Demo Day Run of Show](https://absorbing-toaster-713.notion.site/2a9cd547af3d80229473fb2d72a2ebcc?pvs=25) [The AI Engineering Bootcamp, Cohort 8 Demo Day YouTube Playlist](https://www.youtube.com/playlist?list=PLrSHiQgy4VjEBDUvOzGtUTlAq7SqnFa9n) | Submit your final GitHub repo, slide deck and project data for YouTube |
| Live Session 21: Graduation Ceremony After 10 weeks together and crushing Demo Day, it’s time to celebrate off the record! | n/a | n/a | n/a |
|  |  |  |  |

Other questions? Email

greg@aimakerspace.io