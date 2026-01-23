# Day 5 - Podcast Transcript

---

So, you know, you can whip up an AI agent prototype really fast these days. Maybe just minutes, right? Fetch some data, make a basic decision. It looks great.

Uh, the demo is always impressive.

But here's the kicker, the sort of um reality check from people actually deploying these things.

Getting that cool demo into production, making it something the business can really rely on.

That's a whole different ballgame.

That's the infamous last mile production gap we hear about. And honestly, it feels more like a canyon sometimes. Yeah, exactly.

And that's precisely what we're tackling today. We're diving into the operational life cycle. They call it agent tops essentially. How you get an agent from being a clever toy to a robust enterprise ready solution.

And our guide for this is the day five white paper from the 5-day of AI agents intensive course by Google X Kaggle. The paper's titled deploying scaling productionizing and A2A. Sounds like the operational manual. Basically,

it really is. It's aimed squarely at AI engineers, MLOS's folks, system architects, anyone needing to make these agents work reliably in the real world.

So, our mission today is to unpack what that takes. Pre-production, keeping it running, getting agents to talk to each other, that A2A thing.

Exactly. And if you need proof that this operational stuff matters, I mean, get the stat from the abstract. Something like 80% 80% of the development effort isn't the core AI smarts.

No way.

Yeah. It's the infrastructure, the security, the constant validation, all the plumbing needed to make it safe and dependable.

Wow. 80%. That just fundamentally shifts your perspective, doesn't it? It's not about tweaking the prompt nearly as much as building the robust system around the prompt.

Precisely. And you know, traditional MLOps helps, but it doesn't quite cut it for these autonomous agents.

Why not? What's so different?

Well, think about it. Standard ML models are predictable, right? Input X gives you output Y more or less. Agents, they're dynamic. They interact. They remember things. Their paths change constantly.

Okay. I see. Like uh this dynamic tool orchestration idea. The agent figures out what tool to use and how on the fly.

Exactly. And how do you reliably test or version something that might never take the same execution path twice? It's a headache.

Right. And that connects to the state management thing, too.

It does. Scalable state management. Agents need memory to be useful across interactions. Managing that securely, efficiently, especially when you have thousands or millions of users, that's a serious system design challenge.

And I bet the unpredictable cost and latency are a nightmare for budgeting.

Oh, absolutely. An agent might take one step or 50. It might call one cheap tool or 10 expensive ones. Without smart controls like caching or budgeting limits, costs can just spiral.

So, okay, it's complex. The white paper must offer some solutions, right?

Yeah.

What are the key pillars here?

Yeah. It boils it down to three foundational things you have to get right. First, automated evaluation. Second, automated deployment. Think CI/CD pipelines. And third, comprehensive observability.

Automation seems key.

Yeah.

But before we dive into the tech, the paper actually starts somewhere else, doesn't it?

It does. Yeah. It emphasizes starting with people and process, which makes sense. I mean, if your customer service agent starts, I don't know, accidentally giving away discount codes, it shouldn't,

right?

That's probably not the model's fault fundamentally. It's likely a process failure. A team didn't define the right guard rails or didn't test them properly. It's about governance.

So, getting the team structure and responsibilities right is step zero. We still need our cloud platform folks, our envelopes teams. Yeah.

But who are the new players specifically for generative AI? The paper highlights two key new specialized roles. Prompt engineers and AI engineers.

Okay, prompt engineers. I've heard that term a lot. What do they actually do?

It's a really interesting mix actually. They need technical chops to write effective system instructions and prompts, but they also need deep domain knowledge. They're the ones defining the agents constitution, its safety boundaries, what kind of answers are good or bad in that specific context.

Sort of like the agents conscience and rule book combined.

Yeah, kind of. Yeah. And then the AI engineers, they're the ones who take that blueprint and make it real robust and scalable.

They build the backend systems.

Exactly. They handle integrating the guard rails, setting up RAG systems if needed, connecting the tools, and crucially building and maintaining that automated evaluation system we mentioned. They make the prompt engineers vision work reliably at scale.

And all these teams, new and old, have to work together super tightly, right? like ensuring the cloud team sets up authentications. The agent literally cannot access that forbidden database no matter what the prompt says.

Absolutely. That tight coordination is non-negotiable. And it leads us straight into the next big topic, the actual journey to production, the pre-production engine.

And the core principle here sounds like it's all about testing first.

Completely. The paper frames it as evaluation gated deployment. It's simple. No agent gets to touch real users until it passes rigorous checks, proving it's effective and safe.

But evaluating an agent isn't like evaluating a standard ML model, is it? You said their paths are dynamic,

right? You can't just look at the final output. Did it hallucinate? Sure, that's bad. But you also have to ask, did it choose the right tool? Did it use the tool correctly? Did it follow the reasoning path it was supposed to? You're evaluating the whole process, the behavioral quality.

Okay. And how do you actually implement that check that quality gate?

The paper discusses a couple of ways. There's the manual prepration. So the engineer runs the evaluation suite, gets a report and has to link that report in their pull request. It's a mandatory human review step before merging code.

Bit more flexible maybe.

Yeah. Or for earlier stages. But the really robust approach is the automated inpipeline gate. This is where the evaluation tests run automatically as part of your CI/CD pipeline. Ah, so if the agent's performance on key metrics like I don't know task completion rate or safety score drops below a certain threshold against your golden data set.

Exactly. That golden data set your trusted set of test cases is crucial. If it fails against that, the pipeline stops. The deployment is automatically blocked. No human override needed unless specifically configured.

That sounds like proper engineering control. And this gate is part of the bigger automated CI/CD pipeline which the paper describes as a funnel.

Yeah, a progressive funnel. The idea is to shift left catch errors as early and cheaply as possible. It has three main phases.

Okay. Phase one.

Phase one is premerge integration. Your basic continuous integration CI. This runs before code gets merged into the main branch. It needs to be fast. Run unit tests, code style checks, linting, maybe some quick security scans, and definitely run that core agent quality evaluation suite. Quick feedback is the goal.

Got it. Keep the main branch clean. If it passes CI, then what?

Then phase two, postmerge validation and staging. This is the continuous deployment CD part. The agent gets deployed to a staging environment that mirrors production as closely as possible.

And this is where the heavier tests happen,

right? Things that take more time or resources. load testing to see how it handles traffic, integration test with real external services, maybe internal user testing, what people often call dog fooding, where your own employees use it.

Okay, makes sense. Find the subtle bugs before real users do. And phase three,

phase three is the gated deployment to production. After passing staging, you promote the exact same build artifact that was validated, not a new build. Consistency is key, and this step usually needs a final human thumbs up. Maybe the product owner signs off

and all this relies on things like infrastructure as code Terraform for instance to keep those environments consistent.

Absolutely. And you need automated testing frameworks like piest maybe that are adapted to handle agent specific things testing conversation flows checking the reasoning trace validating memory content. It's more complex than typical software testing.

Even with all that testing stuff can still break in production, right? So how do you roll it out safely?

Yeah, you need safe rollout strategies. So you don't just flip the switch for everyone. Maybe you start with a Canary release, push the new version to just 1% of users, monitor closely for errors or weird behavior

or blue green deployments

or blue green. Yeah, you have two identical production environments. You deploy the new version to the green one while users are on blue. Once it looks good, you switch traffic over. It means zero downtime and instant roll back if something goes wrong.

You could also do AB testing, right? comparing different agent versions on actual business metrics.

Definitely that's crucial for seeing if your better agent actually performs better in the real world. And underlying all of this is meticulous versioning.

Version everything.

Everything. The code obviously, but also the prompts, the schemas for any tools it uses, the structure of its memory. Everything needs a version number so you can instantly roll back to a previous known good state if things go sideways. It's your production undo button. That roll back capability sounds critical, especially given the unique security risks agents pose.

The paper mentions things like prompt injection. Yeah, prompt injection is a big one, tricking the agent into ignoring its instructions, but also data leakage where it might accidentally reveal sensitive info or even memory poisoning or an attacker corrupts the agents memory to influence future behavior.

Yikes. So, how do we defend against these? The paper mentions Google's secure AI agents approach based on SIF. Three layers of defense.

That's right. Layer one is policy definition. This is about setting the agents fundamental rules through its system instructions. Think of it as its constitution.

Okay. The core guidelines. Layer two.

Layer two is guard rails and filtering. This is where you implement hard stops and checks. It includes input filtering using tools like say the perspective API to block harmful or malicious user inputs before the agent even sees them.

And output filtering too.

And output filtering. Yes. Checking the agent's response before it goes to the user. Using things like vertex AI safety filters to catch PII, hate speech, things like that. Critically, this layer also includes human in the loop, hit escalation.

So for really risky actions, a human has to approve it.

Exactly. like confirming a large financial transaction or deleting critical data. It adds a vital safety check.

And the third layer,

layer three is continuous assurance. Security isn't a one-time setup. You need ongoing rigorous evaluation focused on safety, dedicated, responsible AI testing and proactive red teaming.

Red teaming like deliberately trying to break your own agents safety features.

Precisely. You have teams whose job is to think like an attacker and find vulnerabilities before the bad guys do. It makes the whole system much stronger over time. Security is an ongoing process.

Okay, so we've built it safely, deployed it carefully. Now it's live. The focus shifts completely to operations, right? Managing it day-to-day,

right? We enter this continuous operational loop. Observe, act, evolve. Because agents are autonomous, you can't just deploy and forget. You have to constantly watch and manage.

So step one is observe. Building the agents sensory system, as the paper puts it.

Yeah. You need deep insight into what it's doing and why. This relies on the three pillars of observability. Logs, traces, and metrics.

Okay, logs are pretty standard. The detailed record of events,

right? The factual diary, every decision, every tool call, timestamped, but logs alone can be overwhelming. That's where traces come in.

Traces link the logs together.

Exactly. They provide the narrative. A unique ID follows a request all the way through the agents reasoning and tool calls, even across different services. It lets you see the causal chain of events which is crucial for debugging dynamic behavior

and metrics are the highle view.

Yep. The aggregated report card tracking things like latency, error rates, tool success rates, cost per interaction, user satisfaction scores gives you the overall health picture.

That detailed observation then lets you act apply operational control. How do you keep the system healthy and scalable?

Well, a key architectural principle is decoupling the agents logic from its state. store the memory and session data externally, maybe in loadb or cloud SQL. This lets you scale the agent logic horizontally. Just add more instances without state becoming a bottleneck.

And there are trade-offs to manage, right? Speed versus reliability versus cost.

Not always. For speed, you use caching or parallelized tasks. For reliability, you need things like automatic retries with exponential backoff for tool calls, but that requires the tools to be idotent.

Idempotent meaning you can safely retry them. Exactly. Calling a getw weather tool twice was fine. Calling a charge credit card tool twice is not fine. So tools involved in state changes need to be designed carefully so retries don't cause problems. For cost you optimize prompts, maybe batch requests. It's a constant balancing act.

And what if despite all the defenses, a security issue does happen? You need a plan, right? A security response playbook.

Absolutely. You need it predefined so you can react instantly. The sequence is generally first containment immediately. Stop the bleeding. Use a circuit breaker or a feature flag to disable the compromised tool or feature instantly.

Okay. Stop the damage then

then triage. Route suspicious request or affected users to a human review Q HITL to understand the scope and nature of the attack.

Investigate and finally

finally resolve. Develop a patch. Maybe update a prompt. Strengthen an input filter. Fix a code bug. test it and deploy it immediately using that automated CI/CD pipeline you already built. Rapid response is key.

That leads perfectly into the last part of the loop. Evolve learning from what you see in production.

Right? This isn't just about fixing bugs reactively. It's about proactively making the agent better based on real world data. And again, that automated CI/CD pipeline is the engine that makes rapid evolution possible.

So the workflow is see a problem in production logs or metrics.

Uh-huh. analyze it. Yeah.

Maybe turn that specific failure case into a new test case for your golden evaluation data set.

Ah, so production failures directly improve your future testing. Clever.

Exactly. Then you refine the agent, maybe tweak the prompt, adjust a guardrail, update a tool, and push the improvement through the pipeline, potentially deploying a better, safer version in hours or days, not weeks or months. That's the goal.

Okay, that covers managing a single agent really well. But what happens when you have lots of agents, different teams building specialized ones? The paper talks about interoperability, right?

Yeah. This is crucial for scaling impact. If you have a great customer service agent built by one team and a sharp fraud detection agent built by another, they're often isolated. They can't easily collaborate or share insights, which is hugely inefficient.

You get silos. How do you break those down?

That's where protocols for agent interaction come in. The paper clarifies two main complimentary ones. Model context protocol MCP and agent 2 agent A2A protocol.

Okay, MCP first. What's that for?

MCP is primarily for agents interacting with tools or static resources. It's generally stateless. Think of the agent saying fetch me the current weather for London. It's a specific structured request to a known capability.

Got it? Like using an API and A2A.

A2A is for agents collaborating with other intelligent agents. It's stateful and goal oriented. It's less about do the specific action and more about achieve this complex objective like telling a specialized analysis agent analyze recent customer turn data and suggest three retention strategies.

So one's for tools, one's for partners

kind of. Yeah. And they often work together. The paper uses a great analogy, an auto repair shop. The shop manager, an agent, might delegate a complex task like diagnose and fix this engine problem to a mechanic agent using A2A.

Yeah.

But then the mechanic agent might use MCP to interact with specific tools like querying a diagnostic scanner or looking up a part number in a database, A2A for the highle goal, MCP for the low-level tool interactions.

That makes sense. How do agents using A2A find each other and know what others can do?

They need to be discoverable. The standard proposed involves agent cards, basically structured JSON files that act like a business card for an agent. It describes its capabilities, how to interact with it, its URL, security requirements, maybe even its skills.

And technically, making A2A work requires more infrastructure.

Definitely, you absolutely need robust distributed tracing to follow a request as it jumps between multiple agents. and managing the state and transactional integrity across collaborating agents is much harder than with just one.

When does the idea of a central registry come into play? Do you always need one?

Not necessarily at first, but the paper suggests you need registry architectures when the scale and complexity get really high. Imagine you have thousands of internal tools or hundreds of specialized agents. How does anyone, human or agent, find the right one?

Discovery becomes a bottleneck.

Exactly. So you might have a tool registry using MCP standards to catalog and govern all available tools and you might have an agent registry using A2A agent cards to catalog all the available intelligent agents.

And the main benefit is just making things findable and and maybe enforcing some governance

pretty much. It aids discovery, prevents redundant development, and allows for centralized oversight when your ecosystem gets large and complex.

Wow. Okay. So wrapping this all up, Agent Tub sounds like a really significant shift. It's not just tech, it's process, people, governance.

It really is an organizational transformation. It's about bridging that huge 80% last mile gap between a cool demo and a trustworthy system. And while the immediate drivers are often stability and security,

the ultimate prize, as the paper points out, is velocity. Getting good at agent tops means you can deploy meaningful improvements and fixes in hours or days, not weeks or months. Your agents continuously evolve and get better. So for someone listening maybe starting out on this journey, what's the first most crucial step based on all this?

I'd say focus on those fundamentals we talked about early on.

Seriously, build a solid representative evaluation data set for your agents task and get at least a basic CI/CD pipeline in place with automated evaluation as a gate. That foundation is key.

Get the testing and deployment automation right first.

Yeah, that gives you the safety net and the speed to iterate and improve everything else.

Makes sense.

Yeah. And maybe a final thought to leave people with.

I think the really exciting frontier here isn't just making individual agents smarter. It's orchestrating systems where multiple agents collaborate effectively, learn from each other, and tackle truly complex problems together. Agent Tops isn't just about making one agent reliable. It's the essential groundwork we need to build those incredible collaborative AI ecosystems of the future and do it responsibly.

That's a great place to end. And that actually wraps up our deep dive series covering the material from the five-day of AI agents intensive course by Google XCaggle. This was day five.

Been quite a journey through the material.

Absolutely. So if you listening haven't checked out the content from the earlier days, things like evaluation frameworks in more detail, REGG architectures, tool use patterns, we definitely recommend going back and reviewing that course material. There's a ton of great stuff there. Go build amazing
