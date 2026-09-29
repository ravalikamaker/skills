---
name: capture-learning
description: Saves reusable lessons from verified causes, recovery results, constraints, consequential decisions, or user preferences, and records explicitly requested observations with their evidence limits. Checks an authorized destination for existing notes before choosing to skip, update, or create a note.
license: MIT
---

# Capture Learning

Preserve a lesson that changes a future decision or prevents repeat work. Record an uncertain observation when the user requests it, keeping its limits explicit.

## Identify the lesson

Look for a verified cause, an environmental constraint, a recovery with demonstrated results, a consequential decision, or a user-stated preference that will matter again. Routine completion and temporary status belong in a task summary or checkpoint. An untested fix is not a proven lesson, but an explicit request to record it can be honored as an observation or hypothesis.

A failed or disproved attempt can prevent repeat work. Retain the attempted
approach, conditions, expected and observed result, and evidence showing what
it did not establish. Scope the negative result to that check; do not turn it
into a universal prohibition or a permanent rule. Saving it still requires the
write authority described below.

For a forecast-versus-actual or capability lesson, retain only what was observed:
the completion endpoint, forecast assumptions, actual elapsed time if measured,
relevant human attention or external wait, task/model/harness, available tools,
checks, and rework. Explain which assumption changed; do not invent timings,
benchmark results, or a general speedup from one sample. Save private execution
lessons only to an authorized private destination; a public skill example may
use clearly labeled synthetic data, never private traces.

For recurring development friction, retain the affected task, environment,
observed obstacle, supported remedy, and rerun evidence when these change a future
action. Keep an untested workaround labeled as such; a useful note does not
create command capabilities, harness loading, or authority to change configuration.

Do not generalize one observed incident into a universal rule. Separate observed facts, inferences, and user preferences.

For a consequential decision, retain the context, chosen option, rationale, and
accepted consequences or tradeoffs. Include the governing requirements and when
they apply or should be rechecked; a different contract may need a different choice.
A choice is not proof that it worked. Read
relevant existing decisions and identify an explicit supersession when the new
choice replaces one; do not erase the original reasoning or silently treat a
proposal as accepted. Use established decision records when available instead
of creating a parallel record system.

Record a cause as proven only when the evidence distinguishes it from plausible alternatives; otherwise state the narrower observation and unresolved cause.

## Choose an authorized destination

An explicit capture invocation or standing authorization allows the corresponding local note write, subject to host, workspace, and memory restrictions. Optional closeout discovery does not create that authorization: present a concise candidate if saving is not authorized. A research-only task remains read-only unless the user separately authorizes capture.

Choose the user's specified destination first, then established project knowledge conventions within the authorized scope. Otherwise, for an authorized project note, use `docs/learning/<descriptive-slug>.md`. Outside a project, use an existing authorized destination or return the candidate without writing elsewhere. Choose the destination before searching notes, and do not create a file or directory until the comparison below warrants it.

Check the destination's audience and repository visibility before saving. Do not silently export a private lesson into a public repository. Omit credentials, unnecessary personal information, and third-party confidential content; a gitignore entry is not a privacy boundary. If sanitization would destroy the lesson's usefulness, retain only a safe candidate and identify the need for an appropriate destination. Do not autonomously modify skills, `AGENTS.md`, global memory, or policy files. If explicit memory rules prescribe an append-only update mechanism, follow that mechanism within the granted authority.

## Compare existing notes

Search the chosen destination using the relevant component, symptom, decision, and version terms. If it does not exist, there are no notes there to compare. Read close matches, including related notes that may narrow or contradict the
candidate. When evidence supports it, include an early warning signal or a
practical prevention action for future reuse. These are optional: do not invent
a cause or prevention rule from an isolated observation. Then choose:

- **Skip:** an accurate note already covers it, or there is no future use and no explicit request to record it. Point to an existing note when it satisfies the request.
- **Update:** the same lesson needs a correction, tighter conditions, or newer evidence. Preserve its sources; identify what replaces the earlier claim and why.
- **New:** a distinct lesson has a future use, or the user requested a distinct observation. Preserve uncertainty and evidence limits.

## Write the smallest useful note

Use this template, omitting irrelevant fields and marking unknowns:

```markdown
# <Specific lesson>
- Kind: observed fact / inference / decision / user preference
- Applies when: <conditions, component, environment and version scope>
- Finding and cause: <supported conclusion; separate unknowns>
- Decision context, rationale, and consequences: <if recording a decision>
- Evidence: <source/artifact, decisive check and result, checked date>
- Reuse: <action to take or avoid, and how to verify it helps>
- Recheck when: <change or counterexample that invalidates this advice>
- Relationship: <existing note updated/superseded, with reason and provenance>
```

Prefer durable source pointers over raw logs or session transcripts. Cite a preference to the user's instruction, not to an invented technical justification. Keep an observed workaround's scope and drawbacks visible. Resolve overlapping notes narrowly; do not launch a cleanup or archive sweep.

Read back the saved note and check that its scope, evidence, and destination match the authorized lesson. Report whether you skipped, updated, or created a note and its location; say when a candidate was only proposed. Do not claim that saving a note makes every future host or session load it automatically. Return to any remaining active task unless the user asked to pause or stop; capturing a lesson does not complete that task.

## Worked example

Synthetic inputs: an authorized local capture finds a note saying “the preview
renders all supplied pages,” based on check C1. New check C2 on preview v4 shows
page 3 omitted when a four-page input is used; no other version was checked.

Update the same note with the scoped correction:

> Finding: preview v4 omitted page 3 for the four-page input in C2.
> Evidence: C2 contradicts the broad claim based on C1; retain both pointers.
> Reuse: inspect page coverage for this input before relying on the preview.
> Limits: cause and other versions remain unverified.
> Relationship: replaces the “all supplied pages” claim; it does not establish
> that every preview fails.

Read back the updated note. If capture is not authorized, return this as a
candidate rather than saving it or changing policy.
