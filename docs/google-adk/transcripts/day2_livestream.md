# Day 2 - Livestream Transcript

---

Hello everyone, welcome. I'm Ka Patlola. I'm one of your co-hosts for the five days of AI agents intensive course. I'm here with Anan Navalya who would be my co-host as well. An why don't you go and say hi.

Hi everyone. I'm Anant. I'm an AI engineer and uh the founder of this five days of AI series and I'm looking forward to working with K and the rest of the team to give you an exciting live stream session. Thank you. Welcome, welcome everyone to the day two agent tools and oper operatability with MCP. Um and we are super excited to have you all here.

Over the past couple of days, we have seen increased momentum in different social platforms. We have seen you um learning. We have seen you sharing your key takeaways. We are seeing observing community helping each other in discord and other platforms insightful questions which gives us a pause.

We saw one of the act discord user created an issue uh documentation in adk docs and we were a able to immediately resolve it. This is exactly how we want the community to grow and we are so grateful you're all being part of it. Um just as a reminder um you would it would be very similar to our previous assignments.

Every assignment would have um code labs, white papers, in-depth white papers and we would have a podcast summary and you would be able to choose the medium you would want to learn. uh there is a capstone course or towards the end that would be launched on day five where you could test your building skills and you would be able to u check all the content out on your own pace as well.

You don't have to do it uh live but we recommend certainly for the community to help each other to be able to test it out. So please do do that. Uh as mentioned earlier there are three ways for you to be able to get the content. One, if you have registered, you would be getting an email. Two, if there is the learning course website, you would be able to access the content from.

And three, the Discord community announcements, we will be posting it every day um for the next day assignment as well. Um, as I mentioned yesterday, it is a village. It takes 100 plus volunteers to put both all of these content together. Um, I highly recommend you all reach out in the Discord community where these moderators are active. They are answering your questions.

You probably already saw Brenda, Anan, Kolong, Sitha, Urban, um, Eric, all of them posting content, engaging with you. These are folks who are engaged with customers every day and they are here to help you on your learning journey.

So I strongly recommend keep the chat chat active, keep the conversation going and we are here to support you on your journey and this course was designed like as Anand said he has done this previously two iterations.

This is the third time of this event and uh AI agents if I recall correctly Anand it was a one-day agent course and now we are at five days and honestly speaking we could still talk a lot more about AI agents. This is a condensed course as such.

Um we start from defining agents and then we add more color to it and then we see under the hood and then we talk about how do you get it functional and then we release a capstone course. So the course was built to encourage you on your learning journey. I highly recommend you follow the structure so you will get there.

Next today is data and um going from your defining the model how do I add my API key to adding a tool and giving eyes and hands to your agent is going to be an exciting journey but to talk this about this more Anand why don't you jump

thank you K really exciting introduction and yes before I go over to the overview of the white paper I wanted to call Um you've seen some errors of resource exhaustic errors on on discord 429 and that's mainly due to the overwhelming demand which uh and we are working uh to resolve it uh and you will hear from us once it's resolved so it will be fixed so stay tuned.

Um all right then to the white paper. Um so in yesterday's white paper um day one's white paper you learned about basic agents and the agentic architecture the levels of various agents and the various components of agents. In today's white paper, we you will discuss agent tools and interoperability with MCP.

Uh and this white paper basically start off by covering best practices for tool design to ensure reliable performance. That is very critical uh because one of the things that distinguishes agents are tools. The facts that they have hands and eyes to interact with the external world.

And uh further on uh we emphasize that tools should represent granular specific tasks not just generic API wrappers and should ideally have crystal clear documentation because that documentation is the prompt that tells the LM how to utilize that tool to achieve its task. Then further on in the white paper, we address the major industry challenge.

The as I like to call it the NXM or N into M integration problem where connecting every model to every existing tool becomes very unsustainable as it becomes it scales quadratically with the amount of models and tools. So uh and here's where we enter the uh model context pro protocol or MCP as it is better known.

It's an open standard that solves this by decoupling agents from specific tool implementations. You can think of it much like USB for AI or AI agents so to speak. Uh later on uh we also broke down the MCP architecture of hosts, clients and servers and its core primitives, tools for taking actions, resources for reading external data like files or logs and prompts for sharing reusable instructions.

Finally, we examine the critical new security landscape that is being introduced by MCP. And this is something which would be especially critical in in in production workflows for enterprises and anything that goes beyond a demo or prototype would we would benefit a lot from this.

Uh in here we looked at the unique risks like tool shadowing where a malicious tool might trick an agent into using it instead of a legitimate tool. Right? Um, and then we also looked at dynamic capability injection where an agent might suddenly inherit dangerous new abilities without the necessary approvals required to use it.

And all of this coming together hint uh hints together uh hints towards need for strict uh governance um of of of the MCP and the agents which use it. So that's a rough over overview of the white paper.

For those of you who haven't read the white paper yet, I would recommend starting off with the notebook LM generated AI podcast where you get a quick summary and then diving deep and using notebook LM to analyze the the entire white paper or just reading it old school from top to bottom. [laughter] So that's it. Uh we'll be going into the code labs later. Um off to you Kunch.

Oh, thanks Anand. Now, can we have um the Q&A speakers onto the stage? Thank you. Thank you everyone for joining. Really appreciate it despite your busy schedule, taking the time. The community loves it. They want to hear from the industry speakers. We see that in the YouTube live chat. So, thank you for taking the time. Truly honored. And we have an external speaker, Dr. Alex Besn. So, thank you. Why don't we why don't we start with the intros, Dr. Alex?

Yes, thank you for having me. Uh, so I'm a computer scientist and a physicist and I spend almost all of my time thinking about solving the the world's hardest problems with AI. Uh, basically the the thesis is we're on the verge of solving super intelligence to the we haven't already. And I I think a lot about what comes after super intelligence. How do we solve math, science, engineering, medicine, the world's hardest problems with super intelligence, including with super intelligent agents?

Thank you. We are so glad to have you here to share your thoughts and insights to the community. Thank you. Ourel, thank you for joining.

Yeah, thanks. Yeah, thanks for having me. Um, yes, I'm Ourel Vin. I'm uh VP of drastic research and I'm the co- tech lead of the Gemini model uh together with the amazing Jeff Anom and been at Google for believe 12 years and five days. So glad to be here.

Thank you. U it's so great to hear from you all as you were working in the models as well and folks have been testing incredibly with the Gemini models. Uh Edward, why don't you go next? Thank you.

I am Ed Graphinstead. I'm a director of research at Google Deepbind in our Frontier AI unit uh and an honorary professor at University College London. Uh I've been working in deep learning for NLP before it was cool. I feel entitled to say that because of the hipster stash for November.

Um and I've also been working on agents through the medium of reinforcement learning and more recently LLM powered agents while it was cool. So I'm really glad to be here to talk about this. super excited and also thank you for working it when it was not cool as well. Thank you. Oh, Mike.

Yeah, thanks K. Um really happy to be here. This is such an exciting course uh to be part of. Um I have also been at Google for about 12 or 13 years. I'm a a software engineer and a computer scientist. I worked um I'm one of the co-authors of the white paper that you all reading. So along with along with Kunch, if you find any errors or mistakes, you can throw them throw them my way.

Uh I studied AI at Stanford long ago under some of the the leading lights of the AI movement.

Sebastian Thran, Andrew Ing, Fay Fay Lee um many years ago and I've been at Google now for for a long time and I spend most of my time now as a um solution architect helping our customers figure out how to get the most out of our AI technology and build some of these amazing agents that we're all working on.

Thank you.

Very excited to be here with everyone.

Thank you. We are so excited to have you all here and we are going to jump to the meat of it. Uh An why don't you start?

Sure thing K uh so excited to have you and Oriel and Edward the first question is for you too. So uh we've been thinking which exciting frontier LLM driven agents or can you think or where are the uh uh which exciting direction are the front LLM driven agents heading towards in the next few years?

uh what do you in your personal opinion what do you think um uh what do you what do you think that these agents can do to help achieve um AGI uh AGI in the next uh long-term horizon u maybe I start since my name is on the left um so yeah I guess there's two questions there um perhaps selfishly the on the you know where where agents are going.

I'm definitely very excited to see agents that can start to perform the kind of AI and ML research that we've been performing for many years. So in a way like agents that do our science is super exciting. I think it's super exciting because that also obviously would enable the acceleration of um the Gemini model development for instance itself like by by basically automating parts of that process.

So that would be quite quite drastic. Um I mean agents is super exciting overall. I think I think no one sort of would have believed LLM in themselves would be um would be able to achieve AGI. So I certainly believe that LLMs are already evolving to be agents, right? That's the full picture.

So the systems that have LLMs as part of their components, but there can be quite much more complex, that's to be honest even the original mission or vision that we had in in Gemini early days a couple years ago.

Um and then to the second question for breakthroughs I think probably finding um scalable methods especially in post training I would say I mean pre-training has given us a lot and there's still a lot of progress we are finding and unlocking but I think postraining you know reinforcement learning agents uh and all those sorts of things are in a way a little bit in its infancy maybe if I can summarize that answer kind of unblocking what we've seen with selfplay but for LLM agents would be I I think that would be like a step change and I'm clearly working on that uh very strongly but curious to hear also what Ed has to say on to you then

yes thank you Oro I mean I'm not going to disagree with anything you've said here and that I I think that characterizes my view as well so maybe to add some color I got into when I started working in machine learning I started working on natural language understanding because I saw language as one of the substrates of human intelligence and you know the support for our generality our ability to reason about the world but at the time a lot of what people were doing in natural language understanding and processing were kind of specific tasks things like sentiment analysis machine translation important tasks or contributed many seminal works here um and but I I you know we we we want intelligence to do things in the world for us so that led me like very much like oral to look at reinforcement learning also as an interesting domain to build agents.

And there it was sort of the opposite problem. Like it was open-ended what they could do. We could put them in general purpose environments and have them learn to play go at a superhuman level to fold proteins. But they didn't we always were training them tabular raza without sort of leveraging the tremendous amount of information that humanity uh operates on.

We we we come into a world with context, right? And so it was so exciting when I saw some of the first papers by Google like Lambda or Mina that sort of tried to bridge both of these approaches. take something that is intrinsically a language model, a sequence model, but interpret some of the outputs as actions as operations on an external environment.

And we've really seen this whole line of work flourish in particular thanks to the part of the organization Oreo Citizen to have, you know, models that are the best of both worlds that can leverage a tremendous amount of human knowledge compressed into the LLM and act on arbitrary environments that thanks to protocols like MCP are almost defined at point of use.

So that's already an exciting time to be in. And I could answer the second question by saying let's see where this goes.

But I think there's even broader and more interesting questions here like where how can we imbue these agents with a certain notion of self-directedness, the ability to set their own goals to measure whether or not their goals are successful with decreasing human involvement and attention such that they can become truly autonomous partners in our activities and in our society.

And I think tremendous amounts of research need to be done to address these. But it's an exciting time to be involved.

Wow. That's that's very exciting. And I love uh I personally love the the analogy that um we represent our knowledge and intelligence. Sorry, knowledge and intelligence through language. And by modeling language good enough, you can transitively model intelligence.

So I like the direction where we heading towards and thanks a lot or the great work on Gemini models and Edward as well for the work in agents. Uh okay perfect. Shall we move on to the next question? Um right so the next question this is for you Edward.

So we rely a lot on golden data sets for baselining but given your work on open-endedness how do we move beyond fixed benchmarks to evaluate true adaptability and robustness to novel situations like as you say out of distribution situations.

So in some forums I like to be spicy and say that the age of the benchmark is dead but we're we have a learned audience here today that want a bit more sophistication and subtlety. So benchmarks are still important, right?

We've spent 10 years sort of trying to constantly develop more and more complex benchmarks for more and more complex and valuable behavior from can you classify handwritten digits to can I translate Chinese into English passibly to sort of can I generate valid Python code at scale and so we still find a lot of utility for benchmarks.

But benchmarks are a proxy for the actual sort of deployment capability we're trying to measure the quality of, right? there's sort of like a guess usually an informed guess informed by data and by usage of what are the sort of things the model and agent are likely to face uh at deployment time.

The problem and what makes this a delightful area to do research in is that the actual applications that the agent is going to be uh involved in at uh deployment time are now increasingly directed by the user. they're uh in the hands of the prompt engineer of the person providing the context perhaps an MTP server um and no longer in the hands of the designer.

So this creates a bit of a you know chicken and egg or cat and mouse game where we need to have a source of in if we want to continue using benchmarks to measure regressions to model the capabilities to improve the LLM and other components that underly our agents we need to constantly track where the boundary of utility is.

Where do we most need to uh sort of close a gap between machine and human and then exceed it? And um the best way to do this in practice is to rely on actual applications on having people build things, people use this in the real world and tell us or inform us about where where there are problems.

And so it's wonderful to see a broad community of developers that are trying to build with this, that are trying to build new businesses, new applications and services that will um both benefit from the improved models that we deploy time and time again, but in doing so also be perhaps the most reliable and most important source of information in terms of where there are worlds left to conquer.

And that's why we're very happy to be partnering with a broad community externally.

Amazing, Edward. I love that answer because uh we are covering a lot about real world applications deployment and evaluation of agentic systems later in in the course. Um so stay for the audience listening to this live stream stay tuned we'll be covering this in more detail. Amazing. Uh then the next question please. So this is for you Oriel.

Uh uh so current protocols require in context tool definition uh consuming valuable tokens and hindering reasoning. What breakthrough would according to your opinion would allow natively handling thousands of tools without this overhead? We had discussed a similar question yesterday but this is uh future looking. What do you think uh can be done uh in the technology space?

Yeah, thank yeah thanks for the question. I actually would probably challenge the question and would actually want to turn it around a little bit. Um because actually if you think about the ability for for the model to follow instructions to do in context learning.

I mean these these are both critical features of intelligence and we would definitely want to see the models being very good at this on our quest to build AGI. So I think defining like more of these um tools in context I actually think is a feature.

Um now now the question or the challenge is you know how to make this context management more efficient right like a year ago more than a year ago with Gemini 1.5 we broke um the 10 million token length context length um but of course we haven't stopped right we are working hard to make context on the one hand even longer and on the other hand cheap free basically if possible and super fast right so hopefully you can define these tools in context and not suffer from what the question alludes to.

Um and then I mean at the same time maybe some tools that are very core that should always be accessed maybe they can be absorbed into the model weights but I actually think especially as a developer as a you know this tinkering with the model it's great that you put something in context and the model pays attention to it and truly learns and does what you're asking it to do.

Um so maybe the challenge for us is to make longer context um you know cheaper better etc. Absolutely. In working with um uh real applications with customers I I love the the performance Gemini has even in very long context which is something uh yes so it kind of changes the way you think about things and you can stuff a lot of tools. That's that's great. Uh great answer. Thank you.

Thank you so much Ariel. Um then let's go on to the community questions. Kunch would you like to take that over?

Sure. So this is from uh community questions. Nha uh for Mike. Mike, how do you ensure reliability and error handling in tool chains uh where one tool's output is becomes another tools input given that agents would are expected to behave unexpectedly. Yeah, thanks K and thanks for the question.

This is a it's a great question in um in the agentic context as the question points out agents can and often do adapt and respond unexpectedly. So the first thing I would say is is that agents are a tool. Um but make sure you're using the right tool for the job. There are there are more than one tool for writing workflows.

And if it's really important that you have a deterministic workflow that proceeds from A to B in sequence and gets everything right, um it could be that an agent is not the right tool. Uh there are there are workflow tools and program you can program you can write a deterministic workflow in many tools and this is how we've been programming for years.

So look into this first of all and check check that an agent the agented context is really what you want for this for this use case. Another thing to think about as you if you if you are writing in an agent context is tying the input and output together using schemas. So in our in our open source framework you can define an input and an output schema to each agent in the in the flow.

If you use that schema approach you can provide a better guarantee for the consistency of the input and the output of each stage in the workflow. So that ties the pieces together in a more consistent way. Um and the third thing I would add uh another thing to add think about four things.

Another thing to add is in again there are also deterministic workflow agent types again in some of the frameworks like ADK. Uh there are agent types that are deterministic not based on an LLM output but you can use those to actually define a programmatic workflow that also gets tied into an agentic context.

So you can use them in the context of a broader multi- aent system but they provide that kind of deterministic guaranteed workflow steps that you can rely on. The final thing I wanted to add is you can also remember that the error output from a tool also an instruction to the the agent.

So if an agent replies if a tool step fails and and returns an a an error, you can use the error output to provide instructions back to the calling agent about what to do in case of that error.

So, uh, that's often something that's overlooked in developing these multi-agent systems, but use use every piece of information you have and every piece of documentation you have to give instructions to the agent as to what to do and how to handle how to handle error conditions or failures or retries and instructed on what to do in each of these cases.

Thank you Mike and thank you for the four pointers and uh I believe you were you did discuss those in the white paper with the best practices of the tool design what what would be the best approach to be able to

right some of those some of those are in the white paper there especially the point about documentation. So yeah those are those are key um best practices that we go into more detail about in the white paper.

Thank you. Uh so now um back to oral uh from Rishi Rashi Thiagi uh do you see model training evolving to include simulated tool use episodes uh rather than learning tool used purely from prompting and schemas?

Yeah, thanks for the question.

Um I think a bit related to the the first question about um you know what breakthroughs right I think if if we unlock um through selfplay you know curriculum learning etc then we most certainly I would expect right that that the model in some form right it will have to come up with their own tools new tools variations combinations etc as they train Um and perhaps uh and then there's a dilemma whether tool use are an artifact of the current um model limitations uh that might be removed and eventually absorbed into the weights of the model, right?

But uh certainly um you could you know have a world model in a way of every tool eventually if you train for a very long time. Um, and so that simulation might be a step towards actually the removal of needing the tools. But personally, I I would bet against that at the moment. I think um, you know, tools are great.

They're they're abstracting and um, in a ways kind of how we think about uh, like reusability of software and so on so forth.

So I wouldn't I wouldn't bet against that even if because of our own biases as the creators of the technology but certainly we would expect um yeah as we train and as we evolve our um you know no way tool use is kind of an agent is like the newest modality like it's not um that mainstream for that long as vision has been or or audio or of course text.

So there's a lot to discover but certainly um these kind of techniques that would make the model um either yeah discover new tools, simulates new tools and so on I think are probably a key ingredient to the scalability limitations of post training that I I mean I I was dis discussing earlier. So so yeah great great question.

maybe um you know try some ideas during this these five days and beyond and if something works let me know or let us know and maybe we'll work together.

Yeah. And um so that might be an exciting capstone project idea for those of you who are listening. Uh

uh I was going to say so this is exciting and we you have certainly increased curiosity in others as well. So thank you and as models become more agentic these are things which we all need to be aware of appreciated. So um the next question is from Brian u I'm not even going to throw in the rest of the numbers.

Um, if MCP succeeds in standardizing how a AI agents interact with tools, could it eventually lead to an internet of agents, a decentralized mesh where autonomous systems, trade, data, services, and even goals? What would governance look like in that world? Al um Dr. Alex, this is for you.

Yeah, I love that question, but I I also think we're likely to find ourselves in near future where the boundaries between agents more or less trace liability, informationational governance boundaries that we have in existing social systems.

So, one could imagine a near-term future where the the ratio between humans involved in productive economic activities and the number of agents just gets fully diluted. You have humans overseeing vast fleets of agents.

In which case the the limitation for agency of individual agents in those fleets is is less about capability which is sort of where we are right now and starts to look a lot more like liability where ultimately the the the limitations on the the free agency of uh of AI systems is limited more by what is the the minimum number of natural human persons that can oversee them and be ultimately legally ethically responsible.

responsible for their behavior. So that that's the the first thought. The second thought is I I guess also the elephant in the room. Something I think about a lot is how many agents want to exist in an enterprise environment that is fully observable internally.

So if you if you imagine just as a thought experiment an enterprise where there are no internal informationational boundaries and and obviously in the fullness of time we we would like to I at least would like to see enterprise work fully automated. Does that does that setting want to be a single agent? Does it want to be a million agents? Does it want to be zero agents?

I I would argue that in in the limit we we want a single in at least internally fully observable enterprise to consist of exactly one agent because agents ultimately if if there's only one outer boundary of sort of corporate personhood in an enterprise and no internal information boundaries we want one very strong singleton agent that doesn't have to hide information from from various sub aents and as as oral I think very eloquently pointed out earlier.

Ultimately, one of the reasons why tool use is attractive in the long term is as abstraction.

So, so in my mind, the questions, I guess jumping up a few levels, less about do we do we find ourselves in an internet filled with agents interacting autonomously and more do we saturate corporate personhood as it's currently construed with approximately one agent per corporate person assuming no internal information boundaries?

Uh that's definitely thoughtprovoking because we have been thinking about you know A2A with agent to agent protocol and also adopting a agent with MCP uh inside and when to use what what would be the recommendation but thinking of it with internet of agents particularly a singleton agent is um certainly something for our enterprises to consider. Thank you Dr. Alex.

Um so the next uh question is from Dublin car uh how do you design a multi- aent communication protocol that safely coordinates concurrent tool calls in a single query while resisting prompt uh tool injection. Mike, why don't I start with you and then I'll go to Dr. Alex.

Sure. Yeah, that's fine.

So do I I mean it's a it's a security and coordination um and resisting prompt injection uh tool injection these are really important questions for for the agent agentic paradigm uh and particularly around MCP we talk a lot about these in the white paper um you know I I look at this question as really asking about how do you design a multi- aent system that addresses some of these issues and and manages some of the threats uh and risks that are being introduced in this in this paradigm.

Um, Alex just made a really interesting point about having a singleton agent and I think part of the part of the dynamic here that we have in the development of these agents is from one perspective an agent might be might present a single interface and a single conversational interaction with the user and in that in that way represent a single agent but under the hood it can be built as a and composed of multi multiple agents that are contributing to that output.

So it may all may at the same time be a single agent and a multi- aent system. Um in designing a sing a multi- aent system that coordinates this way. I think one of the things that I mentioned before is also really important here which is constraining the inputs and outputs of each of each of the agent in the system uh through the use of schemas.

So matching the input from one agent to the output to the output from another agent um by constraining the schema that limits the possibilities of um you know ris risky or un or or you know uh un un uh unwanted output or input from any of the components um programmatically.

Another part of this though really important in this paradigm is is trust and the trust between each of the each of the sub aents that are part of these part of these systems is very important to establish. So for instance trusting your tool sources prompt tool injection arises when an MCP server or another tool source is able to uh to present a tool that wasn't expected.

So as you're composing a system like this, ensuring that you trust the operator, the maintainer, the uh the system that is that is generating and and presenting the list of tools to your agent is critical. Um uh access control also is another really important point.

Making sure that you are that the tools know how to trust the user and the trust is propagated from the user through your system through the tools to the end to the uh whatever data source or system is being accessed. Um so again propagating the trust through each of the components in the system is super important.

Uh and another thing to to uh to add is that there also is um in the MCP protocol for instance there is the option that's often recommended for some of these the the capabilities of using a human in the loop uh capability. So popping that that action or question up to a human operator and bringing in the human in the loop for sensitive operations.

um that's an option that is that's is available and recommended as part of many of the components of the MCB protocol. So those are three mitigations that that I certainly would recommend here. Um but I'd love to hear Alex love to hear your thoughts on this too.

Yeah. No, I I think it's a perfect description. Mike, I I would maybe jump up a few levels and suggest that the question seems to be separable in into two separate sub questions. One is the issue of concurrency. And without sounding overly glib, I I think that that's more or less an engineering problem, less of a research problem.

But the the the the other half which is I think about prompt injection via MCP calls that I think is is profoundly interesting in so far as with you know historically before uh before the the modern generative AI revolution, we would have treated prompt injection as just an engineering problem. There they're best practices to to fully mitigate code in injection.

You can use regular expression matching. You can use templates. Lots of lots of tools to to basically guarantee 100% security against prompt injection.

Now though, now that we're in this unstructured natural language world where machines understand completely unstructured data to to a great extent, I I I think prompt injection turns from just a simple engineering problem into arguably one of the the grand challenges of of AI and machine learning that probably again in the fullness of time requires some degree of self-reflection.

Uh I I I would treat prompt injection from MCP calls as a special case of a more general class of poisoning attacks against autonomous systems. In this case, poisoning attacks introduced in context via return values of of MCP calls.

But if you think about it like what in the fullness of time when when super intelligence is maybe not fully solved, but we've made a lot more progress than we have right now, what does the solution to prompt injection look like?

I I would suspect it it looks like autonomous systems that are able to introspect into their internal activations or whatever internal activations evolve into and are able to recognize that uh that that they're being steered in in some sense through their their input stream. that that level of self-awareness.

I I think we're only starting to see the the glimmers of that out of Frontier Labs, including DMIN right now, but I expect to see much more self-awareness as a defense against prompt injection in the future.

Um just wanted to add uh to this that um this um the uh part of the at least evaluating uh tool use and prompt injection involves agentic evaluation measuring how agents like evaluating the overall performance of agents and that's what we will also be covering in in uh in later days. So stay tuned.

Yeah. And some of the security as well. But uh those are like great points and thank you for you know sharing all of your insights. Um we it would be great to hear from you like what final thoughts for the community what you would like to share. So um Edward you are in my screen in the end. So if you would like to go first if there's anything you want to share to the community. I

mean just maybe to reiterate some of the points like one of the two following things is true. Either we are at we have all the ingredients for super intelligence and we just need to scale them or we don't. And to determine which of these two situations we're in, we basically need to see where the limits of the capabilities of agents built on this technology lie uh or whether we hit a wall.

And if we do it at all, we have been doing research. We we can continue to build exciting technology that will service humanity. But you as builders, as people using this technology, play an integral part in this.

The more you try and develop complex use cases and agents, the more you try and demonstrate the economic and personal value of this technology in things that matter to you, the more we will understand where the limits are or whether or not we're off to infinity.

Thank you, Edward. Appreciate it. Uh Oreal, why don't you go next?

Sure. Yeah, I mean lots of thoughts during this Q&A.

So maybe the one that um maybe to re-emphasize is this evolution of the technology like meaning maybe more generically machine learning right so I I think we've seen general algorithms like stoastic gradient descent and neuronet networks applied to you know narrow relatively narrow pro problems like go alpha fold that evolved through language large language models that did language only then we added mod modalities.

So these these models became extremely good at also understanding images, sound, videos, etc. And I think a next stage of evolution which we're starting to see and I mean if you're obviously I think it's here to stay for a while perhaps all the way up to AGI is this scaffolding around these amazing powerful models with all the interesting questions um that comes with that.

So I think the the agentic kind of era um has started and it builds on top of many many things we've seen before.

So either you're new and you know add a lot of energy and creativity if you maybe have been around for a while understand the big picture bring back some of the um old ideas that often times are very successful and yeah looking forward to seeing what you know the whole community really builds on top of the models and the agents and beyond. Thank you, Oruriel.

Appreciate your insight, particularly the world scaffolding. I think I'm going to keep using that from now on. Thank you. Um, Mike, you are on my screen next.

Yeah, sure. Well, I I would just say I think I think this is a really really exciting time. Um, I spend a lot of my time really in the in the trenches with customers, helping them helping them build their agents today and see what's what's working and what isn't. And uh often often I spend more time thinking about what isn't working and what agents are not able to do than what they are able to do.

But but a lot of the things that I've seen them out of do agents do out of the box are really really impressive and they give me a lot of hope and a lot of um uh a lot of kind of um excitement about where this is going and what we're able to do here. But I I also want to say let's you know as we're developers, you know, we're talking to developers and engineers here on this call.

Um remember to think about you know what agents can do and what they can do and think carefully about about when when it is when you should and shouldn't apply them and what their right use cases are.

Thank you Mike. Limitations are really very much important and I think you and I are living and breathing that [laughter] Dr. Alex last but not the least. Thank you. Any final thoughts?

Two thoughts. one, thank you for inviting me to to join this amazing event. Uh, and the second thought is I I I spend, as indicated earlier, almost all of my time thinking about what comes after super intelligence. I I think there have been some amazing points articulated here already regarding how we get to super intelligence to the extent we're we're not already there to some extent already.

I think about what comes afterwards and I I think what comes afterwards is solutions to some of the hardest problems in the world. And I I would just love to engage with the community. If if there are folks in in this amazing community that are also interested in solving the hardest problems with agents, I would love to connect with them.

Thank you Dr. Alex and thank you so much uh for the for your time all of you spending uh your time talking with the people um and also welcoming their ideas. I think that is what we want this to be and we are really looking forward to see where all of this is going to take and I am actually tempted Anand to do a capstone myself to see hey [laughter] I put my ch so uh thank you

this is for the community lunch uh we do keep it for the community

keeping me in check

we would love to see some of the ideas and thoughts presented here if it reflects in your capstone project or as much or you can tackle some of the challenges like many to use how do you um go beyond like putting uh how how do you like putting all the tools in the context window or you try putting as many tools in the context window see how you can come up with more creative solutions and prompt injection tool injection I would love to see all of this in the capstone to see what creative solutions you come up with

all of the questions can be um a capstone so we are really really looking forward to And as Dr. Alex and others have me Ari oriel have also mentioned please do you know if there is a creative idea we would love to see it. So thank you to the speakers. We are truly truly honored to have you all of you here. We are super excited to see how u the how the community is going to build. Thank you.

Thank you.

Thank you everyone. Thanks. So now uh most of you have already you know experimented with code labs and uh we have been seeing a lot of comments. Um before we bring up Lakshmi I I do want to see um where in the community you are all where in the world you are all from. Yesterday we saw a lot of popups going and uh it was hard to catch up.

So thank you for the folks from wherever you are joining from.

Um you are amazing particularly folks who are you know doing off hours trying to catch up your work making this work we are really really uh thankful for your time um Lakshmi um why don't you come on stage hey K hello everyone welcome to day two so yesterday we learned how to create agents with powerful built-in tools like Google search. And today we are going to take the next step.

So I hope you are all ready. So we'll explore today how to build the custom tools, delegate to specialist agents and handle the kind of real world complexities that you will face in your own projects. So the advantage of built-in tools like Google search is that you can use them with zero setup. But what if we are building agents to solve your specific business problems?

This is where custom tools come in. They are exactly what they sound like. The tools that you build yourself using your own code and your own business logic. They give you complete control. And if you know how to write a Python function, you already know how to write an ADK tool. Create a standard Python function, add it to your agents tool list. That's it. You have created an ADK tool.

Now, let's think about a real world problem. When you're traveling to a different country, one of the most important tasks is to find out how much local currency you would need for your trip. And this involves multiple steps. First, we need to find the transaction fees associated with the exchange.

And depending on whether you're using a credit card, a debit card, or a bank account, these rates vary. Next you need to find the current currency exchange rate and then the most important step perform precise calculations so that you will have enough money when you reach the country. Awesome. So what if we could build an agent to do this and today we are going to do exactly that.

Build a currency converter agent. We start by defining two Python functions. get fee for payment method and get exchange rate and then as the next step we add them to our agent as tools. Fairly simple, right? But here are some tips. When you write these functions always make sure to include dock strings. Also make sure that you have dictionary returns.

You can read more about this and other best practices in our white paper. So the next step I told you is to add these functions to the currency agent and once we do that again there are few points that you can keep in mind here. Use the precise function names in your instructions. This helps removing ambiguity about the tools to call. Awesome. So is everything done? Is that it? Unfortunately, no.

Because sometimes the LLM can make mistakes in calculations. So what could happen um here is that it might use a wrong formula for calculation or it might use the right formula but do mistakes while doing the calculation and how can we solve it? What can we do?

So let's instruct the agent to write and execute a Python script for doing the alithmatic and we do this by creating a specialist calculation agent which uses the built-in code executor tool to do this. Awesome. So what is the next step? That is to add this calculation agent to our currency converter. So for that we are defining a new agent called enhanced currency agent and we do two steps.

One explicitly tell the agent that you know you are prohibited from doing any arithmetic calculations yourself and instead use your calculation tool to do everything that you need when when you see numbers and uh calculations. Awesome done. And then what next? Next is to add the calculation agent as a agent tool here.

Now when we run a query for a uh conversion from a US dollar to I innard you can see that in the code that the enhanced currency agent is able to transfer the uh transfer the uh calculations to your calculation agent which in turn generates the Python code for getting the answer. But wait, what is this agent tool? Right? So yesterday we talked about uh sub agents but what is a agent tool?

So this is a very uh key point that you need to keep in mind. So when agent A calls agent B as a tool then the B's response goes back to A but still A is in control. By this what I mean is that it is still agent A which is talking to the users. But if you define B as a sub agent to A, what happens over here is that A transfers the control to B which then does all his all the its tasks.

But also from that point on it is B which is talking to the user and not A. So depending on your business scenario and your requirements, choose either the agent tool or the sub agent. And with that we come to the end of the first notebook.

So we have provided links to the other built-in tools and custom tools that you can uh experiment with and build your solutions for the capstone uh project and otherwise. And next we start looking at the MCP tools and longunning functions. And for that I need to switch my notebook. So give me a second. Awesome. So we are on notebook two for day two.

So last notebook we built custom Python functions. Now um let's kind of think about the real world problems that we have. Suppose we want to connect to external systems like GitHub or Slack. So, how can we do that without writing custom API clients? And second, how do we handle tasks that aren't instantaneous? For example, tasks that might need to pause and wait for a human decision.

We are going to solve these with two very powerful patterns, MCP and ADK's built-in resumability features. So let's start with MCP or the model context protocol. This is an open standard that lets agents connect to communitybuilt integrations thereby avoiding the need for custom API clients. It works by connecting your agent the MCP client to external MCP servers using a standardized interface.

This enables scalable access to live data and tools from diverse sources. So using MCP is very simple. It's just a four-step workflow. Choose your MCP server and the tools that you want to use from within the server. Then create the MCP tool set by configuring the connection. And once that is done, simply add the tool to your agent and you're ready to run and test it.

So in this notebook what we have done is we are using a everything MCP server. This is an npm package designed specifically for testing client integrations. While it's not meant for production use it's perfect for learning because it exercises every feature the MCP protocol provides the prompts the tools the resources and more. So we'll be using a get tiny image tool from this server. Awesome.

So first step we configure the connection using the MCP tool set and once that is done uh we add it as a tool to our image agent and then when we test with a prompt like provide a sample tiny image what happens is that the agent automatically calls the tool and the server returns an image and we can print out this image. So that's what you see here. It's a tiny image. It's just a 16x6 image. Cool.

Awesome. And there is also a Kaggle MCP server which is available which helps you to connect to the data sets and competitions. So what I want you to do is you know uh uh build a agent and use the Kaggle MCP server as a tool and run queries like you know listing data sets that have say OCR data and let let us know how it goes.

Now to the second part, the human in the loop for the long runninging operations. So standard agents are designed for speed, right? They call a tool and they expect an immediate answer. But that doesn't work in real life. So you often need to say uh that okay wait this is a big decision and I need a human to sign off on this first.

So the uh so let's kind of build a shipping coordinator agent to show you what exactly I mean. The first step as always is to define a function in this case the place shipping order. And here you will see that this function has a a parameter called tool context. So this is the secret of longunning task. It gives your tool two essential new capabilities.

the ability to pause execution to ask for approval and the ability to check what the human has actually decided. So there is also a workflow over here. So here you can see that if it's a small order there's a auto approval but if the order is large then uh the request confirmation is called and whenever the human approves the agent kind of uh uh makes a decision based on the human's input. Awesome.

So next we create a shipping agent and then add this tool. But wait, there's a catch. Standard agents are stateless. If they pause, they forget everything. Who the user was, what they wanted, where in the flow uh they were when they pause. To uh fix this, we wrap our agent in an app with the resumability config set to true.

This crucial step ensures that when it pauses, the entire state is saved to a persistence level. Awesome. So if you kind of uh scroll down to the section 4.5, you will see that we have provided three demos, one for each of the scenarios that we talked about. So high uh highly encourage you to kind of you know change some values out there and test them out.

And with that we come to the end of day two where you have added two new super massive superpowers to your toolkit. one MCP for standardized integrations and longunning operations for reliable human in the loop workflows and tomorrow we are going to go even deeper into session state and memory and I'm totally excited about tomorrow and thank you everyone for listening in and back to you K and

thank you so much Lakshmi and I tried the code labs I have to say the instructions are very detailed I would suggest the learners to not skip the instructions and just run the cells. It was really important because I skipped it for day one and the Google search was not in the ADK web UI which was intentional but I didn't know about it.

So thank you Lakshmi for creating and walking through a great job and we are looking forward to see how everyone is going to be you know testing it out and coming up with problems and challenges. So tag Lakshmi in discord. She's there to answer your questions and she will be there for you. So on to our last piece.

Anand this is the most exciting thing because as I see folks answering um this is um the pop quests and Anand why don't we take

a moment.

Yes.

Go over sorry um my slides are not moving. Okay.

Yeah. So hi everyone. um get your pencil and paper ready and you put your thinking caps on. We will test now or you will test yourself um uh the knowledge of the white papers that uh you have read and the day two white paper specifically. Um so let's get to the first question. What primary problem was the model context protocol MCP designed to solve? This one should be an easy warm-up question.

The options are A the high latency of LLM inference in production. B the N intom integration problem between varied AI applications and external tool systems. C the lack of standardized benchmarks for agent reasoning or D the difficulty in managing long-term memory for agents. So um on a count of three we'll show the right answer.

Answer is popping up. [laughter] Three, two, one. The answer is B. So, if you've been listening uh even if you haven't read the white paper, but if you're listening to the Q&A, yeah,

we discussed a lot of the things including benchmarks and and into M. So, you should have the answer. That was a warm-up question. It only gets more difficult from here. Let's go to the second question. Which of the following is not one of the three core architectural components of MCP? So not one of the three components. The options are A the host, B the client, C the server or D the gateway. So take a couple of seconds to think.

I see some wrong answers though. [laughter]

Yes. But I as you see some people got it right. So 3 2 1 and D. Gateway is not one of the architectural components of an MCP. All right. Off to the next question. So the next question is in the context of MCP what is a resource?

Your options are A resource being a function that the agent uh can execute to perform an action or B is it a standardized way for a server to provide contextual data like log files database records to the host application or is it C a reusable prompt template provided by the server or maybe it's D a clientside capability that allows the server to request and LLM completion.

So, this one is a bit tricky, but if you read the white paper, um I'm seeing some of you have guessed it, but uh yeah, let's show the answer in three, two, one. The answer is B. So, that's what the resource is.

I just wish they have one common taxonomy across all of these [laughter] because it just gets confusing. Yes, we lot of uh technology. So it's good to be confused sometimes. [laughter] Next question. So talking about confusion. [laughter] What is the confused deputy problem in the context of MCP security? Your options are A.

When an MCP server crashes because it receives too many simultaneous requests. This might be uh something which is happening in your notebook right now. So we are working on fixing that.

Yes. Uh or B when an AI agent with legitimate permissions is tricked by a user into performing a harmful action with a highly privileged MCP server. Or C when multiple agents try to use the same tool at the same time causing a deadlock situation. or D when a user cannot distinguish between AI agent and a human operator.

So your options are as your answer would be shown in three two one and show the answer. So confused deputy is B. So when um uh strict and agent is strict uh by the way D uh goes more into the touring test. So hopefully you elimin eliminated that option from your uh from your list quite quickly. So let us move on to question number five.

The question is what is the recommended transport protocol for remote MCP client server communication? Your options are A standard input output or B web sockets or C streamable HTTP or D gRPC. So think about it and the correct answer will be shown in 3 2 1. So the correct answer is C. All right. Well, thank you for joining everyone.

I see a lot of answers there. So, thank you so much for, you know, connecting with us through Popquest. We definitely enjoy doing this. So, uh, thank you for being here and for folks who are watching live stream or on demand after, we really appreciate it and we do see the comments in the live chat and in the discord channels.

So please continue to keep engaging with us and see you tomorrow with a fresh set of curriculum with day three context engineering sessions and memory and this is one of the most requested topics. So we are looking forward to having you all with a fresh set of uh speakers as well. Um looking forward to seeing you here tomorrow same time.

Thank you everyone. Same time same channel and don't forget to put your questions for day three in the discord channel in the thread that Brenda created. All right, take care everyone. Bye.

Thank you. Bye.
