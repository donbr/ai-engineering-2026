# Day 3 - Podcast Transcript

---

Welcome back to the deep dive. Today we're jumping straight into something really fascinating, uh, kind of complex, but super important in AI right now. We're talking about how you actually give a large language model a working brain, something like memory. And our main source for this is the day three white paper from that uh, 5day of AI agents intensive course by Google X Kaggle.

Really great stuff in there. Yeah, if you're thinking about building agents that you know remember who you are, what you like, what you talked about last time, well, this paper is basically the blueprint. Our goal here is to kind of decode the key bits, the architecture you need to turn a basic LLM call into something stateful, persistent, and well, genuinely smart feeling.

Exactly. And to really get there, you have to understand three core ideas. They're all linked, and honestly, they represent a big shift in how we interact with these models. First up is context engineering. Think of this as like the master controller. It's about dynamically grabbing and managing all the right info within the LLM's context window every single time you talk to it.

Okay. Dynamic management. Got it. What's number two? Number two is sessions. A session is basically the container for one whole conversation. It keeps track of the history like chronologically and also the agents sort of working memory for that specific interaction.

The immediate stuff,

right? And then third, there's memory. This is the long-term play. Memory is how you capture a process and uh consolidate knowledge across many sessions. That's what gives you real personalization over time.

Context engineering sessions. Memory powerful trio. Okay, let's unpack that. Start with context engineering. You called it the foundation. It sounds like it tackles the LLM's biggest well weakness.

It absolutely does. It addresses the Achilles heel of LLMs. They are fundamentally stateless. Every API call is like starting fresh. The model has zero memory of the last turn. Its entire awareness is just locked into the context you provide in that specific call. So if you want statefulness, you have to build this uh complex information package dynamically every single time. That's context engineering.

Wow. Okay, that sounds way more involved than say traditional prompt engineering. Prompt engineering often feels like crafting a really good maybe static system message, but context engineering sounds like it's constantly adapting the input. How does that dynamic part really change things?

Well, think of it like this. Prompt engineering is like giving a chef just a recipe. You'll get a dish probably. Okay. Context engineering though is like setting up the chef's mislass. You ensure they have all the right ingredients prepped high quality. That's the relevant context plus the right tools function definitions. And they know your dietary needs user memory.

Ah okay. So it's about preparing everything perfectly for that specific cooking moment, not just the recipe. Exactly. It ensures the model gets precisely what it needs optimized for right now leading to a much better more tailored result.

So context engineering is managing all the data that goes in. That includes the operational stuff like system instructions, tool definitions, maybe fshot examples to guide reasoning.

Precisely. But it's also crucial for the external data. This means pulling relevant bits from long-term memory, fetching documents using arguin retrieval augmented generation, you know, from a knowledge base, and even adding the outputs from tools the agent just used.

And of course, the immediate conversation stuff, the history, the turnbyturn dialogue, any temporary scratchpad info, and the user's latest message. The white paper mentions a big challenge here. Context rot. What is that, and how does context engineering help?

Right? Context rot. That's what happens when the context window gets too full, too noisy. The model's ability to pay attention to the important bits, to reason effectively, it just degrades. Context engineering fights this using uh dynamic history mutation. Basically smart ways to trim the fat summarization. Maybe selectively pruning old returns to keep the signal strong.

That sounds like it has to happen constantly. What does that context management cycle actually look like behind the scenes? Say during a single turn.

Yeah, it's a tight loop. The white paper lays it out. Figure one. First, fetch context. Go get relevant memories, RA docs, whatever is needed. Second, prepare context. This is the crucial bit. It's on the hot path, meaning it blocks the response where you actually assemble the full prompt string. Third, invoke LLM and tools. Send the prepared context off.

Get the response, maybe run some functions. And finally, fourth, upload context. Take any new insights or facts learned in that turn and save them to persistent storage. This last step is usually and should be done in the background asynchronously.

Okay, that makes the session versus memory thing clearer. Steps one to three generates session data, the immediate stuff. Step four, updates the long-term memory. So, the session is like the messy workbench for this project. And memory is the organized filing cabinet for future projects. Makes sense. Let's focus on that workbench. The session,

right? The session is self-contained. It's specific to one user. And it holds the context for just one continuous conversation. It usually has two parts. Events, which is the strict chronological log. User says X, agent says Y. Agent calls tool Z and state, which is more like structured working memory. think uh items in a shopping cart or maybe what step you're on in a booking process.

Got it. And the paper notes that how frameworks handle sessions varies a lot. That sounds like it could cause problems down the line, right? ADK uses an explicit session object with events and states separate. But Langraph does something different. It uses a mutable state object as the session. Why is that important?

That mutability is key because the state object itself can be changed. Langraph can directly implement compaction strategies right there. It allows you to say replace a chunk of old messages within the state object with a summary in place. It simplifies managing long conversations.

Okay, that makes sense for a single agent. But what about multi- aent systems, MAS? How do multiple agents share history or state? The paper mentions shared versus separate histories.

Yeah, two main ways. Shared unified history. All agents basically read and write to the same central log. This is good when agents are working really closely together like an ADK's delegation model. Everyone sees everything.

Downside being maybe it gets cluttered, hard to track who did what

potentially. Yeah. The other way is separate individual histories. Here agents are more like black boxes. They only communicate through explicit messages maybe like an agent as a tool setup. This gives them autonomy but they lose that rich shared context. And that isolation is exactly why you often need that abstract framework agnostic memory layer we me mentioned earlier a way to share synthesized knowledge between these isolated agents.

Right? The filing cabinet needs to be accessible regardless of which workbench you use. Now thinking about production managing sessions must have big security and performance implications. Privacy seems paramount strict isolation ACL that's table stakes. But the paper stresses PII reduction before storage. Why is that timing critical? It's absolutely critical for compliance things like GDPR or CCPA.

Yeah,

you need to scrub personally identifiable information using tools like maybe model armor before that data ever hits your persistent session logs. You can't store it first and redact later.

Okay, makes sense. And data hygiene things like TTL time to live policies.

Yeah, you need policies for how long sessions live and ensuring the event order is always deterministic. And performance is huge because again session data is on the hot path. Retrieving and processing a massive session history slows everything down.

Which brings us right back to compaction. You called it the savvy traveler packing a suitcase analogy. You can't just throw everything in. You hit those limits. Context window size API costs go up. Latency gets bad and quality drops because of that context rot.

Exactly. So you need strategies. Yeah,

the simple ones are like just keep the last end turns a sliding window or uh token based truncation where you literally count tokens backwards from the newest message and chop off the oldest when you hit a limit.

Pretty crude though. What about more sophisticated methods? Recursive summarization sounds powerful. How does that work?

It's clever. You use the LLM itself. Periodically, the system takes a chunk of the older conversation history and asks the LLM to summarize it concisely. That summary then replaces the original messages, usually prefixed to the more recent verbatim turns. You keep the essence, but drastically cut the token count.

But that sounds computationally heavy running an LM just to manage history.

It is, which is why it absolutely must be done asynchronously in the background. You trigger it based on maybe the number of turns or a period of inactivity or maybe when a specific task within the conversation is completed. It should never block the user from getting their next response.

Okay. Async background processing is key for sophisticated compaction that feels like a natural bridge to memory. We're moving from the sessions workbench to the memories filing cabinet. The paper draws a really clear line between memory and RJ. I like the analogy they used.

Me too. ARID is like your research librarian. It's great with static shared factual information. It makes the agent knowledgeable about the world. Memory though is the personal assistant. It deals with dynamic users specific stuff. It makes the agent knowledgeable about you. They work together, but they serve different purposes.

And the types of things stored in memory mirror human memory, right? They talk about declarative memories.

Yeah. The knowing what facts, events, figures, like knowing the user's favorite team or their destination city for an upcoming trip.

Then procedural memories.

That's the knowing how.

Yeah. skills, workflows, like the exact sequence of tool calls needed to successfully book that complex flight itinerary you mentioned earlier. It remembers the process.

How do you typically organize this stuff? Is it just a big list?

Usually more structured. You might have collections, different sets of memories per user or topic or a structured user profile like a quick reference contact card for corefax or maybe a rolling summary, a single document that continuously evolves. And where does this live? Architecturally speaking, vector databases seem common for search.

Definitely, vector DBs are great for semantic search on unstructured memories, finding things that are about a certain topic. But you often see knowledge graphs, too.

Why both? Why the hybrid approach?

Because sometimes you need relational insights. Vector search finds things like X. A knowledge graph can answer how is X related to Y and Z. Think connecting memories about a user, their family members, and their travel plans altogether. You often need both kinds of queries.

Gotcha. And memory scope user level is most common, sticking with the user across sessions. Session level is just for temporary insights from one chat. And application level is global stuff, often procedural, but needs careful handling. Right.

Exactly. Application level memory needs sanitizing. You don't want one user's interaction leaking into a global procedure inappropriately.

What about multimodal images, audio? The source can be multimodal absolutely but the memory itself is typically stored as text. The key insight or fact extracted from that image or audio clip. Text is still the lingua frana for LLM processing and search.

Okay, let's get into the memory generation process. The paper calls it an LLMdriven ETL pipeline. Extract, transform, load. Sounds intense.

It is pretty sophisticated. It starts with extraction. This isn't just summarizing. It's targeted filtering. You define what's meaningful based on the agents purpose. Maybe using rules, topic definitions, examples. A support bot cares about different details than a wellness coach. You're pulling specific signal from the conversational noise.

Okay, so you extract the potentially useful nuggets. Then comes consolidation. This sounds like where the real intelligence happens. Self-editing, handling conflicts.

Absolutely. Consolidation is where the LM looks at new potential memories alongside existing ones. M

he has to decide should I create a new memory,

update an existing one or maybe even delete or invalidate an old conflicting or irrelevant one. This is also where memory relevance decay forgetting is managed.

How does it make those calls? How does it judge trustworthiness or relevance? Does it just guess?

No, it relies heavily on provenence. Where did this memory come from? How old is it? Was it explicitly stated by the user or inferred by the agent? Confidence scores can evolve. If a user mentions their dog Winston three times, confidence goes up. If a memory hasn't been accessed or reinforced in months, its relevance decays. It's trying to mimic that natural process of reinforcing important things and letting trivial details fade.

That sounds computationally expensive. Extraction, comparison, conflict resolution, updating storage, which explains why the paper is so adamant. Memory generation should be asynchronous. Running in the background

100%. If you try to do all that consolidation synchronously while the user is waiting for a response, the latency will be unacceptable. The agent will feel incredibly slow. You respond quickly, then update the memory store behind the scenes.

That's a critical design pattern and it leads nicely into this idea of memory as a tool, letting the agent manage its own memory.

Exactly. It's a more autonomous approach. Instead of relying solely on predefined rules or triggers for memory generation, you give the agent itself tools like create memory or query memory. The LLM can then decide during the conversation. Hey, this piece of information seems important. I should use my tool to save it. Or I need to know the user's preferences here. I'll use my tool to check my memory.

Okay, so we've generated memories. Now, retrieval. We need to get the right memories back into the context for the next turn. The paper says simple vector relevance isn't enough. We need to blend scores.

Right? Just finding the most semantically similar memory isn't always best. You want to blend scores across maybe three factors. Relevance, the similarity score, recency, how recently was it used or created? And importance, how critical did the system initially deem this memory? That blend often gives you much more useful context.

And retrieval strategy is proactive versus reactive.

Proactive means you fetch potentially relevant memories at the start of every turn. It's simple, ensures memory is always there, but might add latency if the retrieval is slow or brings back irrelevant stuff. Reactive is more like the memory as a tool approach. The agent specifically decides when to query memory during its reasoning process. More efficient perhaps, but requires a potentially smarter agent or an extra LLM call for that decision.

Okay, last step, inference. You've retrieved the perfect memories. Where do you actually put them in the prompt you send to the LLM? Does it matter? It matters hugely. Placement signals authority. Put memories in the system instructions. They carry a lot of weight. Good for stable facts like a user profile, but risky if the memory is slightly wrong. It could really bias the LLN's response.

And the other option, injecting them into the conversation history.

That's often noisier. The LLM might get confused and think the memory is something the user or agent actually said in the current dialogue. It can dilute the flow of the real conversation. So, it's a trade-off you have to design for carefully. And finally, testing all this. It sounds complex. You can't just chat with it and say, "Seems better, right?"

Definitely not. You need rigorous testing for generation metrics like precision and recall. Did we capture the right memories? For retrieval, things like recall at K. Did the right memory appear in the top K results? And crucially, latency, you want memory lookups to be fast, ideally under 200 milliseconds. But the ultimate measure is endtoend task success.

Does having this memory system actually help the user achieve their goal more effectively? You often use another LLM, an LLM judge to objectively score this across many test cases.

Wow. Okay, that really covers the whole life cycle. So, let's wrap this deep dive based on the Google XKaggle white paper. I feel like context engineering is the big umbrella discipline here.

It really is. It orchestrates everything.

And sessions handle the immediate conversation, the low latency now. They need isolation and smart compaction to stay efficient.

Yep. The workbench. While memory handles the long-term persistence, personalization driven by that sophisticated ETL cycle. Extract, consolidate, retrieve.

The filing cabinet built carefully over time. Mastering that interplay, that LLM driven ETL is how you shift from an agent that just knows facts, maybe via array, to one that actually seems to learn and adapt to know you.

That really is the key takeaway. Moving from factual recall to personalized assistance. It provides the foundation for building genuinely adaptive AI experiences that grow with the user.

So the framework is clear now. The path to building agents that learn, remember, and personalize is laid out handling the complexities of state through these session and memory systems. The provocative thought then is now that you have this blueprint, what personalized persistent experience are you going to build first? Maybe try implementing that recursive summarization for yourself. It sounds like a great place to start experimenting.
