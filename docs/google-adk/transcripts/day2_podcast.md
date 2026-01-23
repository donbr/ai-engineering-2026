# Day 2 - Podcast Transcript

---

Okay, so today we're diving into uh what feels like the core question for anyone working with AI right now. How do you get these incredibly smart language models to actually do something useful in the real world?

Right? Because a powerful foundation model,

I mean, it's brilliant, but it's fundamentally stuck inside its training data, you know?

Yeah. It's like this amazing pattern matching machine, but completely isolated from anything current or anything it can act on.

Exactly. It's like having memorized every book in the library but having no hands or eyes. You can write code, sure, or generate amazing text, but it can't like call an API on its own or check a real-time stock price or even send an email.

And that ability to perceive and act, that's what makes Agentic AI potentially revolutionary, especially, I think, when we talk about using it inside businesses in the enterprise.

That's the key transformation. And the map for how we get there, how models go from just thinking to actually doing is what we're digging into today.

Yes, exactly. Our source material is the day two white paper from that 5day of AI agents intensive course by Google and Kaggle. It really lays out the architecture for making models active agents.

And this is where the idea of tools becomes absolutely central. Tools are basically the agent senses and actuators. It's eyes and hands like you said.

Okay. But you know, historically getting these tools hooked up was a massive headache. If you had, say, n different models and m different tools or APIs.

Oh, I can see where this is going.

Yeah. You ended up with this exponential n* m problem. Just this fragmented mess of custom code, bespoke connectors for every single pair. It just didn't scale.

Sounds like a nightmare. Honestly,

it really was. And the solution that the industry seems to be coalescing around now is the model context protocol or MCP. came about in 2024.

MCCP.

Yeah, MCP. It's designed as an open standard to sort of streamline all this integration. The goal is a unified almost plug-andplay way to connect tools which fundamentally decouples the agent, the brain, the reasoner from the specific tool doing the work, the actor.

Okay, that sounds promising. Let's unpack that starting right at the beginning.

Yeah.

When we say tool in this AI agent context, what exactly are we talking about? So fundamentally a tool is just a function or maybe a program that an LLM based application uses to do something that the model itself can't do natively,

right?

And crucially, these tasks fall into two main buckets. Either letting the model know something new like fetching that real-time weather forecast using an API

or letting the model do something like actually sending a message, updating a database, making something happen in the outside world.

Got it. know something or do something. And the developer community based on the white paper seems to break these down into what? Three main types.

That's right. Three main categories. First up, you got function tools. Okay.

These are the ones developers explicitly define themselves. They're external functions, maybe Python code. And you often use things like detailed dog strings, especially in frameworks like Google's ADK. These dock strings are critical. They define the contract, the inputs and outputs between the model and the function.

Right? Like you might define a function say set light values for a smart home and the dock string specifies you need brightness and color as inputs.

Exactly that the model reads that documentation to figure out precisely how to call your function correctly. It's all about that contract.

Makes sense. What's the second type?

Second are built-in tools. Now these are different because they're provided implicitly by the model service provider. So as a developer you don't really see the tool definition. It just works behind the scenes. a okay like um Gemini's ability to use Google search for grounding right or execute a bit of code itself

perfect examples grounding with search code execution even fetching content from a URL you provide those are often built-in capabilities of the platform

and the third type this one sounds really interesting agent tools

yeah this is a powerful concept an agent tool means you're actually invoking another separate agent as if it were a tool

okay

but the key distinction here is that you're not completely handing off the conversation or the main task. Your primary agent stays in charge. It calls the sub agent, gets a result back, and then uses that result as like an input or a resource for its own reasoning. Often managed with something like an agent tool class in an SDK.

So, it's more like delegation than a full transfer.

Exactly. It's hierarchical. Think of it like a manager asking a specialist team for a report rather than just forwarding the whole project to them.

Okay, I can see that. So if my main agent needs to I don't know analyze some data then email a summary it could call a data analysis agent as a tool get the summary and then use a separate send email function tool itself

precisely you compose capabilities now zooming out a bit the white paper also talks about a broader taxonomy grouping tools by what they do

right like information retrieval

yep getting data action execution which is about making changes in the real world like sending that email or booking something

system API integration obvious Obviously

connecting to other software and importantly human in the loop tools for when the agent needs to stop and ask for permission or clarification from a person.

That structure is helpful but you know having all these tool types is one thing making them work reliably so the agent doesn't constantly fail. That seems like the real challenge. This brings us to best practices which feels critical for anyone actually building this stuff.

Absolutely critical. If you're developing tools for agents, these aren't just suggestions. They're pretty much essential for success.

Okay, laid them on us. What's rule number one?

Rule number one, non-negotiable. Documentation is paramount. Seriously, the only way the model knows what your tool does, what it needs, and what it returns is through the documentation you provide. The name, the description, the parameters. This info is literally fed into the model's context.

So clarity is key.

Utterly key. Use clear, descriptive names. The example in the paper is great. Create a critical booer with priority is infinitely better for the model than something vague like update to Jura. Be specific.

The name and description basically become the instruction manual for the LLM.

Exactly. Which leads to the next point. Describe the action, not the implementation detail. You need to tell the model what task it should accomplish. Create a bug to describe this issue, not how to call your specific function. Use the create bug tool. Ah, okay. Why is that distinction so important?

If you tell it how, you risk confusing it. The model might just repeat your instruction back or get stuck thinking about the tool name instead of the goal. [snorts] You want the LLM to do the reasoning. I need to create a bug and the tool should just be the simple mechanism that executes that decision. Let the LLM reason, let the tool act,

right? Reinforcing that separation of concerns. LLM is the brain, tool is the hand.

Precisely. And related to that is publish tasks, not just raw API calls. It's tempting, especially with complex enterprise APIs, to just create a thin wrapper. That's usually a mistake because those APIs can be huge, maybe dozens of parameters.

A good tool should encapsulate a single clear high-level task the agent needs to perform, not expose the raw complexity of some legacy system. Think book a meeting room, not call the complex calendar API endpoint with these 15 optional flags. Keep it task focused and abstract away the underlying complexity. That makes sense. And this focus probably impacts the output too, right? What about the data the tool sends back?

Huge point. Design for concise output. This is vital. If your tool pulls down, say a massive spreadsheet or a huge log file and tries to stuff it all back into the LLM's context window.

Bad news.

Very bad news. You get context window bloat. It eats up tokens which cause money. It increases latency. And crucially, it actually degrades the LLM's ability to reason because it's waiting through tons of irrelevant data.

So, what's the alternative?

Don't return the raw data. Return a concise summary or maybe just a confirmation or better yet, return a reference, like a URI pointing to where the full data is stored externally. Systems like Google ADK's artifact service are built for exactly this. Let the agent know where the data is. Don't dump it on the agent.

Okay, keep the context clean. Makes perfect sense. One last practice. things will inevitably go wrong. How should tools handle errors?

Errors happen. Yeah. First, use schema validation on your inputs and outputs rigorously. But when an error does occur during execution, the error message itself needs to be descriptive and ideally instructive.

Not just error 500.

Definitely not. A good error message tells the LLM what went wrong and maybe even how to recover. Something like API rate limit exceeded. Please wait 15 seconds before calling this tool again. that gives the agent context and a clear path forward. It turns a failure into something potentially actionable.

Those are really practical guidelines. Anyone defining agent functions can probably use those right away. Okay, let's shift gears now to the model context protocol itself, MCP. This is the standardization layer aiming to make all this tool use scalable and interoperable. You mentioned it's inspired by the language server protocol LSP. How does that client server interaction work?

Right. It borrows that core architectural idea. You basically have three main pieces working together. First, there's the MCP host.

Okay, that sounds like the main application, maybe the thing the end user interacts with.

Exactly. The host manages the overall user experience, orchestrates the agents thinking process, decides when tools are needed, but critically it's also the enforcer it's responsible for applying any safety guard rails or policies. It's the traffic cop.

Got it. Then there's the MCP client.

The client is sort of embedded within the host. Think of it as the dedicated communication module. Its job is to maintain the connection to the server, manage the session life cycle, and actually send the commands to execute tools based on what the host needs.

And finally, the MCP server.

That's the actual program providing the tools or capabilities. The server's job is to advertise what tools it offers, listen for commands from the client, execute those commands, and then send the results back. So this separation is key because

it allows developers building the agent logic in the host to focus purely on reasoning while other teams maybe third parties can focus on building specialized secure reliable tools in the server. It promotes modularity

and how do these components talk to each other? What's the language?

The communication layer uses JSON RPC 2.0. It's a wellestablished textbased standard. Keeps things relatively simple and interoperable.

Okay. standard message format. What about getting those messages back and forth? The transport layer.

MCP defines two main ways. For local development or when the server can run as a child process, you often use DDO standard input output. It's super fast, direct communication, very efficient if everything's on the same machine,

right? But for most real world distributed systems,

then you typically use streamable HTTP. This is really designed for remote connections. It supports server send events s which means the server can stream results back which is great for tools that might take a while to run. It allows for more flexible often stateless server deployments across a network.

Now the white paper mentions MCP defines several primitives like tools, resources, prompts but it really emphasizes that tools are the main event right like almost universal adoption compared to the others.

Absolutely. Tools are the core value proposition of MCP today where most of the implementation effort has focused. The other primitives exist in the spec, but tool definition and execution is the killer feature driving adoption.

So let's zero in on that tool definition within MCP. How does the protocol enforce rigor there?

It uses a standardized JSON schema. A tool definition must have fields like name and description. We talked about how critical those are. And importantly, it requires an input schema defining what the tool expects. and optionally an output schema defining what it will return.

The paper had that get stock price example I remember.

Yeah, classic example. It clearly shows you need to define the expected input like the stock symbol, maybe an optional date and the structure of the output, the price the data was fetched using these schemas. This ensures the host knows exactly how to call the tool and what kind of result to anticipate. No guesswork.

Okay, so the schema provides the contract. When the tool runs successfully, how does the result come back?

Results generally come back in one of two forms. They can be structured, which means a JSON object that strictly conforms to that output schema you defined. This is preferred because it's easy for the host in the LLM to parse and reason about reliably.

Then the other form,

unstructured. This is for things that don't fit neatly into JSON like raw text, maybe an audio file, an image, or importantly those references the URI is pointing to external resources we discussed earlier to avoid context bloat.

Got it. And we touched on errors before in best practices. But how does MCP formally signal when a tool execution fails?

Yeah, there are two levels. You have standard JSON RPC protocol errors like if the host tried to call a method that the server doesn't actually offer or sent badly formed parameters. That's a protocol level failure.

Okay,

but then you have errors that happen during the tools execution. Maybe the external API it relies on is down or it couldn't find the requested data. In this case, the server sends back a result object but it sets a specific flag as error.

True. Ah, so the call technically completed but the outcome was an error.

Exactly. And setting that is error flag is the signal to the host and the LLM that something went wrong within the tools logic. And crucially, the result object can still contain that descriptive error message we talked about guiding the LLM on how to potentially recover.

That seems like a robust way to handle it. Okay, stepping back to the bigger picture, what are the main strategic wins that this kind of standardization through MCP brings to the whole AI agent ecosystem? Well, the biggest one is probably accelerating development and fostering a reusable ecosystem. By having a standard way for tools and agents to talk, you dramatically reduce the friction and time it takes to integrate new capabilities,

lowering the barrier to entry.

Definitely. And there's already talk about things like public MCP registries where people can publish standardized declarations for their servers. Imagine a future where you can easily browse and plugandplay certified tools from different vendors. That's a huge network effect waiting to happen.

And for the agents themselves, does it make them smarter or more capable?

It enables dynamic capabilities because tools can be advertised and discovered via the protocol. Agents could potentially find and start using new tools at runtime without needing to be explicitly reprogrammed. That enhances their autonomy and adaptability.

Interesting. And it also gives you significant architectural flexibility by decoupling the agents core reasoning logic from the specific tool implementations. You can build more modular systems. People are talking about creating an agentic AI mesh networks of specialized agents and tools communicating via MCP. It supports much cleaner designs.

Okay, those are compelling advantages. But let's talk about the flip side of the challenges. You mentioned context window bloat earlier when we discussed best practices. Doesn't standardizing everything with detailed schemas through MCP risk making that problem worse if an agent has access to hundreds maybe thousands of tools.

That is the major nonsecurity scaling challenge right now. You're absolutely right. If an agent hypothetically has access to a thousand tools, loading all thousand detailed definitions, names, descriptions, schemas into the LLM's prompt context every time,

forget about it.

Yeah, it's completely infeasible. You hit context limits, costs skyrocket and worse, the Lon gets overwhelmed and struggles to even figure out which of the thousand tools is the right one for the current task. Its reasoning quality plummets.

So standardization creates this potential fire hose of tools, but the LLM can only sip from it. How do we bridge that gap?

The most promising mitigation strategy being explored and mentioned in the paper is essentially applying a rag retrieval augmented generation approach, but for tools.

Okay. Tool retrieval.

Exactly. Instead of preloading all possible tool definitions, the idea is when the agent needs a tool, it first performs a quick semantic search over an index database of all available tools. This search identifies maybe just the top three or five most relevant tools for the immediate task.

Ah, so you only load the definitions for those few highly relevant candidates into the context.

Precisely. You dramatically reduce the context below by turning tool discovery into an efficient targeted search problem first. Only the relevant information gets loaded for the final reasoning step. It's seen as the most viable path forward for scaling to large numbers of tools.

That makes a lot of sense. Filter before you load. Now, let's briefly touch on security. The white paper acknowledges that MCP itself was designed more for decentralized innovation and interoperability and it doesn't have heavy built-in enterprise security features like strong authentication or authorization. This seems like a significant gap for enterprise use. It's a gap in the core protocol.

Yes. And it opens up several risks, but the one the paper really flags as critical in this model is the classic confused deputy problem.

The confused deputy. Can you unpack that quickly?

Sure. It's a well-known vulnerability. Imagine you have an MCP server that have high privileges. Maybe you can access sensitive databases or code repositories. Now imagine a low-privilege user crafts a clever prompt that tricks the AI model, the host, into asking the MCP server to perform a sensitive action. The MCP server sees the request coming from the trusted AI model. So it executes it.

It acts as a confused deputy performing an action based on the AI's request without verifying that the original user actually had the permissions for that specific action. The user basically launderers their malicious request through the trusted AI.

Right? prompt injection leading to privilege escalation via the tool server.

Exactly. That's a major concern because the protocol itself doesn't handle that enduser authorization context.

So given that MCP itself doesn't solve this, how are enterprises supposed to adopt it safely? What's the practical solution?

The clear consensus and what the paper points towards is that you absolutely must wrap the raw MCP protocol in layers of external centralized governance and security. Meaning you don't expose MCP servers directly. You put something like an enterprisegrade API gateway, think Apogee or similar platforms in front of them. This gateway handles the critical tasks.

Robust authentication of the user, fine grained authorization checks for the specific action being requested, rate limiting, logging, filtering potentially malicious inputs before they even reach the MCP server or the LLM.

So the security isn't in MCP, it's around MCP.

Precisely. You leverage existing mature enterprise security infrastructure to provide the necessary secure framework. Yeah,

the protocol enables the connection, but the enterprise security layers ensure it's used safely.

Okay, that clarifies the approach. So, bringing this all together, it feels like this white paper gives us a really solid framework for thinking about how to build agents that can actually interact reliably with the world.

I think so too. The core takeaway is simple really. Foundation models are powerful brains, but they need tools to act. MCP is emerging as the standard language to connect those brains to the hands and eyes.

But, and it's a big but getting the most value means being disciplined about those tool design best practices. We covered clear names and descriptions, focusing on tasks, not APIs, keeping outputs lean, handling errors instructively, and critically layering those robust external security and governance frameworks around the protocol for any serious enterprise deployment.

And a lot of this is stuff you, the listener, can put into practice right now. Even if you're not using MCP directly yet, thinking carefully about how you define your agents functions or tools that documentation, the granularity, the output design, that will make your agents more effective and reliable immediately.

Absolutely.

Yeah,

those principles are universally applicable.

So, as we wrap up, here's something to chew on. Building directly on that confused deputy risk we just discussed, as these autonomous agents get more deeply woven into our critical systems, how do we actually design the interfaces and the guardrails to ensure that an agent is always acting on the user's authorized intent, not just blindly following the user spoken command?

And how do things like audit trails need to evolve to capture that crucial difference between what was asked for and what was actually allowed?

That's a deep question. M

it's about control, authorization, and true accountability in an agentic world.

Definitely something to think about.

Food for thought as you hopefully start experimenting with these concepts. That's all we have time for in this deep dive. Thanks for joining us. Thanks for having me.
