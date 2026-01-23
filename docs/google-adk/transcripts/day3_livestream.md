# Day 3 - Livestream Transcript

---

Hello everyone. I'm K. I'm one of the hosts of five days of AI agents intensive course. I'm here with Anand. Anand why don't you say hi?

Hi everyone. Welcome to uh day three and uh I'm looking forward to host you for the with Kunch for the rest of this live stream.

Thank you. Welcome welcome everyone. We are truly honored to have all of you back here on the third day of the series for context engineering sessions and memory management. We have been super excited and grateful to see all of the collaborations partnership across the platform. We have seen community helping each other. We have seen community starting their own capstone courses already.

So we are super excited to see all of the momentum that is this has generated and thank you for the thoughtful questions, follow-ups and feedbacks. We really appreciate it. This is what we want from the community. The collaboration, the learning and the sharing. As a reminder, you we have now we are now pro at this. I think [laughter] we have started uh the course all week long.

You would be getting assignments which are white papers with our code companion podcasts and codelabs. Code labs are basic to advanced and they are of course one some are mandatory and some are optional. And towards the end of the course Brenda Flynn will be joining us and announcing the capstone project.

So you could start and show your newly built agent building skills and the live stream em seminars are so helpful for the community. so they can hear from the experts every day. As we previously mentioned, there are three avenues you would get this information. Uh if you have registered, you would get an email. If you haven't, please do follow the content page or the discord announcements channel.

So let's just jump into it. Sorry. Um this is not possible without the moderator community. The discord channel has been a stream of information and these folks have held it together. I would like to call out Brenda, Colon, Rey, Melissa, Kenal, Anan, all of us have been able to, you know, answer the questions, keep the engagement going.

So, please do hop in with them, answer questions, ask questions. So, we would love to encourage the participation. So the we are in day three. So we are at a midpoint. By now you already are aware of defining an agent. We have talked about the hands and highs of how you would give it to the agent. And today is super important. Google is fundamentally a company that organizes information.

AI in this context is finding relationships between the information, between concepts and getting faster. And I am super excited to have this session which is context engineering sessions and memory. You uh you probably already read the white paper and it is super dense and I'm here looking forward to see what Anand has to say. An why don't you give us an overview?

Thanks Kunch. So yes uh um I hope you have been reading the white paper for today. uh and I'll just give a quick overview of what um it entails to pave the way for the rest of the conversation in the Q&A session. So as Kunch mentioned in day one you saw the agents core loop and the architectural components and the kind of agents as well as some examples.

In day two you gave the the tools to the agent to help it interact with the external world via protocols such as MCP as well as customdefined um uh tools. And now in day three, it's about time we give our agent some memory so it doesn't have amnesia every time it talks to you. [gasps] So in day three, we are tackling context engineering sessions and memory.

So since LLMs are fundamentally stateless, building intelligent agents that remember requires us to dynamically assemble the perfect context window for every single turn. As you know, even though models like Gemini have a quite a large context window, it's still finite. And this uh leads to the core of the white paper.

So, we started off the white paper with sessions, the short-term workbench that hold the immediate conversation history. Uh and then we discussed the need for compaction strategies, for example, recursive summarization or tokenbased truncation to prevent what we call context rot and keep sessions from overfling the window or driving up costs for you.

Um since a lot of LLM's uh uh um price uh LM's pricing is based on costs of token costs as well. So then we move to long-term memory, the organi organized filing cabinet for persistent knowledge which you also read in a substantially big section of the white paper. Unlike standard rag which retrieves static global facts, memory is dynamic, user specific and evolves over time.

Think of it like personalization. So the paper also detailed the active memory ETL pipeline which consists of extracting key fats from facts from noisy dialogue using an LLM and then consolidating them to resolve conflicts and then finally merging duplicates and keeping the knowledge base knowledge base fresh.

We also differentiated between uh declarative memory which is knowing facts and procedural memory which is knowing how to do things and then highlighted critical production considerations specifically ensuring memory generation is a nonb blocking background operations to avoid lag and rigorously redacting PII to maintain user trust.

That and is is the white paper in a nutshell, but I highly recommend going through these podcast if you haven't already and then going uh through um the white paper in detail um and also perhaps loading up the white paper in notebook LM and creating mind maps, audio overviews and video overviews to help you navigate and ask questions as well.

we have the notebook LM's um PM uh the head PM of notebook LM Stephen joining us so you'll hear from him later but yeah that would be it for the white paper off to you Kunch for the Q&A

thank you an from amnesia to having memory I love that so let's jump into Q&A um we are super excited for this meat of the session uh which is very popular by the way so um let's jump into the expert hosts who are joining us from internal to Google and from our external speaker as well Jay, Stephen, Kimberly and Julia on stage please.

Hi everyone. Thank you. Thank you so much for joining despite your busy schedule. It has been it this is the most popular session. the community loves it and we are super excited to have you all here to share and learn from you. So, thank you.

Um so, um Jay um why don't you go first with a quick intro.

Incredible to be here. Thank you for having me. Really excited to be a part of this. Uh my name is Jay Alamar. I'm the co-author of Hands-On Large Language Models uh for O'Reilly. And we're also currently, we just announced a book on agents called an illustrated guide to AI agents.

Also director at cohhere where I get to build uh the LLMs that power sort of the next generation of uh so happy to sort of be sharing what we learn along the way with with the incredible Kaggle community.

Thank you for being here Jay and this session is um complete with having from multiple different faces and you uh representing the model world so thank you for joining Stephen why don't you give us a quick intro

yeah hi everyone it's great to be here my third time uh at this event u I'm an old-timer uh I uh I'm Stephen Johnson uh my title here at Google is I'm I'm kind of the founder co-founder of of notebook notebook LM am now editorial director at Notebook LM and Google Labs. Um before I came to Google, I spent most of my career as a writer.

I've written 14 books about science and history and the history of innovation. Um I was really inspired by the work that I was doing as a researcher, as a writer to uh to come to Google and build and build notebook LM.

Thank thank you for joining and uh we have been prescribing notebook LM across the whole course. So the whole content is now notebook LM.

We love it. We love it. Thank you.

And for those for those of you who are listening and haven't tried loading up your white papers in notebook LM yet, try out the mind map feature. My personal favorite uh and the video overviews, the new stuff.

Video is the one which I love it. So thank you. [laughter] Uh Kimberly, why don't you go next?

Hi everyone. Um I'm Kim Milm. I am a software engineer at Google. I'm also the tech lead of agent engine memory bank and lastly I'm also the author uh one of the authors of the day three uh white paper context engineering sessions in memory.

Thank you Kimberly and it's a 72page doc white paper but it's great which covers all the details. Thank you for being here Julia. Last but not the least. Hey everyone. Much like Stephen, I've been here the third time. Really excited to be back. I'm Julia Visinger. I am a PM at Google.

I kind of look over the agent ecosystem and cover things like uh ADK which I think you all have spent quite a bit of time playing with this week. Uh I was also the uh author of the original agents white paper that we included in the first version of this course and have uh led some of the work for function calling for Gemini. So, I've been thinking about agents for probably about seven years now.

Yes. Julia um Julia and Patrick wrote the original. For those of you who haven't read it, do go back and find the agents white paper by Patrick Marlo and Julia Visinger. It it sets the foundation and then we have upgraded that to the day one white paper uh introduction. So,

folks have started loading that already to notebook in the comments. I see it because they are like okay this is the first white paper and this is the third white paper what changed so thank you for doing that so let's jump into the questions and the first question Stephen this is for you

oh um Ananda why didn't you take this go forward I knew you had prepared for this

yes I'm always so excited to talk anything but notebook LM Stephen so what have what has the notebook LM team been working on in the agentic world, how do you manage large contexts in it?

Yeah, I mean this two great questions actually I'll take them in reverse order I think.

Um so in a way from the very beginning we have thought of notebook as a in a sense of like consumerf facing UI for context management right it's it's you load up the documents that you were working with you are putting them implicitly into the context of the model so that the model is then grounded on the information that you provided which allows you to personalize the model it allows you to reduce hallucinations all the all the great attributes that come from source grounding as we call it.

Um, and so we've we've we kind of built the whole UI to give even kind of non-coders control direct control over what is in the context of the model. Um, so one of the most powerful versions of that is like next to every source, not only can you add the sources and control the sources, but you can uh choose to focus the model on specific sources um just by selecting them.

Um, and so you can be like, look, I I've got 50 or a hundred different papers in here, but right now I just want to generate a mind map or an audio overview or I want to have a chat just with this one source. And so you can select it. Um, that's just a super powerful tool that you know, if you're a power user of notebook, you're probably already using it as it is.

We have done a lot of work behind the scenes on the the underlying context window. So we now are running all users get access to the full um kind of million token uh context window if it's needed if you have that me that that much uh source material that you're working with. Um which is a big step forward. It's amazing.

You can put the whole collected works of Shakespeare in there and it just the model can kind of see all that information. It's it's extraordinary. We're also doing a lot of like really interesting stuff behind the scenes with Rag um in if the user exceeds the contacts.

So we're we're basically generating alternate versions of the query um which then retrieves different passages um so that we get the the best sample. If you have you know 50 million words of information in your notebook which amazingly you can have we want to make sure we get the most relevant passages and bring them back.

Um so that's just happening behind the scenes uh just by using notebook elem you don't even need to think about it as a user. Um, in terms of the agentic stuff, it's we really want we we really want notebook the Gemini inside of notebook, the AI inside of notebook to have a full sense of the app itself, like all of its tools. Um, so right now the user decides I want to create an audio overview.

Um, I want to create a mind map. But we think actually that the AI in chat should be able to suggest those things and actually trigger those things and say things like hey given your questions like you should really create a custom audio overview here on this particular topic using the critique format. It sounds like that's what you're looking for. Do you want me to build that for you?

Uh so we think that that that we haven't integrated that yet. We're kind of experimenting with it but we think that's a really powerful direction to explore.

Wow. Uh I'm thinking just about having a personal assistant which is like you know what use this custom prompt and let me use this passage I can create something cool for you that would save so much time instead of manually having to think about this. That's

one of the things that's really cool on is there we have a kind of a featured notebook that everybody sees called introduction to notebook and basically the AI in that notebook is an expert in how to use the product and so you can go in and say hey I'm a lawyer I'm working on this particular like you know brief and I've got a lot of deposition text here that I'm working on like how can I use this product and it will give a detailed explanation customized for that particular use case like saying oh this is how you should use it this is how you should set up your sources blah blah blah.

So, it's there's a hint of that kind of agentic future in that particular featured notebook. Um, but you're going to see a lot more of that in the coming year.

Thank you. Thank you, Stephen. That was amazing. Uh, to everybody who's listening, hopefully you get some inspiration also, more inspiration for your capstone project. Maybe you make the a new new notebook in your capstone project and then share it with Stephen. [laughter] All right. Thank you, Stephen. Thanks a lot for your insight. Uh pan shall we move on to the second question? All right.

So what kind So Julia, this is for you. What kind of exciting features are on the horizon for context engineering and scaled memory man management in ADK specifically ADK?

Yeah, thanks so much. Uh so for me particularly context is super super exciting especially when you start to combine it with tool use and memory. Um there's so many opportunities around personalization and and things that we can do in this space and we also realize it's a area that the community has been super actively requesting.

Uh lots of feedback around it and I want to just take a little bit of a step back before I look forward. So [snorts] in the last couple weeks we've released a ton of really really exciting things that I think people still have yet to discover. So from simple things like uh context caching to more simple context management techniques, think about compaction, truncation etc.

Um but one of the most exciting things I think for me that we recently added in was actually something that we learned from some of our internal work with uh folks building on ADK internally. We needed a way essentially to keep the user message clean for auditing purposes for kind of production for scaling.

And so we actually created kind of a very clean split of of of components that the model will ultimately see within the framework. So we have what's called a static instruction which is kind of the core identity. It's the the system instructions and many other kind of frameworks. It's the non-negotiable safety policies, the JSON schema, etc. Um ADK can cache it.

Um and um I think that's a like a fairly well-known piece.

And then we have the end user message obviously which is the thing that is kind of your user's voice right um and it's end user typed and we keep it really clean from a logging and eval perspective and then lastly we added what we call a turn instruction which in many senses you could see kind of as your application's voice um it is the controller owned message that your backend will generate for every single request and it's um for kind of dynamic and and per turn steering.

We found this really interesting and exciting because it really has helped um customers externally as well as internally um keep these pieces separate, log these things over time and actually kind of um um scale their their agentic use cases from there. So I think uh that that's something that's really exciting to me.

But moving forward now, I think you'll continue to see us invest heavily here in a couple of different areas. Uh think about more dynamic context. So as some of the things that Stephen was talking about as well with regards to notebook LM supporting developers wanting to build those type of capabilities so you can inject that context in a more dynamic way.

The model kind of figures it out to provide that end experience for the user. And then secondly a part that I'm really looking forward to leaning into more because I think there's a huge amount of opportunity here is memory. Uh really ensuring that the journey to smooth out how memory personalizes these experiences for customers over time.

I think is is is something that you'll continue to see us lean heavily into work closely with Kim's team and and really ensure that there's a really cool journey and and opportunities there. So, lots of lots of exciting stuff on the road map.

Julia, um one thing you mentioned was context caching, but I wonder if some of our users might not be familiar with that concept. Would you mind giving like a quick 15 second summary on what context caching is? Essentially, context caching is the ability to um store the context and then inject it. Uh so essentially that the LLM doesn't need to be called that you can store it and you can inject it um um at runtime when it's necessary.

So it's faster and cheaper then.

Exactly. You hit the uh you hit exactly the two the two key benefits for me.

Yes. And um for those of you who want to know more details about the more fundamental LLM components like context caching and such, please check out the previous courses foundational model paper and uh my first white paper there has a lot of details around uh prefix caching which is context caching and a bunch of other techniques. Um thanks a lot Julia that was very insightful a lot. Seems like ADK is really shaping up to be the framework for to to to rule it all. [laughter]

All right.

Well, we we we want to hear that from our users. So,

so yeah. Cool. All right. Uh then let's go on to our next question, K. So, this is for you, Jay. Um memories are often stored in vector databases for semantic similarity, but also in knowledge graphs for relationships. So are there any scenarios where a hybrid approach for example using both of these um vector databases as well as graphs would be necessary for an agent?

That's a great question. There's a lot of kinds of memory systems that are possible and really your use case your end use case that you're sort of trying to build for is what determines what the right memory system is. there isn't one architecture for memory or system design that ev that works for every agent roll out and we're still in the early sort of stages.

Um, and that's why you start to hear about a lot of the topics covered in in in in the in the content so far are how the the industry is finding sort of its way. So, first how to deal with context. You have short context and you have long conversations.

how to do short-term memory of compaction as we've heard um and to carry over relevant information uh into the the current uh context longer term memory. So that we can think of that as as short-term memory. Longer term uh memory there's some inspiration that people can take from how human brains work.

uh things like episodic memory and semantic memory and procedural procedural memory that encode different kinds of of of information and retrieve them differently. But you can one way maybe that is convenient to think about memory system is to abstract them as this system where you can add a a memory you can retrieve a memory or you can uh update a memory if something is relevant.

Now when you're retrieving or searching you can think of that as a search system and you can add whatever we know from search systems into that uh a lot of people when they s first started to build rag systems they started with a vector database but it turns out that's good for a lot of use cases but it's not enough.

It's really better to have a hybrid system of both keyword search as well as but then you look at actual search engines out there and they have re-rankers. They have tons of rerankers uh that improve all kinds of signals that are beneficial for for the retrieval of that of that use case. U so don't limit yourself to sort of these initial sort of models.

the the model can be uh the system for retrieval can be as sophisticated as we know how to build search systems. Uh and that does have a room for um rerankers, keyword search as well as graph uh databases and and graph encoded information.

I think one interesting thing with memory is also that retrieval comes into play in two different spots. There's retrieval when you're actually using the memories with your agent, which is probably what most people think about, but then there's also retrieval when you're doing that update process or consolidation. Um, and for that, a graph-based approach would be very useful because then memories aren't like a siloed entity and are more connected and have that relationship between them.

Exactly. And I I love the both the answers because um uh like graph-based database from personal experience graph rag as we call it uh can really incorporate the human domain knowledge as well. But then sometimes uh uh um that's that's too much context or sometimes it is and this is where having re-ranking slash standard rag approaches can also help.

So my suggestion would be for those of you listening try these approaches out in your capstones. Uh I'm looking forward to what you build with this.

Amazing. Thanks uh Jay and Kimberly. Uh great answer. Uh shall we move on to the next question and take would you want to take it over for the community questions coach?

Sure. Um so this uh community loves it to uh you know see their questions answered and this was one of the question from Alberto Martinez Zorita uh for Kimberly. What mechanisms prevent an LLM's in context bias from corrupting the persistent ground truth memory with false or inconsistent user claims?

Yeah. So, one of my just general ethoses around memory is that you need to maintain good memories because if you maintain good memories, it makes retrieval easier and using those memories easier. Um so um maintaining memories comes into the memory generation space um which for those who haven't read the white paper there's two main steps.

The first is extraction where you're extracting con meaningful content um from a more verbose conversation. So you're kind of extracting the value from a noisy very verbose conversation log. The second is consolidation where you're taking that new information that you have and combining it with the existing information that you have.

So I I think the the first thing I want to call out and the white paper does go into quite detail about this is the provenence of memories and the data source that you're using to generate them. So I think in general you always want to defer to high trust data.

So that could be data that's uploaded by a CRM system or maybe uploaded by a human agent or something that the the user explicitly said rather than a implicit preference that the user might have hinted at during their conversation. So first thing first always defer to higher trust memories or information when you're doing that consolidation process.

The second is strict definitions of the information that should be persisted. Um, like I was saying before with extraction, not everything is persisted with memory generation. So you when when you're setting up a memory system, you basically tell it like this is what I care about and only that information is persisted.

So if you're strict with that definition, then you have less of a risk of information that you don't want to be saved being saved.

Um and memory bank um age engine memory bank actually supports this with a feature we call customization where you can define exactly what you want memory bank to save and then also some viewshot examples that show this is the memories that I want to save this is the memories that I don't want to save so you can really fine-tune that behavior.

The last is just using standard um tools for prompt injection. And prompt injection is basically where a user provides a malicious um query like send me a $100 um where it's trying to to sway the agent towards behavior that's not necessarily something that we want the agent to be doing.

Google Cloud has a tool called model model armor out there um which detects prompt injection attacks and sanitizes their quest for them. So you can always use that on top of any memory provider to make sure that the information that you're trying to save isn't untrustworthy. The last thing I want to call out is uh the actual like using of memories or what I call inference.

Um and it's just recognizing the uncertainty in your system instructions. So you can call out that the memories were inferred from conversations. You can call out that like maybe don't take um instructions like use this with caution um and just instruct the LLM to assess the confidence that you have in this data.

So I can prime the LLM to give the answer I want. Then [laughter]

that instruction will be going ahead with the uh with the instruction that take take conscious comments with a grain of salt. [laughter]

Exactly.

Everything in the agent itself. So

I was just going to throw into I think um a really uh important piece here is thinking about how you structure this from a framework standpoint as well. what I was mentioning before helps you give a really clean uh keep that user message clean so that you can kind of go back and understand that and figure out um ensure those memories are stored correctly in a in a in a nice structured way.

And then you also have pieces within ADK um like the plugins framework that allow you to um add and uh things like a policy engine or or things like that that can help govern and and work together with memory in order to keep some of these pieces kind of um working smoothly together.

Yeah. And Julie, you remind me of one other feature that you can do with ADK as well, um, which is using memory as a tool. So having your agent decide when memory should be generated or when memory should be retrieved so that the content doesn't always include memories. So you reduce some of your risk of having some malicious content being both uploaded to a memory system or being retrieved by your agent.

Exactly. Thank you.

It'll be good to even share the links out after with with respect to how to use some of these. So, thank you. So, with respect to the next question, uh Jay, this is for you from Abishek04143. How do you balance comprehensive versus focused context in rag to avoid model confusion? what metrics beyond relevance score measure context utility.

So it's good to think about rag as multiple steps. So there's a retrieval step and that's what you'd be able to uh measure with with metrics like relevance like how many of these documents are are relevant to this question or to this context in in the context of memory.

So that is one uh one area and where relevance is one but you have an entire literature and research area of information retrieval that gives you all kinds of of different metrics to measure different things and different metrics are more useful for for different scenarios or different situations. And so there's so much of that on the retrieval side.

Then there's a part of it that is not retrievable which is more on the generative side and that measures how this model deals with whatever information that you've you've delivered to it and how much of it did you bring the top three results and injected that into the context or did you bring the top 20 results and and injected those into did you bring summaries of the documents or did you dump entire 15page PDFs in there?

Um does the answers do do does the context actually have the information even though they are the most relevant documents to the question do they in fact contain the answers that the question has seek that is not a guarantee there as well and so rag is like a lot of LLM capabilities or agentic capabilities you can think of them as a collection of many subbehaviors and so this other way of measure measuring the the the the generative model uh the closer you are measuring it to the end use case that you're actually going to deploying be deploying it in the better the higher value this this metric will be to actually measuring the end performance that you will you will have uh and so this part is called we we sometimes is called grounded generation so given that there is a context of a specific how useful is is the output and you can evaluate that with an LL LM as a judge.

You can ask an LLM saying I gave this context to a a a model. It gave me this answer. These were its instruction. Rate this on the metrics that I care about. How useful is it? Does it contain information that is for example outside of the context that is incorrect?

And so thinking about it as as these two two ways and there are also in the grounded generation field there are metrics you can look at. um a rag evaluation uh libraries like ragas for example that gives you metrics like like faithfulness like how faithful is the answer to the context actually being being provided.

Uh most state-of-the-art models will generally be good but it's good for you to own um a little bit of that and sort of catch if there's any regression on a specific use case on a specific version of the model. uh that will be very useful for you to sort of have a a comprehensive understanding of of of the use case for um in that rag deployment.

I I almost feel like some of these answers are like staged appropriately because like the next uh white paper which we are going to be taking care of is evaluation where LLM and the judges one of the key things. So the speakers are staging up our papers in the days [laughter] accordingly. So thank you for you know sharing the insight. Um the the next question is for Julia uh from Suraj Mar 1229.

When managing long conversations what is the critical tradeoff that dictates whether an agent should simply truncate the session history?

Yeah. So, the trade-off that you're constantly making is a trade-off between cost and context, right? Um, on the one side, you've got the ability kind of for the session history to be truncated, which is at the end of the day more cost-effective. It means you're cutting off older parts of the conversation. It means, you know, um, you're getting rid of some of some of those pieces.

Maybe you're storing them into something like a memory bank. But this approach kind of is a bit risky in the sense that it's indiscriminate and it kind of risks deleting some of that crucial information that might be relevant to a future conversation or to a later part of the specific conversation. So that's uh kind of the the the the more cost-effective side.

Now if you're looking at something more sophisticated, you would probably turn to something like more sophisticated compaction. So think of um context preservation through um recursive summarization.

So you would condense kind of the conversation history uh over time using another model in the background um and injecting that then um into into the into the LLM's context um and to the agents context. That of course requires another LLM uh to create those kind of summaries.

And at the end of the day, between those two kind of components, you're really trying to make the decision on are you prioritizing immediate or are you prioritizing the idea of minimizing a cost or are you prioritizing kind of higher quality contextually aware conversations?

And at the end of the day, a lot of that comes down to are you trying to do something fairly simple or are you really trying to go into complex multi-turn, multi-agent uh tasks where you need more sophisticated compaction strategies in order for that agent to remain effective.

I think one benefit though of using compaction um and specifically the more mature advanced um compaction strategies like summarization or long-term memory management is that even though you need that additional LLM call to do the summarization or the memory extraction, you're only processing that input once to extract what's meaningful from it and then using that more condensed version multiple times.

So although you do have an additional LLM call that's hopefully running in the background so you don't have that latency and it's also taking what's meaningful and using that for the future so that you're not unnecessarily processing the same information over and over

agree and I think that they do in the code labs one of the things which Christopher highlights is also that so I'm sure folks are experimenting so The the last question uh for Stephen. Could AI agents u this is from sorry by the way DH Kiter 66895. Uh could AI agents use narrative structure to organize long-term experience essentially using state storytelling for state management?

You know this is such a terrific question. Um, and I've actually in a couple internal docs that I've written over the last couple months I've used exactly this storytelling metaphor. Um, so the reason why it's so important is particularly with a tool like notebook, but I think this is true for a lot of different other kind of use cases.

Like one of the main ways in which people use notebook LM is as a space for their projects, right? So, you're a student. You've got your course readings for the semester. You're trying to master something, get a good grade at the end of the semester. You put it into a notebook, and that's where you do your thinking and your reading and your research and so on.

You're a lawyer, you're preparing a brief, it's going to take six months to put it all together, whatever. The thing that's important about a project is that it changes over time, right? There's you're at the early stage of a project, you're at the middle stage of the project, you're at the end of the project, and the state of the project is an evolving thing.

And things that happened earlier in that story are generally less relevant than things that happen more recently. But every now and then, like in all stories, there's some really important event that happens early in it that you want to keep in your memory. You keep coming back to. It's an important foundational thing.

And so if you work with an AI that just knows the details of everything that has happened over the course of the project, but doesn't organize it into some kind of chronological narrative- like story where some things are more important than others and there's a sense of a timeline that you are making progress and advancing towards your goals.

If the agent just knows all the information but hasn't organized it that way, it doesn't really work. like you I and I see this actually in notebook right now because it's not quite as good as this as as I would like it to be.

Um where sometimes I'll be asking a question or getting asking for advice on something and it'll say oh Stephen you should think about this and I'll be like no dude we solved that problem like a year ago [laughter] like like why are you still obsessed with that? And it's because it's not fully seeing it in that kind of narrative timeline.

And so there is a sense in which like our work in building these tools is a kind of storytelling or we have to like create a a narrative in the mind of the model for them to really be as helpful as we want them to be.

Thank you. And looking forward to you know having an advanced storytelling with notebook. We enjoy um that's one of our favorite products. So

that's that's why I know you love the word storytelling Stephen. That's why this question is for you. Yeah, thank you. Right on. Teed it up for me. I appreciate it.

Yeah. So, but before we wrap up, like is there any final thoughts you would want to share? Like, you know, we will start with Julia, you are in my screen first. Do you want to jump in?

Yeah, I think for me the next kind of phase of of where we go with generative AI really is around context and memory um and personalization that brings all of those kind of key components together and makes these experiences magical in many senses for users.

And I think that's really the part that's really exciting for me where we're building towards um and why this space is particularly interesting to me um and and and what motivates me in many senses every single day. Thank you, Kimberly. You are next in this one.

Uh, awesome. So, I think as you probably all can tell from this conversation, there's a lot of tradeoffs when we think about both implementing a memory system and then also using it with your agent.

Um, so I encourage you if this makes you interested in some of those trade-offs, um, to to read through the day three white paper because we do walk through a lot of those trade-offs with more more detail. Um but I think in general it backs up my assertion that it is easy to do memory poorly. It is very very hard to do memory well. [snorts]

Yes. Thank you Kimberly. Limitations has been one of the concern across our you know days with yesterday with tools and today with the memory as well. So looking forward to if you haven't read the white paper highly suggest please do. Stephen, you are next on my screen.

You know, it's just such an important topic. Um, and it really gets to why I I came to Google in the first place.

I mean, I had this dream as a writer of working with software that essentially like could remember everything that I'd ever read and everything that I'd ever written so that I could sit down on my computer and start working on an idea and the software would say, "Hey, you know, you read something highly relevant to this like 14 years ago [laughter] and here's the summary of it and let's think about how this could integrate with um you know, what you're currently working on right now at this moment." And like that was a complete fantasy three years ago.

I mean it was no no computer in the world could do that. And now I have a notebook that has like you know millions of quotes from books that I've read and all all the complete text of my books and I I'm able to do that in a way that's just continuously amazing. And it's all about context management basically.

Thank you Stephen. uh you kind of contradicted there I think because uh initially you didn't want the previous year's context versus now it's like 14 years ago context and that's why it's important for us to be able to um prioritize and understand which memory is important in that relevant

yeah I think I think is about putting context in context

context

and that's the difference between prompt engineering and context engineering

[snorts]

Thank you. Um Jay, final thought from you.

Yes, two two quick ones. One is to tell the community, shoot for the sky. Uh LLMs and agents would not be here without a lot of the collaboration that happened happened in Kaggle over the last decade or more. Uh fine-tuning a lot of these ideas came from from Kaggle pioneers, uh Jeremy Howards and and and others.

And so what you can build can be very uh transformative for for the future of agents and AI. And then the second one is to say uh ask yourself when you're tackling problems, what would Stephen do?

And in this case like if your mind was blown the first time you heard a podcast from from from Notebook um like I am and we're sitting here and this technology exists and we don't uh act like it's it's the most incredible thing out there in the world.

Think of how a lot of information out there or content there is some sort of a of a step or a formula or a pipeline to arrive at the best sort of formulation of it where it's a pipeline that is augmented by by models and once you really nail the pipeline you can have agents sort of go in and and steer it a little bit more. So that's part of the problem sort of exploration but yeah I'm a a huge fan.

So, thank you for

tagline is sorry tagline for this session. Think what Stephen will do. [laughter]

That's actually really not good advice. I got to tell you.

So, [snorts] I took out ADK notebook LM uh and all of the stuff that we discussed today is really powerful tools. So, I'm looking forward to what everybody builds with it. Thanks for joining us everyone.

Thank you. So it's great to have all of you here to have a meaningful conversation and you being available for the call is really good. We have two more segments by the way but uh thank you speakers for joining and being here and participating in this session despite your busy schedules. It's been truly an honor to having all of you.

Anand now we are jumping into code labs but before by like you know Chris comes on stage why don't we just do a pulse check on where the community is logging in from today.

Um I I don't if you saw this there has been a lot of requests on YouTube asking us to change the time slot um I wish we could uh but some of this is set already but I think for the future sessions we do need to take it in consideration. So thank you for vising that by the way to the

yeah and however we have heard your voice about the resource issues that they encountered in the first couple of days and as promised yesterday they should have been fixed now so you should not have the resource error so most of you should not have

yes and we do uh constantly watch uh all the platforms so thank you for rising it and we do take that seriously and we will consider it uh but unfortunately this uh time has been set for this uh sessions for other logistic other logistical reasons. Oh, why don't we have Christopher on the stage?

Hi there. Hello everyone. [snorts]

Hi Chris.

Hi and welcome. And so in this part of the session, we're going to dig a little bit into the code labs. Uh my name is Chris Overhalt and I'm a developer advocate here at Google. Uh I work very closely with agent development kit specifically the documentation the tools ecosystem and especially the thirdparty tools uh and all of the open source activity.

So I'm super happy uh to walk you through some of the day three material today. You may remember me from day one when we talked about your first agent in ADK uh and different agent architectures. And just a super quick note, you may have noticed in some of the communications that Sam Path was going to present today.

Uh we had a last minute change uh in his schedule and so I'll be presenting in his place, but I highly recommend that you go, you'll find links to SPath social media. And Sath is always posting really cool articles about uh new features in Gemini and some of the latest things going on in ADK. And he also authored these notebooks that we're walking through today. So thank you, Sath.

Uh and we'll carry through uh with that today. So if you go to the landing page for the resources today under day three, you're going to see context engineering sessions and memory. So a lot of the things that were covered in the QA, we're going to be looking at code and implementations of that in ADK and you're actually going to get a chance to do that hands-on.

So super cool uh content discussed in the in the Q&A section. There are two notebooks, one on sessions and one on memory. So, I want to take a few minutes to walk through each one of those notebooks so that you can kind of u the the assignments you were sent out, you'll know what to expect. Um, if you've done them already, we can kind of walk through highle concepts.

If you haven't done them already, that's okay. We're going to walk through and look at some key points in the notebooks and also cover some highle concepts that'll map to exactly what some of the speakers were talking about uh in the Q&A. So let's dig in to the first notebook. So the first of two notebooks for today focuses on sessions and session management.

And so in this notebook, you're going to learn about what are sessions, how do they show up in ADK, and really the whole point of this is how do you build stateful agents? So, if you've ever worked with a generative model or an AI agent, one of the most annoying things is when you have to constantly repeat yourself in a conversation or when you start a new conversation.

Uh, and it gets really old having to tell it, you know, this is my name, this is my job, this is where I live. And so, if you think about the user experience, sessions are really, really important because they are conversations. And you probably won't want to have one conversation with your agent. You probably want to have many.

and you probably want to have them over the course of a few days or weeks or even years as end users are using your product. So, we're going to talk in this notebook about how to use sessions, uh how to store state and how to do context management. So, if you scroll past if this is your first time using Kaggle notebooks, there's some tips about how to do that and some videos about getting API keys.

So, we'll assume that you've done that already and we'll go down to the actual start of the notebook in section two. So session management, let's just take one minute to talk about what does it mean to have sessions and why are they important. So when you interact with a generative AI model and you make API calls to it, those calls are inherently stateless.

So that means if I make one call and a second call, the second call will have no idea what I mentioned or what the results of the first call was. This is where sessions come in. So if you're using ADK and you spin up an agent and you start up ADK web, you'll see in the top right there's a session ID. So that is your conversation ID. Why is this important?

And in the first notebook, we'll talk about sessions. You can think of sessions as short-term memory or and this is where your conversation is actually happening. So what's inside of a session? A session has events and state. And if you kind of look at a diagram of that, you have your agent, your user, and your session.

And that specific conversation means these events are things like user input, the agents response, making a tool call. So maybe you had to do a Google search along the way uh or you uh called an MCP server. These are all different events that are happening within your session. State is kind of like a scratch pad where we're storing key values.

maybe the name of the user, where they're from, things like that. So in ADK, there's something called session services and runners. And you'll see this showing up in the code, this simply means that your session service is what is driving the management of those sessions. And the runner is what actually executes the agent.

So if you look at this in code and we say, let's build our first stateful agent. So the nice thing about this is you build your agent, you add tools, then when you get to the point of hey I need to think about multiple users and multiple conversations over time. This is exactly when you'll care about sessions.

So first we will in the notebook you'll create an agent and then you'll instantiate this in-memory session service and just by doing that when we put that into our runner we now have sessions and so we can test that. I like to test that because it becomes really clear of what sessions uh are important for and what they're not important for.

So if we have a first conversation turn like, "Hi, my name is Sam. What's the capital of the United States?" And then we send a second conversation turn to the agent. Hello, what is my name?

In the response, you can see the second conversation turn and response said, "You told me your name is Sam." So that's happening because the session's being managed by ADK and we made those two conversation turns within the same session. So far so good. So we have memory within that given session. Now there's some optional exercises. I highly recommend you do it.

It'll kind of prove to you how these sessions work and what's stateful and what's not. So if I actually stop this agent and here I do that by restarting the kernel or or restarting the notebook uh here in Kaggle. If you actually run all of these cells except the one we just ran where we told it our name and I say what did I ask you about earlier and remind me what's my name?

Uh in this case we ran through uh all the cells so it knew that. But if I restarted and did not tell it my name it would basically say I don't know who you are. Uh and so that's exactly the problem we're trying to address is how do we make uh sessions uh persistent between agent restarts. So that's exactly where database session services come in.

And so in ADK we're very modular in how we help you prototype very quickly. That's what the in-memory session services for. But we have other session services. The database session service is one and then Vert.Exi agent engine is another. So these are ways for you to store your session history somewhere persistent whether that's on disk or somewhere in the cloud. So we show you how to do that.

Uh you instantiate the database session service instead of the in-memory session service. And just like that we can verify persistence. So again in the notebook we ask what you know here's my name what's the capital of the United States. uh you can do the same test to see um where that uh where the session data is persisted and where it's not here because it's a database service.

If you restart the notebook and run your session history will be there. So now we're actually writing that to disk. Um another neat thing you can do in this notebook is you test session isolation. So if a if if I come later as the same user and start a new session and I ask what is my name, it won't know that because so far we've only scoped things to the session level.

Uh and finally, you can actually poke around and see how this data is stored session wise by looking through some of the SQLite data. Another part of this notebook that's really important is context compaction. Uh some of the speakers talked about that in the Q&A section.

This is where instead of storing the entire session history and everything that was said, ADK has a method, an eventbased way of compacting uh this session history. So the notebook walks you through how to use this event compaction config. It's really simple to use. Give it a couple of configuration parameters about how often to compact and how much the session should uh the turn should overlap.

And just like that, there's an example here of where we ask some very verbose, we ask some questions that give a lot of output. Uh, and then after you go through all of that output, we show how ADK is actually compacting that information down so that we don't have to store all of that raw session history. So you think of this as like summarization and context compaction.

That way when you need to recall something, you don't need to send all of those tokens back to the model. Um once you've done that uh we then talk about how to work with session state uh and you do some exercises in here that actually show rather than storing the entire conversation history can I just extract meaningful variables out of this.

So those are state variables like the user's name, their location, their preferences. Uh so there's some good exercises in here on how to do that. and I'll skip to the end and we basically say um here is how you can store session state variables and use them at different points in the session.

So really nice way to work with sessions interactively and the takeaway from this should be sessions are important for as as conversations and I need to think about how my end user is going to want or what will they expect when they start a new conversation with your agent. So with that, there's a lot of links in here to the ADK documentation about session management.

And this leads naturally into the second notebook, which is all about memory. So in terms of memory, the biggest difference that you need to know about notebook one and notebook two is notebook one was about short-term sessions. Notebook two is about long-term storage of memories.

So in this case we talk about how memories can be used across multiple conversations uh and we talk about why do you need that. So again if your user comes back a week from now they will not have their previous conversation the previous session open you need to do things like recall important preferences uh semantic search across memories and this notebook is all about that.

So a few key points in this notebook. I'll skip to the part where the notebook starts here in the memory workflow. There's a memory service. So just like there's a session service for managing sessions, there's a memory service for managing memories. You can store those memories with an in-memory memory service or you can store those in something like Vert.exai memory bank.

And so just a couple of examples to show. If you initialize the memory service and attach it to your agent, then when you have a conversation with your agent, um you can actually look let's look at an example of that. So we start a conversation. We say this is my favorite color. Can you write a poem? Uh and then we go and we can actually see the session events that were happening.

And we wrote a new function called add session to memory. So you can decompose that when you go through the notebook. This is the key step that takes your session history and writes it to memory. So then when you go to memory retrieval, this is the part your user actually cares about. Um there are a couple of pre-built functions like load memory and preload memory.

And the notebook walks through how to use that. I'll show one quick example here and then as you go through the exercise, you'll go a lot deeper. But basically here we give a tool to our agent called load memory. And now whenever we interact with our agent say what is my favorite color the agent will actually use a tool load a memory and be able to answer the user's question.

The last part of this notebook is important because it has to do with uh automatically handling memory storage. So long story short is that there are a lot of callbacks in ADK that you can use. These callbacks can happen before the agent runs, after the agent runs or uh before and after model or tool invocations.

Uh but the main thing here is we can easily create a callback to save things to memory and then we hand that to our agent and this line right here does exactly that. So now whenever I have a conversation with my agent, it's automatically going to load uh and save those memories without me having to do any extra method calls.

So hopefully by the time you get through these two notebooks, you'll have a way better understanding of this. These are what sessions are. These are what memories are. And you'll pick up some really good patterns to implement in your agents. Uh so that your users can have the best personalized experience and long-term memory experience with your agent.

Uh so with that, I hope you enjoy day three activities here and we look forward to seeing you in the ADK community. I'll hand it back to Kunch and Anant to take us to the next section. Thank you.

Thank you, Chris. Um thank [clears throat] you for the last minute switch. uh you did amazing and both the notebooks credit to sat he did an excellent job walking through short-term long-term memory. So thank you

absolutely.

Now on to our favorite part of the session which Anand and I love pop quiz and the the community loves it too. I see the things um answers going

stream the stream of answers we get in on YouTube that uh in last

amazing. Yeah. All right, let's get started.

Yeah. So, everyone uh testing your knowledge on this white paper. First question, which analogy best describes the difference between a session and memory as used in the agent architecture? Your options are A, a session is a library of books. Memory is a single page. B. A session is a temporary workbench while a memory is an organized filing cabinet. C.

A session is long-term storage where memory is a short-term cache. D. A session is for facts. Memory is for user preferences. So, think about it and answer will be shown in

I popping in.

Yeah. Uh some of you got it. Yes. Three, two, one. Answer is B. um at least in the agent architecture this is what we mentioned in the white paper. Moving on to the next question. What is context engineering? Now this should be pretty straightforward. Uh but let's move on to the options. Is context engineering a the process of fine-tuning a model on a specific domain data set?

Or is it B the dynamic assembly and management of information within an LLM's context window?

or is it C the practice of writing static system instructions for a chatbot kind of in the direction that uh Julia was mentioning earlier or D the hardware optimization used to increase the the size of an LLM's context window okay I see this some of you a lot of you got it right so the answer is 3 2 1 B that's essentially we talked a lot about that right also like putting context in context as Stephen mention um uh and as well as like context compaction strategies to all of this with man Julia and Kimberly mentioned.

So great perfect. Um and moving on to the next question. What is the key functional difference between declarative and procedural memory? For those of you who listen to my course overview, this should be a no-brainer. Uh and the options are A declarative is for short-term facts but procedural is for long-term facts.

B declarative is stored in vector databases while procedure is stored in SQL databases. C declarative is knowing what procedural is knowing how. Um or D declarative is generated by users but procedural is generated by the LLM. So think about it. tell you though some of the answers I feel like ah this could be it that [laughter] could be it so

the detail lies in the nuance uh can't this is why rag models are not the best to answer Q&As's all the time [laughter] uh all right perfect so the answer will be shown in three two one the answer is C um it's in the white paper but also I mentioned the course overview so I saw a lot of answers. So, we got this.

Yes. Glad everybody's listening carefully. All right, moving on to the next question. What is the primary goal of memory consolidation in a memory manager? This is a bit tricky, but uh think about it. Your options

so

that's true. [laughter] Your options are A to merge new information with existing memories by resolving conflicts and dduplicating data. B to speed up the retrieval of memories using caching or C to encrypt memories before they are stored in the database or D to compress the raw session logs into a smaller file format. So think about what Kimberly mentioned today in case we haven't read the white paper yet. Uh and uh all the

video um

exactly [laughter] all right the answer would be shown in three two one a we discussed a lot about context compaction summarization uh all of that so this goes in that direction. All right, let's move on.

The code labs though I hope that like I see the answers coming but hopefully the code labs would make you um understand the concept better.

And you have designed this course to be like all the white papers, code labs, the questions and the Q&A to be very closely knitted to in sync with each other. So to reinforce your concepts and knowledge and experience um all through our course so yeah let's move on to last question. Kunch. How does rag differ fundamentally from memory in an agendic system? Your options are A.

Rag acts as a personal assistant knowing the user while memory acts as a research librarian knowing the global facts. B rag is for dynamic user specific context while memory is for static external data. Or C rag acts as a research library knowing global facts while memory acts as a personal assistant knowing the user. So opposite of option A or D there is no difference.

They are interchangeable terms for the same technology. You can use one or the other. Um

yes. Um this will really test your knowledge of memory and wagon what you have learned. Um so let's show the answer in three two one and your answer is B. So this is a metaphor but um hope you uh understand what rag and memory are meant for different purposes and you read more about this

by the way.

Yes. So if you ever want to explain it to your uh to to somebody a friend of yours who does not understand um these concepts very well. This is where I would recommend you start using an analogies to explain concepts. Big fan of that. All right. Perfect. Then this is the last question for the day. Um very great to have you all here and I'm looking forward to hosting you for tomorrow same time same channel right Kunch

yes we have now learned how to build an agent how do you add eyes and ears how to add memory and how tomorrow under the hood of an agent and I think this is very interesting and the white paper is super well done so looking forward to see the white papers code labs punk companion podcast all of you can try it tomorrow with agent quality observability topics. See you all. Thank you.

See you. Bye.

Bye.
