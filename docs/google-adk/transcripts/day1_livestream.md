# Day 1 - Livestream Transcript

---

Welcome everyone. We are super thrilled and excited to have you all here for the Kaggle Google uh 5day AI agents intensive course. Um I'm Ka Parlola. I'm one of the co-hosts with Anand Nalgria on the rest of the five days in this course. Thank you for being here. Anand do you want to say hi?

Hi everyone. U thanks K. I'm Anand. uh uh I'm seeing you again after our first two iterations of the course and one of the founders of the course as well and welcome you here and looking forward to the rest of the live stream with you.

Thank you. So we have seen um great excitement over the last couple of days in the all the platforms. So thank you thank you community for your active participation and engagement. We truly are humbled and grateful you we have you as part of your learning journey. So, thank you. Um on the like you know in the YouTube live chat, we would love to see where in the world you are from.

Um I I would like to see where you know you're participating from. Oh, I see some names from India. It's too late for you but thank you for joining. Uh and I see some East Coast.

Thank you Ann I see some names from Discord very familiar names so thank you thank you for participating I truly truly appreciate it so let's jump in um and Karpathi says uh it's not a year of agents it's a decade of agents the next revolution of AI would start with agents and you are in the right place for the next five days as part of your learning journey as you might have observed Yesterday you would throughout the week you would learn through assignments.

The assignments could be white papers, code labs, summary podcast which you all loved um and live Q&A similar to this. The there is an optional capstone towards the end that you could test your agent building skills you have learned. There are if you have registered you would get an email of the content.

If you haven't, you could also see that in the Kaggle learner content portal and it would also be in the discord announcements for you to be able to have a look at. So, uh this is not possible without this village. There is hundreds of volunteers who have participated and you also see several moderators who are actively engaging with you for meaningful conversations.

So these are folks with real life uh experiences. So I would confidently ask you to you know chap in ask them what what their experiences sounds like. Thank you moderators for your active participation. So how is the overview of this course going to look like? We have designed this course in such a way that we are starting from the basics.

There would be intro uh which is today and then you would try to look at how do I put you know hand and ice to it or how do I add memory to it? How do I look at what the agent is performing is correct? How do I go from prototype to production? So these uh course materials is intended to be from basic to advanced and even the code labs are meant to be in that format.

So today we are in day one and for day one um again as I said uh you are going to understand what is an agent how do you define an agent but to know more Anand why don't you jump in. Thanks K, great introduction and great transition to our white paper overview.

So for those of you who uh have not yet looked at the white paper, I highly recommend uh looking at the podcast first or hearing the podcast first and then giving a read of the white paper.

Um, so before I jump into the like overview of today's white paper, I would like to give a shout out to the original agents white paper and the first iteration of our course and the second one as well written by Julia and Patrick um released about an year back. That was kind of the thought leadership to kind which got a lot of you started on agents.

And in this uh the third iteration which is this course we are we have refined and built upon that white paper and uh made a new version for you called introduction to agents and agentic architectures. So this paper moves us from passive AI models to active autonomous agents.

So we start off by defining the core architecture of an agent that is the model which acts as the brain with the tools which serve as the hands as Kunch mentioned earlier for taking action in the external world and the orchestration layer which is the reasoning engine or the nervous system that manages memory and planning. More on that in later days in this course.

The paper uh details a very fundamental think act observe loop right this is how um where agents don't just generate text but continuously perceive the environment plan actions and iterate based on the feedback thereafter we also explored a taxonomy of agentic systems ranging from level zero pure reasoning engines all the way to level four self- evvolving systems that can create their own tools.

We also see examples of some of the level three and level four agentic systems pioneered by Google uh such as co-scientist and alpha evolve.

Crucially, let's not forget that we uh we're talking about agents and therefore multi- aent systems are very important where we go beyond single agents and where uh multi- aent systems um uh have multiple agents like collaborating with each other to solve complex workflows especially enterprise problems or large scale problems as such.

Finally, the paper introduced vital concepts for the future interoperability. So how agents talk to humans uh and how agents talk to each other via the A2A protocol and even transact money and then we also looked at security for creating a new class of agent identity to ensure governance and trust in autonomous systems. Now that was a rough overview of uh of the white paper.

Please have a look in detail and uh and give it a read or for those of you who um uh want to have a quick summary have a look at the podcast and that's it and I'll hand it over to you uh Kunch uh for the Q&A.

Thank you. Um and it's a great overview and you should all review the podcast first as Anand mentioned and then jump into the white papers. So now let's go to the meat of the section which is the Q&A with our industry experts. So can I have all of the folks? Oh, thank you. Thank you for joining everyone. We are super excited to have all of you here.

Um these are industry experts who live and breathe AI agents every day. So thank you for you know in your busy schedule for taking the time. Let's jump in. Uh Anand, why don't you start here? Yes. So, uh the first question, thanks Kunch. The first question is from Mike, Mike Clark.

Mike, would you mind introducing yourself uh quickly and then the question for you would be uh or maybe just do an introduction quickly?

Yeah, no problem. Hey everybody, I'm Mike Clark. I uh work on product on AI agents in Google Cloud. um on the team that helps support and build ADK and agent engine and Vert.Ex AI, agent builder, a lot of the pieces that we're working through here today. Just as finish my intro, I want to thank everybody that's helped pull this together.

Both the community that has contributed so much that we've seen all around the world around the weekend. It was so great to watch in the Discord channel, but then Kodan for helping to kick us off today. Thank you.

Pleasure, Mike. Uh it was our pleasure and thanks to our awesome community which we have joining us today. So Mike question time. So the there there seems to be a massive shift shift for developers moving from brick layers who write explicit code to directors who guide autonomous agents. So how does designing the agent platform and tools like ADK help make this mental and technical leap for you?

like how does it how would you suggest that agent platform and ADK is helping out with this from your experience?

Yeah, I I think it's more than one shift occurring. I think there's shifts all around us. Um agents and AI agents and how people think about them and what they're trying to do with them is an entire paradigm shift.

I've written lots of both bad and good code throughout my career and uh a lot of the code that we write to is to solve one task to go solve the next task to then go solve the next task in a row and always thinking about how to solve that next thing. Agents shift that to where what we're trying to think about overall is how we're trying to solve for the outcome of this of what this agent can do.

And today that involves giving it some instructions to get started and how to work along the way. As models get better in some cases just letting it go off and do these things autonomously which is which is a word we see quite a bit that it makes these probabilistic decisions that it may not make the same decision every time and what it does but what is it trying to get to in that outcome.

I think for individual developers, it's the craft of being a developer for so many years had its own um creative elements. It had its own art and how I wrote code and what our syntax and other things were.

But the more and more we see the shift into coding agents and other kinds of things, it's it's less about the shape of my code and how it how it specifically functions or looks and more about how is it actually solving for that outcome? How is it solving for what we're trying to do? Being able to evaluate that and and really like measure the performance of the overall process.

It also means that as developers, I have to help all these citizen developers and these these folks that haven't written code before, but now can be able to be able to get their code working in the spaces that it needs to.

So, it it's a really exciting time, but it's a lot of shifts to make some folks uncomfortable, but it's it's about embracing that and really like learning how to build the best agents and the safest agents in responsible ways.

Great. Great. Great u viewpoint Mike uh and uh for the folks listening we'll be covering more on evaluation uh and other aspects what Mike mentioned in later days so stay tuned amazing perfect

thank you Mike

all right and uh next question this one is for you uh Michael and Antonio Michael Gishin Har and Antonio G from u the Google cloud team so uh the question for you would What is your long-term vision for how these self-improving agentic systems will fundamentally change typical enterprise workflows like compliance or research and development?

So, how do you see um uh this happening like not just six months from now but let's say three years from now, five years from now? Uh and uh would love to hear a short introduction as well for the community.

Hi everybody. Uh my name is Michael Gersonenabber. a VP of product management here here at Google for the Vert.Ex platform. That's our that's our AI platform. Um, allin um I love this question. I'm going to answer it in in three ways, but I I want to start with with a a little bit of history. When I started shipping models was was about March of last year.

And back then um very few models made it into production. And everybody was talking a little bit about whether it was the year of experimentation, the year of development, but nobody was really calling it the year of production yet. That was sort of forecast for for 2025 or 2020 um six. And what we found was that around June of that year, we did start to get to production.

And how we got to production was in coding specifically, which I'm going to use as a metaphor here. with coding. In June of last year, you could hit tab in your IDE and write about five minutes of code in about 70 milliseconds interacting with with the with the agent. By October of the same year, you could talk to your IDE.

You could ask the the agent to write whole functions and you can interact with it to make those functions good, make them production ready and and ship them to your customers. In February is when Ethan Mollik, I think it was when Ethan Mollik coined the term vibe coding. This is where you could have an agent. You could you could sort of give it an idea of what you were trying to accomplish.

You could assign it a Jira ticket, however that Jira ticket was written, a linear ticket, something like that. And you could fork it off into the cloud while you did other work. A lot of the time this meant forking off several agents with several tasks. Sometimes it meant go to the bathroom or or or or doing tests, but either way, those agents were were running autonomously.

And so what happened in that time um was was more significant than it looks. I mean, I know it looks significant, but a lot happened there. One is that um new engineers were were created.

So on the far call it right hand side you had GitHub you had cursor you had um companies building for 10x engineers and that was making those 10x engineers into 100x engineers these are professionals who work for a company that that deliver software to support the business but then you had companies like replet and lovable sort of far on the left side where a lot of us who didn't write code for a living could write code in ser in service of our business for the first time and so it created this whole class of engineers and I think I can credibly say that all of us really are engineers now.

So one major way in which this is transforming the business is that I see every day I see salespeople doing engineering work building demos for their customers to show how their products are going to be work in work in bespoke ways for those c customers. I see I see product managers doing statistical analysis that they couldn't do before because they can generate code.

Um I I I I see I see specs changing into prototypes, right? Again, it's going to change the way a lot of people do business just by giving access to production workloads to people who don't write Pythonic idiomatic code, beautiful code that they can um that they can maintain in production. Then there are two other ways, right?

on the on the mundane side, not mundane really, is individual productivity. This is one person doing research from themselves. Think of a seller who wants to fully understand one of their customers, right?

They can they can do they can use a deep research agent, they can use Gemini Enterprise and they can really put a dossier together um for for that customer and they can accelerate their their time.

And then finally there's like process transformation which I think probably until others are going to spend more time but this is where this is where um somebody like Fizer or Novo Nordisk can go from database lock after a clinical study to analysis of the data in that in that database to writing an abstract for the FDA all autonomously which means their clinicians can spend much more time on protocol development and and drug discovery filling the pipeline.

And so this is more of a team exercise, right? Getting all the way from from from clinical study to to the FDA um instead of individual productivity.

Yeah, Michael u you summarized this very well. I think that everyone is uh astonished by the acceleration that we are seeing and uh you know the fact that many many things are now available to people that before were not able to to do this thing.

So I think agentic is is is helping in this way in a in in a clear in a very clear way specifically on the question I believe that you know self-improving agents are u changing the way in which we we we we operate. I'm in Google since uh nine years at this point. My background is in search and uh and AI. Uh I work for office of the CTO.

Uh I see that people are more and more thinking also in terms of designing patterns for for agents like for selfimproving agents. Uh I think that there are a number of of things that people are are applying right now like for instance guard rails. uh way to prevent an agent to break rules and you know make war wrong moves. Uh a lot of attention on evaluation and metrics.

We talk a bit more about this but one thing that is really impressing me is that these agents are actually improving themselves. Like for instance one design pattern applied a lot these days is agents are producing uh results and then other agents are actually criticizing. So pattern of critic uh for agents are are actually acting as destinated critics to evaluate the the main agent on homework.

And this is one of the reason why we we basically see this acceleration because these agents are acting as a team members for for for group of people.

Awesome. Thanks a lot Antonio and Michael. That was very insightful. And tying back to Michael uh Mike's um point about citizen uh development as well. Um amazing. Shall we move to the next question? All right. The next question um is for Michael, Mike and Alan.

So uh the question would be as agents move beyond simple chat bots into live mode uh with voice interactions and kind of direct computer use which we saw a Gemini model release recently around computer use. What what are the new capabilities these are unlocking uh and how are developers managing these complex multimodal states in a in a primarily textual uh agentic systems.

could go, but Alan hasn't got to go yet. [laughter]

All right. Hey y'all. Um, I'm Alan. I'm a product manager and former software engineer, so I fit into that pocket of citizen developer. Uh, because I'm I'm I'm rusty. Um, the, uh, new tools and new modalities on the outside of what we would think of as a text interaction um, are really just extra layers on top. And actually sort of pro tip, I recommend you start with the simple thing.

Start with the simple thing and wire in some tools and debug it in a simplified scenario and then lay on new interfaces on top, new inputs on top and new tools and capabilities on top. Right? So start start small and grow from there. Uh because it just be it's going to set you up for success later on.

Um the uh computer use specifically is quite interesting because it allows your agent to be able to do all of the things that you can do on a computer, right? If if you can click on something, if you can type in a form, if you can log in and navigate to a thing, you will be able to automate those steps. Not all things are currently available via APIs.

And so it basically grows the scope of capabilities for what your agent can do. Similarly, I do think that live mode is quite interesting. Um, as you uh create something that is useful to you, your interface to that thing, maybe a chat window is great. Maybe you want to go for a walk and just turn on your headset and be able to interact with your thing on your device.

Uh, it's nice to have a lot of these options that feels very sci-fi futuristic. Uh, two years ago, I wouldn't have believed it. And now I can just do it today uh on my phone. is pretty amazing. All right, I I'll stop. Go ahead, uh Mike, maybe.

Sure. I I love how this question breaks it down into all these kinds of interactions. I think just to, you know, just to add on to what Allan was saying, I when I look at the agents, I use the interactions I have with them are very minimal. Um, in fact, it's it's the least amount of interaction agents that are the best. The ones that know my email, know my chats, know my other things.

And then in the morning I get a nice little way to interact with them. And and I think the only thing I would call out in this question is these are ways of connecting with the world, understanding the world, getting access to that data and making changes in it.

But it's the combination of all of those together with the the magic of having something done without having to go do it that is, you know, don't don't put creative boundaries around it by having these buckets of interaction. Allen's point, start simple, but build into these really creative things and you'll find there's a lot you can do with agents.

There are a couple things that I would love. I mean, Mike hit it on the head, right? There's so much you can you can do with agents that are are creative. I want to focus on on on two of my favorites and and I'll try to be quick. Um, but you have a a company called Door Dash that allows their drivers to deliver packages.

Live audio is perfect for this because if you think about the dasher and I I actually quite empathize here, right?

You have you have a person holding a package with both of their hands with their bike chained up behind them with trying to deliver this package to a house with a dog in the yard who's yapping at them and doesn't know whether or not they're allowed to just like put it down in the front yard, if they have to get through the dog, if they bring it with them to their next delivery.

They want to look up a policy and they want to look up a corporate policy and and so they speak to an agent. They say, "Am I allowed to just, you know, leave the package here? What is the policy? How should I act?" Audio to audio is beautiful because it does take their hands off of um off of the agent interaction.

It keeps it on the package or on the hands and keyboard and uses this this voice channel to communicate. But you probably have to prepare your data for a situation like this, right? In real time, we're talking about 70 to 200 milliseconds in order to look up a complex policy. We give you many tools. You might want to prepare your data with rag, which is a very fast way to access data.

Instead of writing SQL queries and executing those SQL queries, which takes time to write and time to execute. Then there's a a second one. We have um a memory bank feature, right? where you could, and I'm speculating a little bit, fork off a sub agent which is analyzing the behavior of the mage agent in real time.

That sub agent might be saying like this is a common problem and could store synthetic data in the memory bank so that it can be retrieved quickly next time and new analysis doesn't have to be done. Then you can prompt cache it close to the accelerator and make it available.

Everything you're doing using Vertex in this in this way is preparing data to be accessed very very quickly for a live interaction again to keep that um that that delivery person's hands off of their phone instead of having to drop their their package.

There are a couple other examples actually I'm going to I'm going to prune myself here but this is the kind of way you want to be able to to think about these interactions I think.

Amazing. Yeah, certainly a lot a lot being unlocked with multimodal agentic AI systems. And for those of you um who who are not aware with Vortex, that's Google Cloud's um AI platform where you can try a lot of this. Um so, okay, awesome. K, would you want to take over the community question?

Yes. Uh thank you. So, thank you for uh you know, I'm walking through the real life examples actually to very simulated. So um this question is from Nishad Muhammad um for uh Mike Clark and Allan. What are the key design principles behind the Google's AI agent framework because the folks have learned ADK for the first time I think most of them. So can you just walk us through?

I I'll I'll give a very high level answer and Alan I always know loves to go into great detail. I think uh the first thing you're going to learn about the whole platform, not just ADK, but all the pieces that tie it together and interoperability is one of the most important things.

I think we witnessed in the industry these silos of agents getting built and they couldn't talk to each other and it was hard to get tools connected and so one they're open source. Two, they interop and connect with other kinds of agents. You're going to learn about protocols like A2A and how agents can talk between each other.

things like MCP and how tools interconnect that is that is like one of the largest design principles that we put into building out this platform. Alan.

Yeah. Yeah. No, interoperability is certainly key. Uh I will also call out on that spec it works with lang chain uh components. It works with lang graph sub aents. It works with crewi agents etc. Like those things are easy to bring in. Uh, it works with Python code or whatever other code you've written as functions. It works with MCP servers.

It works with regular APIs that you've written with open API spec. It works with enterprise wrappers around APIs for API governance. Um, the whole spectrum is open and the goal is for it to be relatively easy to interoperate without exposing any security risk. So, that's that's a that's probably the top concern. Um, let me give you sort of a peak under the cover to the design strategy.

design strategy is betting on the language model. Um, so ADK is very intentionally betting that models are good and getting better at agentic capabilities. Not trying to constrain the model and just sprinkle a little bit of AI on top of an otherwise deterministic workflow, but saying let's maximize the utility and capability of this model and uh set the stage for growth in the future.

Um, one last thing, it is uh a Google the best of Google all brought together under one bundle. Um, so a better together platform but fully open and extensible. So it's like we're trying to maintain both of those things like let's make the most use out of Gemini, let's make the most use out of Vert.Ex, let's make the most use out of all of our tools.

um we are building our own agents on top of this exact same platform and framework but we don't want to lock you in. So you can bring other models, you can bring other platforms, you can bring other tools. So so that's that's really the design principles in a nutshell.

Yes. And I love I think one more design principle just from my side which is the how easy it is to use agents as an atomic unit and yet you can go down at the and define all your custom agents. So it's very easy to get started, but you have all the control you need to go into the nitty-g gritties. So

thank you. I actually I love that it's open uh as you all pointed out, interoperable, open source, open for any language. I think for developers, that's what they're looking for. It needs to be much more accessible. So thank you for uh highlighting those

and Go now. Yay. Oh yes, Java, Go and Python if I'm correct.

Do you have any other plans, Salon? Anything you could share?

Nothing that I can share.

Okay, [laughter] that's good. The next question is from Predictra uh for Antonio. What architecture enables AI agents to autonomously self-organize? that is form merge or dissolve based on performance metrics rather than static predefined configurations.

Well, I love this question and I think a lot of research is going in this direction. Um, so I heard a lot of people talking about design, design principles, design patterns. I'll tell you what is the status of the art today and where and where things are going. So two different things.

one today agents and when I say agents I actually mean a plurality of agents multiple agents that are collaborating normally have an access to tools and they have a prompt and this prompt is written by humans now agents are already improving their own prompts in automatic way uh what is happening is that as as the agents are evolving like considering the time factor uh if the agent understands that the front itself can be improved that there is a way to do this.

Google has tools for doing this and these tools are already in G. Uh but that's an initial step. One thing that is happening at this point is uh the agents are evolving the topology uh of the agents themselves. So what is the meaning of this? Think about uh a team and human team and we normally have org charts right.

So there is a there is a structure in the organization in which in which uh humans are are operating. When you have a team there are different roles and this and these roles are are uh well understood. Now think about having an a an agent broker.

So an agent that and the scope of this agent is to hire new agents, let some agents go and sometime merging agents essentially creating the perfect team setup or agent setup coordinating these agents in such a way that they perform at the best. I recently wrote a book about this. This is uh called agentic design uh pattern. There is an article from uh from Google that I strongly recommend.

It's called multi-agent design and basically that what is happening is this paper talks about optimizing the prompts and then optimizing the way in which the agents are are set up the teams themselves like let me give you a specific example if over the evolution of the time a team of agents so a squad of agent is actually detecting that uh something is missing perhaps a new agent is added to the topology to to this to the team and this new agent has a role for instance of a critique agent and so this agent will doublech checkck the the work made by others.

There is a lot of research in this direction and I will expect to see more and more breakthroughs in in applying these principles of changing the prompts and changing the topologies in into 2026. That's that's one forecast I make

and critically I think it needs uh evaluations right we're we're coming up on that soon but it's like you you mentioned optimizing multiple times Antonio but if people are not familiar the only way to optimize is to be measure measuring quality or measuring efficacy and uh that we do that through evaluations predominantly

absolutely uh I totally agree with you uh Alan uh evaluation and setting the right the right metrics is large part of the problem is actually probably the most important problem and uh I will add also evaluation that are kept and monitored over the time.

So in such a way that when the agent is actually performing it's not only important to have one snapshot today but to observe how the agent or the team of agents are performing over time and if there is some drift or some something new data that is appearing so how the agents are are performing in these new scenarios.

Thank you. And it like with the papers and the book you mentioned uh very much all of those principles can be built with ADK today right so uh all of those principles like apply with our uh with the platform which the developers are learning today. Yeah, totally. I think ADK is one one tool. Uh, NCP server is another set of Swiss. Nice. We have A2A is another one. So, we have a a polarity of of uh platform and technologies that we can use today.

Yes. Thank you. Thanks, Antonio. The next question is for Michael G from Mehak. I hope I pronounced it right. How can teams best ensure robust secure integration of AI agents with existing enterprise infrastructure like databases, CRM would u and what pitfalls should they avoid during development and this is one of the common questions which we keep saying to SQL before too.

Not only is it a common question but I want to represent upfront that it is an evolving answer. I would say Mike Mike Mike Mike Mike here and I were just talking about it just as as as recently as Friday afternoon. Um but but this is something that that we think about all day and I I think a lot of engineers think about all day.

Um at the very beginning um I I I think that a separation of concerns is necessary and and two products make this possible. MCP model context protocol and and ATA um make this very organic for teams.

both uh agent agent protocol sorry both of those move the governance of the data and the access to data over to the data team to expose MCP exposes the data literally um with with a response and ADA can um expose the data as as um as mitigated as not mitigated sorry as as implemented by an agent.

So not only does an engineer have an agent trying to access data, but on the defense, you have somebody who owns the data who is responding with an agent instead of giving raw access to a user database or something, right? And so now we have two products that allow a a owner of data to expose that data, they can begin governance. Governance usually means setting policy.

um it means auditing for compliance with policy and sometimes it means intervening to enforce policy and all three of these things are possible with these tools. Uh right. So first you have to know what's in your database and and you have to know how to how to protect it. But this is where we were talking about eval earlier.

Um you probably want to implement some sort of telemetry that can be evaluated offline. Um and so this looks like common logging products. Um you can integrate uh with with with cloud monitoring with with data dog with with many products but but either way you want to be monitoring the behavior of agents touching your data. Then on enforcement, this is where uh your corporate uh policies come in.

Um do you want to answer with the raw data? Do you want to use A to A to answer with a summarized version of the data by trying to understand the intention of the caller? Do you know the identity of that caller? Are they a service account or they a synthetic agent impersonating a human? Right? All of these things are probably contemplated in the way that you respond with your own agent.

I I don't want to accidentally fall down a rabbit hole here, but like I say, there there are quite a few mechanisms at your disposal. Common ones from from the old world of distributed systems as well as novel ones um specifically for exposing agents uh data to to synthetic agents. I don't know, Mike, you think about this all the time. If you have um something to add here.

No, I think I I think you really like you nailed down. It's all in the nuance of implementation. And I think it's also we're going to see a bunch of changes. We announced ear earlier last week um new protocol around A2 UI and like starting to introduce that it's now just not about actions and handing things off but it's about you being able to generate UI as part of this at the same time and not just for the web and not just for mobile but on new things you haven't imagined yet. [clears throat]

Thank you Mike. That one was a That's a stealth announcement. So, go find it because it's fun. Uh, no, it's good. It's good. Um, I'm going to add one more bit. Uh, classic software engineering best practices still exist, right? Control your surfaces, control your users, control your ales.

Basically, you will expose a level of data uh through your APIs and resources and then expose them through your agents and tools. I think that Michael was was setting that stuff up for it, but just like start with that bottom level and the the normal software engineering best practices of defense and depth and least access still apply. And now you have a language interface on top, right?

Don't forget about all of the normal foundational stuff. You're implementing the normal foundational stuff through your agents. One other thing, we were talking a little bit earlier about how the the models are getting smarter, but you can delegate a lot of this protection to the agent itself, right?

You can classify a prompt um from somebody else's agents on its way in before it ever touches the data or any policy is applied. You can classify the output after they got access to the data, like Alan said, as a matter of defense in depth. Did they seem like a good actor, but are they really excfiltrating data? That's another layer of classification that you can be doing.

So you can you can apply the LLM to classify these things on several in several places as well. Thank you. That is actually really great particularly when um you know when we think about this it's not a new thing. We have seen this in the past. We have done this in the past. So do your governance, do your you know establishing the monitoring all of those in the past.

So, thank you for walking us through. We um multiple viewpoints. Appreciate it. So, um this one is for Alan. I think um this probably is the last question. Um from techfed, what emerging patterns are production teams actually using to chain 50 plus tools reliably? Like 50 plus. That itself sounds a large number.

Yeah. Yeah. Um frankly, I I don't do that. I don't [laughter] uh I I don't try and stuff that many tools into a single agent. Um I enjoy decomposing my agents into more specialized personas or subsets of capabilities uh wherein they can have a handful of tools one or five or 10 uh tools where they specialize in capabilities and then it's about routing to the appropriate specialist.

That's predominantly what we do.

there's stuff coming right so you can do tool retrieval and uh at real time I actually retrieve from a database of you know a thousand tools I'm only going to get these four tools that are appropriate for this context and I'm going to change my instructions I'm going to change my examples all on the fly you can do that today some people are doing that for kind of a just in time dynamic agent um and then there are uh things in the works for uh better planning and task decomposition.

Right? So when you're talking about a lot of tools, picking the right tool is not important. Picking a plan across several interactions or tasks across several tools is what's important. And um because these are not predefined and pre-garanteed, uh you might go five steps in, realize that it didn't work out, and have to come up with a new plan along the way.

uh agents are good at this uh but uh at 50 tools it can get messy pretty quickly. I I think that we are working on some interesting bits to make that a little bit simpler but uh uh I I don't have a better answer for you now than decompose orchestrate that will work today for sure. Dynamic just on time will also work but it feels like a lot to to maintain and then we got more exciting things coming.

I I think there's some really simple ways of thinking about this especially as all of you are jumping in for the next five days to learn about agents more in depth.

um a framework I use and that that helps me is like when I'm when I'm using tool like MCP I'm using that for a transactional element but sometimes when I actually have a broader problem to solve that's when I'll push things off to another agent is using where it's about not just asking a question and getting a single answer but it's going through a process to get to an answer that's more meaningful and took more work.

You'll start to figure out these patterns. um getting to, you know, having having an agent that needs 10 steps or 50 steps or 100 steps. What you'll find is as you get to more and more steps and you add more and more tools, it it's like anything else. You add complexity, you add higher risk for things regressing and and not getting to the answer that's as optimal as it could be.

The other thing that happens is um as you know you've got you've got things to use free right now but as you're building these systems at scale if you take something that has 100 turns in order to get to an answer or 500 turns that context ends up being shifted a lot back and forth through the model.

And so finding ways to break out some of that work into other agents doing some of that in parallel, finding the right models that work for you means that it may cost less, it may happen faster, and you may get better results. And so these are the patterns that you're going to have to experiment.

And frankly, that's a lot of the reason we wanted to make sure you had access to all these resources this week, so that you can not just this week, but also onward, start to build out some of these different agents, try and solve more complex things. Start to just like when working with LLMs, it's not just about the prompts.

In fact, you'll find more and more it's about the context and the structure of that context that really determines the quality of the answer you're going to get to.

Thank you. This this was quite helpful particularly u having you all here with experience who with like real life experience when you were able to share door dash story or you know how do you chain 50 tools in one model which I don't recommend. So thank you for you know sharing us part of the journey. Now we jump to the next exciting one with code labs overview.

Um I know many of you have already started the code labs. We have been looking at you know the reviews which keeps coming. It was fairly easy. There were two code labs which you were able to you know look at. So on to the stage uh Christopher Overhold and Hank Flynn please.

Hello everyone. Really nice to join you today. My name is Chris Overhalt and I'm a developer advocate at Google. Uh, and today we're going to dig in in this part of the session into coding and hands-on coding with the code labs. So, we wanted to take some time to talk through the code labs and what to expect and really what you're going to get at the end.

So, there's some really exciting stuff uh in day one here. Before we do that, I want to introduce Hangf. Uh, Henfe is an engineer that works on agent development kit. And so we're going to hear a little bit of background and vision and things context to set that up since you will be using agent development kit throughout this course.

So I'll hand it to you Hung and then I'll come back with some code lab walkthroughs.

Um hello everyone. Yeah, I'm Hay Ling and I'm the co-founder and tech lead for agent kit or ADK. So ADK is the framework you'll be using in a collab this week. Uh, I'm really excited to have you all join us for what I believe is the biggest shifts in the history of our industry. Moving from building apps to building agents. So, uh, what's ADK? So, here's the documentation page for ADK.

ADK is an open-source code first toolkit. You'll be using it in Python this week, but is also available in Java and Go. It entire purpose is to bring real software engineering disciplines to AI agent development. We are having developers um we are giving developers the primitive to build modular testable and version controlled agents. When we design ADK we ask ourselves what defines an agent.

We distill it down to a field core primitive that you'll master this week. First the concept of an agent as the core worker. Second tools uh is like the hands and the feet allowing the agent to interact with the world APIs and the databases. Third, a runner to orchestrate the orchestration. Um but that's not enough.

As you'll discover throughout the the course in this week, agents need sessions, states, artifacts to manage memory persistence through the life cycle of agents across users and across time. This state of design is our core differentiator. It's what separates a toy chatbot from a production ready agent that can handle complex and long running tasks. So this is our GitHub page.

Um we our design grounded in real user needs is why we have already hit over 14,000 GitHub stars and over many millions of downloads. Um this focus on real world use case extend to our production story. ADK is built on a simil pass sim pass to the enterprise. Uh you can develop and debug locally with our integrated dev UI ADK web.

When you are ready to deploy, you can with minimal code changes swap those implementations for production grade services like cloud like Google cloud agent engine or SQL databases. So we also support a ton of integr incredibly advanced features like ADK live right in the previous Q&A we have discussed about that for realtime birectional text audio and video streaming.

We also support like rich multi- aent support like through A2A agentto agent protocol which you will learn on day five and the context management including filtering compaction and caching critical for performance and reducing inference cost. Um if I take a step back um our vision is to make ADK the de facto industry standard for agent authoring.

That's why we are focused on becoming a universal and a neutral standard expanding beyond beyond Python to Java and now go. Um by learning ADK this week you are just um you aren't just learning one tool you are learning a framework we believe will power the future of production AI. We are committed to make this most reliable way for you to take agentic AI from prototype to global scale.

Um, so this vision only works because of the community. Whether you are new to agents or an expert, I'm excited to welcome you to the ADK community. We build ADK in a com uh in the open based on year features and the year feedback. In our recent community call, we had developers from the around the globe uh from like a students just starting out or like to architects designing enterprise systems.

Um so we we are always looking for contributors. Uh so we have our contribution guide here. Uh if you are interested to help out the shipping ADK, check out our contribution guide. Uh you can also engage with community through our GitHub discussions. Uh I will show here and also our Reddit as well. Uh as you go through the course list this week, uh think about how you might want to get involved.

Start a discussion on GitHub, write a blog post about what you build or learned, or even open a pull request to improve the core framework. So, uh I can't wait to see what you will build with ADK. Uh now passing to Chris.

Awesome. Thanks so much, Henfe. I really appreciate the uh overview and thank you and the team for everything you do for ADK users, developers. Uh this is really exciting uh to be a part of. So thank you for the deep dive there. Uh so now what we're going to do today is I'm going to walk take a few minutes to walk through each of the two code labs that you will have received.

So, I'll share my screen and I'll kind of show where where we're at, where we're going, and hopefully you'll walk away uh whether you've done these exercises or you're just about to get started with some exciting takeaways of, you know, what is it should I get out of day one code labs. So, on the course overview, uh past the setup instructions, you'll see the day one, uh agenda and topic.

And just below that, you'll see the today's assignments. And inside of there, there's a couple of different notebooks or code labs that are linked to um you can either read through these code labs. Uh you can also copy and edit them. We have instructions on how to do that if this is your first time working with Kaggle notebooks or notebooks in general. Not a problem.

Uh we're here to support you along the way. So the first notebook that you're going to get into uh is called from prompt to action. So this is one of two notebooks for the day. Now, we since this is the very first notebook, uh there is some setup instructions in the beginning of each notebook that talk about how to get started with Kaggle notebooks, how to set up your API key.

So, hopefully you've been able to do that. And once we get past that, there's really, so if this is your first time using agent development kit, there's really three big takeaways that we want you to explore and interact with and be comfortable with for notebook one, uh that you'll use throughout the entire course. So the first thing is what's the difference between an LLM and an agent?

Uh so we'll dig into that in a minute. Uh the second one is how do I actually build an agent? What can I do? So we build a very simple but powerful agent that you'll use that same pattern to keep adding on things as you go through the days. And the third piece for this first notebook is how do I actually play with my agent? How can I look at tracing and evaluation and uh maybe a user interface?

So, we'll show you an ADK web user interface. So, let's dig a little bit more into each one of those. Uh, first, the difference between an AI agent and an LLM. So, you might have worked with a generative AI model like Gemini before, maybe in the Gemini app or an AI studio. Uh, and in that case, you send a prompt and the language model sends you back a response or generates an image.

The difference between an AI agent is that we're actually setting up a framework there. That's where agent development kit comes in. and we layer on those components we talked about before. So, as you go into defining your agent, you'll find things like a model and instruction and tools. So, we're kind of putting these pieces together so that you can ask questions to this agent.

It can decide which tools to use in which order that it wants to uh and then gives you back a response. So, that's the first thing. And then as you progress through the first notebook here, you'll actually build a very simple but powerful agent in less than 10 lines. So, this agent is going to be a a helpful assistant. And the key here is we're going to give it one tool.

We're going to give it a pretty powerful tool, a Google search tool that's built into Gemini. And so, that way your agent can not only answer questions about what it was trained on, but it can actually pull the latest information. And we'll see some of that um in a second.

So when you go to run this agent in the notebook, we'll create a runner uh and then we can ask a question like what is agent development kit from Google and what languages are the SDK available in. And so here our agent is not only just answering from the LLM, but it's doing a Google search uh retrieving the latest information given that we just released uh ADK go for example last week.

There's no way the model would be trained on that. But from this Google search retrieval, you can see it grabs that. It gives us a description about what agent development kit is. And at the very bottom, it says the ADK SDK is available in Python, Go, and Java. And of course, it got that from its tool retrieval.

So hopefully it's a very short and simple agent, but it's very powerful again because it has the ability to fetch real-time information, current information. So you can um kind of have fun with it. And in the follow-up question, you can ask about the weather in your city. Uh I like to ask about sports or movies, like something you know that the model definitely is not trained on.

So you can see uh that it's retrieving information in real time. The last part of this uh is really exciting. It's the ADK web interface. And so if I switch to what you're going to see in that step, you're going to spin up the ADK web UI. And from there, you'll be able to query your agent uh and interact with it there.

And in the later sessions, you'll actually get more into evaluation, observability, and things like that. The second notebook for day one is all about multi- aent systems and patterns. So once you've built your first simple single agent, uh you might have seen one of the questions was about 50 tools, right? There's people you want to add more tools, more capabilities.

So, three things that you want to take away from this notebook that are really exciting to learn are number one, how do I design a multi- aent system in ADK and why would I do that? Uh, and what benefits does it give me? Number two, are there different ways of designing multi-agent systems? There are, and I'll show you in a second.

And number three, now that I've learned all these patterns, when do I use certain patterns for certain things? So those are three big things you'll learn from the second notebook and I'll briefly show uh what that will look like as you're going through. So the first one is why multi- aent systems.

So if you have our single agent like we had before and you keep adding instructions and adding tools and adding complexity at some point you're going to sort of overload the agent just like uh uh just like I would get overloaded at work if you keep adding roles and tasks and tools. So then we design a multi- aent team and we show you how to do that using what's called an LLM agent.

So it gets to decide which tools it wants to use along the way. The second part of this notebook really goes through different patterns. So we go through things like the sequential workflow. So here we want to write a blog post and we want to go exactly in an order through multiple agents sort of like a pipeline that's very reproducible.

Um, and each step will either generate or write or edit content along the way. Another pattern you'll see is parallel workflows. So you might have agents that can actually work independent of one another and you can fan those out and run them. So you're not waiting on each agent to finish. You're actually fanning out and doing multiple things at once.

And the last part here, uh, you'll see us introduce the loop agent. So loop workflows are really useful when you need to iterate and refine on something. So we'll show you how to do that. Generate a short story, generate a critic agent um and be able to iterate until some criteria is met and then we stop.

So to finish off this uh part of the to finish off this part of the notebook, you're going to basically see um sorry about that. You're going to basically see what it would look like to go through and choose different types of agents for different tasks.

So you have sequential agent, parallel agent, loop agent, and this workflow, this flowchart basically guides you through when should I use each agent for a given task. So with that, we hope you enjoy these two notebooks and uh thank you Hangfay for joining along.

We really look forward to having you participate in the ADK community and I'm gonna hand it back to Anant who's going to take us on to the next section. Thank you all.

Thank thanks Christopher and Hfe CTA's contribution to the community do your code labs basic to advanced and we are looking forward to see what you're preparing an off to you.

Thanks everyone and really exciting times here. So um so this part of the uh live stream is about testing your knowledge of what you have learned from our white paper. So get out your pencil and paper and uh I beckon your focus to the screen. Let's go to the first question.

So the first question for you all is according to today's day one white paper what are the three essential components that make up the core anatomy of an AI agent?

So um uh is it uh uh option A the model the user interface and the database or is it B the model tools and the orchestration layer or C the prompt the rag engine and the output or D the reasoning engine the memory bank and the API gateway. So

answers in the live chat already.

Yeah.

Answer.

Yes. So let's count on count of three. It's B. Okay. [laughter]

I'll be careful the next time around.

All right. So uh next question then. Hopefully some of you got that right. So the next question would be which of the following represents the correct order of the five-step agentic problem solving process described in the white paper. So the five-step agent problem solving process described in the white paper.

Your options are A, think it through, take action, get the mission, scan the scene, and observe and iterate. Or you get the mission first, then think, then scan, then take an action, then observe and iterate. Or C, we get the mission, scan the scene, think it through, then take an action, and then you observe and iterate. Or D, scan, get the mission, think, observe, and take an action. So

I read the white paper 50 times but Adam think I can get it. Let's see what happens in the live chat.

Yes. So let's see how many of you get this one right. So on a count of three I present uh the answer. Three two one. Kunch. The answer is C. See how many of you got that one correctly.

I see some answers. Good job.

Amazing. Um, glad everybody's following along. And on to the next question. Uh, in the taxonomy of agentic systems, what capability distinguishes a level two strategic problem solving agent from a level one pure reasoning uh engine agent. So level two from level one. Think back to your thinking gaps and the all your options are a it can use external tools.

So the level two can use external tools like Google search or that level two agents can collaborate with other agents in a team or is it that they can dynamically create new tools on the fly or is it that they use context engineering to plan complex multi-part goals? Think back and um few answers. Yeah,

I see it.

I see the answer. Yeah.

Yes. Great work. Uh, everyone on a count of three, K, would you show the answer? Three, two, one, and it's D.

Yes. So, for example, creating dynamically new tools on the fly is something more towards level four. That's the option C. So, and D is the level two strategic problem solver agent. All right, moving on to the next question. Um so what is the primary role of the orchestration layer in an agent's architecture? So the orchestration layer what role does it play when you build an agent?

The options are A it acts as the conductor. It manages the think act observe loop and the state or B it serves as the brain providing the core reasoning capabilities or does it act as the hence which is option C or D it functions as the memory restores long-term preferences so on a count of three

it's in the first five 10 pages

yeah it's very early yes that's definitely uh so on the count of three two one and the answer is a. So that's the core architecture of uh core like uh core component of an agent which makes an agent an agent.

Uh so yeah moving on the last question for today is what defines a level four self-evolving system agent and your options are A it can execute tasks without human supervision B it can evolve its own capabilities and create new tools C it utilizes a team of specialized agents to complete its job D it uses multimodal model to process images and audio natively so what defines a level four agent on a count of three, two, one.

The answer is B. Um, it relates to the question we had earlier as well. So, uh, hopefully a lot of you got this right and I see that you do. Great. Thank you everyone for being there with us. And that concludes our live stream.

Thank you. Thank you everyone. We look forward to seeing you tomorrow. you would have assignments published shortly and MCP was all over today Q&A. So, it's a nice segue to tomorrow's session. See you all tomorrow. Looking forward to having you back. Thank you.

Same time, same channel, everyone. See you. Bye. Bye.

See youa.
