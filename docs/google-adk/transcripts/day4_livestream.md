# Day 4 - Livestream Transcript

---

Hello everyone. I'm Ka Patlola. I'm one of your co-hosts for the five days of AI agents intensive course. I'm with the I am here with Anand Naval Gria. Anand why don't you say hi?

Hi everyone. Anant here. Happy to host you again today.

Thank you. So we are in day four of the AI agents intensive course. Thank you for staying with us over the last four days. We are super excited and thrilled seeing all the momentum across all the platforms in the in your feedback in your questions in your engagements with us. We really appreciate it. So keep engaging with us and keep asking us questions and we are here to answer it.

Um this a as you all know this is a five-day course and the course is designed in such a way that we are going from basic to advanced in several different ways. You have the option to pick white paper companion podcast with it code labs which are mandatory and optional and towards the end tomorrow we have an exciting uh announcement with capstone and also the production goes up course.

I encourage all of you to join and uh this announcements are all happening uh through your email which was registered or through discord announcements or you could also see it in the course platform as this is a village it is not possible without the moderators who are keeping us engaged. So please ask them questions. They are here. They have a real life experience with customers.

So they would be able to help you in assisting and understanding more about the course. This is designed in such a way that it is going to be intense. Some sometimes some topics are intense. Uh but the we are having uh code labs and stuff to make sure it's from basic to advanced. And today's topic is day four for agent quality.

The future of AI is agentic and the success is determined by its quality. But Anand is here us here to walk us through the white paper overview. Anand.

Hi everyone. Um thanks Kunch.

So uh hopefully you have read today's white paper but over the last few three days as Kant mentioned we have built agents brain given it hands through tools and the memory so it doesn't get amnesia right but before we deploy this complex machinery how do we know it actually works reliably and can act autonomously or semi-autonomously in a production environment and that's why today in day four we cover agent quality and um this is especially important for software that is inherently nondeterministic like our agentic systems.

So if you read today's white paper it's you would have seen that we introduced a new framework built on four pillars of quality effectiveness which answers did it achieve its goal efficiency which measures the cost and speed of um the agents robustness which talks about handling errors gracefully and safety which talks about uh did did the agent adhere to ethical guidelines or not or to what extent it did.

The paper also proposed a strategic hierarchy starting with the outside in blackbox view to find uh validate final outcomes and then moving to the inside out or glassbox view to debug the actual reasoning trajectory because an agent can get the right answer for the wrong reasons.

So the journey matters as much as the outcome especially for agents to see that inside the glass box we need deep observability built on the trinity of structured logs for raw facts end to end traces. This will allow us to follow the casual or the c sorry chain of thought and aggregated metrics for health trends.

Thereafter, we then explored how to scale judgment um of the uh of an LLM evaluation using um LLM as a judge for rapid automated feedback based on reasoning while keeping human in the loop essential for establishing the golden suit uh golden set of ground truth.

All of these powers the a uh powers the agent quality flywheel turning every production interaction into a data point for continuous improvement uh of the agentic systems going forward. Um but this differs significantly from the predictive AI um quality measures which we will hear about later in the Q&A session. That's it for the white paper of the you for the Q&A. punch

there.

There's a lot of content um because it is a complex topic by itself and here we have the judge like the panelists here who have experience in this from several different uh profiles which we have seen and having the experience there some of them like we have authors as well and we are super excited to have um the panelists on stage um and these folks have been working with customers um and also two of them are white paper authors um one of them from the GDM uh research uh can I have them on stage please oh hi everyone thanks for joining

thanks a lot for having us

thank you u like it's so despite your busy schedules thank you for being here and taking the time to answering the questions because it is um very relevant for the community to be able to hear from you. So we really appreciate your time and you know the engagement here today. Uh why don't you start uh Dr. Bafa give a quick intro of yourself.

Yeah sure. Thank you very much Kan and Nance for having me. Uh hi everyone. So I'm a generative AI specialist at Google. I'm based in Paris. uh I lead technical engagements focused on agents and multimodel AI and I'm also co-author of the white paper that was released as part of this course on agent quality and uh really excited to interact with our amazing community today.

Thank you.

Dr. offer. Thank you, Sean. Why don't you go ahead next?

Hi. Yes. So, my name is Sean Gooding and I'm a senior research scientist at Google Deep Mind working on autonomous agents and yeah, really excited and happy to be here. So, thanks for inviting me.

Thank you for you know despite the schedule. Thank you for being here. I appreciate it. Sean Tan, why don't you go next?

Yes. Hi everyone. I'm Tan Bulush joining you from Amsterdam. I'm the head of uh black belts in the applied engineering or within Google. It is the same team as VAFA. Uh I'm also one of the authors for this today's paper. So really happy to be here.

Thank you Tan. Appreciate it. Um doc Jay.

Hello everyone. I'm J from Nvidia. I'm a data scientist and a Chicago grandmaster. I'm working on data science and LM powered agents. Very happy to be here. Thanks.

Thank you Jay. like we are super excited to have you particularly the Kaggle Grandmaster has been like it's a real pleasure to have you here so thank you so we'll jump in quickly because this is what the community is waiting for um an why don't you take it up

yes thanks Kunch so first question Sean this is for you given your experience what are the subtle failure modes or biases developers should watch out for when they start relying heavily on models to judge other models. But we discussed the LLM as a judge in the white paper as well.

Sure. I I think this is a really good question because I think we like to uh maybe sometimes iterate quickly and assume that LLMs as a judge work well out of the box. But we know that these models do have biases and that shows up in the way that they evaluate different types of generations. So I'm going to talk about four uh just at a very high level. So the first is preference bias.

So one thing that we've seen uh you know in practice and also there's many papers that discuss this is that typically models will prefer generations that have been generated by themselves. So if you have a situation where there's multiple models um that have made like generations and you're using one particular model to look at those generations and say whether they're good or not.

um you know it's no surprise actually if there is a preference there for the model to select the generation that was generated by itself um which is something to really look out for um and the the second thing is verbosity.

So interestingly models quite often if you have very confident long verbose uh kind of um generations typically models will favor these which is quite annoying because I'm sure most of us are aware that these models do tend to act very confident and come out with very long verbose um sort of answers. So so that's something that you definitely see uh in in these models as well.

Um another one too in multi- aent setups is sicker fancy. So sometimes you might have um two agents that are discussing or uh kind of analyzing together whether an output is good and same as like how we have sophantic behaviors when we talk to language models.

If one model pushes back and says no actually I think this is a really good generation you do actually see that then the LLM as a judge might be like oh okay sorry maybe it is good. Um and so there are these dynamics that come about when these um agents talk to one another uh kind of about these generations. And then the final one is score bias.

So typically there's this phenomena where the models might try to hedge their bets mainly because uh you know they kind of want to get the right answer.

And so if you have um maybe you have a prompt which is trying to score an agent trajectory on a scale of 1 to 10, don't be surprised if the model continually comes out with five because it's not sometimes they're kind of primed to not make a strong decision either way. Um and this is interesting because you really do have to think about the the way you operationalize or set up these prompts.

Like should it be uh like a number rating? Should it be side by side preferences? um because these things actually can make quite a difference for for how well the model um kind of is able to judge the output.

And I think the the final one too which is probably more applicable to agents is that one of the things we've seen is you might have a trajectory for an agent and an outcome and you might kind of have an LLM as a judge to look holistically at this trajectory and outcome and if the outcome was good then irrespective of how good that trajectory was some of the LLM as a judges tend to be kind of biased uh by what happened in the outcome and not really pay attention um to to kind of the intermediate steps which can have quite perverse um like long-term effects if you don't watch out for it.

So yeah, I think it's a great question and I think one of the ways we typically tend to um adjust for this is it's really important to evaluate your evaluators and make sure that you have a test set um so that you you know you're not just sort of eyeballing it or or feeling like your LLM as a judge is good like you really want that.

Uh that's amazing Sean. Um I think a few things which I take out of this which is really relevant for the community is overtrained tokens especially if you use a numerical uh numerical output. Um uh second thing is recency bias the final outcome mattering more than the trajectory.

And the third thing is evaluate your evaluator uh especially with human correlation right like matching to see if your evaluation correlates with how humans would do it. These are really great uh uh insights. Thanks a lot Sean. Um, awesome. All right. Shall we move on to the second question, Kunch? So, uh, this is for you, Jay.

Um, how do you say talk in the talk in the spirit of evaluation, how do you see evaluation being different now for AI agents versus evaluation for predictive models in the pre- aentic prejai era?

Yeah, that's a great question. So, um, evaluation for AI agents can be very challenging. So you know on Kaggle for every predictive model usually we have a leaderboard. So uh you submit a prediction there's a metric automatically scored. Uh we want to um adopt the same pipeline for evaluating the agent. So I think there can be four things that are useful for agent evaluation.

First is a verifiable metric. So just like a kaggle leaderboard is it possible to set up a quantitative metric that we can just run and uh the agent cannot make shortcuts to get the correct answer. So sometimes that's very um resource intensive and time consuming to set up such evaluation. So that's why we also need grounding. So LM uh has profound knowledge in the in the pre-training stage.

However, you know, we really need to figure out so how does the LM based agent reach to this conclusion. We want agent to provide references and all the other evidences in the thinking process. Third, we need LM as judge. So because agent can generate a large quantity of traces. So sometimes that's so overwhelming for manual review.

So we do need automated like LM based approach to go through those agent uh to go through those traces and look for reflex. But lastly we do need some uh human review especially for the code that generated by the uh LM agent. LM can be really creative when it is forced to come up with a really good answer. So sometimes it can make all these unexpected uh tricks you know while writing the code.

So um we cannot fully cover all those corner cases in a predefined pipeline. So sometimes human has to jump in and look at the code and do that's the last step for the evaluation.

Wow.

Yes, that sound uh definitely seems like going from Sean and your answer LLM tend to do can do uh whatever it takes to uh convince you that they are correct and reach the outcome but that doesn't necessarily align with our objectives and especially quantifying this kaggle really really impressed with how you're managing it nowadays and the non-deterministic era really great awesome let's move on to the next question k uh so what are this for all um three of you Vafa Dr.

Vafa Turan and Sean. So what are the best practices or suggestions you would give for evaluating multi-aggentic systems and I would love it if you could uh draw from your uh applied experience from your customers as well to answer this one.

Yeah sure thanks for the question. Uh so first of all the main challenge with evaluating multi- aent system is that uh even if you have the best model and even if your individual agents are performing really well in isolation the overall system might still fail. Uh it's a bit like a soccer team.

You can have the best players in the world but if they are not working and coordinating together as a team uh you might still lose the match right? So my recommendation number one in addition to the individual components make sure to evaluate the interactions. Uh the orchestration layer is really what makes or breaks a multi- Asian system.

Um and this is not something you should consider at the end. You should really think about this from the very beginning. You need to architect and design your multi- aent system to be uh easy to evaluate. Now how can we concretely evaluate it?

Um we just mentioned there are different approaches and uh the smartest way is to combine several of them because we don't have one single approach that can captures everything yet. So we need to have a multi-layered evaluation uh with uh metrics that can you know uh can you can use them as a first filter to get the global picture of your system health then you can also use LLM as a judge.

uh I want to add that it's very important in multi- aent scenarios to uh choose uh an LLM that has strong reasoning capabilities to handle these complexities of multi- aent system and then of course for every uh critical safety critical areas or uh anything that involve irreversible decisions you would need to invest in human in the loop of course to jump in and and evaluate.

Uh the good news is that you don't need to implement everything by yourself. There are a lot of tools and frameworks a lot of efforts in the industry to make this easy for you. Uh at Google for instance we have agent development kits which is open source uh the vertex AI eval service as well.

So they come with built-in features uh with you know LLM as a judge even human in the loop patterns for production scenarios. So you can leverage those tools uh to speed up your evaluation process. Um and I just want to end here by saying that it's also very important to have the right mindset because evaluation is not about achieving perfection.

Evaluation is more about uh understanding deeply your system and find the best measurable ways to be able to improve it uh over time.

Amazing. Yes. I think they lot of great insights you shared in the white paper. Thanks for sharing with the wider community. Uh for those of you who would like to dive deep into what she mentioned, um please do give a read to the white paper and have a look at the summary podcast. Um

I love the tagline here, not about profession.

Yes. Uh but I mean uh to to some extent I do believe that uh evaluating agents is so complex at the moment. you have a trajectory evaluation, trajectory interactions, multi- aent interaction evaluations. Uh it it's an open field. So there's a lot coming in this field. So and uh thanks for the everybody here who added their insights into the white paper and um

maybe just a quick add-on here because like if you were to go even one step higher, right? So uh from a system design and architectural point of view, it would be also interesting to highlight this deterministic software development practices as opposed to agentic uh development practices. I think that is something uh that is really really important in this new agentic era.

And then one thing that we see across the board with the customers is that evaluation should not be an afterthought. It should be a core component of your agentic design on day zero because otherwise as you grow your sophistication in the agentic design then it might be very much difficult to trace and look at where the failure modes are and then you won't be able to trace them effectively.

So that's why actually uh we should we we would encourage the people who are just developing these agentic systems to have a different state of mind especially as opposed to how you can develop a a software uh in the past really take into account these agents are generating results nondeterministically. There is a probabilistic approach like there is a probabilistic result out of it.

You need to control for let's say sa you need to safeguard it. You need to make sure that the agents are not producing false information. There is a lot more control that needs to be included and that's not an immediate thought that when a software developer is building.

Yeah, definitely. Uh this is using some of the best practices we already have. Thanks a lot. Uh Ton uh perfect amazing conversation guys

Sean. Oh, honestly, I thought those answers were really amazing and I I loved the football analogy as well.

I mean, one thing that we've looked at um in some of our aentic multi- aent systems is um similar to the football team, if you take one player out or you make one player purposely bad, what's the impact overall to try and get a sense of for that node um how much does it impact like the overall um kind of accuracy of the model?

Because I think one thing to consider too is that with this error compounds very quickly. So if you have like multiple interactions even if they're kind of 10% off each agent is 10% off you really start to accumulate error very quickly.

Um and so figuring out where the critical junctures are or like the particular so for instance like we have an agent that does planning and we we found that if you have if the plan to begin with is bad then it will really massively impact and skew the rest of uh the results.

So trying to figure out where those particular nodes are similar to ablation testing actually in machine learning where like you can you know take one out or sub one in or put in particular use cases which are designed to fail so that you can see whether it causes a catastrophic failure um is something that we've done but yeah I think both of those answers were really good.

Yeah, I think uh also another point here is that um the more interactions that happen uh in an agent um multiple agents interacting with each other, the more the context floats because if all of the agents need the entire context and as we know LLMs are autogress aggressive. So it more tokens lead to a higher chance of error the more interactions.

So my personal uh uh insight here would be as well try to keep the token count low, keep the interactions to minimum what's required and not load it unnecessarily. Um yeah. All right. Thanks a lot. That was a very uh insightful conversation. Um awesome. Let's shift gears and move on to the next question. Kunch. So J, this is for you.

Um so uh what do you see as a core strength of the open source ecosystem over the next few years especially in the area of agentic systems?

Yeah. So I really like this question. So I think open-source uh large language model is going to play a critical role in the in the future world of agentic systems. Uh especially let me take one specific example. uh we know you know in the agentic system many of the components they are competing for compute resources.

So you have this LLM, you have to run it on GPU or TPU, you have some code interpreter, you have all these kinds of tools. Some of them are also comput intensive. So um eventually you know one the LM is open source. Uh you have a great community support. So you will find all kinds of quantized versions of the LLM for all the card uh all the hardware.

So you can easily find like uh int 8 quantized version for my 10 years old GPU. And uh by using that you you can save some compute space uh you can save some compute resources and memory space for other components in your pipeline. You can make it really flexible and working just as as good as you know uh a cutting edge new hardware.

So I think this uh customizability and flexibility is a re is a key advantage of the open source models. Wow. Yet uh especially um if I must say uh the quantized models quantized and distilled models in the open source community have reached such a threshold wouldn't have been imaginable two years back.

If you see the quant the quality versus uh non-opensource models they've been increasing steadily. So I'm really excited to see um more of what's coming.

And for those of you who uh would like to know about quantization and distribution and all of these techniques a bit more, please refer to the foundational models white paper which I had the pleasure of authoring in our previous courses um which we go into more details of how all of this works. Um all right, awesome. So K, would you like to take some questions for the community next?

Oh, thank you. Um so the like this part comes from the community based on the discord questions you have posted in the uh expert group which uh Brenda had created. So please post your questions continuously and this was for uh Sean from Akil026720. uh how do we build a robust scalable golden set for non-deterministic AI agent regression testing specifically using an LLM as a judge to validate novel correct trajectories? [clears throat]

Yeah, quite a mouthful.

Um yeah so I think it's an interesting question and I think um you know when we I think so we said earlier evaluation's not exactly um you know an exact science and typically what we're trying to do is build up a framework of many different types of evaluation um folded in throughout the entire process right to be able to like identify where where we're going right or wrong.

Um and it can be complex then when you make changes to your uh system to know exactly how that has impacted um at different points. So typically what we do so there's like at a high level two different areas of evaluation. One is task completion for for our particular agents and the other is uh looking at trace quality.

Um and you know that can vary but there's many different intermediate steps that you might want to evaluate.

Um, and for our golden test set, what we found was most useful was really designing one that had um that gave us really good insight into the different capabilities of the agent and instead of looking at aggregate accuracy or like aggregate sort of task completion metrics, looking at the error distribution and how that error distribution might change when you introduce different components.

Um, and you know, I think it's interesting this idea about novel traces as well because this is something that could be quite hard. Uh, you know, it's always an evolving system. Even when you start looking at LLMs as a judge, the way you calibrate those at the beginning might actually change. Like it's some it's a process that you're continually updating in tandem with building the system itself.

Um and so when it comes to novel trajectories, one of the things that we've looked at for like how do we okay, we haven't seen these types of trajectories before. How do we evaluate them or how do we know whether our LLMs as a judge are actually working well for these? So there's different tricks and like tips and tricks that you can use for that one looking at self-consistency.

So you know if you have an LLM as a judge and you run it multiple times on novel trajectories is there much variance there or is it giving the same answer because that can give some indication as to the certainty of your auto rator um we call it autoator but LLM as a judge there um and also typically people tend to use ensembles of different models when you're looking at um LLM as a judge for different novel traces.

if you have a bunch of different models, how likely is it that they agree that that particular novel trace is good or not? And that can give some type of insight into again the certainty as to whether that's a good trace.

Um, I think one thing that we've used, which is probably something that is not very well utilized at the moment, but we found very useful is you can actually look at novelty of traces or novelty of um trajectories using clustering.

And we use a lot of unsupervised clustering to kind of visualize the space of trajectories so that you can actually see you know if they start being different or there's particular novelty because you've introduced a new tool or something like this you can start to see how a new cluster of trajectories might appear.

So typically this is like visualization strategies which also can help you inform building this sort of golden robust test set as well. Um but I I am actually very curious what other people think about that too because I I I mean it's a really great question.

We we have one thing we have observed over the last three days is every question becomes a capstone project by itself.

Yeah. I was just going to say like we love to see this in the capstone project.

Yeah.

So that that happened over the last couple of days and I almost feel like this is a capstone project by itself uh for the uh person who asked the question and when you mentioned about how it is like the question is about novelty and we talk about consistency and novelty and consistency kind of are not in the same league but your clustering mechanisms are some of the ways which we can try to see where we would be able to you know understand deviation from the results.

So thank you Sean appreciate it. Um the next question is uh for from Yasine for Dr. Baja. When using LLM as a judge for agent evaluation, how can we ensure the judge model itself is reliable um [clears throat] and does not introduce new bias into the quality scoring?

Yeah, thanks for the question and uh really good points.

uh indeed we can uh introduce uh an agent uh an LLM as a judge and it can comes with its own problems especially if we don't know how to use it properly right uh so one of the most common mistakes I see across teams building agents is that uh they just plug in the LLM as a judge and um they just let it give its opinions in a kind of a freestyle manner uh without any guidance and that's actually where it becomes prone to bias and random errors So the best way to improve that uh or to avoid this is by using what we call rubrics.

A rubric is basically like a structured scoring guide. Uh it's like a checklist of all the specific dimensions that you care about. It can be you know safety uh performance whatever matters for your domain or industry or uh area of expertise.

And instead of asking the model a very vague questions like hey is this bad you're asking it to reason step by step against some clear and predefined uh criteria. So the these structures uh keeps the evaluation more consistent and more aligned with your uh quality goals. Now there are also another path that you can take if you want to build more trust in your LLM as a judge which is fine-tuning.

You can always fine-tune the model uh on human preferences or ground truth examples. Uh of course this is uh more costly. It's also slow but uh it's always about trade-offs whenever we talk about evaluation. Uh and as I mentioned earlier, we all agree today that we need to rely on uh multiple approaches. Uh we need to have multiple evaluation angles all working together.

uh and uh I like what you mentioned an this is also a space that is uh evolving uh agent evaluation is really an active research area and a lot of open questions uh we don't have all the answers yet but it's also very exciting field to to explore uh because agent quality is directly correlated to user trust and uh the better we get at judging the quality of agents uh the more trustworthy and uh reliable they will become.

Awesome.

Awesome. Thank you, Wafa. This uh question that LLM as a judge that concept itself, I feel like there is more to it than you know the 70page white paper which which was published with other components. So, thank you for adding more color to it. The next question is uh for from Sharon Ginsburg for Tran. Are there any established quality protocols or key products that we can use to improve agent quality for specific use cases instead of building our own process?

Yeah. Yeah. Very good question, right? Especially uh in the context of you know like a building and deploying agentic workloads to an enterprise setting. This becomes a very critical question to handle.

And then the way that I would like to just approach this question is to take let's say a a different approach on what we mean uh what we do when we are experimenting and when we just deploy agents to production right so uh the protocols wise uh let me just immediately address that one as well luckily uh the whole let's say software development community take this agentic workloads very seriously and then immediately they just come up with standardized protocols on multiple interactions between like within the agentic system.

The the first one is that uh you know we have the MCP for tool utilization. We also release A2A for agent to agent communication. We have also the A2P for example for payments. And these protocols are just going to be coming up quite a lot.

And then from an observability and tracing perspective uh we first need to uh uh first divide it into the deterministic part of an agentic workload versus a non-deterministic part of an agentic workload and then for the deterministic part we don't need to reinvent the wheel right so people have been building systems and putting them to production we have a very established DevOps practices and there is a lot of let's say standards on building let's say observe probability around uh the how the system logs should work and that like I'm not going to go into that right so having said that the nondeterministic part is basically where where it becomes quite interesting and that's when the whole tracing of the agentic work is uh taking place and how we control for that is really important the specific the way that we as let's say Google is approaching through this within the context of uh for example agent development kit is to utilize open telemetry to be able to start building logs of also traces but also system metrics about how an agent is interacting.

So there is an opinionated way of just doing this but then more importantly there are different frameworks just doing the same thing as well.

So this goes back into how you're going to integrate this non-deterministic part into your deterministic already existing observation logs to your system and that is a let's say decision an architectural decision that needs to be made but then one thing as a best practices perspective what I would like to just highlight is that uh first make sure that you're tracing everything that is needed uh what the agent does what the LLM calls are done you even for example think about just logging your thinking budgets, you know, like what the thinking tokens are doing and then you need to just make sure that your outputs are also cor let's say care taken care of and the system metrics around it, right?

One thing that is really really important is the uh for security purposes for example the authentication what the the tool is using for uh just the like if a tool if an agent says that I am going to use this tool and I'm going to do that via this authentication you really need to make sure that all these metrics are accounted for.

So going back to the first part let's say very clearly like a very shortly is that yes we have the development cycle and we have the deployment cycle. The development cycle we have this let's say ADK web where you can just really experiment it quite quickly and it just creates all those logs directly. you can just monitor them.

But then basically you need to have a path to be able to and an integrated let's say uh infrastructure that is able to take your uh workload uh from experimentation to production very very seamlessly and have the same compatibility of each logs on both experimentation and productionization.

One of the things about building agents, right, like I feel like the first three days which we did is all exciting because you're seeing it live and this is I would say kind of boring in the back end for a developer because for them they're like ah should I do it because it's not showing results but this is the most important part to make sure your agent is performing well and the scaffolding you mentioned right like putting together so that the process is there as you build helps your development quicker.

So a developer should care about it. Um and make sure that you are aware of the techniques and processes this needs to be established. And one of the uh reason behind the question is probably also that making sure hey how do I make sure there's one process to establish but it's not necessarily one process.

It's making sure you're aware of all the processes and create an approach for your organization of what best fits. Um so th this has been amazing. Um really grateful to have all of you here um during this time and making sure you're able to answer questions for the whole audience.

Um like we have three more segments to go but I I really do appreciate you taking the time coming answering the questions. The community loves it and as you could see in the live chat as it keeps coming up like folks enjoy hearing from the experts and we are looking forward to you know seeing all the momentum in the discord and other channels and uh please um keep us engaged with it.

Thank you so much for all of your time and uh now on to the next um exciting thing. We have we talked with Jay just now and um he has a demo which he would like to share from his um uh how he works through the data science agents. Um Jay,

hi thanks so much. Yeah, today I'd like to share how I build GPU accelerated data science agents. The traditional data analytics workflow or the ETL is a iterative and interactive process. It takes time to write correct code and we need to wait for the program execution, examine the results and then we can move on to write codes for the next iteration.

So uh this process takes time and how fast we can iterate decides the quality of the analysis. That's why I believe LLM powered uh data science agents can help us automate and accelerate this process. It can do tasks from uh create creating a single plot to writing a full data research report uh just based on uh simple prompts. So to achieve this we need a multi- aent system.

Uh for example if we want the agent to create research report based on a data set uh we could have these four agents. So the planner can uh make plans and break down tasks and the coder is to write the code and execute the code to generate all the artifacts include visualizations. So the vision agent uh can interpret the vision uh all the visualizations and uh uh convert them to natural languages.

So the writer agent will combine all the insights and uh write a report. uh if we look at each agent, it can be as simple as uh LLM uh with some tool calling. So uh in the demo I'm going to show shortly uh we create this simple agent architecture from scratch. Uh we are using the Nvidia Neotron LM and uh uh one thing I want to highlight is the Nvidia KUDF library.

So we are going to use it as a tool to accelerate the data processing. For example, uh here is a standard uh LM tool, a Python interpreter. So we can simply add like one argument use GPU to let the LLM uh to uh turn on GPU acceleration. So the cool thing is LM doesn't need to know how to run QDF if the LM already knows pandas which is uh most mostly most LLM knows how to write great pandas code.

So pandas is a very popular package in data science. So it does tabular data processing. However, it can be slow because it's on CPU and winds uh dealing with a large uh data size. Uh uh KDF has this cool feature called zero code change uh pandas accelerator mode. So basically you only need to add two lines of code.

Import kudf.pandas and kudf.pandas.install install and all the pandas uh code uh below it will just work but they will be accelerated on the GPU. So in our experiment you know the data science agent uh you can see that the data processing time is actually longer than the LM inference time. So it can take 10 seconds for some query on a 2 gigabytes or 5 GB data set.

So the QDF can shorten the time to just one second. So uh our agent has many advanced features like dynamic context management efficient tool calling customized uh chat template for quantiz model model. Uh however unfortunately I don't have time to explain all of them. So please find the details in our write up.

uh once we are familiar with how agent works we can you know when we want to deploy it to the production I recommend uh to use a more uh powerful agentic framework for example the Nemo agent toolkit from Nvidia so it is open-source AI uh framework uh it is enterprise ready composable and reusable and it works with uh any most of the popular frameworks uh you're already familiar with like the Google ADK longchain etc Okay.

Yeah. So, let's take a look at the two examples. Uh two demos. Uh let me switch tab and share the new tab. Awesome. So, uh this is a interactive demo. So, I'm running it uh lively. Uh it is running on uh Kaggle kernel. So, you can see that we have already launched the um the LMS. So, they are running on the GPUs on Kaggle kernel.

So here we want to uh explore a data set interactively by just as asking questions. So for example we can ask uh the LM to uh read this data set and uh tell us the column names. So if you look at the uh the output of the LM uh it will first generate write a code and call the tools to execute the Python code.

So the execution is uh failed because you know this data frame variable df it doesn't exist yet. So the lm can reflect on this failure and generate a new code. So it realize so we have to read the CSV file first and then you can print the column name. So uh yeah and uh so here the agent can uh tell us the correct column names.

So for example we can ask other questions like how many rows and columns. So this data set is a e-commerce data set. So it has nine columns and 42 million rows. So it's about 5 GB on disk but one loaded it takes like 10 GB on the GPU. So the LM so this two calling is super fast. So you when we look at the trace you can uh see yeah let's look at another example.

So if we just want the first five rows from the data frame. So the code takes like 1.5 seconds. So it's a considering the data size and you know and the GPU uh we have so I think it's pretty fast. Okay, let's run this uh uh query lily. So how many unique brands are there? So the agent is going to reason about this request.

So because it has all these history so of this data frames this data frame already exists and the agent knows uh its column names. So the agent can write this code and execute it and tell us like there are 3,445 unique brands and we can ask like what's the most popular brand and uh yeah so again so it's a the agent maintains this history but it also tries to manage the context in the optimal way.

So it actually uh removes you know all the two calling traces after each uh each conversation. So you tell us like the most popular brand is Samsung and uh we can ask like so what's the mean price of all the Samsung products. We can even ask the agent to create a uh a visualization.

So here tells us this is the mean price of Samsung product and uh here it writes the code and generate this plot and show us like the top 10 brand by count. So we can also ask you know uh the mean price of the top 10 brand. So uh yeah you can see here so it maintains this history. So it's like chatbot but now you can execute code. So and everything runs on the GPU on the Kaggle.

So you can see the you can see all these metrics like how much GPU and CPU is utilized and yeah so eventually we have this plot. Okay. So this is the first demo and uh in the second demo yeah let me share uh a new tab. In the second demo, I want to show how we can you uh you know create a full report from a data set. So this is a more much more complicated task and it requires a more capable LLM.

We're going to use the Nvidia uh Neotron super 49 billion parameter LM. So due to the model size, we can no longer run it on Kaggle. So we're going to use the cloud uh the media nim lm inference on the cloud and uh uh use API key and uh use this lm to do it. So I'm not going to run it. As you can see here it takes about five minutes to generate this report.

I'm just going to go through like the process. So uh we want to start with the configuration. Uh you can get a free API key from this website and you can save it as a Kaggle secrets like this is the media API key.

And then we uh just uh you know install some uh helper utility libraries and uh uh functions and uh so here so basically you specify a data set you can so kaggle has a rich data set ecosystem you can find a lot of different tabular data set we're going to use this earthquake data tsunami data set so you specify this data set and you can provide a simple prompt so I'm just going to say explore this data set and uh we can call this uh uh library run from data explorer.

So it's going to generate a lot of traces. So uh it's going to write code, create visualization, verify the if the plot is successful or not, interpret the plot, uh write the you know write the uh insight as a report. So eventually you're going to get this PDI file and uh so it has yeah let me let me try to make it bigger. Uh yeah, so it has everything.

Uh yeah, let me actually make my uh screen okay. Yeah, maybe this is better. So it's going to generate this report. So it has all the insights organized logically and it has all the plots generated by the by the agent. So for each vis visualization. So you can see that uh so try to analyze this figure and collect the insights from each visualization and draw a conclusion uh in the end.

So if you check the outputs of this uh uh of this uh demo. So you can also find in in addition to the report you can also find all the intermediate outputs like all the Jupyter notebooks it generates and all the figures it generates. Okay, let me uh get back to my presentation. Yeah. So hopefully you can enjoy these two demo and uh uh try it.

You can reproduce uh every one of them uh by just running them on Kaggle kernels and if you have any questions please reach out to me. Thank you. That's all.

Thank you so much Jay. This um this demo was amazing particularly the data science piece of it. Uh I have seen uh with my experience with data it is hard to get things correctly. I'm I can't wait to try it. So, thank you for sharing and the and for the write up as well because that was very self-explanatory as as you were walking through. So, thank you.

Thank you.

Thank you so much uh Ji. Now on to our next uh segment which is the code labs that folks have uh experimented already. Um can we have um Sitha on stage please? Sitha has been actively engaged in the discord community. So folks know her already by this time.

Thanks for the intro Kant. Uh really happy to be here. Um thanks Kanan. So hi everyone.

Uh my name is Sitha and I'm a developer relations engineer and I've been working very closely with ADK team since the beginning of this year and [clears throat] uh AI and security are my two biggest passionate areas and I'm really really happy to be here on the live stream today uh to talk to you about the day four code labs and walk you through the important concepts uh that we have.

So let me go ahead and share my screen here. And for the first notebook, we have the agent observability. Uh and the second notebook will be about agent evaluation. But before we dive into the notebooks, I want to take a quick pause, a step out, and then do a quick refresher of what you've seen since the beginning of day one, right?

So you learned how to build agents, how to add tools, and then you also learned how to add sessions and memory to your agent, right? And at this point, you could say your agent is a complete unit by itself, right? Uh and you can deploy it to production. But hold on, no, not yet. We need to do eval observability first.

And today's code labs are all about why do you need to do that and why is it so important with that? Let me jump into the first code lab, which is agent observability. So what exactly is observability? And I like to tie things in agentic land back into software engineering practices that we've been following for so long. And on that note, agent observability is basically three things.

Uh it's logs, traces and metrics. So logs are print statements or log statements that we put in our application code which tells you what happened at a specific point of time, right? And traces. Uh the second pillar is uh are essential because they connect all the logs to form a single cohesive story which tell you what happened when you go debug your agent.

And then the third is super important which are metrics or numbers which tell you um important numbers like what is your agent's average latency over the past month or what has been the failure rate which are super important to have. And with that, let me actually go into the uh crux of this notebook itself.

We're going to skip a little bit of setup steps because these are all the same that you've been doing since day one. So, I'm going to go skip into the hands-on demo we have for you today. And let's start with the agents code itself and I'll jump to the UI screen in a moment. So, the agent that we have today here is a research paper finder agent and it has one simple goal.

when you give it give it a prompt asking for get me the research papers um for quantum computing it's going to use the Google search agent find the list of papers and then it is going to use a simple Python function that you see here to count how many papers the Google search agent um written out right so seems pretty simple right but hold on we have a deliberate flaw in the agent which will debug I'm going to go ahead switch to this other tab for the ADK UI and yes now you see it um so I've already fed in the prompt and then you see that the agent returned all the uh papers that it found for all the quantum computing latest papers and we also see at the end of the response if you look there's a there's a there's a line saying it's a total of,367 papers but we barely see like 15 20 papers listed here right so let's see what happens I'm going to go click to the trace.

Look at the specific uh span that says uh what happened. So this is the span that result uh that returned this observed number,367. Um okay, let's see what is being even fed to this specific function. I'm going to click on the span right above it. And this is the event that the uh for the agent when it called the function.

So you see that the agent called the count papers function and then it passed an argument saying papers. But hold on, we might have found our error. So the papers is a list is a single string instead of a list of string of papers that we were expecting. Let me go back to our notebook and we'll verify this. Yeah, we're right.

So we're counting the length of papers, but we are passing it as a single string. And there you go. We've just debugged our very first agent with ADK web UI. But I want to take a moment, pause here and see what would have happened if we didn't have the observability here, right? We would have had to manually debug our code looking for errors.

But it is also complex because agents are non-deterministic. So it might have worked for one prompt, but it wouldn't have worked for another prompt, which makes it even more crucial to have uh observability implemented for agents. Cool. We're done with the first part of this notebook. So for the second part, we're going to see how do you implement this observability in production.

Um, and for that ADK actually provides us a little nice convenient components called plugins and callbacks. Because if you seen the agent code that we just saw, there was no way for us to add logs or print statements, right? The only place where we could have added it was a Python function that we had. So now we need a way to hook into a agent and to add these log statements.

So if you've seen the live stream for yesterday, you uh you would have learned about callbacks or if you've done the notebooks as well. So callbacks are nothing but Python functions which can plug into your agents life cycle at specific points like for example this callback here is can plug into before agent before an agent runs and run this piece of Python code.

And this can plug into after an agent runs. And this before tool, after toll and similarly. And plug-in is what combines all of these and then makes them applicable to a wider uh set of sub aents tools and everything. There's a bunch of theory for you to read here to understand this more in depth.

But I'm going to go to the next important concept here which is why do we need this plugins and callbacks. Right? So basically callbacks like we've seen is a Python function where you can add the log statements and this makes your life even simpler by adding observability wherever you want to in your agent.

So uh ADK also makes this even simpler for you if you just want standard observability uh in your agents by giving you an option for a built-in logging plug-in.

So this plug-in like like built-in tools comes built in with ADK and all you need to do is basically uh these two lines import the plug-in and then add it to your runner and then when you run the agent the next time you would see built-in observability like this like when the user received the message when the invocation is starting LLM request response all standard observability built in.

So let's quickly recap what we've seen in this notebook before we move to the next. We saw three important things which is use ADK web UI when you're in development when you're debugging your agent in production. You have an option to use plug-in and callbacks.

If you want standard observability right out of the box use uh use the built-in logging plug-in but if you have custom requirements then you can build your own custom callbacks and plugins. Cool. Let with that let me switch into the next notebook that we have for the day which is the agent evaluation. Yes, I'm sharing the right one.

So um I'm going to start with a couple little tidbits about agent eval. So right now in the previous notebook what we saw was a more reactive approach to problem solving. Right? You know something is wrong with your agent and we want to debug and we looked at the logs on how to debug.

But evaluation is more of a proactive approach where you catch quality degradations in your agent much before it happens. And that's why both of these are very complimentary to each other. And the second thing I want to share is evaluation is not standard testing. And this is actually a misconception that I had when I started learning agents.

I thought testing was evil but I couldn't have been more wrong.

So in standard applications that we write with deterministic code when we test them we basically create unit and integration tests right and as long as our code doesn't change no matter how many times we run the code we expect it to pass the test but that's not the case with agents because they're more non-deterministic which means it is not only essential we test the final response from the agent but it becomes even more important that we test the trajectory meaning all the steps that the agent took or all the tools that it used to get to that response and you've seen experts today talk about uh different evaluation measures what you should be considering and those were pretty amazing.

So we also have a bunch of uh links in the resources section for you to read more on uh different kinds of metrics that you could use. But for this notebook we'll be focusing on two parts which is how do you do evaluation with ADK web UI and the second part how do you do it in production. With that I'm again going to step uh skip a bunch of these setup steps and go into straight to our agent.

Um which is interesting part right. Cool. So now we have our agent which is a um a very simple agent here which which mocks and home automation. So it says you're in home automation assistant. You control all the smart devices in the house and it has access to one tool which is set device status.

So whenever we specify saying can you turn on the lights in the hallway it's just going to return okay I've successfully turned it on. If you say turn it off it's going to say okay I've turned it off. Pretty simple right? But this would show us a power of evaluation when we do it in ADK web UI.

So I'm going to briefly stop here and uh bring up the ADK web UI for us so you can see how this works in practice. Cool. So uh now you see u I'm sending an prompt saying turn on the desk lamp in the office and we yeah we get a response saying okay it is now turned on.

But let's go ahead click the eval create a new evaluation set in the UI give it a name and I'm also going to go add in the current session to the eval set meaning the conversation that we have in the right side will now be persisted in the evaluation set. I'm going to go ahead run the eval and you see two metrics which we'll talk which we've seen response score and the trial trajectory right.

So let's go ahead run the eval and let's see if it passes. Yeah it does. Uh yeah, good for us. It passes. But now I want to do something different. Let's go edit our ground truth that we're seeing here uh to see if our evaluation fails. Okay, I'm going to click on the case ID again. And then go edit this uh case that you're seeing here to to say okay, the test clamp is off now. It's not on.

And this is basically a ground truth. So basically when this prompt runs again the agent will be comparing the ground truth again against what result it got and that's how we know if an evaluation passed or failed. So let's click on the start eval again and we see yep perfect it failed and you also get the mad score the threshold why it failed what's the response and so on.

So, I'm going to go back uh share the notebook again. And that brings us to the end of the first section for this notebook. And the second section, let me scroll to the relevant section here. And yes, the um one final section here is how do you do this in production, right? Uh so what we've seen now is how to evaluate with the ADK web UI.

But in production you would need to do three simple steps which is replicate all the thing that we've seen uh locally. So we create an eval config and we give the criteria total trajectory score and response match score. You can also give several other criterias like safety to evaluate if an agent returns safe um responses or hallucination to catch if an agent actually hallucinated a response.

So step one define your criteria. Step two, we'll be creating test cases that we just saw in the ADK web UI, right? So, we'll be feeding this ground truth and there are several ways to create this which we've listed here on how how you can do that. And step three basically is for us to run the ADK eval command itself.

So, if you are running this from in a from a CI/CD pipeline perspective, there are two different options. You can use ADK eval C cla command or if you already using piest to write your unit and integration test you can also use piest with um to run your evaluation and I would love for everyone of you to take that as an exercise to to replace ADK eval with pi test and see how that's working.

So let's go ahead and see what this ADK eval returned to us.

Uh we see detailed responses for each of our test case and it says both test cases failed and and you see you can see why it failed or why it passed and what was the threshold score for results and here you also have a sample how do you analyze this results section with that that brings us to the end of the code lab with one small section here which is also a very interesting uh exercise that I want to leave you with uh which is uses simulation so you see the test cases that we created were all fixed in JSON, right?

But user sim using user simulation, which is a feature that was recently released in ADK, you can just pass a conversation to an agent and then the agent takes a conversation, creates its own evaluation plan and then does it so that you won't need fix it test cases anymore. The links are uh the links to the documentation are down below.

So go ahead, try to see how you can use user simulation to replace or fix it test cases with that. We've now successfully completed both the code labs, a quick refresher for this. We've seen how to evaluate agents with ADK web UI. We also saw uh what different metrics are and then how do you evaluate in production using both piest and ADK CLA command.

With that, thank you so much for u sticking with us on the live stream. U and really appreciate all the great conversations that's coming in Discord. Um so happy to be here and keep the questions coming. We're more than happy to uh have a conversation and back to you Kan.

Thank you Sitha. I love how you broke the agent first and then able to demonstrate because if I recall in the day one that was what happened. Folks are like why is my Google search not working with ADK web like this is how you fix it. You need to first be able to debug and look at it in the debug option with ADK web.

So uh thank you so much SA we really appreciated it and uh the folks have already started testing it right I keep seeing feedback in the discord so please continue to engage there Sitha is active participant in the discord and she is there to answer as well so thank you so much

absolutely uh really happy about that and I see so many debug questions for yesterday's codelabs as well so use all these tools that you learned today to u to debug away thanks K Thank you. Thank you so much Sitha. Bye.

Now on to our most exciting session Anand which is the pop quiz where we see all our folks jumping in with answers and uh let's just jump in.

Yes.

Yes. So let's see how closely you have been reading and listening to us. Your first question. Why do traditional QA practices often fail for AI agents? Your options are A. Agents are just too slow to be tested by traditional methods. B agents are non-deterministics, meaning their failures are often subtle degradations of quality rather than explicit crashes.

C, agents do not use code that can be unit tested. Or D, traditional QA tools cannot connect to LLM app APIs. So your answer will be shown in three, two, one, and the answer is B. I think we talked a lot about this QA, so this should be a no-brainer.

Um, the whole challenge with LLMs and agents comes with uh the non-determinism and the way they try to convince you that they're right without being right sometimes.

Yes. And I see a lot of correct answers popped up, so we are good. Yeah, exactly.

All right, next question. What are the four pillars of agent quality introduced in the framework you read in the white paper? Uh, your options are A accuracy, precision, recall, and F1 score. B, speed, cost, latency, and throughput. C, effectiveness, efficiency, robustness, and safety. Or D, planning, tooling, memory, and orchestration. So, think about it. I see a lot of you answering this already. Great. Your answer will be shown

highlights. You shared that in the highlights too.

Yeah, definitely. Uh three, two, one, your answer is C. So yes, this is the four pillars of the Asian quality and uh I shared this in the very beginning of the live stream as well. Moving on. So question number three, in the context of observability, what is the difference between logs and traces? There's a subtle difference here. Uh your options are A. Logs are aggregated health scores.

Traces are raw text output. B logs are for developers while traces are for product managers. C logs are discrete timestamp events while traces connect these events into a full narrative. D logs measure performance while traces measure cost.

Where do you get these answers from?

Uh yes. So think about that. Uh the difference is subtle but especially crucial for agents. Your answer will be shown in three 2 one C. So remember traces are for the trajectory evaluations end to end while logs are the individual parts which have individual events which are logged not the end to end uh story for the agents

and the white paper in detail covers this so it's good to have

all right question number four what is the outside evaluation hierarchy your options are

oh one second yeah

A evaluating the agents internal reasoning before looking at the final output or B validating end to end task success before analyzing their internal trajectory or C relying solely on external user feedback to judge agent quality or D testing the agent only in production environments. So hopefully you have had some time to think. Your answer will be shown in three.

I see a lot of wrong answers here.

One and B. Yes. So outside in is uh look at the end result and then look at the journey which led you to the destination. All right. Last but not least, question number five. What is the primary purpose of the LLM as a judge paradigm? So, we discussed a lot about this. This should be very straightforward.

Uh, your options are A to use a powerful LLM to scalably score qualitative outputs based on a defined rubric, B to replace human evaluators entirely to save money, or C to generate synthetic training data for the agent, or D to act as a router between different agent models. So think back to the discussion today and the white paper and all the previous white papers we refer to this a lot.

Um your options and your answer will be shown yeah in three two one a think that should be

all right hopefully you reinforce some of your concepts and that brings us to the end of today. See you tomorrow. Tune in. Yes. And see this tomorrow is the most important part in my opinion because it's not just building an agent productionizing is the super hard piece of it and we have excellent Q&A experts who are coming up.

So please do come uh like join and the capstone course will be announced as well. So please do join in tomorrow same time for day five prototype production our last day with us. Thank you for staying with us in the journey. See you same time.

See you tomorrow. Bye. Bye.

Bye.
