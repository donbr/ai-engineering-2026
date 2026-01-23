# Day 4 - Podcast Transcript

---

Welcome back everyone. Today we're jumping into something really fundamental for anyone building autonomous systems.

Yeah, we're taking a deep dive into the Google X Kaggle 5day of AI agents intensive course. Specifically, we're unpacking the day four white paper.

That's the one called agent quality, a practical guide from evaluation to observability. Sounds pretty crucial.

Oh, absolutely. It gets right to the heart of the matter. How do you actually trust an AI agent when you can't predict exactly what it'll do next?

Right. That non-determinism thing.

Exactly. And the paper argues straight up that quality can't be an afterthought. It has to be like an architectural pillar right from the start, not just final testing.

Okay, that makes sense. Designing for quality, not just testing for it. So, if that's the core problem, this unpredictability, what's their big solution? What are the main ideas they put forward?

They lay out three uh really core messages. The first one is a bit of a mindset shift. The trajectory is the truth.

Wait, the trajectory? So, you mean the path the agent took? Yeah. Not just the final answer.

Precisely. Even if the agent gets the right answer, if it took some crazy, inefficient or almost wrong path to get there, well, that's still a quality issue.

Ah, I see. So, just looking at the final output hides all the messy stuff that happened along the way, the near misses.

You got it. The quality is tied up in the whole process, the agent's entire uh chain of thought. Okay, which logically leads to their second point. I guess if the trajectory is the truth, you need to see the trajectory.

Exactly. Observability is the foundation. You absolutely need tools, logging, tracing metrics to actually peer inside the agents reasoning. Without that window, you're flying blind for debugging and evaluation.

Makes perfect sense. Log it, trace it, measure it. And the third message,

the third is about the operational side. Evaluation is a continuous loop. It's not a oneanddone thing before launch,

right? It's more dynamic.

Yeah. They call it the agent quality flywheel. Basically, everything you learn from the agent running in the real world, especially when it messes up, feeds back into making it better. It's a constant improvement cycle.

A flywheel. That definitely implies the old ways of software testing are kind of broken for these agents. They use an analogy, don't they? Something about a delivery truck versus a race car.

Yeah, a Formula 1 car. It's a great comparison. Think about it. Traditional software is like that delivery truck. It has a fixed route, predictable tasks. It either works or it crashes. It fails explicitly.

Okay, simple pass fail.

But the F1 car or the AI agent, it's constantly making dynamic judgments based on complex changing conditions. Success isn't about following a checklist. It's about, you know, nuanced real-time decision-making.

And when it fails, it's different. It might not crash spectacularly.

Exactly. Agents often fail insidiously. The system might report 200. Okay, everything looks fine technically, but the output is subtly wrong, factually incorrect, maybe biased, maybe just unhelpful.

And that quiet failure just eats away at user trust over time. Devastating.

Totally. And the paper lists some really specific failure modes we see with agents that go beyond typical software bugs. Things like um algorithmic bias,

like a resume screening agent accidentally learning and amplifying biases from old hiring data. Precisely penalizing good candidates unfairly or the classic factual hallucination.

Ah yes, the agent just confidently making stuff up.

Yeah.

Inventing sources or data.

Yeah. Makes the whole output useless, potentially harmful. Then there's performance and concept drift.

That's where the world changes, but the agent doesn't keep up,

right? Like a fraud detection agent that was trained on last year's scams suddenly starts missing brand new attack methods because the very definition of fraud has shifted. It's operating on outdated assumptions. And the last one they mentioned sounds really wild. Emergent unintended behaviors.

Oh, this is fascinating. The agent starts developing weird superstitions about what actions get rewarded or it finds clever loopholes in the system rules that nobody anticipated just to achieve its goal.

Whoa. Okay. So that level of complexity, the planning, the tool use, the memory, it just shatters the old evaluation models, doesn't it?

Completely. You move from testing a simple ML model to testing this active agent. It has planning and multi-step reasoning where one slightly off choice early on can cascade into a totally wrong outcome later.

Plus, it's using tools and function calls, right? Interacting with external APIs, databases, things outside its control.

Exactly. That introduces external randomness and failure points. And then there's memory, both short-term working memory and long-term learning. The agent changes over time. So you're not testing a static thing anymore. It's constantly evolving.

Yep. Which means the whole goal of evaluation has to shift. It's not just verification anymore. Did we build the thing right according to the spec?

That has to be validation,

right? Validation. Did we build the right thing that actually helps the user? And to measure that, they propose four key pillars of quality.

Okay, let's break those down. What's pillar number one? The ultimate goal.

Effectiveness. Simply put, did the agent actually achieve what the user intended? Not just did it complete the task, but did it meet the underlying need?

So for a customer service agent, it's not just closing the ticket. It's maybe resolving the issue first time or even making a sale. Yeah.

Connecting to real business goals.

Exactly. Then pillar two is efficiency. Did it solve the problem? Well,

meaning quickly, cheaply.

Yeah. Things like latency, cost measured in tokens usually, and also the complexity of the path it took. Was it a direct three-step solution or a meandering 25 steps with lots of corrections?

Makes sense. Pillar three

robustness. How well does it handle curveballs? You know, API errors, network issues, unclear instructions from the user.

Does it just give up or does it handle it gracefully? Maybe retry or ask for clarification.

Ideally, yeah, it shouldn't just crash or guess wildly. And the last pillar, the absolute non-negotiable one, safety and alignment. This is the big one. Ethics, avoiding harm, security,

all of that. Sticking to defined boundaries, refusing dangerous requests, resisting things like prompt injection attacks. If this pillar crumbles, none of the others matter.

Totally agree. So, we have these four pillars. How do we actually go about judging the agent against them? What's the strategy?

They recommend what they call an outside in hierarchy. Start broad, then zoom in. Okay. So, outside in means look at the final result first. Blackbox style.

Exactly. End toend evaluation first. Focus purely on the outcome. Did it succeed or fail at the overall task? What was a user satisfaction? Maybe a CSAT score. This tells you what went wrong. Mission failed,

but it doesn't tell you why.

Right? So, if the N10 evaluation flags a problem, you move inside out. You open the glass box and do trajectory evaluation. Analyze the actual path it took. This is where you diagnose the failure. What kind of things are we looking for in the trajectory?

You're looking for the break points. Was the LLM planning flawed? Like, did it get stuck repeating itself or lose track of the context?

Okay. Bad reason.

Or was it bad tool usage? Did it like hallucinate a tool that doesn't exist or feed it the wrong information

using the tools incorrectly?

Yeah. Or maybe it was tool response interpretation. The tool worked fine, gave back an error like a 404 not found, but the agent just ignored it and tried to proceed anyway. uh failing to understand the feedback that seems critical.

Yeah.

Now, for the folks actually using the kegle agent development kit, the ADK, there's a cool practical tip here, right?

Oh, yeah. This is great. You can take a run where the agent did really well, a successful trajectory, and save it as an evil case.

What does that save exactly?

It saves not just the final good answer, but the entire sequence of tool calls and thoughts that led to it, all in a test.json file. So you lock in that known good path

precisely. It becomes your ground truth for regression testing. You run that test case later and if the agent deviates from that successful path, you know you've broken something. It prevents backsliding.

That's super useful. Okay, let's talk about who does the evaluating. We can't have humans checking every single run, right? It's a scale.

Definitely not. It has to be a hybrid system. Automation gives you speed and scale.

What kind of automation?

Well, you start with basic automated metrics. things like rouge or bert score. They're quick, cheap ways to measure surface level similarity between the agents output and maybe a reference answer.

Kind of like keyword matching or semantic closeness

sort of. They're best used as trend indicators in your uh CI/CD pipeline, your development workflow. If those scores suddenly tank, it's a quick signal that something might have broken badly, a first filter.

But they don't really understand meaning or usefulness, do they?

Not deeply. No. Which is why the next layer is the LLM as a judge approach. You use a powerful separate LLM maybe like Gemini Advanced to actually assess the quality of the agents output.

Having one AI judge another. How do you make that reliable though? Aren't LLM's biased?

They can be. The key technique the paper highlights is pair-wise comparison. Don't just ask the judge LLM read this output 1 to five. That leads to everyone scoring things a three.

Leg dreaded central tendency bias.

Exactly. Instead, you show the judge LLM the output from agent A and agent B for the same task. Give it a detailed rubric and force it to declare a winner. AVSB forcing a choice makes the signal cleaner. You get a win- loss rate.

Much cleaner, much more reliable signal. It helps mitigate the judge's own biases. And they also mention an even newer idea, agent as a judge.

What's that? That's where you train a specialized agent whose job is to evaluate the execution trace the thought process of another agent. It's judging the quality of the reasoning, the tool choices, not just the final text.

Judging the process, not just the product. Interesting. But even with AI judges, humans are still essential, right?

The human in the loop. Hit

indispensable. Humans bring domain expertise. They understand nuance, tone, creativity in a way models still struggle with. And humans are crucial for creating the golden set, those high quality ground truth evaluation examples.

How do you make human review efficient?

The best practice is a good reviewer UI, something that shows, say, the conversation history on one side and the agent's internal reasoning trace the trajectory on the other.

So the reviewer sees both what the agent said and why it said it side by side.

Exactly. And for really high stakes actions, HITL becomes a safety mechanism. Like the agent needs human approval before doing something critical.

Yeah. Like before executing a payment, execute payment or sending a sensitive email, you build in an interruption workflow where a human must click approve or reject.

That makes sense for safety critical steps. And that ties into the whole responsible AI RAI layer, doesn't it?

Absolutely. RAI isn't just a final check. It's woven in. It involves systematic red teaming. Basically, actively trying to break the agents safety rules and controlled tests,

finding the vulnerabilities before the bad guys do,

right? And architecting safety features as explicit components like guardrails implemented as plugins, maybe a safety plugin.

How would that work? It could have methods that hook into the agents life cycle like a before model call back that scans the user's input for prompt injection attempts and an after model call back that scans the agents plan response for say leaking private information PII before it's shown

building safety checks right into the agent's execution flow.

Very cool. Okay, so we know what to measure the pillars and who measures it the hybrid system. But underpinning all of this is the ability to actually see inside the agent. That's observability,

right? This is the technical foundation for everything else. The paper makes a nice distinction. Monitoring is like checking if a line cook followed the recipe. Observability is like watching a gourmet chef during a mystery box challenge. You need to understand their dynamic thinking.

You need to know is the agent thinking effectively

precisely and that rests on the three pillars of observability. First is logging. Think of it as the agent's detailed diary.

Every little step it took. atomic timestamped entries saying what happened. But crucially, these need to be structured logs, probably JSON, not just plain text. They need to capture context like the chain of thought, the tool inputs, the tool outputs,

which data, not just simple messages. Okay. Pillar two

crazing. This is the agent's footsteps connecting the dots between the logs. [snorts] If logs are individual clues, the trace is the narrative thread showing cause and effect. How one step led to the next.

Exactly. It's usually built on standards like open telemetry which is the industry norm now tracing links related logs called spans together the LLM call the tool use the response processing into one story it tells you why something happened absolutely essential for debugging complex multi-step failures

you can't debug what you can't see makes sense and pillar three

metrics the overall health report these are the quantitative aggregated numbers derived from the logs and traces they tell you how well things are happening And they split these metrics for different teams, right?

Yeah, that's a key operational point. You need different dashboards for the ops or S sur teams. You track system metrics, things like P50, P99 latency, median and worst case response times, error rates, API costs per task, the vital signs,

keeping the lights on,

right? Then for the data scientists and product managers, you track quality metrics. Things like correct scores, how often the agent follows successful trajectories, trajectory adherence, maybe helpfulness ratings, the judgment calls.

Two different views for different needs. But logging and tracing everything sounds like it could be expensive, slow things down.

It definitely can have overhead. That's why the paper recommends dynamic sampling. You don't necessarily need to capture a full trace for every single successful request when things are running smoothly,

but you always want the trace for errors.

Absolutely. So, dynamic sampling might mean trace 100% of all failed requests, but maybe only trace, say, 10% of successful ones. It gives you the crucial diagnostic data for failures without bogging down the system during normal operation.

Smart trade-off, balancing insight with performance. Okay.

So, putting this all together, the pillars, the evaluation methods, the observability, it creates that agent quality flywheel you mentioned earlier.

That's the synthesis. Yeah. It's this continuous loop. You define your quality targets, the pillars. You instrument the agent so you can see inside observability. You evaluate the agents process and outcomes using the hybrid system. And then crucially you architect the feedback loop so that insights from evaluation especially failures directly feed back into improving the agent and refining the evaluation itself.

Turning every interaction, every failure into a learning opportunity to make the system smarter and more trustworthy. It's a whole operational model.

It really is the complete playbook for building reliable agents.

Okay, let's wrap this up. If you had to boil this whole guide down, what are the absolute key takeaways, the core principles for building agents we can actually trust?

I'd say three things stand out. First, evaluation must be an architectural pillar. It's not QA at the end. It's designed in from the start. Your agent has to be built to be evaluatable.

Designed for testability essentially. Second,

second, the trajectory is the truth. Shift focus from just the final output to the entire decision-making process. That's where the real quality story is. And you need deep observability to see it.

Look at the journey, not just the destination. And third,

third, the human is the arbiter. Automation scales evaluation. Yes, LLM judges help.

But ultimately, human values, human expertise, human nuance. That's what defines good. Humans set the standard and handle the edge cases.

Got it. Design it in. Watch the process. Keep humans in charge of the definition of quality. This dive into the Google X Kaggle guide really paints a clear picture. The future is definitely agentic, but this framework shows us how to make that future reliable.

Yeah, it provides the tools and the mindset.

So, for everyone listening, especially if you're working with the agent development kit or similar tools, the call to action seems pretty clear, right? Start instrumenting your agents now. Make them evaluable by design today.

Don't wait until the end.

Exactly. Focus on building agents that aren't just capable, but are truly trustworthy. That seems like the real goal
