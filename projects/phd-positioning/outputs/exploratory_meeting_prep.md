# Exploratory Meeting Prep

## 1. Two-minute self-introduction

My name is João Kasprowicz. My background is in Biomedical Sciences, and over the last few years I have built a research path at the intersection of laboratory medicine, data science, and AI applied to healthcare. I also completed a master's in Health Informatics, where my work focused on automatic identification of hematological cells from peripheral blood smear images.

In practice, I come from both sides of the problem. I have real clinical-laboratory experience, including workflow and quality-management experience, and at the same time I have been developing computational research in digital hematology, especially leukocyte classification, dataset construction, image modeling, and robustness under laboratory variability. This work already generated a Springer publication in SIVP and gave me a solid methodological base in computer vision for hematology.

What interests me now is moving beyond isolated cell classification toward more realistic case-level systems. I want to investigate how morphology from peripheral smears can be integrated with CBC, analyzer information, and laboratory context to support decision-making in a way that is computationally rigorous, clinically grounded, and feasible within a doctoral program. Since I work full-time, I am especially interested in a PhD path that is methodologically strong but also realistic, cumulative, and publication-oriented.

---

## 2. Five-minute research summary

My master's work was centered on hematological morphology intelligence at the cell level. The main problem was that leukocyte differential analysis is clinically important but still depends heavily on manual interpretation, which introduces variability and limits scale. I focused on whether deep learning could support this process robustly in peripheral blood smear images.

Methodologically, I worked on leukocyte classification with a strong emphasis on realistic morphology rather than only clean benchmark classes. One important part of the work was dataset construction and curation, including immature and atypical cells, which is important because many published studies perform well mainly on mature and easy-to-separate classes. I also compared modern architectures, including convolutional models and Vision Transformers, and explored stain-oriented augmentation to improve robustness to laboratory variability.

That stage was important because it established three things for me. First, it validated that AI-based morphology analysis is feasible in hematology. Second, it created practical infrastructure, including annotation experience, image workflows, and evaluation routines. Third, it made the limitation of image-only systems much clearer. Even when cell-level performance is high, laboratory decisions are usually not made from isolated cells alone.

From there, my current interest has shifted toward case-level multimodal support. The literature and my own review suggest that image-only leukocyte classification is already a crowded space. There are also early studies combining morphology and CBC for disease-assist tasks, but there is still much less work on workflow-aware laboratory support using real retrospective laboratory data.

What seems most promising to me is not a universal hematology platform, and not a generic LLM project, but a narrower line of research around multimodal laboratory decision support for peripheral blood smear workflow. The central idea would be to keep morphology as the anchor, but integrate it with CBC, analyzer parameters or flags, and possibly longitudinal laboratory context when available, to support tasks such as review prioritization, suspicious-case detection, or other case-level workflow decisions.

What I am still trying to define, and what I would like to discuss with a potential advisor, is the best level of ambition and the most defensible computational core. I do not want to arrive with a closed thesis title. I want to arrive with a strong direction, a realistic data-driven opportunity space, and openness to shape the final problem in a way that fits the advisor, the program, and the available research conditions.

---

## 3. Likely advisor questions

1. Why do you want to do a PhD now?
2. Why PPGCC/UFSC specifically?
3. Why is this a Computer Science PhD and not only an applied health project?
4. How does this go beyond your master's?
5. What exact problem do you want to solve?
6. Why not continue only with leukocyte classification?
7. What data do you realistically have access to?
8. How feasible is this considering that you work full-time?
9. What kind of publication trajectory do you expect?
10. What role do you expect from the advisor?
11. Are you already fixed on a thesis topic?
12. What is the main risk of your current idea?

---

## 4. Recommended answers

## 1. Why do you want to do a PhD now?

I feel that my master's gave me a strong technical entry point, but it also clarified the limits of what I was doing. I now have both a more mature research question and a better sense of what kind of scientific identity I want to build. The PhD would be the step where I move from a well-defined image-analysis problem to a broader but still focused line of work in trustworthy laboratory AI.

## 2. Why PPGCC/UFSC specifically?

Because I am looking for a program where the work can be judged primarily on its computational contribution, while still allowing strong translational grounding in healthcare. My goal is not only to apply models in health, but to contribute methodologically in multimodal modeling, robustness, and decision-support design. PPGCC seems attractive exactly because it can support that balance.

## 3. Why is this a Computer Science PhD?

Because the core contribution is not the clinical problem alone. The core contribution is in how to design and evaluate computational methods for case-level multimodal inference under real-world laboratory constraints. That includes multimodal fusion, uncertainty handling, robustness, temporal modeling, and human-centered decision support. Hematology is the domain anchor, but the scientific contribution is computational.

## 4. How does this go beyond your master's?

The master's was about morphology intelligence at the cell level. The PhD direction is about moving from isolated-cell recognition to case-level multimodal decision support. So there is clear continuity in domain, data type, and methodology, but also a real increase in abstraction, complexity, and contribution.

## 5. What exact problem do you want to solve?

At this stage, I would present it as a family of tightly related problems rather than a fixed thesis sentence. The most promising direction seems to be workflow-aware support for peripheral blood smear review using morphology plus structured laboratory data. Inside that space, I am especially interested in triage, suspicious-case detection, and review-trigger prediction.

## 6. Why not continue only with leukocyte classification?

Because that would probably be too incremental scientifically. It was an important stage, and I still see morphology as central, but I think the stronger doctoral move is to preserve that expertise and place it inside a case-level multimodal setting.

## 7. What data do you realistically have access to?

I would answer carefully: I have strong reason to believe that a meaningful retrospective laboratory ecosystem can be accessed with the proper institutional and ethics steps, especially structured laboratory records. The exact breadth of linkable multimodal data still has to be formally confirmed, and I see that confirmation as part of the early feasibility phase of the PhD.

## 8. How feasible is this considering that you work full-time?

Feasibility is a central constraint for me, not an afterthought. I am not looking for a highly speculative or overbroad thesis. I am looking for a cumulative program where each study can stand as a publication, and where the first paper can be built from the most accessible data layer before depending on more complex linkage.

## 9. What kind of publication trajectory do you expect?

I would like a thesis structured as a coherent set of publishable studies, ideally starting from a feasible baseline study and then moving into stronger methodological differentiation. I care about publication quality, but also about a realistic sequence rather than aiming at prestige in a disconnected way.

## 10. What role do you expect from the advisor?

I would value an advisor who helps sharpen the computational contribution, challenge scope, and keep the work aligned with what makes sense as a Computer Science doctorate. I am comfortable carrying execution, but I want strong strategic guidance on research framing and thesis discipline.

## 11. Are you already fixed on a thesis topic?

No. I have a clear direction and I have spent time mapping the literature and the opportunity space, but I intentionally do not want to arrive with a closed thesis. I want the final problem definition to emerge from the interaction between literature, data feasibility, and advisor perspective.

## 12. What is the main risk of your current idea?

The main risk is overestimating multimodal data readiness too early. The strongest mitigation is to stage the project so that the first research step depends on the most verifiable data and the later steps depend on progressively richer linkage only after feasibility is confirmed.

---

## 5. Questions you should ask the advisor

1. Given your current research line, where do you see the best fit for a doctoral project in this space?
2. Do you think this direction is better framed as multimodal modeling, decision support, robustness, or another computational axis?
3. In your view, what would make this clearly strong as a Computer Science PhD?
4. Which parts of this direction seem most promising, and which seem too broad or risky?
5. How do you usually structure doctoral work for students who need a publication-oriented and cumulative path?
6. What level of topic definition do you expect at the selection stage?
7. Do you see better alignment with a narrower initial problem before committing to a broader thesis arc?
8. For a student working full-time, what kinds of PhD structures have worked well under your supervision?
9. How do you usually balance methodological ambition with data or institutional constraints in applied projects?
10. If we were to refine this into a proposal, what would you want to see improved first?

---

## 6. Red flags to avoid

1. Do not sound like you already have a fixed thesis and only need formal supervision.
2. Do not oversell data access as if everything were already available and cleanly linked.
3. Do not use generic buzzwords like agentic AI, foundation models, or reasoning systems unless directly justified.
4. Do not frame the project as a universal hematology platform.
5. Do not make the conversation revolve only around the health application; keep the computational contribution visible.
6. Do not sound defensive about working full-time. Present it as a constraint you already incorporate into project design.
7. Do not overstate novelty by implying nobody has combined morphology and CBC before.
8. Do not speak as if high classification accuracy alone is enough for a PhD.

---

## 7. How to discuss the doctoral idea without sounding overcommitted

The best framing is:

I am not arriving with a closed thesis topic, but with a researched opportunity space.

Useful language:

- “What seems strongest to me at this point is...”
- “My current reading of the literature suggests...”
- “The direction I find most promising is...”
- “One possibility I would like your opinion on is...”
- “I am trying to understand whether the stronger contribution is really in triage, decision support, or another framing.”
- “I would prefer to refine the exact thesis question together rather than force a fixed title too early.”

Avoid language like:

- “My thesis will be...”
- “I already defined the final architecture...”
- “The novelty is that I will combine images and CBC...”
- “I just need an advisor for the formal process.”

---

## Final strategic posture for the meeting

The conversation should communicate five things:

1. You already have real scientific continuity from the master's.
2. You are capable of execution and already publish.
3. You understand the literature well enough not to propose something naive.
4. You are mature enough to care about scope, feasibility, and contribution.
5. You are still intellectually open and genuinely looking for alignment, not only approval.

That combination usually makes a much better impression than trying to sound fully finished.
