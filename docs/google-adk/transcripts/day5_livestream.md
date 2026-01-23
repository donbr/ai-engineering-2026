# Day 5 - Livestream Transcript

---

Welcome everyone. Hi, I'm K. I'm one of the hosts of the five days of AI agents intensive course. I'm here with Anand Navala. An why don't you say hi?

Hi everyone. I'm a co-host with Kier and the founder of this course and I'm looking forward to walk you through the rest of day five today the final session.

Thanks Anan. So today the finale of the five days of AI agents intensive course. This has been an amazing journey. We have seen all of your incredible questions, feedback, insights over across all of the social platforms. We sincerely appreciate it. This is a village and as we mentioned earlier, it took nearly 100 plus volunteers working over several months to bring this to life.

I especially would like to call out the leads that worked tirelessly over the last few months. Um, Kel Parak, I don't know if we wouldn't we would have done anything without you for your efforts in marketing and getting us all up to the stage. Brenda Flynn, the force of reason and sometimes hard decisions and also program managing the whole effort.

Holong Lynn lead on code leads code labs to make sure all the nuts and bolts are well placed. So it has been seamless experience for you all. Anand the founder and leader of this effort and sometimes giving us surprises all over the place. Um it it has been an amazing journey. I would be remiss of not calling out Sarah Wal Wally for the run of the show logistics and ensuring the seamless flow.

And last but not the least Ray Harvey for all our program management efforts across the board, white papers, code labs and communications. Thank you. Thank you. Thank you. Um by this time you already are aware of you know the in intensive work and the things which uh have been put in place.

Um as a reminder and some of the questions have popped up that you know would the course be available offline after the session? Yes, it will be available to through the same channels as we discussed above. Um and it is u definitely uh been amazing for us to be able to do this program. Um, Anna, do you have anything to add?

Yes, thank you. Uh, thanks for the intro and yes, looking forward hopefully you've gone through all of these things in the program.

I would also like to uh give a shout out to all our sponsors including Allison Wagenfeld, Ricky Robinet, Will Granis, Sorup, Tiwari, Brian Deahunti, Michael Collague and all the others who um sponsored and supported us even if we haven't mentioned all the names but thank you so much everyone. Thank you. Um and this moderators have been with you over the journey for the last five days.

Um special call out to Brenda in keeping all of us on check and making sure uh it's funnel like the channel communication is transferred across. Thank you. Thank you so much. So we are as you as we mentioned earlier there is a lot we can discuss about AI agents.

We designed this course especially in mind of how you can get started get active you know uh immediate uh scale agent building skills and we are here we are in day five going to discuss about production anand why don't you just join and share the curriculum revia for day five

perfect thanks kunch so everyone uh glad that you've made it this far here is where we talk about prototype to production over the last For days we have designed sophisticated agents with tools in memory and then learned how to rigorously evaluate them.

Now we faced the final hurdle bridging the gap from a local prototype that you built in your labs uh in your K Kaggle code labs to building a secure production system. And day five's paper prototype to production as well as the corresponding um code labs is your operational playbook for bridging this massive uh last mile gap where 80% of the real work often lies.

Uh so the white paper it starts uh with people and process defining their specialized roles needed for mature agent ops from AI engineers designing guardrails to platform teams managing managing um authentication and authorization. A core theme in this white paper in this section is the evaluation gated CI/CD pipeline and I recommend reading uh diving deeper into that section.

It's very interesting in my uh opinion. It's simple but powerful. No agent version should ever reach [clears throat] production without automatically passing a regular rigorous evaluation suite that proves its quality and safety.

We covered safe rollout strategies like canary deployments starting with say 1% of users and blue green deployments to minimize blast radius and allow instant roll backs if something goes already.

Once live, you need a continuous observe act evolve loop using real-time monitoring to trigger immediate fixes like say uh or circuit breaker um works but instead in this context for a failing tool and then feeding insights back into the development for long-term improvements.

The paper concludes by looking at scaling beyond single agents using the agentto aagent or A2A as we call it protocol to build collaborative ecosystems where agents can discover specialized peers and delicate complex goals. That would be it for the summary of the white paper.

uh for those of you who haven't had the opportunity to read it completely, I would recommend starting off with the summary notebook LM generated podcast and then if if you feel like it load that paper up in notebook LM and ask it questions, use the mind map to navigate it as well as get your own video and audio overviews to interactively um uh interact uh uh interact and read the white paper.

All right, Kunch, then uh give it over to you to the exciting Q&A session.

Thank you, Anan. And one of the things about this paper is also it's very short, so it's easy for you to be able to grasp as well. So looking forward to having you place reviews. So now onto the meat of the section with the Q&A. Can we have um Will Granis, Socrates, Katakis, Aliasi, and Suk Tavari on stage, please? Thank you everyone.

Thank you for joining despite your busy schedules in answering questions with the community. Community definitely enjoys it. We see that in the live chat. We see the interactions going on and they appreciate you being here. So, thank you so much for being here for us. Do would you like to do a quick introduction? Um why don't we start with um Alia you are on my screen first.

Thanks K. Nice to meet you all um who are watching this. I'm Helia. I'm a M specialist in cloudi uh looking at helping uh developer customers bringing agents to production

and one of the white paper authors.

And one of the white paper authors. Yeah. And you'll try out his agent starter pack which is very useful as well. I'm sure you would do the [laughter] bragging soon. Thank you. Will, you are in my screen next.

All right. Well, honored to be in your screen. Hi, I'm Will and I'm the CTO here at Google Cloud. Uh, and uh, super excited to be a part of day five of this agent intensive and a big shout out to everybody who put this uh, program together. Amazing stuff. Honored to be here.

Thank you so much, Bill. Appreciate it. Saf.

Yeah. Hi, everyone. uh super excited to be here uh and thank you to all our viewers who are who are watching it. Uh it's an amazing journey that we are working together with you. Uh I lead the cloudi organization which includes uh vortex collab kaggle uh and a few other businesses. Uh by the way one quick shout out that uh I'm also a follower of this course because my kids are trying to follow along. So so so I'm following up as well. [laughter]

We love it. So we would have candid feedback.

Yeah, they're getting expert advice. That's no fair.

Yes.

Great. [laughter]

We have an insider track,

right?

Talk to this.

Hello everyone. I'm a geni black belt for Google Cloud. I help enterprise customers to bring to bring some hundreds of agents into production. And this is my love agent ops, MLOps, and the whole area of ops. And happy to help you today. and one of the authors of the co- white paper

and also the previous two. [laughter]

Thank you. Thank you for everyone for being here and definitely in the live stream we see it and on demand after too there are close to like 200k folks in discord who are continuously asking questions. So we are excited to see what we do here today. Anan why don't you take this first? Thanks Kunch. Excited to ask Sor this question for you.

So going forward, what do you think is more important for models? Deeper reasoning capabilities or the extreme token efficiency and speed required to make realtime multi-agent meshes commercially viable?

No, I think uh this is an excellent question. Um I think at a high level I would say it depends uh depending upon the application.

Uh if you [clears throat] look at from a reasoning perspective, from a core model reasoning perspective, the reasoning needs to be very strong for the models to make choices during the agentic application as to what tools to use, how to act when they are seeing responses which have uncertain outcomes, how to decide which path to navigate etc. So core reasoning is important in many applications.

If we don't have fast enough latency then it may not be viable or like practically viable because you may not want to as a user wait for a very very long time which is there. So I would say it is a trade-off as we go along. Uh let me provide some color from the where the research is heading.

What is happening is that as foundation models are improving a lot of the reasoning is becoming a lot lot thinner because much of the logic is being processed by the model itself internally within within its own systems. So what you should see as we go forward is that the number of reasoning to tokens which are getting produced will become smaller for the same type of task.

Now what that provides us is that we can now then use the model for much more complicated tasks. So you can have instead of creating a mesh of like three agents working together you can now have five 15. Our ambitions over here are pretty high. We do see a world where agents will be able to work across like multiple very complicated structures as as we go along.

One other thing from a practitioner's perspective I would call out is that when we are building agents it is good to simplify the task of a particular agent so that it becomes so the the reasoning becomes a lot more easier.

So you can if you can break down the task into multiple sub agents which can all orchestrate amongst each other instead of one giant prompt and one single super agent which tries to do everything that will help both with latency as well as with quality. Amazing amazing insight.

Thanks to And I find it fascinating that uh just some time ago reasoning uh wasn't there in the models at all and now we had reasoning long traces and now we're going back full circle to minimizing reasoning. So life goes full circle and so do so do agents. This seems

and and the agent sub agents is interesting because in the day one of the question was what if I had agent with 50 tools like that was the question which was out there.

Yeah, actually uh if you look at uh in commercial systems what we are observing is many of the of the developers who are building their agents they start with one or two as a as a toy example but very soon as these agents start performing the the job that they are expecting the expectations rise and then people start throwing more and more tools at it and it becomes basically a reasoning challenge as if you go into like 50 or 100 tools and that's where like having some level of like hierarchy or sub subdivision will be helpful

and if I may we need to treat the sub aents and multi- aent systems as microservices right the same reason that we build microservices is this to reduce the the problem into the minimum effort let's say

yeah but I I believe the statelessness part might might not be necessarily true for agents you might need to share the state but other than that yes definitely with modular design

amazing thank you thanks for the Interesting conversation everyone. All right. Shall we move on to the next question? Kunch. So this one is for you Bill. What is the biggest gap you currently see in the industry's tooling for productionizing uh agents at scale? Uh additionally, in your opinion, how should it be addressed?

Sure. So uh one of the principles that's actually covered in this week's agent intensive is using evals as a quality gate uh before you move agents into production. And I think it's fair to state that the state of our tooling today is that humans are the deployment gate for agents. Um, so where I see things heading is a world where we have so many agents being built.

You know, as that confidence builds, as Sara was talking about inside of organizations and across development teams everywhere, more and more agents need to get into production. They're going to be acting in parallel. You're even going to have agents writing code on the fly to include other agents. It's going to be super difficult for human centered and human gated eval to keep up.

Uh so the tooling I see emerging from this really centers on uh this kind of continuous agentic evaluation. Uh how's it going to take shape? Well let's see uh probably yeah I think you have to think about this in terms of the organization itself.

So in any reasonably sized uh organization about 80% of the use cases or um applications for agents are going to be kind of moderate to lowrisk going to be internal processes going to be things that aren't necessarily in full view of users.

So you know I see a world where uh agentic evaluations can leverage the observability and trust primitives that you know Sarb and the team have built into our cloud and AI platforms today.

Um you can have those and then you have the simulation and offline agent improvement um you know mechanism and the net of all that is is the development of AI evaluators and uh AI evaluators are going to move these lower risk agents into production more quickly and autonomously.

uh it's going to give everyone a lot more confidence and uh it's going to speed up the kind of the big task queue and agent queue that's headed for eval but the best part is that the most complicated and risky deployments which are going to be the focus uh you know kind of for the CTO's the CIOS the CISOs u you know the leadership of these organizations they get to be evaluated by engineers because they have the time to really dig in and look at these more complex or maybe potentially more risky agents um and so the primitives for this architecture that I referred to.

They're already put in place in the Google's cloud and agent platforms. Um things like cloud trace and sessions. This is going to allow all of you to um pre-train these eval agents and you can use either real or simulated agentic behaviors.

Uh and then you combine all this with the manual and automated feedback loops and uh you're really going to be able to build these AI evaluators um that are much more and more capable over time and that's going to enable the scale that's uh of adoption and the climbing of the value curve inside of these organizations.

Uh and it's going to also partition the tasks that we give to agents of the partition the agents themselves um along risk and use case specific boundaries which is really you know an implementation concern for you know every leader in every organization right now deploying agents.

Yeah, one one other thing I would add like completely agree with will on on the the points that he made is that as within particularly within teams uh groups of either small teams or larger teams or organizations what is happening is as different people are building agents there is also this level of like I kind of like the play store analogy of like which agent should I go trust because that is made of high enough quality that I can use as either as a building block or as a standard stand alone agent for my my my task.

So this agent management review process some level of like quality gates etc that is becoming more and more common.

Um another thing that we are seeing is that um there's this notion of an agent marketplace where people can publish agents and then either you can modify them or you can use them as is but again the level of trust etc starts coming into picture and we do have some efforts relating to agent marketplace uh within within vortex uh as well.

Yeah.

and like these reputation mechanisms uh you know because that's really the currency of trust uh you know over time in these organizations is you know both the people that are developing them but also you know just this history of agent development and it it goes beyond I think a lot of the metrics today are around quality uh and you know kind of performance or efficiency but there's also going to be these new metrics that emerge around you know consistency and around like actually staying in alignment with policies especially over long task duration and as Sar was mentioning earlier is you know you have these multi- aent systems gets much more complex.

Yeah. One other uh thing which is uh about security uh as you start putting will was mentioning right as you start putting things into production uh security becomes a big challenge because you can have fairly sophisticated attacks which could be structured uh around uh agents.

An agent can do all the tasks that it is expected to do but then it can do some additional things uh which it is not expected to do. Uh so there is also like when an agent is deployed right how do you monitor it right and how do you give it accredition uh what kind of identity it should use so that we can retrace the the steps back.

Uh there is also some requests for should we have an undo step as part of the agent so that we can retrace some of the step or like the previous state management kind of a thing like for example in your collab notebook uh I know there is a reset all kind of an option that is there in the in the notebook instructions [laughter] the factory reset uh button u something along those lines like these are all uh things that that seem to be important as as agents has become proliferated into the industry as well as in other places

and in terms of security a very important also topic is how you can implement the authentication authorization hopping what I mean by that you have an agent you authorize this agent to use your credentials to do whatever you want and then this agent needs to call another agent this agent needs to call another agent how do you pass this to all these agents

yes

definitely wow that I think that answer summarized pretty like a lot of the topics for all of our five cooking days [laughter] authorizations to to agent emails to the reminds me of the movie Inception agent evaluating other agents which then in turn need to be evaluated uh uh and all the great security as well. Amazing. Thank you everyone. That was very insightful. Awesome.

Uh K shall we move on to the next question? So this is for both of you Sorab and Will. Um so as enterprises struggle uh with decades of legacy IT um do you see agentic interfaces via protocols such as A2A becoming the de facto standard for modernizing these legacy system or is that in your opinion just adding more technical depth which somebody needs to manage?

Well I I mean for me the short answer is uh yes and yes.

uh [laughter] you know yes agentic interfaces and architectures are going to become the standard for modernization and yes there will also be some tech debt that comes with it but it isn't necessarily a terrible thing we'll talk more about that in a bit but um you know just think about the sheer velocity and scale that agentic workflows are enabling it's going to completely transform how organizations think about delivering internal services and their external customer experiences and it's already happening I work with a health system right now that's using agents built on agent development kit and this is uh cascaded out to over 30,000 workers and it gives all of them immediate access to all the policies in their organization without them having to do a bunch of like searches over a bunch of internal sites or deal with like slow keyword matching chat bots.

So like even in highly regulated industries, organizations are already taking this existing architecture that they have in their business processes. They're kind of like breaking them apart and they're recomposing them into these agent-based workflows.

Um, and you know, as the ROI continues to increase, it's just going to encourage more and more of this and more of the existing applications, data stores and systems to be available to agentic workflows. And uh, ironically, the tech debt that's being built uh, is going to be increasingly burned down in parallel by agents that can execute tasks like code reviews, bug fixing, and the like.

So, we we have a way out of, you know, the tech debt uh, possibly for the first time as these uh, agentic systems improve. And I do want to mention one other protocol which um I am I'm really excited about right now and this is the agent payments protocol.

You if you think about the modern web, the foundations are basically a set of standards and protocols that enable high-speed reliable communication. Um but it wasn't until the web became the vehicle for commerce and supported value exchange and payments that it really flourished and and it is the vehicle for digital transformation today of every industry.

I think you're going to see the same art with agents. can imagine how enabling an agent to retrieve items from shops for you based on parameters you provide can make shopping it's better for you and it's better for the merchant. It's way more efficient and it's going to make your everyday life it like you know it's like a superpower operating in parallel to get things done.

And I also think it's going to be true that businessto business transactions are going to be completely reshaped by agents communicating, negotiating, transacting, verifying, even representing suppliers and ecosystems. Um, so the value is going to be really compelling and now the programming model thanks to SAR and the team is natural language.

um it's going to bring more people into the innovation process and you know you're going to end up on this kind of multi-party multi- aent uh commerce engine at web scale and that's going to build upon this agent to agent you know step one you got to be able to build the agents you know ADK step two you need to enable multi- aent you know interaction policies um but the long game is enabling value transaction to happen you know across multiple um agents whether it's within a firm or out or multiple firms coordinating uh and I think that's where you're going to the you know this breakthrough this transformation.

Yeah. No, completely agree with Will on his yes and yes uh to to to the to to the question.

Um if you think about enterprise IT systems, one of the challenges that many of and why the the systems are where they are and and and some of the challenges is because the level of investment is not that heavy because very small teams have to manage a variety of different applications and they can only do so much in any of these areas right and that's why some of the tech debt etc starts getting accumulated one I would say the the if you look on the positive side because of uh the coding capabilities that uh the models have and some of these agentic systems have we actually what I'm expecting is much more better IT systems like from the ground up itself uh that may come up because you are basically now having extremely sophisticated like software engineers building like code independent of whatever is the application and you are not making a choice based on uh like the return on investment or or how and that's that's the big promise of AI right that it kind of democratizes like quality code across the board right that's just one aspect uh of it uh the other thing which these agents are offering is that within the computer use paradigm even if you have traditional enterprise systems which with their UI being a lot more clunkier etc right and hard to use and only the subject matter experts know which button to click after which one in what order etc and so on.

um with computer use the agents can actually create reasonable encapsulations on top of these so that the ramp up time for using some of these uh traditional enterprise applications could be a lot lot easier and I'm talking about obviously there are the SAS providers but also there are very uh when I'm talking about enterprise applications the uh applications provided by SAS providers but also inhome in-houseuilt kind of like applications right so you could have interface cases on top of pre-existing applications which can make them easier to use and interact and with higher enough quality so that the brittleleness between particularly when you are chaining together multiple applications that brittleleness kind of improves quite a bit right now yeah go ahead

so I was also going to say so you know to your point around legacy systems one of the really emergent behaviors we see is um AI and agentic workflows being able to understand legacy code bases or uh proprietary code bases that are specific to an organization being able to reason about how to potentially refactor or to Socrates's point earlier, you know, like how should we go about the dependency mapping and kind of breaking apart some of these larger monoliths and breaking into microservices.

That's another merger behavior that's really exciting.

Yes. And and and so one other one other thing was that one challenge on the on the whether it is going to add technical debt is uh because of the stoastic nature of these agents, we need to design them in the right way.

uh and that's where even from a thinking perspective uh when uh we were doing I think in the lab two that we were doing the currency conversion agent etc uh if if you if you play around you need to be careful with how you construct these agents so that they are not probabilistic because then we are passing on that responsibility of correctness onto the user rather than on the on the agent and so the design etc the earlier conversation that will was talking about about like evaluation systems and agents evaluating other agents etc becomes really really c crucial uh because you don't want just a mesh of agents where each one of them worked in a particular demo and you just connected the whole thing together and you hope that it continues working so we need to be more principled relating to that as well

amazing that was that was a great overview all lot of my favorite topics like code modernization using agents personally working on one project like this really exciting at computer use to uh to um yeah to uh connecting workflows and evaluating them end to end. I think there's a lot in excite a lot of excitement in store even though it's day five for us but hope [laughter] amazing answer. Thank you Sarup and will really uh kunch would you like to move to the community questions now?

Sure. Um I love that Sor you were actively testing the code line [laughter] and thankfully we didn't know this before. I think we would have been even more you know tensed about it. We should next time we should enroll you as a tester. A very unbiased tester.

Unbiased tester. BUT I DIDN'T KNOW THAT BEFORE this call. So I'm super happy that we didn't know about it. So thank you. Um so now with respect to community question particularly these came from the community discord channels and this is from the discord user lassie for alia and softus. What is the recommended security model for crossboundary untrusted thirdparty A2A calls considering that A2A lacks built-in authentication or zero trust mechanisms

why don't you go first

actually so is prepare um specifically let me start and then I'll complement

okay so first of all I want to start with a word on trust trust it right h I am not going to use any agent in my systems if I haven't tested the agent if I haven't passed through the security review we haven't evaluated the agent and generate the performance uh review and metrics that I want right it is like you open the door to an unknown person to your place right and you say get my personal card and do my purchases you cannot do that right uh even in agent payment protocol that will mention mentioned earlier.

What we have introduced there is the notion of mandates with verifiable digital credentials that actually the user needs to sign like a document to say yes I approve this to move on and then a AP2 or agent payment protocol is built on top of A2A. I need to say that and then we can move on to the task and we can perform actually the different actions.

Now about the authentication and and authorization. I want to to to speak about this is what we have seen is different uh users or developers they used to pass the tokens from one agent to another in order to uh authenticate them. I don't recommend that at all. It is not secure at all. Right. Uh second option is to reauthenticate the user every time that uses a new specialized remote agent.

that again this is quite annoying for the user because every time you need to authenticate yourself. Uh what I see in the future coming is something like a central agent authorization authority that you will have all the agents communicating with that storing all the details of the users. What agents we have authenticate already. You don't need to do that multiple times.

Everything will be stored in secret managers. You don't need to exchange tokens. And more or less this authority will play the role of uh agent police if I may say right like a gatekeeper in order to be able to uh perform everything with a very secure way.

Now from A2A perspective also the users they can uh use extensions is a capability that we have over there that they can uh implement any security measure they prefer and on top of that they can augment that with guard rails as well. Ilia.

Yeah. One that we need to think about 88 as a protocol that stands on the top of an existing foundation. Yeah. So you don't need to just use it to solve everything end to end. You can leverage existing practices that are common to other um solutions like a microservices network.

For example, if you think about agents as part of a micros service, you will think about API gateways, access tokens, API keys as a way to enforce authentication and authorization or doing things like rate limiting uh to ensure traffic only reaches the runtime of the agent when it passes a set of uh verification.

uh this is done by design uh so that we avoid to reinvent every security practice on A2A and we actually build on the top of existing things. Uh so you can use like battle tested infrastructure like Google cloud to actually um um build uh these kind of uh skills and capabilities.

Uh one quick call out uh like in the last few days this sounds like an amazing idea to look into kind of like a secure MCP for agents uh for your capstone project. So we'll be evaluating the novelty of these. So those of you listening um might be an idea for you.

Yes. And also last week I think we announced in Vert.exai the agent builder capabilities which has some inbuilt of this. So I think when you're looking at capstone like these are the things which you have to be able to build for yourself. So thank you Ellia and Socrates. Um onto our next question for um will and softus. Um from Daniel Daniel for Burke.

In a system of autonomous generative agent swamps, how can we limit their operational scope and assign accountability for undesirable outcomes including actions?

Well, yeah.

Well, f first off, thanks for the question and uh it's it's interesting because I think it goes back to the last question a little bit and that is in many ways we're going to see the principles of zero trust security show up for agents and uh meaning it's not just going to be your agent isn't just going to inherit permissions from a business function or individual that they're representing in a transaction.

Instead, it's going to be layers of identity authorization and telemetry on a task by task and system by system basis. Um you know, there are things that are out there to help all of you with this.

uh you know maybe like agent identity and agent registries are a great place to start because that'll give you like these initial guard rails and eventually it'll evolve into things like risk management and policies as code or instructions for your orchestrator agents because again as you start getting multiple agents executing more and more complex workflows you're going to have this kind of orchestrator agent you're going to have these sub agents that Sar was talking about earlier and you know you're going to want to be able to uh you know inculcate those agents with the policies that you have and kind of the trust policies that you have within an organization.

Um, and what what I see is is and also, you know, we're just talking about cloudy patterns. You know, we're going to see cloudy patterns all over again. So, um, you know, applying zero trust inside of organization. Um, we use simple cyber security principles and you could stratify trust tiers. Um, you know, for agents.

So you can have agents that exist in different trust tiers just like today you know we have people andor systems that operate in uh in different trust tiers within any given organization based on their inherent risk and based on telemetry and based on like what certificates or what authentication they're carrying with them and also patterns that you know we're we're in such early days like we don't really even know really you know in most cases how these large multi- aent swarms are going to be operating within you know one organization or across organizations.

So there's a lot to build around the kind of signature of agents and uh you know a lot of the things that uh we described earlier in terms of um you know like tracing and sessions and the telemetry and the places where you can you can identify what's happening between agents and between agents and individuals.

That's all going to be the fuel for developing um kind of these patterns and these uh tiers of trust. And I also think we're going to end up uh kind of where we are in autonomous vehicles which we're going to categorize the risk and the permissions of agentic systems kind of in these tiers like we do today in levels of autonomy uh in autonomous vehicles.

So you know plenty of things to get started in terms of collecting the data and uh inculcating you know kind of these sub agents with um forms of trust. Uh but eventually the organization is going to have to define for themselves uh how they feel about you know these trust tiers and how they're going to free up um agent workflows along those trust tiers.

From my side I need a little bit I want to elaborate on what will said because I totally agree with him.

Uh first of all we need to reduce the scope we said right how we can do the operational scope of these agents agent registry agent identityability you mentioned that already will in agent registry we will store all all the different agent cards all the different capabilities of all the different agents but that does not mean that all the applications they need to use the complete set of agents probably we need to store over there this application has access only to those uh agents for example then after we have reduced the scope of the number of agents we can use is about agent identity that we reduce the resources that these agents can use or who is the user that can use this agent.

And of course along this journey we need to uh follow the footprints of uh the agents and to record everything for purpose. But on the other side, we can imagine the swarm of agents or we can parallelize them with real communities or real corporate environments that you at some point you have managers, directors or IC's and more or less you apply the divide and conquer.

What I mean is you can have small teams that they will operate only specific task with specific goals. You can assess them with specific KPIs. So we will see agents like managers, reviewers, approvers, auditors uh that they will start planning and performing uh tasks. I have seen already customers implementing this hierarchical model.

Uh for example, I have seen customers that they build planners before they execute something. They said okay I want to to run this task. Who is the right agent to call this this this and that? Okay, the plan that I said first I will call this agent then that agent etc. And then they give that to the agents.

Then a reviewer assess if this plan was executed correctly and then an optimizer takes this plan and optimize that for later on. Of course even if we have a swarm of agent they can work completely autonomous automatic. We cannot forget that agents have been created for humans. That means that human in the loop is critical.

We need always to have someone for critical decisions in the loop in order to say yes I approve that. with that way also you know that the human is accountable at least for some critical decisions.

Yeah. Just one more thing to you know as you mentioned kind of the architecture of how this is going to emerge.

Uh my belief is that organizations as a whole are going to be more secure and that's because for the first time they're going to have to actually um they're going to have to uh like deliver policies or that you know there's a lot of inside of most organizations there's a lot of like stated policies and then there's like the way things actually work.

But in order to give instructions to agents sufficient for them to execute tasks you have to be very specific. You know this is back to sort of like you have to you know fine grain specific you know very particular things. And in many organizations um they use humans as kind of the interstitial fluid between you know the policies that they have and what actually happens in the real world.

And so as more of these policies come to light or the kind of hidden policies of an organization come to light because they're being um written into software um generally it's going to raise the security level of every organization. So agents as a path to improving security.

Yeah. Thank you so much.

um the lens out is and like as you all were walking through I felt like flashy demos are easy right anyone being able to create it but these hard things which as you all were mentioning eval security governance risk compliance all of the things are what what is going to make a difference when you are u when you are positioning yourself as an expert so thank you um so this uh question is from Archie 617 70.

How are safe degradation strategies defined for a partially unavailable Vortex AI agent engine agent focusing on real time adaptation by pure agents task rerouting and dynamic cap capability downgrades?

Perfect K. Um it's a great question. uh I'll try to unpack it actually because I see two common themes here, two common task uh when building multi- aent systems. The first one is the need for control and the second one is the ability of an agent or a system of agents to be resilient.

So on the first one um we want to avoid those eco chambers right where you have multiple agents interacting together and potentially taking wrong assumption and going on a tangent on these assumptions like in an eco chambers. Uh there are some practices to mitigate this which uh you can put in place.

First, first of all, you can adopt a supervisor pattern where you have a central agent capable of monitoring the conversational flow, interrupting and cutting potential loops. You can also adopt a separate totally independent critic agent that is capable of uh inject itself and dedicated solely at verifying facts, potentially even using code execution as a way to do it if the use case allows it.

Uh I would also consider model diversity. U so potentially considering using a larger or a different model uh for these critical steps compared to the rest of the system. For example, you might have for a part of the system Gemini flash and for the supervisor Gemini Pro.

Uh this prevents share bias uh because it's not the same model uh making decisions uh so that the supervisor is not really blindly agreeing with the workers.

on the second one which is the ability to be resilient um so the ability of like have certain degradation strategies the the real question is if one engine is down and I'm using A2A to have a mesh of agents how do we adapt from it so really I would say the goal there is still provide value to the end user even in the case of failure of course like a common practice will be implement a a strong retrying system for example you might want to consider exponential back off so that we keep retrying even if the agent uh if the remote agent is failing.

But then you can also consider rerooting. So the idea that you might want to back off to a general generalist agent that can answer some of the question you might not be as deep as the agent that is failing but you can still provide value to the end user. I would also consider a transparent UX.

That means that for critical actions, imagine you have a sub agent which has the only task of booking a flight. Yeah. And that agent fails. You don't want to back off to a generalist agent to book the flight. You might want to be transparent with the end user and say the flight is not possible at the moment to book for the flight, but I provide a UR itinerary. If you want, you can book it.

Here are the instructions. So like depending on the UX you can and the product that you're building you can adapt some of it and so the idea is really to give this partial fulfillment of your task where even like if you one agent fails and three others are completely you can still provide value to the end user by partially fulfilling the request.

Yeah and I would uh I would refer back to the assignment which was there uh where I think there are references to where there are references to when you are defining the agent uh be clear with uh their error messages which are there and failure patterns. Don't just silently fail uh fail basically uh let's say you have an a sub agent which is talking about a particular task.

Let's say due to whatever service, whatever reasons the service is not available and and you are calling and it is giving a 429 or a 503 etc. Give nice responses so that the other agents can adjust around themselves. They know what is the reason for the failure and through that they can educate the the user and can bubble up that those messages or the failure patterns which are there.

This actually I I would say because of the natural language capability of the agents these systems can be a lot more resilient than traditional software systems where any code path if it fails it like everything just breaks because you assume perfect responses etc.

Here there is a chances of and and thank you for a very deep question like really appreciate it like the the chances of recovery is lot lot higher with reasonable outputs uh for the end users. Amazing. And you know just one quick thing to add on to that uh in when we talk about agents supervising and figuring out failure modes etc.

Let's not forget humans uh in all of this because there are also ADK offers ways to do longunning forking of control flows to humans. So some kind of risk management to see when it's become too messy for agents to figure out for it to a human to make their decision. Yes,

I'm actually thinking Will's comment too with respect to agents, the coding agents building themselves so that figure out the optimized way of answering this sometimes. Maybe in the future, I don't know if it's there yet, but maybe in the future there would be a agent that gets created that solves the problem and then kills it by itself. So, it'll be interesting to see.

Ephemeral software development agents by agents.

Agents by agents.

Buckle up. automatic automation. [laughter]

We have been doing well on the tagline for the classes. So for the sessions and I think this would be one which really look forward to. Um the next question is u sorry um the last question is for Sab from Chumban Bobch. Um agents can take different reasoning paths making cost unpredictable. What architectural strategies or hardware optimizations do you recommend to keep agent latency and cost stable at scale in production workloads?

Yeah, I think this quick uh very well connects with our earlier question as well, right? So, uh I would say if you look from a end user perspective, there are a few strategies that you can use to control cost as well as token length etc. because it may make some of the applications infeasible, right? If the if the latency is is very very large.

Uh the very first one and we still see a lot of people not even being aware of it is prompt caching. Uh as you might have been writing agents, you might have been seeing that the the the length of the prompts keeps alo increasing because you have all these different conditions uh that are there that you need to capture, you need to describe the tools, you need to do it in a lot more detail.

We just talked about error messages. need to explain that as well to uh to the to the model. Um most of all large language model providers right including Vortex as well as others provide prompt caching where a repeated prompt which is being sent to the model again and again and again you don't need to recmp compute it.

That has two advantages um actually three advantage like one is your costs go down because we are caching and you are not computing it right.

the latency is better right and even to a certain extent pred predictability or uncertainty etc like that also uh goes down as uh as well the second one I would say is relating to model routing and I think there were some other u we alluded to it I think maybe some practice was was mentioning uh it that depending upon the level of task or the complexity of the task you may have a pro model for very very sophisticated top level orchestrator versus a much more simpler like a flashlight even uh that you can uh you can use Gemini flashlight for very pointed tasks right like let's as an example I like the the case that we often discuss internally is if you are if a user is saying hello you don't need uh like I don't know a trillion parameter model to to go decide what's the what's the response over uh over there right so those type of things and then the third one which is a little bit more sophisticated is the constraint sampling uh piece where if you have outputs that you think are within a particular domain and I think maybe well was mentioning about it that we could instruct the model to sample only from that space instead of generating everything in natural language etc and so that can also improve both performance lower cost improve quality all the all the benefits that you can imagine now on the hardware side uh that is I would say a lot more involved uh that is where there are techniques like KB caching uh which is which is there to improve performance that's how we can expose the prompt caching uh aspect to our users and there are some other optimizations that we do under the hood.

There's also speculative decoding to make things faster as well as quantization is a very very strong mechanism through which instead of using well right now we don't use like 64 bits or 32 most of the development is on like 16ish bits then eight then four etc and so on. So those also improve efficiency because you have fewer bits to process etc. So

and if I can add one more thing also guard rails is very important to stop the interaction as soon as possible you find something ADK probably so you saw that in collabs that you already run right we have collabs uh sorry we have callbacks uh before and after calling an agent before and after calling a model before and after calling a tool you can set over there guardrails and to stop immediately the interaction we have in ADK plugins that you can set these guard rails across all your agents and of course you can link everything with model armor and immediately if something is relevant you can say you know I cannot answer this question for example

exactly

and uh just to elaborate the technologies that sort of mentioned things like speculative decoding prefix caching etc this is covered in the first part paper foundational models of our previous iterations of the course for those of you watching uh please go have a look it's uh and we will also attach it in the description of the YouTube uh uh link. Um all right,

thank you. Um so one of the things which um the community really loves is also to understand what are your thoughts of where everything is going like we have had incredible discussion but I would love to hear final thoughts of what you want to say to the community. Um why don't you start ahead Bill? [laughter]

Sure. Well, as you can tell probably from this discussion and probably from the last five days, uh, it's early days and all of us here, you know, building technology for all of you. We're really depending on you rolling your sleeves up and, you know, exposing where things are working well and where things aren't working well.

Um, so your engagement this week, your learning, your interaction, your feedback to us is absolutely critical. Um, you know, Sarb and the team are creating incredible technology at incredible scale. uh and there's lots more to do.

So my final thought is you know please continue you know exploring the rapidly emerging capabilities of you know cloud and AI and vertex and agent platforms um and get your feedback back to us u because that's how we're learning as Sar mentioned earlier he's got his sleeves rolled up this week he's debugging for his son he's blowing stuff away with the delete button uh so we're all doing it and we're counting on you to to really you know give us those insights are going to make our products better and better over time.

So, thanks for your engagement.

Thank you. Well, um

they'll be talking about insights and feedback. We'll be rolling out the postc course survey um right after uh this. So, uh before the capstone. So, please give us these uh your insights there so we can improve the future iterations of this course and see what you liked as well.

Socrates, why don't you go next?

Ah, what do we see in the future? Actually three areas make everything simpler to go to production. We are not there yet. Second is ethics and legal aspect of things. We need to consider we need to create some regulations. It is very important. Nobody talks about or we have started talking about this. And the last thing is live agents. We will see all this multimodality live agents.

We will see new ways of interacting with computers. Probably we know now we have the computer use for example. you can control your uh computers with agents, but probably in the future we might not need computers at all. We might speak in a speaker and we can do everything that we need, right?

Yes. And I know you um Haiko also has a demo. Maybe we could add it to the live agent with computer use that has been very popular. Yes. Elia, why don't you go next? Well, future is difficult to predict, but I will say that we will see more and more agents becoming an amplifier for the value each one of us is delivering. And I will say if I have a suggestion, please start adopting your agents.

What I mean is really invest time into uh developing or using agents that can enhance your productivity. Uh because it's something I personally did for a long time and really I can see like myself looking back in like a year my productivity has increased. So I will see that more and more and more on the on like on the prag pragmatical part of it.

I will say read the way paper because we provide a step-by-step kind of execution how you can build and deploy agents to production. You don't have to start with the fullblown picture. Start simple and iterate over time.

I love it. Last but not least

yeah uh I would plus one uh to Eliah what he said and I will emphasize on the learning part. uh the field is moving extremely extremely fast and actually it is a good learning uh opportunity for all of us like what agents can do today.

uh even if I think there were we have we had references about like for example the ADK we added a lot of new features even just last week uh agent engine capabilities we added core capabilities the AP AP2 the agents payment protocol which we believe is critical for the success of agents in the real marketplace that will was mentioning like all of these things are have happened there are more things that will happen in in future as well and I would say to be very abressed with uh like whatever is the latest technology so that you can absorb it into highly functioning agents which can go into production and as I was mentioning it can also help your productivity the productivity of your organization and whatever is the workplace like super exciting time uh to be here in this particular field and again thank you all as well for participating as part of this journey and this is a learning for all of us together.

I I do have to say though when you said learning um like all of us have blind spots in my opinion we all think oh I we have been I'm sure you all have been doing this for a long time um but even for simple things going from AI first to AI native is so important like the folks might not know sort of we have the cloud AI for AI sessions just that learning what others are doing and incorporating that in our day-to-day life has been really impressive.

So I think all of us need to bring a curiosity for us to be able to build. So thank you. Thank you so much despite your busy schedules being here answering questions um sharing your thoughts.

It has been a really great to hear all of your viewpoints particularly most of us talk about flashy things but you talked about the pro challenges of how the enterprises or everyone would be going through and then how we help try solving them and starting breaking down into smaller pieces and adopting it and having sa try it [laughter] and sharing the concerns.

All of this has been really really amazing. So thank you so much for being here for being part of the journey and for also the support. We have had this crew who have been going through this challenges. So this is real life experience. So thank you. Thank you so much. Appreciate it.

Thanks everyone for joining.

Honor to be here.

Thank you. Thank you all.

Thanks.

Byebye.

This has been amazing. And u now on to our next session. So we have three more segments. Um we have the code labs as normal and then pop quits coming and then the last thing exciting thing which we have um Brenda coming in with the capstone announcement. Code labs. Can we have Laxmi on stage please?

Hi Lakm.

You're back and yes back to day five. Hello Anand. Good. Okay. And what an incredible week it has been. And we are on day five. Right. So for day five, we have two notebooks. We start with agentto agent communication and then end the day with deploying agents to production. So as we start first, I want to give a shout out to Lavi my colleague who has the who is the author of this notebook.

Thank you so much Lavi. Now let's get started right. So as you build agents you find that a single agent is very difficult to handle all the functionality that you have. So as you build complicated scenarios you will need a multi- aent architecture. You will need specialist agents who are experts in one specific area. But how can you do that?

So you might think okay I will have a root agent and then I will have multiple sub agents who are experts but real life is not so simple. You might want to use agents which are built by other teams in your organization or you might want to use agents which are built by another organization. Cool. Awesome. But how do you make sure that these two agents can communicate with each other?

Because they might have been built in a different language or they might have been built using different frameworks and more importantly they might be running in two different networks right or servers. So you need a standard for these agents to communicate and that's where the A2A or agentto agent uh protocol comes in.

It is a standard for cross framework cross language cross organization agents to communicate with each other. Right? So what does all of this mean when you're building an agent? So let's kind of dive a little deeper. So what I'm trying to do today is to build a customer support agent.

And this agent will interact with the user and answer questions about a product like you ask about a specific product, it will give you its price, what are the features of that product and also the availability. Cool. Awesome. But there is a problem. You do not have the data of the products. This data is with your vendor, right?

So the vendor owns the products and he has all the details of the product. So how do you make this work? One, you could uh try asking the vendor for the data. But that's not a practical solution because there are different organizations who own the data. So uh what can I do here?

So I went and spoke to the vendor and they said that they already have a agent called a product catalog agent which does exactly this answer questions about the product. Awesome. So we already have a agent and I already have a customer support agent. So but the product catalog agent is running in the vendor's network. So how can I access it?

So the vendor tells me that the product catalog agent is A2A compatible and customer support agent can talk to that. So what exactly uh does this mean when you say that it's A2A compatible? So and more importantly how will the customer support agent know what the product catalog agent does and how to call it. So these are the two uh questions that we need to solve for.

So when you say that a agent is A2A compatible, what it means is that it is exposing something called a agent card. Think of it as your business card, right? So this is the example of a product catalog agent card.

And here the agent is giving a description of itself and that says that my name is a product catalog agent and this is my description and it also talks about the tool it has which is the get product info and the customer service agent can access this product catalog uh agent and then get this information and how can it access that so since it's A2A a compatible it has been deployed onto a URL.

So in this case we are uh for this notebook we have deployed it locally and hence you will see a URL like local host but in reality this could be the uh you know the server in your organization where you are running it.

So this makes sure that uh you know your there's a way for your agent uh to be called by other agents and also this agent card explains everything that you need to know about the product catalog agent. So if I take a step back here there are actually uh two problems right or uh two parts here.

one how do you build a agent and make it A2A compatible so that all the other agents can access it so that's the first part and the second part is okay there is a agent out there and how do I access it so let's kind of look at the first part now how do you create the product catalog agent so you create a agent as you've done over the last four days and uh that's a uh you know get product info is the tool which takes the product catalog and returns the uh results to the user and then to make it A2A compatible is extremely easy if you are using ADK so if I kind of uh you know get into the technical aspect of it it's as simple as making one function call right so you have built a agent and you're converting it into a A2A compatible agent by saying the port at which it needs to run and specifying the name of the agent.

So that's all you need to provide and you have a agent and when you kind of use this function is when the agent card gets created and this agent card would always be available as you know/ aentcard.json JSON which you can access it and in our case this is on local host since this is for a notebook. Awesome.

So this uh product catalog agent is all ready and then we just need to call it and how can we do it. So at our end we have a customer service uh agent and this um agent can have uh uh so sorry let me just go here. Yeah. So this is the customer support agent and then how do you make sure that it can access the product catalog agent. So create a sub agent, right?

So and the sub aent here is called the remote product catalog agent. And if you look at the remote product catalog agent, it's a little different from the sub agents that you have created before in the sense that this is a remote A2A agent. And again like any other agent it has a name and it has a description right and it also has another field which is the agent card.

And what we need to do is point it to the other agent that you want to call. In this case it is the uh product catalog agent which is running in a local host. Right? So that is how simple this entire part is. So if you kind of uh scroll down in this notebook, we have put in some scenarios for testing the A2A communication. Right? So there are a few queries like can you tell me about iPhone 15 Pro?

Is it in stock? And then what is actually happening behind the scenes is that our customer support agent gets this query. it passes it on to the sub agent which is actually a proxy for the you know remote uh A2A agent and this agent will go and fetch the information from the catalog and return it back to the customer support agent which then uh responds to the user.

So that's how the flow is going to be right and uh that brings us to the end of this notebook but there is a whole lot of information out here the documents that you can read to understand A2A better the sample code you can access and all of that right so also uh I strongly encourage you to try out few of these ideas try adding a inventory agent or try adding a shipping agent and see how it goes and let us know and with that I move on to my next notebook which is on agent deployment.

So let me just uh share the tab. Okay, cool. So you have built agents but it's all in your notebooks, right? And if you kind of stop the session then you cannot access it anymore. So that's one plus since it's in your system nobody else uh outside other than you will be able to access it. So how do we uh solve for this right?

So the way to solve for this is to deploy it and uh today we'll be talking about deploying an agent on GCP. So if you already have a GCP account you can use the GCP project to deploy on it. But in case you don't have, you can sign up for a free Google Cloud account. So there's a link in this notebook on how to sign up. And when you sign up, you will get $300 in pre credits.

And this is valid for 90 days. When you sign up, you will be asked to provide your credit card details, but that's a form of verification. You're not going to be charged.

And then once this $300 uh dollar of credit is over or the 90 days is over whichever is earlier then uh you will not be charged until you explicitly upgrade and also the demo in this notebook this stays within the free tier of the agent engine. So I'll talk more about it as we come and there are a lot of links to the videos and the documents in this notebook.

So uh make sure that you kind of read them and watch this video. Awesome. So let's kind of go back to a very simple agent. So today we are going to uh have a weather agent, right? So what this weather agent does is it calls a function and it will kind of uh return to you the temperature in different uh cities, right? So you have a couple of cities listed out here. Okay, awesome.

So you do have the agent and the next step is deployment. So ADK supports multiple deployment uh platforms. In this notebook, you'll be deploying to the Vert.x AI agent engine. And Vert.x AI agent engine is a fully managed service specifically for AI agents. It's easy to deploy and it has built-in autoscaling and session management.

And then if you want to read more about agent engine, understand what it is, there's a documentation out here. Also, agent engine offers a monthly free tier at the rates of which is again available in this documentation. You can also deploy your agent on cloud run or on kubernetes engine. Cool. Awesome.

So we need to have some configuration again for these deployment and so that's what we are setting in the config file and once that is done we are ready to deploy.

So agent engine is available in multiple regions and for the purpose of this notebook since we are deploying a very simple agent we are randomly going to choose one of the agents but when you're going to uh deploy it in production there are a couple of things that I want you to keep in mind.

One, choose a region which is close to your users for lower uh latency numbers and then again some of the companies might have some requirements with regard to the data right so which again uh relates to what are the policies and uh you know other requirements. So make sure that you follow all of these uh requirements when you choose a region.

So we have done all the settings and all that is remaining now is to deploy the agent and with ADK it is a simple one-step deployment. So it's as simple as ADK deploy agent engine and then you kind of give the name of the agent that you have created which is like sample agent in this case. So when you kind of run this step, it takes around uh 3 to 5 minutes for it to complete.

So please wait while it is completed. So you'll kind of see all the logs while uh it is uh being deployed and once it's deployed you will get a resource name of this format. So awesome your agent is deployed. So what's the next step? The next step is to query it so that you get a response. So in this case what we uh our query is what is the weather in Tokyo.

So what is happening over here is this query is uh basically a query to the remote agent right or the agent which is now running not locally but uh which is kind of deployed and then you get a response. Awesome. So uh so here uh I mean throughout the week we kind of talked about sessions we talked about memory right and then in today's uh notebook we have used a in-memory session.

So what happens is that when you kind of log out and uh when you uh you know uh uh close the session all the conversation until then is forgotten by the agent.

But suppose you know you want to know say for example you ask the weather about Tokyo suppose you want the agent to remember what is uh conversed with it in the previous session what you can do is you can use a memory bank so memory bank gives your agent long-term memory right so irrespective of the number of sessions you have it kind of saves that information and suppose I kind of you know uh ended that session and I kind of start another session and then I ask about okay which uh city was I talk talking about in my previous question and it will kind of tell you that you were talking about uh the weather in Tokyo.

So again there are a lot of resources that you can go uh and read about and some samples that you can test out. Last but not the least once you have used your agent engine and you have tested everything please make sure that you delete the agent engine. So this will ensure that you uh you will avoid incurring additional uh costs uh if you kind of just keep it running. So make sure to do that. Cool.

So uh with that you're ready for your production deployment and again there's a whole lot of documentation on ADK on agent engine on the ADK deployment practices again cloud run deployment as well as GKE deployment. Make sure that you go through them. And with that, we come to the end of day five. We started with simple agents. Then we talked about multi-agent architectures.

We enhanced our agents with tools. We talked about context engineering. We learned about observability. We learned how to evaluate agents. And then we spoke about agent-to-ag communication using the A2A protocol. And finally, we learned how to deploy the agents that you have created into production. But this is just the beginning.

I hope that you complete all the labs over here and we are really looking forward to what you're going to build in the capstone projects. So Brenda will be explaining more to more uh to you about the capstone projects. But first back to you Tanch and Anand.

Thank you Lakshmi. This was great particularly walking through the entire course. It was really good and I hope folks take the benefit of it and all the documentation are right there for you for you to be able to explore further as well. Thank you so much for being here and walking us through the journey. Laxshmi appreciate it.

Thank you.

So now we are on to our favorite part of pop quiz. Ann.

Yes. Get your pencils and pen ready and some popcorn as well.

So, let's go to the pop quiz.

Yes. So, u before we start, should we see where in the world people are from? Can you all start typing while Anand is going with the question?

Go ahead, Anand.

All right. Your first question would be what is evaluation gated deployment? Is it a a process where users must rate the agent before they can use it? Kind of uh uh the thing what Sorup talked about of having a trust reput reputed marketplace or B a principle where no agent version reaches users without passing a comprehensive automated evaluation. We will granice talked a lot about this today.

Uh C a deployment strategy that only releases agents to internal evaluation teams or is it D a method of manually reviewing every single agent interaction in real time. So think about that.

I see answers popping in.

Yes, your answer would be shown in 3 2 1 and B. So it's about evaluating comprehensively without before you uh give it to users and that is I think evaluation we have mentioned in the previous days and emphasized a lot today. So that should ideally be part of your capstone as well. All right moving on to the next question shall we k how do the A2A and MCP protocols complement each other?

These are two separate things. But how do they complement? Is it with a A2A is for delegating complex goals to other autonomous agents while MCP is for standardizing connections to specific tools and resources? Or B, A2A is for connecting to databases while MCP is for connecting to other agents. Or is it C, A2A replaces MCP in an enterprise environments? Or is it D?

MCP is used for remote agents while A2A is you only used for local agents. I see a lot of you have guessed the correct answer in the chat.

I can't believe how you come up with this answers. Thank you.

Really good. Happy to see that you're reading in detail and hopefully it helps you um understand the course even better. So the answer is A. Yes, that's right. A2A is for autonomous agents or MCP is for tools. Movingly, moving on to the next question. Which safe rollout strategy involves running two identical production environments and switching traffic instantly between them?

Uh your options are A Canary deployment or B AB testing or C feature flags or D blue green deployment. Think about even take the course. You should be able to answer this question.

Exactly. Even the question kind of mentioned the answer. But your answer will be shown in three, two, one, and it's D. So blue

I see a lot of right answers.

Yeah, it's a software engineering principle. But this also applies like as implied in other days. This also applies to agents because agents run a software after all. All right, let's move on to the next question. What are the three layers of defense in Google's secure AI framework as applied to agents? Is it A firewalls encryption and identity management?

Or is it B red teaming, blue teaming and purple teaming? Or is it C policy definition with system instructions, guardrails, filtering and human in the loop escalation? Or D unit testing, integration testing and end to end testing. Your answer will be

we talked about this today.

Yeah. in the white paper. So, and if not, you can um think about what could be a possible option here. Uh all right, let's go to the answer in three, two, one, B. So, uh secure frameworks involves all of these guardrails, policies, humans just to make sure that the agents do not go off rail

and ADK lets you define many of this. Yeah,

definitely. And that's why having a good framework, a development framework like ADK is super important for your production workloads. All right, let's move on to the final question for the day and the course.

All right, everybody. So get all of you I would like you to take like think about it like assemble and think about this question. You've got to get this one right. In the observe act, evolve operational loop. What is the purpose of the evolve phase?

Uh, is it A to real time triage security threats using circuit breakers or is it B to use insights from production data to update evaluation data sets and then permanently improve the agents architecture or logic or is it C to monitor dashboards for latency spikes or is it D to automatically scale the agents infrastructure based on load? I see a lot of wrong answers.

This one should be straightforward as well everyone. Um for example, option number D is uh should be suspicious to you [laughter] but uh like doesn't fit into the logic but your correct answer is B because B is where you yeah evolve the agent's logic and architecture to match what it needs to do. All right. Uh that would we conclude our pop quiz and Brenda, would you like to come on stage?

Yes, this is the most exciting thing. Brenda, I think everyone has been asking for it. [laughter]

Hey folks, I'm Brenda from the Kaggle team and I'm so excited to get to announce the details of our capstone project on Kaggle. This is your chance to take what you've learned and put it into practice. In this final project, you will be called upon to build an AI agent. We have four categories you can submit your project in.

The first one is concierge agents which will help solve problems that individuals have like meal planning, shopping assistance or calendar management. The second one is enterprise agents which are designed around corporate problems like business workflows, data analysis or customer management. The third track is agents for good.

These are solutions for problems that humanity experiences like challenges in healthcare, education or sustainability. Finally, if you have a great idea that doesn't fall into one of those three categories, we have a freeze trial track where you can exercise your creativity. We've covered a lot of concepts and technologies through the white paper, code labs, and Q&A sessions during the live stream.

We're really looking forward to seeing how you incorporate them into your final projects. A few things to keep in mind about the capstone project. Each participant can submit to only one track, so choose carefully. You may work individually or in a team of up to four people. It's completely up to you.

The deadline for submitting your projects is the 1st of December, but we recommend submitting early in case any issues arise. Finally, the top three winning teams in each category will receive Kaggle swag and recognition on our social media channels. Every participant in the capstone will get a Kaggle badge.

Now we have heard a lot of you including Sir Rob say that you really want a certificate for your participation in the course as well. I am thrilled to let you know that we have listened and participants in the capstone project will also get a certificate that you can share. The capstone project link will be shared with you all shortly on Kaggle Discord and an email. So keep your eyes peeled.

Thank you so much.

Thank you Brenda. That's amazing. And I know folks have been waiting for this particularly the certificate as well. So we are looking forward to it and I I know and then all of us are looking forward to seeing what the capstone projects are going to be and how what are the things which are coming out of it.

So thank you so much for announcing this Brenda and really appreciate it and thank you for all the help over the course and making you are leading the effort and making things happen. An we are towards the end and we are here. [laughter] Um [clears throat] thank you. Thank you so much for being here.

Of course Anand mentioned it earlier the post survey is really important because that helps us drive towards our next steps. Um is there anything to add Anand for from your end?

No that will be all. Thanks to everyone and I'm looking forward to how you enjoyed it uh and your submissions in the capstone and um maybe stay tuned for uh another iteration of

we're already ready for it

in the future. Yes. All right. Thanks everyone.

Thank you everyone. It was great having all of you for the last five days and we really appreciate your time. Looking forward to the agentic journey.

Take care. Bye.

Thanks. Bye.
